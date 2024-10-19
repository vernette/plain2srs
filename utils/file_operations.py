import json
import os

from core.constants import OUTPUT_DIR


def check_output_dir() -> None:
    """Check if the output directory exists and create it if it doesn't."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_json(json_data: dict, filename: str = None) -> None:
    """Save JSON data to a file.

    Args:
        json_data (dict): The JSON data to save.
        filename (str, optional): The name of the file to save. Defaults to
            'ruleset.json'.
    """
    check_output_dir()
    with open(f'{OUTPUT_DIR}/{filename}', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
