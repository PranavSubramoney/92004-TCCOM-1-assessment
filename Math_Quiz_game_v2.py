import random

# Function to generate a random math question based on the chosen operation
def generate_question(operation):
    if operation == '+':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
    elif operation == '-':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, num1)
        correct_answer = num1 - num2
    elif operation == '*':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2
    else:  # For division
        num2 = random.randint(2, 10)  # Ensure num2 is not 1, and limit to 10 for num2
        max_quotient = 30 // num2  # Increase the range for num1 to avoid consistent results of 1
        num1 = random.randint(2, max_quotient) * num2  # num1 is a multiple of num2
        correct_answer = num1 // num2  # Calculate correct answer using integer division
    return num1, operation, num2, correct_answer

# Function to check if the user's answer is correct
def check_answer(num1, operator, num2, user_answer, correct_answer):
    if operator in ['+', '-', '*']:
        return user_answer == correct_answer
    elif operator == '/':
        return user_answer == correct_answer  # Check if user's answer matches correct answer exactly

# Main routine
def math_quiz(num_questions, operations):
    print(f"You've chosen {operations} operation.\n")
    score = 0
    for i in range(num_questions):
        num1, operator, num2, correct_answer = generate_question(operations)
        print(f"Question {i + 1}: What is {num1} {operator} {num2}?")

        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)  # Convert user input to integer
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        if check_answer(num1, operator, num2, user_answer, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")
    print(f"You scored {score} out of {num_questions}.\n")

# Main routine starts here
# Ask for the number of questions per round or infinite mode
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

To begin, decide how many rounds you want to play or test yourself in infinite mode. If you choose
infinite mode, you'll play until you decide to stop.Enter your desired amount of rounds and 
questions per round.

Solve the Problems:
You can choose one of the four basic operations: Addition, Subtraction, Multiplication and Division
Yuo will be able to change your operation every round so you don't get bored of one operation. 

If you answer incorrectly, we'll gently steer you in the right direction with the correct answer.
You can exit the quiz during any round. Just enter "xxx" as your answer and the quiz will end.

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

num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")
num_questions_per_round = int_check("How many questions would you like per round? ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = float('inf')  # Set number of rounds to infinity

while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n ️♾️️️️🔄 Round {rounds_played + 1} of (Infinite mode) 🔄♾️"
    else:
        rounds_heading = f"\n🕒🕒🕒 Round {rounds_played + 1} 🕒🕒🕒"

    print(rounds_heading)
    print()

    rounds_played += 1

    # Asking for operation for each round if not in infinite mode
    if mode != "infinite":
        while True:
            operation = input("Which operation do you want? (+, -, *, /): ")
            if operation in ['+', '-', '*', '/']:
                break
            else:
                print("Invalid operation! Please choose either +, -, *, or /.")
    else:
        while True:
            operation = input("You're in infinite mode. Which operation do you want? (+, -, *, /): ")
            if operation in ['+', '-', '*', '/']:
                break
            else:
                print("Invalid operation! Please choose either '+', '-', '*', or '/'.")

    math_quiz(num_questions_per_round, operation)

print("Thanks for playing!")
