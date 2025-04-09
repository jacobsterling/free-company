import sys
import os
import json
import logging
import importlib.util
import time

# Add the scripts directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our utility module
from mcp_utils import ensure_server_running, logger


def import_module_from_file(file_path):
    """
    Import a module from a file path.

    Args:
        file_path (str): The path to the file

    Returns:
        module: The imported module
    """
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def setup_project():
    """
    Set up the entire project by running all setup scripts in the correct order.
    """
    logger.info("Setting up project...")

    # Check if the server is running
    if not ensure_server_running():
        logger.error(
            "MCP server is not running. Please start the server before running this script."
        )
        return

    # Define the setup scripts to run in order
    setup_scripts = [
        "create_test_level",
        "setup_character_blueprint",
        "setup_input_mappings",
        "setup_character_input",
        "setup_game_mode",
    ]

    # Run each setup script
    for script_name in setup_scripts:
        script_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), f"{script_name}.py"
        )

        if not os.path.exists(script_path):
            logger.warning(f"Setup script {script_name}.py not found. Skipping.")
            continue

        logger.info(f"Running setup script: {script_name}.py")

        try:
            # Import the module
            module = import_module_from_file(script_path)

            # Get the main function name (assuming it's the same as the script name)
            main_function_name = script_name

            # Check if the function exists
            if hasattr(module, main_function_name):
                # Call the function
                getattr(module, main_function_name)()
            else:
                logger.warning(
                    f"Main function {main_function_name} not found in {script_name}.py. Skipping."
                )

            # Wait a bit between scripts to allow the server to process
            time.sleep(1)

        except Exception as e:
            logger.error(f"Error running setup script {script_name}.py: {str(e)}")

    logger.info("Project setup complete")


if __name__ == "__main__":
    setup_project()
