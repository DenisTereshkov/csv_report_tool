import os
from typing import List


def validate_files_exist(file_paths: List[str]) -> None:
    not_existing_files_paths = []
    for file_path in file_paths:
        if not os.path.exists(file_path):
            not_existing_files_paths.append(file_path)
    if not_existing_files_paths:
        raise FileNotFoundError(
            f"Файл(ы) не найден(ы): {''.join(not_existing_files_paths)}"
        )
