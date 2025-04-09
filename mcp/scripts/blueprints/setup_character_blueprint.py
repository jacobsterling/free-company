import sys
import os
import json
import requests

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def send_command(command_type, params):
    try:
        response = requests.post(
            "http://127.0.0.1:55557/command",
            json={"command": command_type, "params": params},
        )
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def setup_character_blueprint():
    print("Setting up character blueprint...")

    # Create the character blueprint
    command = {
        "blueprintName": "BP_FCCharacter",
        "parentClass": "Character",
        "path": "/Game/Blueprints/Character",
    }
    result = send_command("CreateBlueprint", command)
    print(f"Created character blueprint: {json.dumps(result, indent=2)}")

    # Add components
    components = [
        {"name": "CameraComponent", "type": "CameraComponent"},
        {"name": "SpringArmComponent", "type": "SpringArmComponent"},
        {"name": "CapsuleComponent", "type": "CapsuleComponent"},
        {"name": "MeshComponent", "type": "SkeletalMeshComponent"},
    ]

    for component in components:
        command = {
            "blueprintName": "BP_FCCharacter",
            "componentName": component["name"],
            "componentType": component["type"],
        }
        result = send_command("AddComponent", command)
        print(f"Added {component['name']}: {json.dumps(result, indent=2)}")

    print("Character blueprint setup complete")


if __name__ == "__main__":
    setup_character_blueprint()
