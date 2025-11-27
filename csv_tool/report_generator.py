from collections import defaultdict
from typing import List

from tabulate import tabulate

from .models import EmployeeRow


def generate_performance_report(data: List[EmployeeRow]):
    groups = defaultdict(list)
    for row in data:
        groups[row.position].append(row)
    report_data = []
    for position, employees in groups.items():
        total_performance = sum([e.performance for e in employees])
        avg_performance = total_performance / len(employees)
        report_data.append([position, round(avg_performance, 2)])
    headers = ["Position", "Average Performance"]
    report_data.sort(key=lambda x: x[1], reverse=True)
    return tabulate(report_data, headers=headers, tablefmt="grid")
