import sys
import os
import json

# Add the scripts directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our utility module
from mcp_utils import ensure_server_running, add_blueprint_node, logger


def setup_character_input():
    """
    Set up input handling for the character blueprint.
    """
    logger.info("Setting up character input...")

    # Check if the server is running
    if not ensure_server_running():
        logger.error(
            "MCP server is not running. Please start the server before running this script."
        )
        return

    # Define the blueprint name
    blueprint_name = "BP_FCCharacter"

    # Define the input nodes to add
    input_nodes = [
        # Movement inputs
        {
            "node_type": "InputAxis",
            "node_name": "MoveForward",
            "location": {"x": 0, "y": 0},
            "connections": [
                {
                    "target": "AddMovementInput",
                    "target_pin": "WorldDirection",
                    "source_pin": "AxisValue",
                }
            ],
        },
        {
            "node_type": "InputAxis",
            "node_name": "MoveRight",
            "location": {"x": 200, "y": 0},
            "connections": [
                {
                    "target": "AddMovementInput",
                    "target_pin": "WorldDirection",
                    "source_pin": "AxisValue",
                }
            ],
        },
        # Looking inputs
        {
            "node_type": "InputAxis",
            "node_name": "Turn",
            "location": {"x": 0, "y": 200},
            "connections": [
                {
                    "target": "AddControllerYawInput",
                    "target_pin": "Value",
                    "source_pin": "AxisValue",
                }
            ],
        },
        {
            "node_type": "InputAxis",
            "node_name": "LookUp",
            "location": {"x": 200, "y": 200},
            "connections": [
                {
                    "target": "AddControllerPitchInput",
                    "target_pin": "Value",
                    "source_pin": "AxisValue",
                }
            ],
        },
        # Action inputs
        {
            "node_type": "InputAction",
            "node_name": "Jump",
            "location": {"x": 0, "y": 400},
            "connections": [
                {"target": "Jump", "target_pin": "Execute", "source_pin": "Pressed"}
            ],
        },
        {
            "node_type": "InputAction",
            "node_name": "Sprint",
            "location": {"x": 200, "y": 400},
            "connections": [
                {
                    "target": "StartSprint",
                    "target_pin": "Execute",
                    "source_pin": "Pressed",
                },
                {
                    "target": "StopSprint",
                    "target_pin": "Execute",
                    "source_pin": "Released",
                },
            ],
        },
        {
            "node_type": "InputAction",
            "node_name": "Interact",
            "location": {"x": 0, "y": 600},
            "connections": [
                {"target": "Interact", "target_pin": "Execute", "source_pin": "Pressed"}
            ],
        },
        {
            "node_type": "InputAction",
            "node_name": "PrimaryAttack",
            "location": {"x": 200, "y": 600},
            "connections": [
                {
                    "target": "StartPrimaryAttack",
                    "target_pin": "Execute",
                    "source_pin": "Pressed",
                },
                {
                    "target": "StopPrimaryAttack",
                    "target_pin": "Execute",
                    "source_pin": "Released",
                },
            ],
        },
        {
            "node_type": "InputAction",
            "node_name": "SecondaryAction",
            "location": {"x": 400, "y": 600},
            "connections": [
                {
                    "target": "StartSecondaryAction",
                    "target_pin": "Execute",
                    "source_pin": "Pressed",
                },
                {
                    "target": "StopSecondaryAction",
                    "target_pin": "Execute",
                    "source_pin": "Released",
                },
            ],
        },
    ]

    # Add each input node
    for node in input_nodes:
        result = add_blueprint_node(blueprint_name=blueprint_name, **node)

        if result:
            logger.info(
                f"Added {node['node_type']} node '{node['node_name']}': {json.dumps(result, indent=2)}"
            )
        else:
            logger.error(
                f"Failed to add {node['node_type']} node '{node['node_name']}'"
            )
            return

    logger.info("Character input setup complete")


if __name__ == "__main__":
    setup_character_input()
