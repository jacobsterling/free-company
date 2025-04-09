import requests
import json


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


def setup_character_mesh():
    """Set up the character mesh and components."""
    print("Setting up character mesh and components...")

    # Set the character mesh
    result = send_command(
        "SetComponentProperty",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "Mesh",
            "propertyName": "SkeletalMesh",
            "propertyValue": "/Engine/EngineMeshes/SkeletalMeshes/SK_Mannequin.SK_Mannequin",
        },
    )
    print(f"Setting character mesh: {json.dumps(result, indent=2)}")

    # Set the arms mesh
    result = send_command(
        "SetComponentProperty",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "ArmsMesh",
            "propertyName": "SkeletalMesh",
            "propertyValue": "/Engine/EngineMeshes/SkeletalMeshes/SK_Mannequin_Arms.SK_Mannequin_Arms",
        },
    )
    print(f"Setting arms mesh: {json.dumps(result, indent=2)}")

    # Set the animation blueprint
    result = send_command(
        "SetComponentProperty",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "Mesh",
            "propertyName": "AnimClass",
            "propertyValue": "/Engine/EngineMeshes/SkeletalMeshes/Animations/UE4_Mannequin_AnimBP.UE4_Mannequin_AnimBP_C",
        },
    )
    print(f"Setting animation blueprint: {json.dumps(result, indent=2)}")

    # Set the arms animation blueprint
    result = send_command(
        "SetComponentProperty",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "ArmsMesh",
            "propertyName": "AnimClass",
            "propertyValue": "/Engine/EngineMeshes/SkeletalMeshes/Animations/UE4_Mannequin_Arms_AnimBP.UE4_Mannequin_Arms_AnimBP_C",
        },
    )
    print(f"Setting arms animation blueprint: {json.dumps(result, indent=2)}")

    # Set character movement properties
    result = send_command(
        "SetComponentProperty",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "CharacterMovement",
            "propertyName": "bUseControllerDesiredRotation",
            "propertyValue": True,
        },
    )
    print(f"Setting character movement properties: {json.dumps(result, indent=2)}")

    # Set auto-possess player
    result = send_command(
        "SetComponentProperty",
        {
            "blueprintName": "BP_FCCharacter",
            "componentName": "Character",
            "propertyName": "AutoPossessPlayer",
            "propertyValue": "Player0",
        },
    )
    print(f"Setting auto-possess player: {json.dumps(result, indent=2)}")

    print("Character mesh and components setup complete")


if __name__ == "__main__":
    setup_character_mesh()
