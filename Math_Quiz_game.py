import random


# Function to generate a random math question based on the chosen operation and range of numbers
def generate_question(operation, num_range):
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
        num2 = random.randint(2, 10)  # Ensure num2 is not 1, and limit to 10 for num2
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


# Function to get user's preferred range of numbers
def get_number_range():
    while True:
        try:
            min_num = int(input("Enter the minimum number for the range: "))
            while True:
                max_num = int(input("Enter the maximum number for the range (larger than 20): "))
                if max_num > 20:
                    break
                else:
                    print("Maximum number should be larger than 20. Please try again.")
            if min_num >= max_num:
                print("Minimum number should be less than maximum number. Please try again.")
            else:
                return min_num, max_num
        except ValueError:
            print("Invalid input! Please enter valid integers.")


# Main routine
def math_quiz(num_questions, operations, num_range):
    print(f"You've chosen {operations} operation with numbers in the range {num_range}.\n")
    score = 0
    for i in range(num_questions):
        num1, operator, num2, correct_answer = generate_question(operations, num_range)
        print(f"Question {i + 1}: What is {num1} {operator} {num2}?")

        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)  # Convert user input to integer
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        if check_answer(num1, operator, num2, user_answer, correct_answer):
            print("🟩Correct!\n")
            score += 1
        else:
            print(f"🟥Wrong! The correct answer is {correct_answer}\n")
    print(f"You scored {score} out of {num_questions}.\n")


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

custom_parameters = yes_no("Do you want to use custom parameters for the game? ")

if custom_parameters:
    min_num, max_num = get_number_range()
else:
    min_num, max_num = 1, 10

mode = "regular"
rounds_played = 0

# Ask for the number of rounds
while True:
    num_rounds_input = input("How many rounds would you like to play? Press Enter for infinite mode: ")
    if num_rounds_input == "":
        num_rounds = float('inf')
        mode = "infinite"
        break
    elif num_rounds_input.isdigit():
        num_rounds = int(num_rounds_input)
        mode = "regular"
        break
    else:
        print("Invalid input! Please press Enter for infinite mode or enter an integer for normal rounds.")

while True:
    num_questions_per_round_input = input("How many questions would you like per round? ")
    if num_questions_per_round_input.isdigit():
        num_questions_per_round = int(num_questions_per_round_input)
        break
    else:
        print("Invalid input! Please enter an integer for the number of questions per round.")

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
        operation = input("Which operation do you want? (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation! Please choose either +, -, *, or /.")

    math_quiz(num_questions_per_round, operation, (min_num, max_num))

print("Thanks for playing!")
