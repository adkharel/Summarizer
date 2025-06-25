import os
from box import BoxValueError
from box import Box
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: str) -> Box:
    """Read a YAML file and return its content as a Box object.
    Args:
        path_to_yaml (str): Path to the YAML file.
        Raises:
        ValueError: If the YAML file is empty or not in the correct format.
        e: empty file or not in the correct format."""
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read YAML file: {path_to_yaml}.")
            return Box(content)
    except BoxValueError:
        raise ValueError("yaml file is empty or not in the correct format.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: str, verbose=True) -> None:
    """Create directories if they do not exist.

    Args:
        path_to_directories (str): Path to the directories to be created.
        """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}.")