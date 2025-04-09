"""
Configuration module for MCP.
"""

import os
import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("MCP.Config")

# Default configuration
DEFAULT_CONFIG = {
    "server": {
        "host": "127.0.0.1",
        "port": 55557,
        "max_connections": 5,
        "buffer_size": 4096,
        "timeout": 5.0,
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file": "unreal_mcp.log",
        "max_size": 10485760,  # 10MB
        "backup_count": 5,
    },
    "commands": {
        "max_retries": 3,
        "retry_delay": 1.0,
        "socket_timeout": 5.0,
    },
    "paths": {
        "pid_file": "unreal_mcp.pid",
        "log_dir": "logs",
        "temp_dir": "temp",
    },
}


class Config:
    """Configuration manager for MCP"""

    def __init__(self, config_file: Optional[str] = None):
        self.config = DEFAULT_CONFIG.copy()
        self.config_file = config_file or os.getenv(
            "MCP_CONFIG_FILE", "mcp_config.json"
        )
        self._load_config()
        self._load_env_vars()

    def _load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    file_config = json.load(f)
                self._update_dict(self.config, file_config)
                logger.info(f"Loaded configuration from {self.config_file}")
            except Exception as e:
                logger.error(f"Error loading config file: {e}")

    def _load_env_vars(self):
        """Load configuration from environment variables"""
        env_prefix = "MCP_"
        for key, value in os.environ.items():
            if key.startswith(env_prefix):
                config_key = key[len(env_prefix) :].lower()
                self._set_config_value(config_key, value)

    def _set_config_value(self, key: str, value: Any):
        """Set a configuration value using dot notation"""
        keys = key.split("_")
        current = self.config
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        current[keys[-1]] = self._parse_value(value)

    def _parse_value(self, value: str) -> Any:
        """Parse string values into appropriate types"""
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def _update_dict(self, target: Dict, source: Dict):
        """Recursively update a dictionary"""
        for key, value in source.items():
            if (
                key in target
                and isinstance(target[key], dict)
                and isinstance(value, dict)
            ):
                self._update_dict(target[key], value)
            else:
                target[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value using dot notation"""
        keys = key.split(".")
        current = self.config
        for k in keys:
            if not isinstance(current, dict) or k not in current:
                return default
            current = current[k]
        return current

    def set(self, key: str, value: Any):
        """Set a configuration value using dot notation"""
        self._set_config_value(key, value)

    def save(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.config, f, indent=4)
            logger.info(f"Saved configuration to {self.config_file}")
        except Exception as e:
            logger.error(f"Error saving config file: {e}")

    def reset(self):
        """Reset configuration to defaults"""
        self.config = DEFAULT_CONFIG.copy()
        self._load_env_vars()
        logger.info("Reset configuration to defaults")


# Global configuration instance
config = Config()
