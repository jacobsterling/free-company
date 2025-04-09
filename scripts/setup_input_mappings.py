import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.blueprint_tools import add_input_mapping


def setup_input_mappings():
    print("Setting up input mappings...")

    # Define input mappings
    input_mappings = [
        {"name": "MoveForward", "type": "Axis", "scale": 1.0, "keys": ["W", "S"]},
        {"name": "MoveRight", "type": "Axis", "scale": 1.0, "keys": ["D", "A"]},
        {"name": "Turn", "type": "Axis", "scale": 1.0, "keys": ["MouseX"]},
        {"name": "LookUp", "type": "Axis", "scale": -1.0, "keys": ["MouseY"]},
        {"name": "Jump", "type": "Action", "keys": ["SpaceBar"]},
        {"name": "Sprint", "type": "Action", "keys": ["LeftShift"]},
        {"name": "Interact", "type": "Action", "keys": ["E"]},
        {"name": "PrimaryAttack", "type": "Action", "keys": ["LeftMouseButton"]},
        {"name": "SecondaryAction", "type": "Action", "keys": ["RightMouseButton"]},
    ]

    # Add each input mapping
    for mapping in input_mappings:
        # For Axis mappings, include scale; for Action mappings, don't include scale
        if mapping["type"] == "Axis":
            result = add_input_mapping(
                mapping["name"],
                mapping["type"],
                mapping.get("scale", 1.0),
                mapping["keys"],
            )
        else:  # Action type
            result = add_input_mapping(
                mapping["name"], mapping["type"], 1.0, mapping["keys"]
            )

        print(f"Setting up {mapping['name']}:", json.dumps(result, indent=2))

        if not result.get("success"):
            print(f"Failed to set up {mapping['name']}")
            sys.exit(1)

    print("Input mappings setup complete")


if __name__ == "__main__":
    setup_input_mappings()
