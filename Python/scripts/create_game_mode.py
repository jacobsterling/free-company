#!/usr/bin/env python
"""
Game Mode Setup Script for Free Company
- Creates a GameMode blueprint
- Sets BP_FirstPersonCharacter as the default pawn
- Sets the GameMode as default for the project
"""

import sys
import os
import socket
import json
import logging
from typing import Dict, Any, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("GameModeSetup")


def send_mcp_command(command: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Send a command to the Unreal MCP server with automatic socket lifecycle management."""
    sock = None
    try:
        # Create a new socket for each command
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 55557))

        # Create command object
        command_obj = {"type": command, "params": params}

        # Convert to JSON and send
        command_json = json.dumps(command_obj)
        logger.info(f"Sending command: {command_json}")
        sock.sendall(command_json.encode("utf-8"))

        # Receive response
        chunks = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)

            # Try parsing to see if we have a complete response
            try:
                data = b"".join(chunks)
                json.loads(data.decode("utf-8"))
                # If we can parse it, we have the complete response
                break
            except json.JSONDecodeError:
                # Not a complete JSON object yet, continue receiving
                continue

        # Parse response
        data = b"".join(chunks)
        response = json.loads(data.decode("utf-8"))
        logger.info(f"Received response: {response}")
        return response

    except Exception as e:
        logger.error(f"Error in socket communication: {e}")
        return None
    finally:
        # Always close the socket when done
        if sock:
            sock.close()


def create_blueprint(name: str, parent_class: str) -> bool:
    """Create a blueprint with the given name and parent class."""
    bp_params = {"name": name, "parent_class": parent_class}

    response = send_mcp_command("create_blueprint", bp_params)

    # Check response
    if not response or response.get("status") != "success":
        logger.error(f"Failed to create blueprint: {response}")
        return False

    # Check if blueprint already existed
    if response.get("result", {}).get("already_exists"):
        logger.info(f"Blueprint '{name}' already exists, reusing it")
    else:
        logger.info(f"Blueprint '{name}' created successfully!")

    return True


def set_default_pawn_class(gamemode_name: str, pawn_class_name: str) -> bool:
    """Set the default pawn class for the game mode."""
    params = {
        "blueprint_name": gamemode_name,
        "property_name": "DefaultPawnClass",
        "property_value": pawn_class_name,
    }

    response = send_mcp_command("set_blueprint_class_defaults", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to set default pawn class: {response}")
        return False

    logger.info(f"Default pawn class set to {pawn_class_name} successfully!")
    return True


def set_default_game_mode(gamemode_name: str) -> bool:
    """Set the game mode as default for the project."""
    params = {
        "setting_category": "Project.Maps & Modes",
        "setting_name": "DefaultGameMode",
        "setting_value": gamemode_name,
    }

    response = send_mcp_command("set_project_setting", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to set default game mode: {response}")
        return False

    logger.info(f"Default game mode set to {gamemode_name} successfully!")
    return True


def compile_blueprint(blueprint_name: str) -> bool:
    """Compile the specified blueprint."""
    compile_params = {"blueprint_name": blueprint_name}

    response = send_mcp_command("compile_blueprint", compile_params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to compile blueprint '{blueprint_name}': {response}")
        return False

    logger.info(f"Blueprint '{blueprint_name}' compiled successfully!")
    return True


def set_game_mode_for_current_level(gamemode_name: str) -> bool:
    """Set the game mode for the current level."""
    params = {"property_name": "GameModeOverride", "property_value": gamemode_name}

    response = send_mcp_command("set_world_property", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to set game mode for current level: {response}")
        return False

    logger.info(f"Game mode for current level set to {gamemode_name} successfully!")
    return True


def main():
    """Main function to create a game mode with the first-person character as default pawn."""
    logger.info("Starting game mode setup...")

    # Name of the game mode blueprint to create
    gamemode_name = "BP_FirstPersonGameMode"

    # Create the game mode blueprint
    if not create_blueprint(gamemode_name, "GameModeBase"):
        return

    # Set the default pawn class
    if not set_default_pawn_class(gamemode_name, "BP_FirstPersonCharacter"):
        return

    # Compile the blueprint
    if not compile_blueprint(gamemode_name):
        return

    # Set as default game mode in project settings
    if not set_default_game_mode(gamemode_name):
        logger.warning(
            "Could not set as default game mode in project settings, will try setting for current level only"
        )

    # Also set it for the current level as a fallback
    if not set_game_mode_for_current_level(gamemode_name):
        logger.warning("Could not set game mode for current level")

    logger.info("Game mode setup completed successfully!")
    logger.info("BP_FirstPersonCharacter should now be the default pawn for your game.")
    logger.info("You can now press Play to test the character controller.")


if __name__ == "__main__":
    main()
