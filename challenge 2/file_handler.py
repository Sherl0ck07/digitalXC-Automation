import pandas as pd
from models import Employee

class FileHandler:
    """Handles reading and writing CSV files."""

    @staticmethod
    def load_employees(file_path: str):
        """Loads employees from CSV and returns a list of Employee objects."""
        try:
            df = pd.read_csv(file_path)
            return [Employee(row["Employee_Name"], row["Employee_EmailID"]) for _, row in df.iterrows()]
        except Exception as e:
            raise ValueError(f"Error reading employees file: {e}")

    @staticmethod
    def load_previous_assignments(file_path: str, current_employees):
        """Loads previous assignments and filters only valid employees."""
        try:
            df = pd.read_csv(file_path)
            valid_names = {emp.name for emp in current_employees}
            assignments = {}

            for _, row in df.iterrows():
                santa_name = row["Employee_Name"]
                child_name = row["Secret_Child_Name"]

                if santa_name in valid_names and child_name in valid_names:
                    assignments.setdefault(santa_name, set()).add(child_name)

            return assignments
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_assignments(file_path: str, assignments):
        """Saves Secret Santa assignments to a CSV file."""
        df = pd.DataFrame(
            [(s.santa.name, s.santa.email, s.child.name, s.child.email) for s in assignments],
            columns=['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        )
        df.to_csv(file_path, index=False)
