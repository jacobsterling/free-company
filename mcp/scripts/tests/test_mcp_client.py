import requests
import json
import time


def test_mcp_server():
    base_url = "http://127.0.0.1:8000"

    try:
        # Test 1: Check server status
        print("\nTest 1: Checking server status...")
        response = requests.get(f"{base_url}/status")
        print(f"Server status: {json.dumps(response.json(), indent=2)}")

        # Test 2: Create a Blueprint
        print("\nTest 2: Creating Blueprint...")
        response = requests.post(
            f"{base_url}/command",
            json={
                "command": "CreateBlueprint",
                "params": {"name": "TestBlueprint", "parentClass": "Actor"},
            },
        )
        print(f"Response: {json.dumps(response.json(), indent=2)}")

        # Test 3: Add a component
        print("\nTest 3: Adding component...")
        response = requests.post(
            f"{base_url}/command",
            json={
                "command": "AddComponent",
                "params": {
                    "blueprintName": "TestBlueprint",
                    "componentType": "StaticMeshComponent",
                    "componentName": "TestMesh",
                    "location": [0, 0, 0],
                    "rotation": [0, 0, 0],
                    "scale": [1, 1, 1],
                },
            },
        )
        print(f"Response: {json.dumps(response.json(), indent=2)}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    test_mcp_server()
