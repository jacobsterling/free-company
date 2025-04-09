import sys
import os
import json
import socket
import logging
import time
import subprocess
import signal
from typing import Dict, List, Optional, Union, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("unreal_mcp.log"), logging.StreamHandler()],
)
logger = logging.getLogger("MCP")

# Default server settings
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 55557
SERVER_SCRIPT = "unreal_mcp_server.py"
MAX_RETRIES = 3
RETRY_DELAY = 1.0
SOCKET_TIMEOUT = 5.0


# Command types
class CommandTypes:
    # Actor commands
    GET_ACTORS_IN_LEVEL = "get_actors_in_level"
    FIND_ACTORS_BY_NAME = "find_actors_by_name"
    CREATE_ACTOR = "create_actor"
    DELETE_ACTOR = "delete_actor"
    SET_ACTOR_TRANSFORM = "set_actor_transform"
    GET_ACTOR_PROPERTIES = "get_actor_properties"
    ADD_ACTOR = "AddActor"

    # Editor commands
    FOCUS_VIEWPORT = "focus_viewport"
    TAKE_SCREENSHOT = "take_screenshot"
    CREATE_LEVEL = "CreateLevel"
    SAVE_LEVEL = "SaveLevel"
    REFRESH_CONTENT_BROWSER = "RefreshContentBrowser"

    # Blueprint commands
    CREATE_BLUEPRINT = "create_blueprint"
    ADD_COMPONENT_TO_BLUEPRINT = "add_component_to_blueprint"
    SET_COMPONENT_PROPERTY = "set_component_property"
    SET_PHYSICS_PROPERTIES = "set_physics_properties"
    COMPILE_BLUEPRINT = "compile_blueprint"
    SPAWN_BLUEPRINT_ACTOR = "spawn_blueprint_actor"
    SET_BLUEPRINT_PROPERTY = "set_blueprint_property"
    SET_STATIC_MESH_PROPERTIES = "set_static_mesh_properties"

    # Blueprint node commands
    CONNECT_BLUEPRINT_NODES = "connect_blueprint_nodes"
    CREATE_INPUT_MAPPING = "create_input_mapping"
    ADD_BLUEPRINT_GET_SELF_COMPONENT_REFERENCE = (
        "add_blueprint_get_self_component_reference"
    )
    ADD_BLUEPRINT_SELF_REFERENCE = "add_blueprint_self_reference"
    FIND_BLUEPRINT_NODES = "find_blueprint_nodes"
    ADD_BLUEPRINT_EVENT_NODE = "add_blueprint_event_node"
    ADD_BLUEPRINT_INPUT_ACTION_NODE = "add_blueprint_input_action_node"
    ADD_BLUEPRINT_FUNCTION_NODE = "add_blueprint_function_node"
    ADD_BLUEPRINT_GET_COMPONENT_NODE = "add_blueprint_get_component_node"
    ADD_BLUEPRINT_VARIABLE = "add_blueprint_variable"
    ADD_BLUEPRINT_NODE = "AddBlueprintNode"
    ADD_INPUT_MAPPING = "AddInputMapping"

    # Game commands
    CREATE_CHARACTER_CLASS = "create_character_class"
    CREATE_CHARACTER_INSTANCE = "create_character_instance"
    CREATE_ENEMY_TYPE = "create_enemy_type"
    CREATE_ENEMY_INSTANCE = "create_enemy_instance"
    CREATE_EFFECT_TYPE = "create_effect_type"
    CREATE_EFFECT_INSTANCE = "create_effect_instance"
    CREATE_DUNGEON_TYPE = "create_dungeon_type"
    CREATE_DUNGEON_INSTANCE = "create_dungeon_instance"
    CREATE_BOSS_TYPE = "create_boss_type"
    CREATE_BOSS_INSTANCE = "create_boss_instance"
    CREATE_VAMPIRE_CHARACTER = "create_vampire_character"
    CREATE_VAMPIRE_ENEMY = "create_vampire_enemy"
    CREATE_BLOOD_EFFECT = "create_blood_effect"
    CREATE_VAMPIRE_CASTLE = "create_vampire_castle"
    CREATE_VAMPIRE_LORD = "create_vampire_lord"

    # Level commands
    SET_LEVEL_GAME_MODE = "SetLevelGameMode"


