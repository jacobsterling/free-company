import sys
import os
import logging
import signal
from typing import Dict, Any

from .server import MCPServer
from .registry import CommandRegistry
from .mcp_utils import (
    CommandTypes,
    get_actors_in_level,
    find_actors_by_name,
    create_actor,
    delete_actor,
    set_actor_transform,
    get_actor_properties,
    add_actor_to_level,
    focus_viewport,
    take_screenshot,
    create_level,
    save_level,
    refresh_content_browser,
    create_blueprint,
    add_component_to_blueprint,
    set_component_property,
    set_physics_properties,
    compile_blueprint,
    spawn_blueprint_actor,
    set_blueprint_property,
    set_static_mesh_properties,
    connect_blueprint_nodes,
    add_input_mapping,
    add_blueprint_node,
    set_level_game_mode,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("unreal_mcp.log"), logging.StreamHandler()],
)
logger = logging.getLogger("MCP.Main")


def register_commands(registry: CommandRegistry):
    """Register all command handlers"""
    # Actor commands
    registry.register(CommandTypes.GET_ACTORS_IN_LEVEL, get_actors_in_level)
    registry.register(CommandTypes.FIND_ACTORS_BY_NAME, find_actors_by_name)
    registry.register(CommandTypes.CREATE_ACTOR, create_actor)
    registry.register(CommandTypes.DELETE_ACTOR, delete_actor)
    registry.register(CommandTypes.SET_ACTOR_TRANSFORM, set_actor_transform)
    registry.register(CommandTypes.GET_ACTOR_PROPERTIES, get_actor_properties)
    registry.register(CommandTypes.ADD_ACTOR, add_actor_to_level)

    # Editor commands
    registry.register(CommandTypes.FOCUS_VIEWPORT, focus_viewport)
    registry.register(CommandTypes.TAKE_SCREENSHOT, take_screenshot)
    registry.register(CommandTypes.CREATE_LEVEL, create_level)
    registry.register(CommandTypes.SAVE_LEVEL, save_level)
    registry.register(CommandTypes.REFRESH_CONTENT_BROWSER, refresh_content_browser)

    # Blueprint commands
    registry.register(CommandTypes.CREATE_BLUEPRINT, create_blueprint)
    registry.register(
        CommandTypes.ADD_COMPONENT_TO_BLUEPRINT, add_component_to_blueprint
    )
    registry.register(CommandTypes.SET_COMPONENT_PROPERTY, set_component_property)
    registry.register(CommandTypes.SET_PHYSICS_PROPERTIES, set_physics_properties)
    registry.register(CommandTypes.COMPILE_BLUEPRINT, compile_blueprint)
    registry.register(CommandTypes.SPAWN_BLUEPRINT_ACTOR, spawn_blueprint_actor)
    registry.register(CommandTypes.SET_BLUEPRINT_PROPERTY, set_blueprint_property)
    registry.register(
        CommandTypes.SET_STATIC_MESH_PROPERTIES, set_static_mesh_properties
    )

    # Blueprint node commands
    registry.register(CommandTypes.CONNECT_BLUEPRINT_NODES, connect_blueprint_nodes)
    registry.register(CommandTypes.ADD_INPUT_MAPPING, add_input_mapping)
    registry.register(CommandTypes.ADD_BLUEPRINT_NODE, add_blueprint_node)

    # Game commands
    registry.register(CommandTypes.SET_LEVEL_GAME_MODE, set_level_game_mode)

    logger.info("All commands registered successfully")


def main():
    """Main entry point for the MCP server"""
    try:
        # Create command registry
        registry = CommandRegistry()
        register_commands(registry)

        # Create and start server
        server = MCPServer()

        # Register command handlers
        for command_type in registry.list_commands():
            server.register_command(command_type, registry.get_handler(command_type))

        # Handle shutdown signals
        def handle_shutdown(signum, frame):
            logger.info("Shutdown signal received")
            server.stop()
            sys.exit(0)

        signal.signal(signal.SIGINT, handle_shutdown)
        signal.signal(signal.SIGTERM, handle_shutdown)

        # Start server
        server.start()

    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
