import sys
import os
import json

# Add the scripts directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our utility module
from mcp_utils import ensure_server_running, add_actor_to_level, logger


def create_test_level():
    """
    Create a test level with basic actors.
    """
    logger.info("Creating test level...")

    # Check if the server is running
    if not ensure_server_running():
        logger.error(
            "MCP server is not running. Please start the server before running this script."
        )
        return

    # Define the actors to add
    actors = [
        # Floor
        {
            "actor_class": "StaticMeshActor",
            "name": "Floor",
            "location": {"x": 0, "y": 0, "z": 0},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 10, "y": 10, "z": 1},
        },
        # Player character
        {
            "actor_class": "BP_FCCharacter",
            "name": "PlayerCharacter",
            "location": {"x": 0, "y": 0, "z": 100},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
        # Main light
        {
            "actor_class": "DirectionalLight",
            "name": "MainLight",
            "location": {"x": 0, "y": 0, "z": 1000},
            "rotation": {"pitch": -45, "yaw": -45, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
        # Sky light
        {
            "actor_class": "SkyLight",
            "name": "SkyLight",
            "location": {"x": 0, "y": 0, "z": 1000},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
    ]

    # Add each actor
    for actor in actors:
        result = add_actor_to_level(**actor)

        if result:
            logger.info(f"Added actor {actor['name']}: {json.dumps(result, indent=2)}")
        else:
            logger.error(f"Failed to add actor {actor['name']}")
            return

    logger.info("Test level created successfully")


if __name__ == "__main__":
    create_test_level()
