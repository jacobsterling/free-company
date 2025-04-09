#!/usr/bin/env python
"""
Test fixtures for MCP tests.
This module provides fixtures for setting up and tearing down test environments.
"""

import os
import sys
import json
import socket
import time
import tempfile
import pytest
from pathlib import Path
from typing import Dict, Any, Generator, Optional

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

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


def create_test_level() -> Dict[str, Any]:
    """Create a test level for testing"""
    command = {
        "type": "create_level",
        "params": {"level_name": TEST_LEVEL_NAME, "template": "EmptyLevel"},
    }
    return send_command(command)


def delete_test_level() -> Dict[str, Any]:
    """Delete the test level"""
    # First, get all actors in the level
    get_actors_command = {
        "type": "get_actors_in_level",
        "params": {"level_name": TEST_LEVEL_NAME},
    }
    actors_response = send_command(get_actors_command)

    # Delete all actors in the level
    if "actors" in actors_response:
        for actor in actors_response["actors"]:
            delete_command = {
                "type": "delete_actor",
                "params": {"actor_name": actor["name"], "level_name": TEST_LEVEL_NAME},
            }
            send_command(delete_command)

    # Delete the level itself
    delete_level_command = {
        "type": "delete_level",
        "params": {"level_name": TEST_LEVEL_NAME},
    }
    return send_command(delete_level_command)


def ensure_server_running() -> bool:
    """Ensure the MCP server is running"""
    try:
        # Try to connect to the server
        server_config = config.get("server", {})
        host = server_config.get("host", "127.0.0.1")
        port = server_config.get("port", 55557)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1.0)
        client_socket.connect((host, port))
        client_socket.close()
        return True
    except:
        return False


@pytest.fixture(scope="session")
def mcp_server() -> Generator[None, None, None]:
    """Fixture to ensure the MCP server is running"""
    # Check if server is running
    if not ensure_server_running():
        # Start the server if it's not running
        import subprocess

        subprocess.Popen(
            ["python", "-m", "mcp.server"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Wait for server to start
        time.sleep(2)

    yield


@pytest.fixture(scope="function")
def test_level(mcp_server) -> Generator[str, None, None]:
    """Fixture to create and clean up a test level"""
    # Create the test level
    response = create_test_level()
    if "error" in response:
        pytest.skip(f"Failed to create test level: {response['error']}")

    # Yield the level name
    yield TEST_LEVEL_NAME

    # Clean up the test level
    delete_test_level()


@pytest.fixture(scope="function")
def temp_config_file() -> Generator[str, None, None]:
    """Fixture to create and clean up a temporary configuration file"""
    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({}, f)
        config_file = f.name

    yield config_file

    # Clean up
    os.unlink(config_file)
