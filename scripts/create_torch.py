import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.blueprint_tools import create_blueprint, add_component


def create_torch_blueprint():
    print("Creating torch blueprint...")

    # Create the torch blueprint
    result = create_blueprint("BP_FCTorch", "FCTorch")
    print(json.dumps(result, indent=2))

    if not result.get("success"):
        print("Failed to create torch blueprint")
        sys.exit(1)

    # Add point light component
    add_component(
        "BP_FCTorch",
        "PointLightComponent",
        "TorchLight",
        location=(0, 0, 50),
        scale=(1, 1, 1),
    )

    # Add particle system component
    add_component(
        "BP_FCTorch",
        "ParticleSystemComponent",
        "TorchParticleSystem",
        location=(0, 0, 0),
        scale=(1, 1, 1),
    )

    # Add audio component
    add_component(
        "BP_FCTorch",
        "AudioComponent",
        "TorchAudio",
        location=(0, 0, 0),
        scale=(1, 1, 1),
    )

    print("Torch blueprint creation complete")


if __name__ == "__main__":
    create_torch_blueprint()
