from typing import Dict, Any, Type, Callable
import logging
from .mcp_utils import CommandTypes

logger = logging.getLogger("MCP.Registry")


class CommandRegistry:
    """Registry for managing MCP commands"""

    def __init__(self):
        self._commands: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {}
        self._command_types = CommandTypes()

    def register(
        self, command_type: str, handler: Callable[[Dict[str, Any]], Dict[str, Any]]
    ):
        """Register a command handler"""
        if command_type in self._commands:
            logger.warning(
                f"Overwriting existing handler for command type: {command_type}"
            )
        self._commands[command_type] = handler
        logger.info(f"Registered handler for command type: {command_type}")

    def unregister(self, command_type: str):
        """Unregister a command handler"""
        if command_type in self._commands:
            del self._commands[command_type]
            logger.info(f"Unregistered handler for command type: {command_type}")

    def get_handler(
        self, command_type: str
    ) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
        """Get the handler for a command type"""
        handler = self._commands.get(command_type)
        if not handler:
            raise KeyError(f"No handler registered for command type: {command_type}")
        return handler

    def has_handler(self, command_type: str) -> bool:
        """Check if a handler exists for a command type"""
        return command_type in self._commands

    def list_commands(self) -> list:
        """List all registered command types"""
        return list(self._commands.keys())

    def validate_command(self, command: Dict[str, Any]) -> bool:
        """Validate a command"""
        command_type = command.get("type")
        if not command_type:
            return False
        return command_type in self._commands

    def execute(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a command"""
        command_type = command.get("type")
        if not command_type:
            raise ValueError("No command type specified")

        handler = self.get_handler(command_type)
        return handler(command.get("params", {}))
