import json
import socket
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_command(command_type: str, params: dict) -> dict:
    """Send a command to the MCP server and return the response"""
    try:
        # Create socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 55557))

        # Prepare command
        command = {"type": command_type, "params": params}

        # Send command
        sock.send(json.dumps(command).encode("utf-8"))

        # Receive response
        response = sock.recv(4096).decode("utf-8")
        return json.loads(response)

    except Exception as e:
        logger.error(f"Error sending command: {e}")
        return {"error": str(e)}
    finally:
        sock.close()


def setup_game_mode():
    """Set up the game mode with the player character as default pawn"""
    try:
        # Create game mode blueprint
        result = send_command(
            "CreateBlueprint",
            {
                "name": "BP_FCGameMode",
                "parentClass": "GameModeBase",
                "path": "/Game/Blueprints",
            },
        )

        if "error" in result:
            logger.error(f"Failed to create game mode blueprint: {result['error']}")
            return False

        # Set default pawn class
        result = send_command(
            "SetDefaultPawnClass",
            {
                "gameMode": "/Game/Blueprints/BP_FCGameMode",
                "pawnClass": "/Game/Blueprints/Character/BP_FCCharacter",
            },
        )

        if "error" in result:
            logger.error(f"Failed to set default pawn class: {result['error']}")
            return False

        # Set game mode for level
        result = send_command(
            "SetLevelGameMode",
            {"levelName": "TestLevel", "gameMode": "/Game/Blueprints/BP_FCGameMode"},
        )

        if "error" in result:
            logger.error(f"Failed to set level game mode: {result['error']}")
            return False

        logger.info("Game mode setup completed successfully")
        return True

    except Exception as e:
        logger.error(f"Game mode setup failed: {e}")
        return False


if __name__ == "__main__":
    setup_game_mode()