def send_command(
    command: Dict[str, Any], host: str = DEFAULT_HOST, port: int = DEFAULT_PORT
) -> Dict[str, Any]:
    """
    Send a command to the MCP server and wait for a response.

    Args:
        command (Dict[str, Any]): The command to send
        host (str): The host to connect to
        port (int): The port to connect to

    Returns:
        Dict[str, Any]: The server's response

    Raises:
        ConnectionError: If unable to connect to the server
        TimeoutError: If the server doesn't respond in time
    """
    for attempt in range(MAX_RETRIES):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(SOCKET_TIMEOUT)
                sock.connect((host, port))

                # Send the command
                data = json.dumps(command).encode("utf-8")
                sock.sendall(data)

                # Receive the response
                response = b""
                while True:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk

                return json.loads(response.decode("utf-8"))

        except (ConnectionRefusedError, socket.timeout) as e:
            if attempt < MAX_RETRIES - 1:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying...")
                time.sleep(RETRY_DELAY)
            else:
                logger.error(
                    f"Failed to send command after {MAX_RETRIES} attempts: {str(e)}"
                )
                raise ConnectionError(
                    f"Failed to connect to MCP server at {host}:{port}"
                )

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse server response: {str(e)}")
            raise ValueError("Invalid response from server")

        except Exception as e:
            logger.error(f"Unexpected error while sending command: {str(e)}")
            raise


def ensure_server_running(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> bool:
    """
    Check if the MCP server is running and accessible.

    Args:
        host (str): The host to check
        port (int): The port to check

    Returns:
        bool: True if the server is running, False otherwise
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(SOCKET_TIMEOUT)
            sock.connect((host, port))
            return True
    except:
        return False


# Actor Commands
def get_actors_in_level(level_name: str) -> Optional[Dict[str, Any]]:
    """
    Get all actors in a level.

    Args:
        level_name (str): The name of the level

    Returns:
        dict: The response from the server
    """
    command = {"level_name": level_name}
    return send_command(command)


def find_actors_by_name(actor_name: str) -> Optional[Dict[str, Any]]:
    """
    Find actors by name.

    Args:
        actor_name (str): The name of the actor to find

    Returns:
        dict: The response from the server
    """
    command = {"actor_name": actor_name}
    return send_command(command)


def create_actor(
    actor_class: str,
    location: Dict[str, float],
    rotation: Optional[Dict[str, float]] = None,
    scale: Optional[Dict[str, float]] = None,
    name: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """
    Create an actor in the level.

    Args:
        actor_class (str): The class of the actor
        location (dict): The location of the actor (x, y, z)
        rotation (dict, optional): The rotation of the actor (pitch, yaw, roll)
        scale (dict, optional): The scale of the actor (x, y, z)
        name (str, optional): The name of the actor

    Returns:
        dict: The response from the server
    """
    command = {"actor_class": actor_class, "location": location}

    if rotation:
        command["rotation"] = rotation

    if scale:
        command["scale"] = scale

    if name:
        command["name"] = name

    return send_command(command)


def delete_actor(actor_name: str) -> Optional[Dict[str, Any]]:
    """
    Delete an actor from the level.

    Args:
        actor_name (str): The name of the actor to delete

    Returns:
        dict: The response from the server
    """
    command = {"actor_name": actor_name}
    return send_command(command)


def set_actor_transform(
    actor_name: str,
    location: Optional[Dict[str, float]] = None,
    rotation: Optional[Dict[str, float]] = None,
    scale: Optional[Dict[str, float]] = None,
) -> Optional[Dict[str, Any]]:
    """
    Set the transform of an actor.

    Args:
        actor_name (str): The name of the actor
        location (dict, optional): The location of the actor (x, y, z)
        rotation (dict, optional): The rotation of the actor (pitch, yaw, roll)
        scale (dict, optional): The scale of the actor (x, y, z)

    Returns:
        dict: The response from the server
    """
    command = {"actor_name": actor_name}

    if location:
        command["location"] = location

    if rotation:
        command["rotation"] = rotation

    if scale:
        command["scale"] = scale

    return send_command(command)


def get_actor_properties(actor_name: str) -> Optional[Dict[str, Any]]:
    """
    Get the properties of an actor.

    Args:
        actor_name (str): The name of the actor

    Returns:
        dict: The response from the server
    """
    command = {"actor_name": actor_name}
    return send_command(command)


def add_actor_to_level(
    actor_class: str,
    location: Dict[str, float],
    rotation: Optional[Dict[str, float]] = None,
    scale: Optional[Dict[str, float]] = None,
    name: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """
    Add an actor to the level.

    Args:
        actor_class (str): The class of the actor
        location (dict): The location of the actor (x, y, z)
        rotation (dict, optional): The rotation of the actor (pitch, yaw, roll)
        scale (dict, optional): The scale of the actor (x, y, z)
        name (str, optional): The name of the actor

    Returns:
        dict: The response from the server
    """
    command = {"actorClass": actor_class, "location": location}

    if rotation:
        command["rotation"] = rotation

    if scale:
        command["scale"] = scale

    if name:
        command["actorName"] = name

    return send_command(command)


# Editor Commands
def focus_viewport(location: Dict[str, float]) -> Optional[Dict[str, Any]]:
    """
    Focus the viewport on a location.

    Args:
        location (dict): The location to focus on (x, y, z)

    Returns:
        dict: The response from the server
    """
    command = {"location": location}
    return send_command(command)


def take_screenshot(filename: str) -> Optional[Dict[str, Any]]:
    """
    Take a screenshot.

    Args:
        filename (str): The filename to save the screenshot to

    Returns:
        dict: The response from the server
    """
    command = {"filename": filename}
    return send_command(command)


def create_level(
    level_name: str, template: str = "EmptyLevel", save_path: str = None
) -> Optional[Dict[str, Any]]:
    """
    Create a new level.

    Args:
        level_name (str): The name of the level
        template (str, optional): The template to use
        save_path (str, optional): The path to save the level to

    Returns:
        dict: The response from the server
    """
    command = {"levelName": level_name, "template": template}

    if save_path:
        command["savePath"] = save_path

    return send_command(command)


def save_level(level_name: str, save_path: str = None) -> Optional[Dict[str, Any]]:
    """
    Save a level.

    Args:
        level_name (str): The name of the level
        save_path (str, optional): The path to save the level to

    Returns:
        dict: The response from the server
    """
    command = {"levelName": level_name}

    if save_path:
        command["savePath"] = save_path

    return send_command(command)


def refresh_content_browser() -> Optional[Dict[str, Any]]:
    """
    Refresh the content browser.

    Returns:
        dict: The response from the server
    """
    return send_command({})


# Blueprint Commands
def create_blueprint(
    name: str, parent_class: str, path: str
) -> Optional[Dict[str, Any]]:
    """
    Create a new blueprint.

    Args:
        name (str): Name of the blueprint
        parent_class (str): Parent class of the blueprint
        path (str): Path where the blueprint should be created

    Returns:
        Optional[Dict[str, Any]]: The server's response if successful, None otherwise
    """
    command = {
        "type": "CreateBlueprint",
        "params": {"name": name, "parentClass": parent_class, "path": path},
    }

    try:
        return send_command(command)
    except Exception as e:
        logger.error(f"Failed to create blueprint: {str(e)}")
        return None


def add_component_to_blueprint(
    blueprint_name: str, component_class: str, component_name: str
) -> Optional[Dict[str, Any]]:
    """
    Add a component to a blueprint.

    Args:
        blueprint_name (str): The name of the blueprint
        component_class (str): The class of the component
        component_name (str): The name of the component

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "AddComponentToBlueprint",
        "params": {
            "blueprintName": blueprint_name,
            "componentClass": component_class,
            "componentName": component_name,
        },
    }
    return send_command(command)


