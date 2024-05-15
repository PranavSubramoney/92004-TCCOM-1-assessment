import random

# Stores total points scored for each difficulty level
difficulty_points = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Extra Hard': 0}

# Stores total number of questions answered for each difficulty level
difficulty_questions_answered = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Extra Hard': 0}


# Function to choose difficulty level
def choose_difficulty():
    # Prompts users to choose difficulty
    print("Choose a difficulty level:")
    print("1. 🟩 Easy (1-10)")
    print("2. ⬜ Normal (1-20)")
    print("3. 🟨 Hard (1-100)")
    print("4. 🟥 Extra Hard (1-1000)")

    while True:
        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            return 10
        elif choice == '2':
            return 20
        elif choice == '3':
            return 100
        elif choice == '4':
            return 1000
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Test the function
if __name__ == "__main__":
    difficulty_range = choose_difficulty()
    print(f"You have chosen the difficulty range: 1-{difficulty_range}")
