#!/usr/bin/env python
"""
Tests for the MCP configuration module.
"""

import os
import json
import tempfile
import pytest
from pathlib import Path
import sys

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.config import Config, DEFAULT_CONFIG


def test_default_config():
    """Test that the default configuration is loaded correctly"""
    config = Config()
    assert config.get("server.host") == "127.0.0.1"
    assert config.get("server.port") == 55557
    assert config.get("logging.level") == "INFO"


def test_custom_config_file():
    """Test loading a custom configuration file"""
    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        custom_config = {"server": {"host": "0.0.0.0", "port": 55558}}
        json.dump(custom_config, f)
        config_file = f.name

    try:
        # Load the custom configuration
        config = Config(config_file=config_file)
        assert config.get("server.host") == "0.0.0.0"
        assert config.get("server.port") == 55558
        # Default values should still be used for other settings
        assert config.get("logging.level") == "INFO"
    finally:
        # Clean up
        os.unlink(config_file)


def test_env_vars():
    """Test that environment variables override config file"""
    # Set environment variables
    os.environ["MCP_SERVER_HOST"] = "0.0.0.0"
    os.environ["MCP_SERVER_PORT"] = "55558"

    # Create a configuration instance
    config = Config()

    # Check that environment variables override default values
    assert config.get("server.host") == "0.0.0.0"
    assert config.get("server.port") == 55558

    # Clean up
    del os.environ["MCP_SERVER_HOST"]
    del os.environ["MCP_SERVER_PORT"]


def test_set_and_save():
    """Test setting and saving configuration values"""
    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({}, f)
        config_file = f.name

    try:
        # Create a configuration instance
        config = Config(config_file=config_file)

        # Set a value
        config.set("server.host", "0.0.0.0")
        assert config.get("server.host") == "0.0.0.0"

        # Save the configuration
        config.save()

        # Create a new configuration instance with the same file
        new_config = Config(config_file=config_file)
        assert new_config.get("server.host") == "0.0.0.0"
    finally:
        # Clean up
        os.unlink(config_file)


def test_reset():
    """Test resetting configuration to defaults"""
    # Create a configuration instance
    config = Config()

    # Set a value
    config.set("server.host", "0.0.0.0")
    assert config.get("server.host") == "0.0.0.0"

    # Reset the configuration
    config.reset()
    assert config.get("server.host") == "127.0.0.1"


if __name__ == "__main__":
    pytest.main([__file__])
