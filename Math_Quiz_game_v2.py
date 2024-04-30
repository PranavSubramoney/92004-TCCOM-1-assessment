import random

# Global variable to store round history
round_history = []


def choose_difficulty():
    print("Choose a difficulty level:")
    print("1.🟩 Easy (1-10)")
    print("2.⬜ Normal (1-20)")
    print("3.🟨 Hard (1-100)")
    print("4.🟥 Extra Hard (1-1000)")

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
        return choose_difficulty()


# Function to generate a random math question based on the chosen operation and range of numbers
def generate_question(operations, num_range):
    operation = random.choice(operations)
    if operation == '+':
        num1 = random.randint(num_range[0], num_range[1])
        num2 = random.randint(num_range[0], num_range[1])
        correct_answer = num1 + num2
    elif operation == '-':
        num1 = random.randint(num_range[0], num_range[1])
        num2 = random.randint(num_range[0], num1)
        correct_answer = num1 - num2
    elif operation == '*':
        num1 = random.randint(num_range[0], num_range[1])
        num2 = random.randint(num_range[0], num_range[1])
        correct_answer = num1 * num2
    else:  # For division
        num2 = random.randint(1, 10)  # Ensure num2 is not 1, and limit to 10 for num2
        max_quotient = num_range[1] // num2  # Increase the range for num1 to avoid consistent results of 1
        num1 = random.randint(num_range[0], max_quotient) * num2  # num1 is a multiple of num2
        correct_answer = num1 // num2  # Calculate correct answer using integer division
    return num1, operation, num2, correct_answer


# Function to check if the user's answer is correct
def check_answer(num1, operator, num2, user_answer, correct_answer):
    if operator in ['+', '-', '*', '/']:
        return user_answer == correct_answer
    else:
        return False  # Handle unknown operation


# Main routine
def math_quiz(num_questions, operations, num_range, round_number):
    print(f"You've chosen {operations} operation(s) with numbers in the range {num_range}.\n")
    score = 0
    round_history.clear()  # Clear round history for each new round
    for i in range(num_questions):
        num1, operator, num2, correct_answer = generate_question(operations, num_range)
        print(f"Question {i + 1}: What is {num1} {operator} {num2}?")

        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == "quit":  # Check if user wants to quit
                return False
            try:
                user_answer = int(user_answer)  # Convert user input to integer
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        is_correct = check_answer(num1, operator, num2, user_answer, correct_answer)
        round_history.append((round_number, i + 1, num1, operator, num2, user_answer, is_correct))  # Add round history
        if is_correct:
            print("🟩Correct!\n")
            score += 1
        else:
            print(f"🟥Wrong! The correct answer is {correct_answer}\n")
    print(f"You scored {score} out of {num_questions}.\n")
    return True


# Integer checker function
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return True
        if response == "no" or response == "n":
            return False
        else:
            print("Please enter either yes or no")


def instructions():
    print('''
    *** Instructions ***
Hey there! Welcome to the Math Quiz.
To begin, decide how many rounds you want to play or test yourself in infinite mode.
If you choose infinite mode, you'll play until you decide to stop. Just press Enter for infinite mode.
Solve the Problems:
You can choose one of the four basic operations: Addition, Subtraction, Multiplication and Division.
You will be able to change your operation every round so you don't get bored of one operation.
If you answer incorrectly, we'll gently steer you in the right direction with the correct answer.
You can exit the quiz during any round. Just enter "quit" as your answer and the quiz will end.
Check Your Progress:
Curious to see how you did? Look at your progress at the end of the game with the Quiz History option.
Good luck!
    ''')


print()
print('''
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
    ✦   🔢🔢🔢  Welcome to the Math Quiz! 🔢🔢🔢    ✦
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
  ''')
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions:
    instructions()

mode = "regular"
rounds_played = 0
operations = ['+', '-', '*', '/']
all_round_history = []  # Store history for all rounds

# Ask for the number of rounds
while True:
    print()
    num_rounds_input = int_check("How many rounds would you like? Press Enter for infinite mode: ")
    if num_rounds_input == "infinite":
        num_rounds = float('inf')
        mode = "infinite"
        if mode == "infinite":
            print("You have chosen infinite mode!")
        break
    else:
        num_rounds = num_rounds_input
        mode = "regular"
        if mode == "regular":
            print(f"You have chosen {num_rounds_input} rounds.")
        break

while True:
    while True:
        num_questions_per_round_input = input("How many questions would you like per round? ")
        try:
            num_questions_per_round = int(num_questions_per_round_input)
            if num_questions_per_round < 1:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    print(f"You have chosen {num_questions_per_round} questions.")
    break

while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n ️♾️️️️🔄 Round {rounds_played + 1} of (Infinite mode) 🔄♾️"
    else:
        rounds_heading = f"\n🕒🕒🕒 Round {rounds_played + 1} 🕒🕒🕒"

    print(rounds_heading)
    print()

    rounds_played += 1

    # Asking for operation for each round
    while True:
        operation_choice = input("Which operation do you want? (+, -, *, /, random): ").lower()
        if operation_choice in ['+', '-', '*', '/', 'random']:
            if operation_choice == 'random':
                operations = ['+', '-', '*', '/']  # Include all operations
            else:
                operations = [operation_choice]
            break
        else:
            print("Invalid operation! Please choose either +, -, *, /, or random.")

    num_range = (1, choose_difficulty())  # Ask for difficulty for each round

    # Start the quiz for the current round
    if not math_quiz(num_questions_per_round, operations, num_range, rounds_played):
        # If user quits mid-round, add the round history to all rounds history
        all_round_history.extend(round_history)
        break  # Break the loop if user quits

    # Add round history to all rounds history
    all_round_history.extend(round_history)

# Print history for all rounds
print()
show_history = yes_no("⏪ Do you want to see the round history? ⏪ ")
if show_history:
    if len(all_round_history) == 0:
        print("There is no history to show.")
    else:
        print("\nRound History:")
        current_round = 0
        for round_data in all_round_history:
            round_number, question_number, num1, operator, num2, user_answer, is_correct = round_data
            if round_number != current_round:
                print(f"\nRound {round_number}:")
                current_round = round_number
            result = "Correct" if is_correct else "Incorrect"
            print(f"Question {question_number}: {num1} {operator} {num2} = {user_answer} ({result})")

print()
print("Thanks for playing!")
