import requests
import json


def send_command(command, params):
    base_url = "http://127.0.0.1:8000"
    try:
        response = requests.post(
            f"{base_url}/command", json={"command": command, "params": params}
        )
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def setup_game_mode():
    print("Setting up game mode...")

    # Create game mode blueprint if it doesn't exist
    result = send_command(
        "create_blueprint",
        {
            "name": "BP_FCGameMode",
            "parent_class": "GameModeBase",
        },
    )
    print("Creating game mode blueprint:", json.dumps(result, indent=2))

    # Set default pawn class to our character
    result = send_command(
        "set_blueprint_property",
        {
            "blueprintName": "BP_FCGameMode",
            "propertyName": "DefaultPawnClass",
            "propertyValue": "/Game/Blueprints/Character/BP_FCCharacter",
        },
    )
    print("Setting default pawn class:", json.dumps(result, indent=2))

    # Set the game mode in the level
    result = send_command(
        "SetLevelGameMode",
        {
            "levelName": "TestLevel",
            "gameMode": "/Game/Blueprints/BP_FCGameMode",
        },
    )
    print("Setting level game mode:", json.dumps(result, indent=2))

    print("Game mode setup complete")


if __name__ == "__main__":
    setup_game_mode()
