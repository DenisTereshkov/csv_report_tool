import pytest

from csv_tool.file_reader import read_csv
from csv_tool.models import EmployeeRow


@pytest.fixture
def sample_csv():
    return "tests/test_data/sample1.csv"


@pytest.fixture
def another_sample_csv():
    return "tests/test_data/sample2.csv"


def test_read_csv(sample_csv):
    employees = read_csv([sample_csv])
    assert len(employees) == 2
    assert isinstance(employees[0], EmployeeRow)
    assert employees[0].name == "Alex Ivanov"
    assert employees[1].name == "Maria Petrova"


def test_read_csv_multiple_files(sample_csv, another_sample_csv):
    employees = read_csv([sample_csv, another_sample_csv])
    assert len(employees) == 4


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_csv(["non_existent_file.csv"])
