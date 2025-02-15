from secret_santa import SecretSanta

if __name__ == "__main__":
    santa = SecretSanta('data/employees.csv', 'data/previous_assignments.csv')
    santa.save_assignments('data/new_assignments.csv')
    print("🎅 Secret Santa assignments saved successfully in data folder!")
