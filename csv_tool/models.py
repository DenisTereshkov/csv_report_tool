from dataclasses import dataclass


@dataclass
class EmployeeRow:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skils: str
    team: str
    expirience_years: int
