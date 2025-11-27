from csv_tool.file_reader import read_csv
from csv_tool.report_generator import generate_performance_report


def test_generate_performance_report(sample_csv):
    data = read_csv([sample_csv])
    report = generate_performance_report(data)
    assert isinstance(report, str)
    assert "Position" in report
    assert "Average Performance" in report


def test_generate_performance_report_multiple_files(
    sample_csv,
    another_sample_csv
):
    data = read_csv([sample_csv, another_sample_csv])
    report = generate_performance_report(data)
    assert isinstance(report, str)
    assert "Backend Developer" in report
    assert "Data Scientist" in report
