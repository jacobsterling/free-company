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


def setup_character_input():
    print("Setting up character input nodes...")

    # Add input handling for movement
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAxis",
            "nodeName": "MoveForward",
            "location": [0, 0],
            "connections": {
                "AxisValue": {
                    "targetNode": "AddMovementInput",
                    "targetPin": "ScaleValue",
                }
            },
        },
    )
    print("Setting up forward movement:", json.dumps(result, indent=2))

    # Add input handling for right movement
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAxis",
            "nodeName": "MoveRight",
            "location": [300, 0],
            "connections": {
                "AxisValue": {
                    "targetNode": "AddMovementInput",
                    "targetPin": "ScaleValue",
                }
            },
        },
    )
    print("Setting up right movement:", json.dumps(result, indent=2))

    # Add input handling for looking around (Turn)
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAxis",
            "nodeName": "Turn",
            "location": [0, 100],
            "connections": {
                "AxisValue": {
                    "targetNode": "AddControllerYawInput",
                    "targetPin": "Val",
                }
            },
        },
    )
    print("Setting up turn:", json.dumps(result, indent=2))

    # Add input handling for looking up/down
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAxis",
            "nodeName": "LookUp",
            "location": [300, 100],
            "connections": {
                "AxisValue": {
                    "targetNode": "AddControllerPitchInput",
                    "targetPin": "Val",
                }
            },
        },
    )
    print("Setting up look up:", json.dumps(result, indent=2))

    # Add jump input handling
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "Jump",
            "location": [0, 200],
            "connections": {"Pressed": {"targetNode": "Jump", "targetPin": "Execute"}},
        },
    )
    print("Setting up jump:", json.dumps(result, indent=2))

    # Add sprint input handling
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "Sprint",
            "location": [300, 200],
            "connections": {
                "Pressed": {"targetNode": "StartSprint", "targetPin": "Execute"},
                "Released": {"targetNode": "StopSprint", "targetPin": "Execute"},
            },
        },
    )
    print("Setting up sprint:", json.dumps(result, indent=2))

    # Add interact input handling
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "Interact",
            "location": [0, 300],
            "connections": {
                "Pressed": {"targetNode": "Interact", "targetPin": "Execute"}
            },
        },
    )
    print("Setting up interact:", json.dumps(result, indent=2))

    # Add primary attack input handling
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "PrimaryAttack",
            "location": [300, 300],
            "connections": {
                "Pressed": {"targetNode": "StartPrimaryAttack", "targetPin": "Execute"},
                "Released": {"targetNode": "StopPrimaryAttack", "targetPin": "Execute"},
            },
        },
    )
    print("Setting up primary attack:", json.dumps(result, indent=2))

    # Add secondary action input handling
    result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "SecondaryAction",
            "location": [0, 400],
            "connections": {
                "Pressed": {
                    "targetNode": "StartSecondaryAction",
                    "targetPin": "Execute",
                },
                "Released": {
                    "targetNode": "StopSecondaryAction",
                    "targetPin": "Execute",
                },
            },
        },
    )
    print("Setting up secondary action:", json.dumps(result, indent=2))

    print("Character input setup complete")


if __name__ == "__main__":
    setup_character_input()
