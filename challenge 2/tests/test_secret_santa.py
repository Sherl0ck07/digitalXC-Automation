import unittest
from secret_santa import SecretSanta

class TestSecretSanta(unittest.TestCase):
    def test_assignments_count(self):
        """Ensure every employee gets exactly one Secret Santa."""
        santa = SecretSanta('data/employees.csv', 'data/previous_assignments.csv')
        assignments = santa.assign_santa()
        self.assertEqual(len(assignments), len(santa.employees))

    def test_no_self_assignment(self):
        """Ensure no one is assigned themselves."""
        santa = SecretSanta('data/employees.csv', 'data/previous_assignments.csv')
        assignments = santa.assign_santa()
        for assignment in assignments:
            self.assertNotEqual(assignment.santa.name, assignment.child.name)

if __name__ == '__main__':
    unittest.main()
