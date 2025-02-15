from models import Employee, Assignment
from file_handler import FileHandler
from utils import Utils
import random

class SecretSanta:
    """Main class to handle Secret Santa allocation."""

    def __init__(self, employees_file, previous_assignments_file=None):
        self.employees = FileHandler.load_employees(employees_file)
        self.previous_assignments = FileHandler.load_previous_assignments(previous_assignments_file, self.employees) if previous_assignments_file else {}

    def assign_santa(self):
        """Assigns Secret Santa while ensuring no repeats from previous years."""
        employees = self.employees[:]
        available_recipients = set(employees)
        assignments = []

        Utils.shuffle_list(employees)

        for santa in employees:
            valid_recipients = Utils.get_valid_recipients(santa, available_recipients, self.previous_assignments)

            if not valid_recipients:
                raise ValueError(f"Unable to assign Secret Santa for {santa.name}. Retry with a new shuffle.")

            child = random.choice(valid_recipients)
            assignments.append(Assignment(santa, child))
            available_recipients.remove(child)

        return assignments

    def save_assignments(self, output_file):
        """Saves assignments to a file."""
        assignments = self.assign_santa()
        FileHandler.save_assignments(output_file, assignments)
