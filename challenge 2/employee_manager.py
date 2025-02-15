import pandas as pd

class EmployeeManager:
    def __init__(self, employees_file, previous_assignments_file=None):
        self.employees_file = employees_file
        self.previous_assignments_file = previous_assignments_file
        self.employees = self.load_employees()
        self.previous_assignments = self.load_previous_assignments() if previous_assignments_file else {}

    def load_employees(self):
        try:
            df = pd.read_csv(self.employees_file)
            return list(df.itertuples(index=False, name=None))
        except FileNotFoundError:
            raise Exception(f"Error: {self.employees_file} not found.")

    def load_previous_assignments(self):
        try:
            df = pd.read_csv(self.previous_assignments_file)
            assignments = {}

            # Get current employee names
            current_employees = set(name for name, _ in self.employees)

            for _, row in df.iterrows():
                employee_name = row["Employee_Name"]
                child_name = row["Secret_Child_Name"]

                # Ensure the employee is still present in the current year
                if employee_name not in current_employees:
                    print(f"⚠️ Warning: {employee_name} from last year is not in this year's list. Skipping...")
                    continue  # Skip employees not in this year's list

                if employee_name not in assignments:
                    assignments[employee_name] = []
                assignments[employee_name].append(child_name)

            print("\nFiltered Previous Assignments:", assignments)  # Debugging output
            return assignments
        except FileNotFoundError:
            return {}
