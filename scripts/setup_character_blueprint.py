import requests
import json
import time


def send_command(command_type, params):
    """Send a command to the MCP server and return the response."""
    url = "http://localhost:8000/command"
    data = {"command": command_type, "params": params}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error sending command: {e}")
        return None


def setup_character_blueprint():
    """Set up the character blueprint with necessary nodes."""
    print("Setting up character blueprint nodes...")

    # First, create the character blueprint
    print("Creating character blueprint...")
    create_blueprint_result = send_command(
        "create_blueprint",
        {
            "blueprintName": "BP_FCCharacter",
            "parentClass": "Character",
            "folderPath": "/Game/Blueprints/Character",
        },
    )
    print(
        f"Creating character blueprint: {json.dumps(create_blueprint_result, indent=2)}"
    )

    # Add necessary components to the blueprint
    print("Adding components to character blueprint...")
    add_mesh_component = send_command(
        "add_component_to_blueprint",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "Mesh",
            "componentClass": "SkeletalMeshComponent",
        },
    )
    print(f"Adding Mesh component: {json.dumps(add_mesh_component, indent=2)}")

    add_arms_mesh_component = send_command(
        "add_component_to_blueprint",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "ArmsMesh",
            "componentClass": "SkeletalMeshComponent",
        },
    )
    print(f"Adding ArmsMesh component: {json.dumps(add_arms_mesh_component, indent=2)}")

    # Add character movement component
    add_movement_component = send_command(
        "add_component_to_blueprint",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "CharacterMovement",
            "componentClass": "CharacterMovementComponent",
        },
    )
    print(
        f"Adding CharacterMovement component: {json.dumps(add_movement_component, indent=2)}"
    )

    # Now add the input nodes
    print("Setting up input nodes...")

    # Movement inputs
    move_forward_result = send_command(
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
    print(f"Setting up forward movement: {json.dumps(move_forward_result, indent=2)}")

    move_right_result = send_command(
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
    print(f"Setting up right movement: {json.dumps(move_right_result, indent=2)}")

    # Action inputs
    jump_result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "Jump",
            "location": [0, 200],
            "connections": {"Pressed": {"targetNode": "Jump", "targetPin": "Execute"}},
        },
    )
    print(f"Setting up jump: {json.dumps(jump_result, indent=2)}")

    sprint_result = send_command(
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
    print(f"Setting up sprint: {json.dumps(sprint_result, indent=2)}")

    interact_result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "Interact",
            "location": [0, 400],
            "connections": {
                "Pressed": {"targetNode": "Interact", "targetPin": "Execute"}
            },
        },
    )
    print(f"Setting up interact: {json.dumps(interact_result, indent=2)}")

    primary_attack_result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "PrimaryAttack",
            "location": [300, 400],
            "connections": {
                "Pressed": {"targetNode": "PrimaryAttack", "targetPin": "Execute"}
            },
        },
    )
    print(f"Setting up primary attack: {json.dumps(primary_attack_result, indent=2)}")

    secondary_action_result = send_command(
        "AddBlueprintNode",
        {
            "blueprintName": "BP_FCCharacter",
            "nodeType": "InputAction",
            "nodeName": "SecondaryAction",
            "location": [0, 600],
            "connections": {
                "Pressed": {"targetNode": "SecondaryAction", "targetPin": "Execute"}
            },
        },
    )
    print(
        f"Setting up secondary action: {json.dumps(secondary_action_result, indent=2)}"
    )

    print("Character blueprint setup complete")


if __name__ == "__main__":
    setup_character_blueprint()
