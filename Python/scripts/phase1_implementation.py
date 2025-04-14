#!/usr/bin/env python
"""
Main implementation script for Free Company Phase 1
Executes the implementation steps in sequence:
1. Project Setup and Structure
2. First-Person Character Controller
"""

import sys
import os
import logging
import importlib.util
import time

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("Phase1Implementation")


def import_module_from_file(module_name, file_path):
    """Import a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    """Main function to run the implementation steps."""
    logger.info("Starting Free Company Phase 1 Implementation...")

    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Step 1: Project Setup and Structure
    logger.info("Step 1: Project Setup and Structure")
    project_setup_path = os.path.join(current_dir, "project_setup.py")
    try:
        project_setup = import_module_from_file("project_setup", project_setup_path)
        project_setup.main()
        logger.info("Step 1 completed successfully!")
    except Exception as e:
        logger.error(f"Error in Step 1: {e}")
        return

    # Wait a moment before proceeding to the next step
    time.sleep(2)

    # Step 2: First-Person Character Controller
    logger.info("Step 2: First-Person Character Controller")
    character_controller_path = os.path.join(current_dir, "first_person_controller.py")
    try:
        character_controller = import_module_from_file(
            "first_person_controller", character_controller_path
        )
        character_controller.main()
        logger.info("Step 2 completed successfully!")
    except Exception as e:
        logger.error(f"Error in Step 2: {e}")
        return

    logger.info("Phase 1 Implementation Steps 1 and 2 completed successfully!")


if __name__ == "__main__":
    main()
