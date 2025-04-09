#!/usr/bin/env python
"""
Simple test client for MCP.
This script connects to the test server and sends a simple message.
"""

import socket
import json
import sys
import time
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.config import config


def main():
    """Run a simple test client"""
    # Get server configuration
    server_config = config.get("server", {})
    host = server_config.get("host", "127.0.0.1")
    port = server_config.get("port", 55557)
    buffer_size = server_config.get("buffer_size", 4096)

    print(f"Connecting to test server at {host}:{port}...")

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to test server")

        # Send a message
        message = {"type": "test", "params": {"message": "Hello from test client"}}
        client_socket.send(json.dumps(message).encode("utf-8"))
        print(f"Sent message: {message}")

        # Receive a response
        data = client_socket.recv(buffer_size)
        if data:
            try:
                response = json.loads(data.decode("utf-8"))
                print(f"Received response: {response}")
            except json.JSONDecodeError:
                print("Invalid JSON received")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Test client stopped")


if __name__ == "__main__":
    main()
