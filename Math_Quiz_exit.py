import random

# Stores question history
question_history = []

# Stores total points scored for each difficulty level
difficulty_points = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Diabolic': 0}

# Stores total number of questions answered for each difficulty level
difficulty_questions_answered = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Diabolic': 0}

# Updates total points for each difficulty level if correct
def update_difficulty_points(difficulty_level, points):
    difficulty_points[difficulty_level] += points

# Determines the difficulty based on number range
def difficulty_name(difficulty_range):
    if difficulty_range == 10:
        return 'Easy'
    elif difficulty_range == 20:
        return 'Normal'
    elif difficulty_range == 100:
        return 'Hard'
    elif difficulty_range == 1000:
        return 'Diabolic'

# Main routine
def math_quiz(num_questions, ops, num_range):
    correct_answers = 0
    num_correct = 0
    num_incorrect = 0
    question_history.clear()
    difficulty_name_str = difficulty_name(num_range[1])
    points_per_question = 1  # Simplified for testing

    if num_questions == "infinite":
        num_questions_placeholder = 10 ** 9
    else:
        num_questions_placeholder = int(num_questions)

    difficulty_questions_answered[difficulty_name_str] += num_questions_placeholder

    for i in range(num_questions_placeholder):
        print(f"\nQuestion {i + 1}:")

        user_input = input("Your answer: ")

        if user_input.lower() == "quit":
            print("You have quit the quiz.")
            total_points = correct_answers * points_per_question
            update_difficulty_points(difficulty_name_str, total_points)
            return False, num_correct, num_incorrect

        # Simulated correct/incorrect answer checking
        # This part is simplified since the focus is on testing the exit feature
        if user_input == "correct":
            correct_answers += 1
            num_correct += 1
        else:
            num_incorrect += 1

    total_questions = "infinite" if num_questions == "infinite" else num_questions_placeholder
    score = correct_answers * points_per_question
    update_difficulty_points(difficulty_name_str, score)
    return True, num_correct, num_incorrect

# Integer checker function
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more, or push enter for infinite questions."

        to_check = input(question)

        if to_check.strip() == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine starts here
print()
print('''
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
    ✦   🔢🔢🔢  Welcome to the Math Quiz! 🔢🔢🔢    ✦
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
  ''')
print()

# Ask for the number of questions
print()
num_questions = int_check("How many questions would you like? Enter a number or push enter for an infinite amount: ")
if num_questions == "":
    print("You chose infinite questions.")
else:
    print(f"You chose {num_questions} questions.")
# Asks for operation
operations = ['+', '-', '*', '/']
difficulty_value, difficulty_str = 10, 'Easy'  # Default difficulty for testing
num_range = (1, difficulty_value)

# Starts quiz
result, num_correct, num_incorrect = math_quiz(num_questions, operations, num_range)
