from typing import NamedTuple

class Employee(NamedTuple):
    """Data structure to hold employee details."""
    name: str
    email: str

class Assignment(NamedTuple):
    """Data structure to store Secret Santa pairings."""
    santa: Employee
    child: Employee
