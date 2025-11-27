import pytest


@pytest.fixture
def sample_csv():
    return "tests/test_data/sample1.csv"


@pytest.fixture
def another_sample_csv():
    return "tests/test_data/sample2.csv"
