import requests
import json
import sys
import os

# Add the parent directory to the path so we can import from tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.blueprint_tools import create_blueprint, add_component


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


def create_character_blueprint():
    """Create the first-person character blueprint with necessary components."""
    print("Creating first-person character blueprint...")

    # Create the blueprint
    result = create_blueprint("BP_FCCharacter", "FCCharacter")
    print("Blueprint creation result:", json.dumps(result, indent=2))

    if not result.get("success", False):
        print("Failed to create blueprint. Exiting.")
        return

    # Add camera component
    result = add_component(
        "BP_FCCharacter",
        "CameraComponent",
        "FirstPersonCamera",
        location=[0, 0, 90],
        rotation=[0, 0, 0],
        scale=[1, 1, 1],
    )
    print("Camera component result:", json.dumps(result, indent=2))

    # Add arms mesh component
    result = add_component(
        "BP_FCCharacter",
        "SkeletalMeshComponent",
        "ArmsMesh",
        location=[0, 0, 0],
        rotation=[0, 0, 0],
        scale=[1, 1, 1],
    )
    print("Arms mesh component result:", json.dumps(result, indent=2))

    print("Character blueprint creation completed.")


if __name__ == "__main__":
    create_character_blueprint()
