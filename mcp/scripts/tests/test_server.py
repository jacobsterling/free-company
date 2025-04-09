#!/usr/bin/env python
"""
Simple test server for MCP.
This script creates a basic server that listens for connections and responds with a simple message.
"""

import socket
import json
import sys
import os
import time
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.config import config


def main():
    """Run a simple test server"""
    # Get server configuration
    server_config = config.get("server", {})
    host = server_config.get("host", "127.0.0.1")
    port = server_config.get("port", 55557)
    buffer_size = server_config.get("buffer_size", 4096)

    print(f"Starting test server on {host}:{port}...")

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind the socket
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Test server listening on {host}:{port}")

        # Accept a connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        # Receive data
        data = client_socket.recv(buffer_size)
        if data:
            try:
                message = json.loads(data.decode("utf-8"))
                print(f"Received message: {message}")

                # Send a response
                response = {
                    "status": "success",
                    "message": "Test server received your message",
                }
                client_socket.send(json.dumps(response).encode("utf-8"))
                print("Sent response")
            except json.JSONDecodeError:
                print("Invalid JSON received")
                client_socket.send(
                    json.dumps({"error": "Invalid JSON format"}).encode("utf-8")
                )

        # Close the connection
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Test server stopped")


if __name__ == "__main__":
    main()
