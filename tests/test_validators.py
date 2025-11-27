import pytest

from csv_tool.validators import validate_files_exist


def test_validate_files_not_exist():
    with pytest.raises(FileNotFoundError):
        validate_files_exist(["nonexistent_file.csv"])


def test_validate_multiple_files_not_exist():
    with pytest.raises(FileNotFoundError) as exc_info:
        validate_files_exist(["nonexistent1.csv", "nonexistent2.csv"])
    error_message = str(exc_info.value)
    assert "nonexistent1.csv" in error_message
    assert "nonexistent2.csv" in error_message