def set_component_property(
    blueprint_name: str, component_name: str, property_name: str, property_value: Any
) -> Optional[Dict[str, Any]]:
    """
    Set a property on a component.

    Args:
        blueprint_name (str): The name of the blueprint
        component_name (str): The name of the component
        property_name (str): The name of the property
        property_value (any): The value of the property

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "SetComponentProperty",
        "params": {
            "blueprintName": blueprint_name,
            "componentName": component_name,
            "propertyName": property_name,
            "propertyValue": property_value,
        },
    }
    return send_command(command)


def set_physics_properties(
    blueprint_name: str, component_name: str, properties: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """
    Set physics properties on a component.

    Args:
        blueprint_name (str): The name of the blueprint
        component_name (str): The name of the component
        properties (dict): The physics properties to set

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "SetPhysicsProperties",
        "params": {
            "blueprintName": blueprint_name,
            "componentName": component_name,
            "properties": properties,
        },
    }
    return send_command(command)


def compile_blueprint(blueprint_name: str) -> Optional[Dict[str, Any]]:
    """
    Compile a blueprint.

    Args:
        blueprint_name (str): The name of the blueprint

    Returns:
        dict: The response from the server
    """
    command = {"type": "CompileBlueprint", "params": {"blueprintName": blueprint_name}}
    return send_command(command)


