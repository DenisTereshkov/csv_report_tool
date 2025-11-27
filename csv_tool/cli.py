import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Генератор отчётов по файлам csv"
    )
    parser.add_argument(
        "--files", required=True, nargs="+", help="Путь к файлам csv"
    )
    parser.add_argument(
        "--report", required=True, choices=["performance"], help="Тип отчёта"
    )
    return parser.parse_args()
