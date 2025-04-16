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


def add_class_variable(
    blueprint_name: str, variable_name: str, variable_type: str, default_value: Any
) -> bool:
    """Add a class variable to the blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "variable_name": variable_name,
        "variable_type": variable_type,
        "default_value": default_value,
        "is_exposed": True,
    }

    response = send_mcp_command("add_blueprint_variable", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add variable {variable_name}: {response}")
        return False

    logger.info(f"Variable {variable_name} added successfully!")
    return True


def add_event_node(
    blueprint_name: str, event_type: str, node_position: list = None
) -> Optional[str]:
    """Add an event node to the blueprint."""
    params = {"blueprint_name": blueprint_name, "event_type": event_type}

    if node_position:
        params["node_position"] = node_position

    response = send_mcp_command("add_blueprint_event_node", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add {event_type} event node: {response}")
        return None

    logger.info(f"{event_type} event node added successfully!")
    return response.get("result", {}).get("node_id")


def add_function_node(
    blueprint_name: str,
    function_name: str,
    target: str = "self",
    params: Dict[str, Any] = None,
    node_position: list = None,
) -> Optional[str]:
    """Add a function node to the blueprint."""
    function_params = {
        "blueprint_name": blueprint_name,
        "function_name": function_name,
        "target": target,
    }

    if params:
        function_params["params"] = params

    if node_position:
        function_params["node_position"] = node_position

    response = send_mcp_command("add_blueprint_function_node", function_params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add function node {function_name}: {response}")
        return None

    logger.info(f"Function node {function_name} added successfully!")
    return response.get("result", {}).get("node_id")


def connect_nodes(
    blueprint_name: str,
    source_node_id: str,
    source_pin: str,
    target_node_id: str,
    target_pin: str,
) -> bool:
    """Connect two nodes in the blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "source_node_id": source_node_id,
        "source_pin": source_pin,
        "target_node_id": target_node_id,
        "target_pin": target_pin,
    }

    response = send_mcp_command("connect_blueprint_nodes", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to connect nodes: {response}")
        return False

    logger.info(f"Nodes connected successfully!")
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


def create_game_mode_with_default_pawn(gamemode_name: str, pawn_class_path: str):
    """Create a game mode blueprint with a specific default pawn class."""
    # Create the blueprint
    if not create_blueprint(gamemode_name, "GameModeBase"):
        return False

    # Try a different approach - create a Construction Script that sets the default pawn class
    logger.info("Setting up Construction Script to set default pawn class...")

    # Add a begin play event
    construction_script_id = add_event_node(
        blueprint_name=gamemode_name,
        event_type="Construction Script",
        node_position=[-400, 0],
    )

    if not construction_script_id:
        logger.error("Failed to add Construction Script event")
        return False

    # Create a Class Reference Variable
    var_name = "DefaultPawnClassRef"
    if not add_class_variable(gamemode_name, var_name, "Class", pawn_class_path):
        return False

    # Add a "Set Default Pawn Class" function node
    # This is a direct approach to modify the DefaultPawnClass property
    set_default_pawn_node_id = add_function_node(
        blueprint_name=gamemode_name,
        function_name="SetDefaultPawnClass",
        target="self",
        params={"InClass": {"class_path": pawn_class_path}},
        node_position=[0, 0],
    )

    if not set_default_pawn_node_id:
        # Try an alternative approach with "Set Class" generic function
        set_default_pawn_node_id = add_function_node(
            blueprint_name=gamemode_name,
            function_name="SetPropertyByName",
            target="self",
            params={
                "PropertyName": "DefaultPawnClass",
                "Value": {"class_path": pawn_class_path},
            },
            node_position=[0, 0],
        )

        if not set_default_pawn_node_id:
            logger.error("Failed to create node to set default pawn class")
            return False

    # Connect the Construction Script to the Set Default Pawn Class function
    if not connect_nodes(
        blueprint_name=gamemode_name,
        source_node_id=construction_script_id,
        source_pin="Then",
        target_node_id=set_default_pawn_node_id,
        target_pin="Execute",
    ):
        return False

    # Add a comment to explain what this does
    comment_params = {
        "blueprint_name": gamemode_name,
        "comment_text": "Sets BP_FirstPersonCharacter as Default Pawn Class",
        "position": [-400, -100],
        "size": [600, 200],
    }

    send_mcp_command("add_blueprint_comment", comment_params)

    # Add a hint for developers - print string to output log
    print_node_id = add_function_node(
        blueprint_name=gamemode_name,
        function_name="PrintString",
        params={
            "InString": f"GameMode using {pawn_class_path} as default pawn",
            "bPrintToLog": True,
        },
        node_position=[250, 0],
    )

    if print_node_id:
        connect_nodes(
            blueprint_name=gamemode_name,
            source_node_id=set_default_pawn_node_id,
            source_pin="Then",
            target_node_id=print_node_id,
            target_pin="Execute",
        )

    # Compile the blueprint
    return compile_blueprint(gamemode_name)


def spawn_blueprint_actor(
    blueprint_name: str, actor_name: str, location: list = None
) -> bool:
    """Spawn an actor from the specified blueprint."""
    spawn_params = {"blueprint_name": blueprint_name, "actor_name": actor_name}

    if location:
        spawn_params["location"] = location
    else:
        spawn_params["location"] = [0.0, 0.0, 100.0]  # Default 100 units up

    response = send_mcp_command("spawn_blueprint_actor", spawn_params)

    if not response or response.get("status") != "success":
        logger.error(
            f"Failed to spawn actor from blueprint '{blueprint_name}': {response}"
        )
        return False

    logger.info(
        f"Actor '{actor_name}' spawned from blueprint '{blueprint_name}' successfully!"
    )
    return True


def main():
    """Main function to create a game mode with the first-person character as default pawn."""
    logger.info("Starting game mode setup...")

    # Name of the game mode blueprint to create
    gamemode_name = "BP_FirstPersonGameMode"

    # Specify the pawn class (using Blueprint path format)
    pawn_class_path = (
        "/Game/Blueprints/BP_FirstPersonCharacter.BP_FirstPersonCharacter_C"
    )

    # Create the game mode with the default pawn class
    if not create_game_mode_with_default_pawn(gamemode_name, pawn_class_path):
        logger.error("Failed to create game mode blueprint with default pawn class")
        return

    # Set as default game mode in project settings
    if not set_default_game_mode(gamemode_name):
        logger.warning(
            "Could not set as default game mode in project settings, will try setting for current level only"
        )

    # Also set it for the current level as a fallback
    if not set_game_mode_for_current_level(gamemode_name):
        logger.warning("Could not set game mode for current level")

    # Spawn the game mode in the level for immediate use
    spawn_blueprint_actor(gamemode_name, "FirstPersonGameMode")

    logger.info("Game mode setup completed successfully!")
    logger.info("BP_FirstPersonCharacter should now be the default pawn for your game.")
    logger.info("You can now press Play to test the character controller.")


if __name__ == "__main__":
    main()
