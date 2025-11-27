import sys

from csv_tool.cli import parse_args
from csv_tool.file_reader import read_csv
from csv_tool.report_generator import generate_performance_report
from csv_tool.validators import validate_files_exist


def main():
    try:
        args = parse_args()
        validate_files_exist(args.files)
        data = read_csv(args.files)
        if args.report == "performance":
            print(generate_performance_report(data))
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
