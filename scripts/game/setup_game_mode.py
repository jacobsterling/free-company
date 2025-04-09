import sys
import os
import logging
import argparse
import socket
import json
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("setup_game_mode.log"), logging.StreamHandler()],
)
logger = logging.getLogger("SetupGameMode")


def send_command(command: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Send a command to the Unreal MCP server and get the response."""
    try:
        # Connect to Unreal MCP server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 55557))

        try:
            # Create command object
            command_obj = {"command": command, "params": params}

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

        finally:
            # Always close the socket
            sock.close()

    except Exception as e:
        logger.error(f"Error sending command: {e}")
        return None


def setup_game_mode(level_name: str, game_mode: str) -> bool:
    """
    Set up the game mode for the specified level.

    Args:
        level_name (str): Name of the level to set up
        game_mode (str): Path to the game mode blueprint

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create the game mode blueprint if it doesn't exist
        blueprint_name = os.path.basename(game_mode)
        blueprint_path = os.path.dirname(game_mode)

        logger.info(f"Creating game mode blueprint: {blueprint_name}")
        result = send_command(
            "create_blueprint",
            {
                "blueprintName": blueprint_name,
                "parentClass": "GameModeBase",
                "path": blueprint_path,
            },
        )

        if not result or not result.get("success"):
            logger.error("Failed to create game mode blueprint")
            return False

        # Set the default pawn class
        logger.info("Setting default pawn class")
        result = send_command(
            "set_blueprint_property",
            {
                "blueprintName": game_mode,
                "propertyName": "DefaultPawnClass",
                "propertyValue": "/Game/Blueprints/Character/BP_FCCharacter",
            },
        )

        if not result or not result.get("success"):
            logger.error("Failed to set default pawn class")
            return False

        # Set the game mode for the level
        logger.info(f"Setting game mode for level: {level_name}")
        result = send_command(
            "SetLevelGameMode", {"levelName": level_name, "gameMode": game_mode}
        )

        if not result or not result.get("success"):
            logger.error("Failed to set level game mode")
            return False

        logger.info("Game mode setup completed successfully")
        return True

    except Exception as e:
        logger.error(f"Error setting up game mode: {e}")
        return False


def main():
    """Main function to set up the game mode."""
    parser = argparse.ArgumentParser(description="Set up game mode for a level")
    parser.add_argument("--level", default="TestLevel", help="Name of the level")
    parser.add_argument(
        "--game-mode",
        default="/Game/Blueprints/BP_FCGameMode",
        help="Path to the game mode blueprint",
    )

    args = parser.parse_args()

    if setup_game_mode(args.level, args.game_mode):
        logger.info("Game mode setup completed successfully")
        sys.exit(0)
    else:
        logger.error("Game mode setup failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
