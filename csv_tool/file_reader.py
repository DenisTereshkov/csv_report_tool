import csv
from typing import List

from .models import EmployeeRow


def read_csv(file_paths: List[str]) -> List[EmployeeRow]:
    employees = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee = EmployeeRow(
                    name=row['name'],
                    position=row['position'],
                    completed_tasks=int(row['completed_tasks']),
                    performance=float(row['performance']),
                    skils=row['skils'],
                    team=row['team'],
                    expirience_years=int(row['expirience_years'])
                )
                employees.append(employee)
    return employees
