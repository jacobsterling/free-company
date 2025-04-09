import sys
import os
import json
import time
import traceback

# Add the parent directory to the path so we can import the blueprint_tools module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.blueprint_tools import send_command


def add_actors_to_level():
    print("Adding actors to existing TestLevel...")

    try:
        # Add a floor
        print("Sending AddActor command for floor...")
        result = send_command(
            "AddActor",
            {
                "actorClass": "StaticMeshActor",
                "actorName": "Floor",
                "location": {"x": 0, "y": 0, "z": 0},
                "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
                "scale": {"x": 10, "y": 10, "z": 1},
                "staticMesh": "/Engine/BasicShapes/Plane.Plane",
            },
        )
        print(f"Add floor result: {json.dumps(result, indent=2)}")

        # Add a player character
        print("Sending AddActor command for player character...")
        result = send_command(
            "AddActor",
            {
                "actorClass": "BP_FCCharacter",
                "actorName": "PlayerCharacter",
                "location": {"x": 0, "y": 0, "z": 100},
                "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
                "scale": {"x": 1, "y": 1, "z": 1},
            },
        )
        print(f"Add player character result: {json.dumps(result, indent=2)}")

        # Add a directional light
        print("Sending AddActor command for directional light...")
        result = send_command(
            "AddActor",
            {
                "actorClass": "DirectionalLight",
                "actorName": "MainLight",
                "location": {"x": 0, "y": 0, "z": 1000},
                "rotation": {"pitch": -45, "yaw": -45, "roll": 0},
                "scale": {"x": 1, "y": 1, "z": 1},
            },
        )
        print(f"Add directional light result: {json.dumps(result, indent=2)}")

        # Add a sky light
        print("Sending AddActor command for sky light...")
        result = send_command(
            "AddActor",
            {
                "actorClass": "SkyLight",
                "actorName": "SkyLight",
                "location": {"x": 0, "y": 0, "z": 0},
                "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
                "scale": {"x": 1, "y": 1, "z": 1},
            },
        )
        print(f"Add sky light result: {json.dumps(result, indent=2)}")

        print("Actors added to TestLevel successfully!")
        print("\nTo view the level:")
        print("1. Open Unreal Editor")
        print("2. Go to File > Open Level")
        print("3. Navigate to Content/Maps/TestLevel")
        print("4. Click Open")

    except Exception as e:
        print(f"Error adding actors to level: {str(e)}")
        traceback.print_exc()


if __name__ == "__main__":
    add_actors_to_level()