def spawn_blueprint_actor(
    blueprint_name: str,
    location: Dict[str, float],
    rotation: Optional[Dict[str, float]] = None,
    scale: Optional[Dict[str, float]] = None,
    name: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """
    Spawn a blueprint actor in the level.

    Args:
        blueprint_name (str): The name of the blueprint
        location (dict): The location of the actor (x, y, z)
        rotation (dict, optional): The rotation of the actor (pitch, yaw, roll)
        scale (dict, optional): The scale of the actor (x, y, z)
        name (str, optional): The name of the actor

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "SpawnBlueprintActor",
        "params": {"blueprintName": blueprint_name, "location": location},
    }

    if rotation:
        command["params"]["rotation"] = rotation

    if scale:
        command["params"]["scale"] = scale

    if name:
        command["params"]["name"] = name

    return send_command(command)


def set_blueprint_property(
    blueprint_name: str, property_name: str, property_value: Any
) -> Optional[Dict[str, Any]]:
    """
    Set a property on a blueprint.

    Args:
        blueprint_name (str): Name of the blueprint
        property_name (str): Name of the property to set
        property_value (Any): Value to set the property to

    Returns:
        Optional[Dict[str, Any]]: The server's response if successful, None otherwise
    """
    command = {
        "type": "SetBlueprintProperty",
        "params": {
            "blueprintName": blueprint_name,
            "propertyName": property_name,
            "propertyValue": property_value,
        },
    }

    try:
        return send_command(command)
    except Exception as e:
        logger.error(f"Failed to set blueprint property: {str(e)}")
        return None


def set_static_mesh_properties(
    blueprint_name: str, component_name: str, properties: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """
    Set static mesh properties on a component.

    Args:
        blueprint_name (str): The name of the blueprint
        component_name (str): The name of the component
        properties (dict): The static mesh properties to set

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "SetStaticMeshProperties",
        "params": {
            "blueprintName": blueprint_name,
            "componentName": component_name,
            "properties": properties,
        },
    }
    return send_command(command)


# Blueprint Node Commands
def connect_blueprint_nodes(
    blueprint_name: str,
    source_node: str,
    target_node: str,
    source_pin: str,
    target_pin: str,
) -> Optional[Dict[str, Any]]:
    """
    Connect two blueprint nodes.

    Args:
        blueprint_name (str): The name of the blueprint
        source_node (str): The name of the source node
        target_node (str): The name of the target node
        source_pin (str): The name of the source pin
        target_pin (str): The name of the target pin

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "ConnectBlueprintNodes",
        "params": {
            "blueprintName": blueprint_name,
            "sourceNode": source_node,
            "targetNode": target_node,
            "sourcePin": source_pin,
            "targetPin": target_pin,
        },
    }
    return send_command(command)


def add_input_mapping(
    name: str, positive_key: str, negative_key: Optional[str] = None, scale: float = 1.0
) -> Optional[Dict[str, Any]]:
    """
    Add an input mapping.

    Args:
        name (str): The name of the input mapping
        positive_key (str): The key for positive input
        negative_key (str, optional): The key for negative input
        scale (float, optional): The scale for the input

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "AddInputMapping",
        "params": {
            "name": name,
            "positiveKey": positive_key,
            "negativeKey": negative_key,
            "scale": scale,
        },
    }
    return send_command(command)


def add_blueprint_node(
    blueprint_name: str,
    node_type: str,
    node_name: str,
    location: Dict[str, float],
    connections: Optional[List[Dict[str, str]]] = None,
) -> Optional[Dict[str, Any]]:
    """
    Add a node to a blueprint.

    Args:
        blueprint_name (str): The name of the blueprint
        node_type (str): The type of the node
        node_name (str): The name of the node
        location (dict): The location of the node (x, y)
        connections (list, optional): The connections of the node

    Returns:
        dict: The response from the server
    """
    command = {
        "type": "AddBlueprintNode",
        "params": {
            "blueprintName": blueprint_name,
            "nodeType": node_type,
            "nodeName": node_name,
            "location": location,
        },
    }

    if connections:
        command["params"]["connections"] = connections

    return send_command(command)


# Game Commands
def set_level_game_mode(level_name: str, game_mode: str) -> Optional[Dict[str, Any]]:
    """
    Set the game mode for a level.

    Args:
        level_name (str): Name of the level
        game_mode (str): Path to the game mode blueprint

    Returns:
        Optional[Dict[str, Any]]: The server's response if successful, None otherwise
    """
    command = {
        "type": "SetLevelGameMode",
        "params": {"levelName": level_name, "gameMode": game_mode},
    }

    try:
        return send_command(command)
    except Exception as e:
        logger.error(f"Failed to set level game mode: {str(e)}")
        return None
