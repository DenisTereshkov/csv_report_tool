from dataclasses import dataclass


@dataclass
class EmployeeRow:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: str
    team: str
    experience_years: int
