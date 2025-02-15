import random
from models import Employee

class Utils:
    """Utility functions for randomization and validation."""

    @staticmethod
    def shuffle_list(items):
        """Shuffles a list randomly."""
        random.shuffle(items)
        return items

    @staticmethod
    def get_valid_recipients(employee, available, previous_assignments):
        """Filters valid recipients for a given employee."""
        return [e for e in available if e.name != employee.name and e.name not in previous_assignments.get(employee.name, set())]
