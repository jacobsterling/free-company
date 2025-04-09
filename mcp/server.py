import socket
import json
import logging
import threading
import time
import os
import signal
from typing import Dict, Any, Optional, Type, Callable
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

from .mcp_utils import CommandTypes, logger
from .config import config


class MCPServerError(Exception):
    """Base exception for MCP server errors"""

    pass


class ConnectionError(MCPServerError):
    """Raised when there are connection-related errors"""

    pass


class CommandError(MCPServerError):
    """Raised when there are command-related errors"""

    pass


class MCPServer:
    """Main MCP server class with robust error handling and connection management"""

    def __init__(self):
        server_config = config.get("server", {})
        self.host = server_config.get("host", "127.0.0.1")
        self.port = server_config.get("port", 55557)
        self.max_connections = server_config.get("max_connections", 5)
        self.buffer_size = server_config.get("buffer_size", 4096)
        self.timeout = server_config.get("timeout", 5.0)

        self.server_socket = None
        self.running = False
        self.connection_pool = {}
        self.command_queue = Queue()
        self.thread_pool = ThreadPoolExecutor(max_workers=self.max_connections)
        self.command_handlers = {}
        self.pid_file = config.get("paths.pid_file", "unreal_mcp.pid")

        # Configure logging
        self.logger = logging.getLogger("MCP.Server")

    def register_command(
        self, command_type: str, handler: Callable[[Dict[str, Any]], Dict[str, Any]]
    ):
        """Register a command handler for a specific command type"""
        self.command_handlers[command_type] = handler
        self.logger.info(f"Registered handler for command type: {command_type}")

    def start(self):
        """Start the MCP server"""
        try:
            # Save PID to file
            with open(self.pid_file, "w") as f:
                f.write(str(os.getpid()))
            self.logger.info(f"PID saved to {self.pid_file}")

            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(self.max_connections)
            self.running = True

            self.logger.info(f"MCP server started on {self.host}:{self.port}")

            # Start command processing thread
            self.thread_pool.submit(self._process_commands)

            while self.running:
                try:
                    client_socket, address = self.server_socket.accept()
                    client_socket.settimeout(self.timeout)
                    self.logger.info(f"New connection from {address}")

                    # Handle client in a separate thread
                    self.thread_pool.submit(self._handle_client, client_socket, address)

                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:
                        self.logger.error(f"Error accepting connection: {e}")
                    break

        except Exception as e:
            self.logger.error(f"Server error: {e}")
            raise MCPServerError(f"Failed to start server: {e}")

    def stop(self):
        """Stop the MCP server"""
        self.running = False

        # Close all client connections
        for client_socket in self.connection_pool.values():
            try:
                client_socket.close()
            except:
                pass
        self.connection_pool.clear()

        # Close server socket
        if self.server_socket:
            self.server_socket.close()

        # Shutdown thread pool
        self.thread_pool.shutdown(wait=True)

        # Remove PID file
        if os.path.exists(self.pid_file):
            os.remove(self.pid_file)
            self.logger.info(f"PID file {self.pid_file} removed")

        self.logger.info("MCP server stopped")

    def _handle_client(self, client_socket: socket.socket, address: tuple):
        """Handle client connection"""
        self.connection_pool[address] = client_socket

        try:
            while self.running:
                try:
                    data = client_socket.recv(self.buffer_size)
                    if not data:
                        break

                    try:
                        command = json.loads(data.decode("utf-8"))
                        self.command_queue.put((command, client_socket))
                    except json.JSONDecodeError:
                        self.logger.error(f"Invalid JSON received from {address}")
                        client_socket.send(
                            json.dumps({"error": "Invalid JSON format"}).encode("utf-8")
                        )

                except socket.timeout:
                    continue
                except Exception as e:
                    self.logger.error(f"Error handling client {address}: {e}")
                    break

        finally:
            client_socket.close()
            self.connection_pool.pop(address, None)
            self.logger.info(f"Client {address} disconnected")

    def _process_commands(self):
        """Process commands from the queue"""
        while self.running:
            try:
                command, client_socket = self.command_queue.get(timeout=1.0)
                self.thread_pool.submit(self._execute_command, command, client_socket)
            except Queue.Empty:
                continue
            except Exception as e:
                self.logger.error(f"Error processing command: {e}")

    def _execute_command(self, command: Dict[str, Any], client_socket: socket.socket):
        """Execute a command and send the response"""
        try:
            command_type = command.get("type")
            if not command_type:
                raise CommandError("No command type specified")

            handler = self.command_handlers.get(command_type)
            if not handler:
                raise CommandError(f"Unknown command type: {command_type}")

            response = handler(command.get("params", {}))
            client_socket.send(json.dumps(response).encode("utf-8"))

        except Exception as e:
            self.logger.error(f"Error executing command: {e}")
            try:
                client_socket.send(json.dumps({"error": str(e)}).encode("utf-8"))
            except:
                pass
