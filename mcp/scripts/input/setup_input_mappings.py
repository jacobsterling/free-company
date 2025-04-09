import sys
import os
import json

# Add the scripts directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our utility module
from mcp_utils import ensure_server_running, add_input_mapping, logger


def setup_input_mappings():
    """
    Set up input mappings for the character.
    """
    logger.info("Setting up input mappings...")

    # Check if the server is running
    if not ensure_server_running():
        logger.error(
            "MCP server is not running. Please start the server before running this script."
        )
        return

    # Define the input mappings
    input_mappings = [
        # Movement
        {"name": "MoveForward", "positive_key": "W", "negative_key": "S", "scale": 1.0},
        {"name": "MoveRight", "positive_key": "D", "negative_key": "A", "scale": 1.0},
        {"name": "Turn", "positive_key": "MouseX", "scale": 1.0},
        {
            "name": "LookUp",
            "positive_key": "MouseY",
            "scale": -1.0,
        },  # Inverted for natural feel
        # Actions
        {"name": "Jump", "positive_key": "SpaceBar"},
        {"name": "Sprint", "positive_key": "LeftShift"},
        {"name": "Interact", "positive_key": "E"},
        {"name": "PrimaryAttack", "positive_key": "LeftMouseButton"},
        {"name": "SecondaryAction", "positive_key": "RightMouseButton"},
    ]

    # Add each input mapping
    for mapping in input_mappings:
        result = add_input_mapping(**mapping)

        if result:
            logger.info(
                f"Added input mapping {mapping['name']}: {json.dumps(result, indent=2)}"
            )
        else:
            logger.error(f"Failed to add input mapping {mapping['name']}")
            return

    logger.info("Input mappings setup complete")


if __name__ == "__main__":
    setup_input_mappings()
