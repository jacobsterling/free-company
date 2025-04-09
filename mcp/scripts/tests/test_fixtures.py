import json
import socket
from typing import Dict, Any

from mcp.config import config

# Test level name
TEST_LEVEL_NAME = "MCP_Test_Level"


def send_command(command: Dict[str, Any]) -> Dict[str, Any]:
    """Send a command to the MCP server and return the response"""
    server_config = config.get("server", {})
    host = server_config.get("host", "127.0.0.1")
    port = server_config.get("port", 55557)
    buffer_size = server_config.get("buffer_size", 4096)
    timeout = server_config.get("timeout", 5.0)

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(timeout)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Send the command
        client_socket.send(json.dumps(command).encode("utf-8"))

        # Receive the response
        data = client_socket.recv(buffer_size)
        if data:
            return json.loads(data.decode("utf-8"))
        return {"error": "No response received"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        client_socket.close()
