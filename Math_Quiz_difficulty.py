# Function to choose difficulty level
def choose_difficulty():
    # Prompts users to choose difficulty
    print("Choose a difficulty level:")
    print("🟩 Easy (1-10)")
    print("🟨 Normal (1-20)")
    print("🟥 Hard (1-100)")
    print("💀 Diabolic (1-1000)")

    while True:
        choice = input("Choose a difficulty level: ").strip().lower()

        if choice in ['e', 'easy']:
            return 10, 'Easy'
        elif choice in ['n', 'normal']:
            return 20, 'Normal'
        elif choice in ['h', 'hard']:
            return 100, 'Hard'
        elif choice in ['d', 'diabolic']:
            return 1000, 'Diabolic'
        else:
            print("Invalid choice. Please enter a valid item from the list.")


# Call the function to choose difficulty
difficulty_range, difficulty_name = choose_difficulty()

# Now you can use the difficulty_range and difficulty_name variables in your code
print(f"Difficulty chosen: {difficulty_name} (1-{difficulty_range})")
