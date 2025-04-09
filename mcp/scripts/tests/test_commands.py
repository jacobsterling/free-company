import os
import sys
import time
import subprocess
import json
import socket
import pytest
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.config import config
from mcp.server import MCPServer


def test_setup_venv():
    """Test the setup-venv command"""
    result = subprocess.run(["mcp.bat", "setup-venv"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Virtual environment setup complete" in result.stdout


def test_start_server():
    """Test the start-server command"""
    # First, ensure no server is running
    subprocess.run(["mcp.bat", "stop-server"], capture_output=True)
    time.sleep(1)  # Wait for server to stop

    # Start the server
    result = subprocess.run(["mcp.bat", "start-server"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Starting MCP server" in result.stdout

    # Verify server is running
    assert os.path.exists("unreal_mcp.pid")
    with open("unreal_mcp.pid", "r") as f:
        pid = int(f.read().strip())
    assert os.path.exists(f"/proc/{pid}")  # This will only work on Unix-like systems


def test_stop_server():
    """Test the stop-server command"""
    result = subprocess.run(["mcp.bat", "stop-server"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "MCP server stopped" in result.stdout
    assert not os.path.exists("unreal_mcp.pid")


def test_restart_server():
    """Test the restart-server command"""
    result = subprocess.run(
        ["mcp.bat", "restart-server"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "Starting MCP server" in result.stdout
    assert os.path.exists("unreal_mcp.pid")


def test_test_server():
    """Test the test-server command"""
    result = subprocess.run(["mcp.bat", "test-server"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Running test server" in result.stdout


def test_test_client():
    """Test the test-client command"""
    # Start the server first
    subprocess.run(["mcp.bat", "start-server"], capture_output=True)
    time.sleep(1)  # Wait for server to start

    # Run the test client
    result = subprocess.run(["mcp.bat", "test-client"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Running test client" in result.stdout


def test_setup_game():
    """Test the setup-game command"""
    # Start the server first
    subprocess.run(["mcp.bat", "start-server"], capture_output=True)
    time.sleep(1)  # Wait for server to start

    # Run the setup-game command
    result = subprocess.run(["mcp.bat", "setup-game"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Setting up game mode" in result.stdout


def test_clean():
    """Test the clean command"""
    # Create some temporary files
    with open("unreal_mcp.log", "w") as f:
        f.write("test log")
    with open("unreal_mcp.pid", "w") as f:
        f.write("12345")

    # Run the clean command
    result = subprocess.run(["mcp.bat", "clean"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Cleanup complete" in result.stdout
    assert not os.path.exists("unreal_mcp.log")
    assert not os.path.exists("unreal_mcp.pid")


def test_config_loading():
    """Test that the configuration is loaded correctly"""
    assert config.get("server.host") == "127.0.0.1"
    assert config.get("server.port") == 55557
    assert config.get("logging.level") == "INFO"


def test_config_env_vars():
    """Test that environment variables override config file"""
    os.environ["MCP_SERVER_HOST"] = "0.0.0.0"
    os.environ["MCP_SERVER_PORT"] = "55558"

    # Reload config
    config._load_env_vars()

    assert config.get("server.host") == "0.0.0.0"
    assert config.get("server.port") == 55558


if __name__ == "__main__":
    pytest.main([__file__])
