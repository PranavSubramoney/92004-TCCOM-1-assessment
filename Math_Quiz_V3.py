import random


# Updates total points for each difficulty level if correct
def update_difficulty_points(difficulty_level, points):
    # increases the points for the chosen difficulty by the given points
    difficulty_points[difficulty_level] += points


# Updates questions answered
def update_difficulty_questions(difficulty_level, num_questions):
    # increases the number of questions answered for the specified difficulty
    difficulty_questions_answered[difficulty_level] += num_questions


# Determines the difficulty based on number range
def difficulty_name(difficulty_range):
    # maps difficulty to their number range
    difficulty_mapping = {10: 'Easy', 20: 'Normal', 100: 'Hard', 1000: 'Diabolic'}
    return difficulty_mapping.get(difficulty_range, 'Unknown')


# Function to choose difficulty level
def choose_difficulty():
    # prints the difficulty options
    print("Choose a difficulty level:")
    print("🟩 Easy (1-10)")
    print("🟨 Normal (1-20)")
    print("🟥 Hard (1-100)")
    print("💀 Diabolic (1-1000)")

    # maps user inputs to difficulty to levels to their corresponding number range
    difficulty_mapping = {
        'e': (10, 'Easy'),
        'easy': (10, 'Easy'),
        'n': (20, 'Normal'),
        'normal': (20, 'Normal'),
        'h': (100, 'Hard'),
        'hard': (100, 'Hard'),
        'd': (1000, 'Diabolic'),
        'diabolic': (1000, 'Diabolic')
    }

    # loop until user provides a valid input
    while True:
        choice = input("Enter the difficulty level: ").strip().lower()
        if choice in difficulty_mapping:
            return difficulty_mapping[choice]
        print("Invalid choice. Please enter a valid item from the list.")


# Generates a math question based on the specific number range chosen
def generate_question(ops, num_range):
    # Selects a random operation from the given list
    operation = random.choice(ops)
    # Generates two numbers within the specified range
    num1 = random.randint(num_range[0], num_range[1])
    num2 = random.randint(num_range[0], num_range[1])

    if operation == '+':  # addition
        correct_answer = num1 + num2
    elif operation == '-':  # subtraction
        num2 = random.randint(num_range[0], num1)
        correct_answer = num1 - num2
    elif operation == '*':  # multiplication
        correct_answer = num1 * num2
    else:  # Division case
        num2 = random.randint(1, 10)  # Avoids division by zero
        num1 = random.randint(num_range[0], num_range[1] // num2) * num2  # ensure the dividend is in specified range
        correct_answer = num1 // num2

    return num1, operation, num2, correct_answer


# Checks if user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


# Determines number of tries based on chosen difficulty
def determine_num_tries(difficulty_level):
    # maps the number of tries to the difficulties
    tries_mapping = {'Easy': 1, 'Normal': 2, 'Hard': 3, 'Diabolic': 4}
    return tries_mapping.get(difficulty_level, 1)


# Main function used to generate math operation based questions
def math_quiz(num_questions, ops, num_range):
    print(f"You've chosen {ops} operation(s) with numbers in the range {num_range}.\n")

    # initialise the counters for number of correct and incorrect answers
    correct_answers = 0
    num_correct = 0
    num_incorrect = 0

    question_history.clear()
    difficulty_name_str = difficulty_name(num_range[1])
    points_per_question = determine_num_tries(difficulty_name_str)
    num_questions_placeholder = 10 ** 9 if num_questions == "infinite" else int(num_questions)

    update_difficulty_questions(difficulty_name_str, num_questions_placeholder)
    # Loop through each question up to chosen number or infinite mode
    for i in range(num_questions_placeholder):
        num1, operator, num2, correct_answer = generate_question(ops, num_range)
        print(f"\nQuestion {i + 1}: What is {num1} {operator} {num2}?")

        # keeps track of number of attempted answers
        num_tries = points_per_question
        attempted_numbers = set()

        while num_tries > 0:
            user_input = input("Your answer: ")

            if user_input.lower() == "quit":
                # Allows user to quit the quiz
                if i == 0:
                    print("You've barely started and you're already retiring? Retirement goals, I like it!")
                    raise SystemExit
                else:
                    # if quitting later, provide statistics and history
                    print("You have quit the quiz.")
                    total_points = correct_answers * points_per_question
                    update_difficulty_points(difficulty_name_str, total_points)
                    return True, num_correct, num_incorrect

            try:
                user_answer = int(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue
            # ensures there are no duplicate inputs
            if user_answer in attempted_numbers:
                print("You have already tried this number. Please enter a different one.")
                continue

            attempted_numbers.add(user_answer)

            if check_answer(user_answer, correct_answer):
                print("✅ Correct!")
                correct_answers += 1
                num_correct += 1
                question_history.append((i + 1, num1, operator, num2, correct_answer, True))
                if num_tries != points_per_question:
                    print(f"You got the answer in {points_per_question - num_tries + 1} tries.")
                break
            else:
                num_tries -= 1
                num_incorrect += 1
                if num_tries == 0:
                    print(f"❌ Incorrect! The correct answer is {correct_answer}")
                    question_history.append((i + 1, num1, operator, num2, user_answer, False))
                else:
                    print(f"❌ Incorrect! You have {num_tries} tries left.")

    total_points = correct_answers * points_per_question
    update_difficulty_points(difficulty_name_str, total_points)
    total_questions = num_questions_placeholder if num_questions != "infinite" else "infinite"

    print()
    print(f"You scored {total_points} out of {total_questions * points_per_question} points.")
    if num_questions != "infinite":
        print(f"You answered {correct_answers} questions correctly out of {num_questions_placeholder}.\n")
    # returns the result and statistics
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
            if response >= 1:
                return response
            print(error)
        except ValueError:
            print(error)


# Checks user enters yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ['yes', 'y']:
            return True
        if response in ['no', 'n']:
            return False
        print("Please enter either yes or no")


# Displays instructions to user
def instructions():
    print('''
📝 Instructions 📝

Hey there! Welcome to the Math Quiz. Here's how to answer:

1. Choose the Number of Questions:
Decide how many questions you want to answer. You can choose a specific number or test 
yourself in infinite mode by pressing enter to answer unlimited questions until you decide stop.

2. Select the Operation:
Choose one of the four basic operations: addition (+), subtraction (-), 
multiplication (*), or division (/). You can also choose the random option to answer a mix
of all operations.

3. Choose the Difficulty Level:
You'll be asked to select a difficulty level for your questions by inputting the first 
letter of your chosen difficulty:
- 🟩 Easy: Numbers from 1 to 10, suitable for beginners.
- 🟨 Normal: Numbers from 1 to 20, a moderate challenge.
- 🟥 Hard: Numbers from 1 to 100, for advanced practice.
- 💀 Diabolic: Numbers from 1 to 1000, for math experts!

4. Answer the Questions:
For each question, you'll be given multiple attempts depending on the difficulty level.
- Easy: 1 attempt
- Normal: 2 attempts
- Hard: 3 attempts
- Diabolic: 4 attempts

5. Review Your Performance:
After the quiz, you'll see a summary of your performance, including the number of correct 
and incorrect answers, and the points you've earned based on the chosen difficulty.

Point System:
🟩 Easy: 1 point
🟨 Normal: 2 points
🟥 Hard: 3 points
💀 Diabolic: 4 points

Type "quit" at any time to exit the quiz. 

Good luck and have fun! 🎉
''')


# Main routine starts here
print()
print('''
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
    ✦   🔢🔢🔢  Welcome to the Math Quiz! 🔢🔢🔢    ✦
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
  ''')
print()

# Stores question history
question_history = []

# Stores total points scored for each difficulty level
difficulty_points = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Diabolic': 0}

# Stores total number of questions answered for each difficulty level
difficulty_questions_answered = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Diabolic': 0}

# Display instructions if user wants to see them
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions:
    instructions()

# Ask for the number of questions
print()
num_questions = int_check("How many questions would you like? Enter a number or push enter for an infinite amount: ")
print(f"You chose {num_questions if num_questions != 'infinite' else 'infinite'} questions.")

# Asks for operation
while True:
    operation_choice = input("Which operation do you want? (➕, ➖, ✖️, ➗, random): ").strip().lower()
    # Maps emoji to operation symbols
    emoji_to_operation = {'➕': '+', '➖': '-', '✖️': '*', '➗': '/'}

    if operation_choice in emoji_to_operation:
        operations = [emoji_to_operation[operation_choice]]
        break
    elif operation_choice in ['+', '-', '*', '/']:
        operations = [operation_choice]  # Use the selected operation
        break
    elif operation_choice == 'random' or operation_choice == 'r':
        operations = ['+', '-', '*', '/']  # Includes all operations
        break
    else:
        print("Invalid operation! Please choose either +, -, *, /, random.")

difficulty_value, difficulty_str = choose_difficulty()  # Asks for difficulty
num_range = (1, difficulty_value)

# Starts quiz
result, num_correct, num_incorrect = math_quiz(num_questions, operations, num_range)

# Quiz history section
print()
show_quiz_history = yes_no("⏱️ Do you want to see the quiz history? ⏱️ ")
if show_quiz_history:
    if not question_history:
        print("There is no quiz history to show.")
    else:
        print("\n⏪ Quiz History ⏪:")
        for question_num, num1, operator, num2, user_answer, is_correct in question_history:
            result = "✅ Correct" if is_correct else f"❌ Incorrect"
            correct_answer = num1 + num2 if operator == '+' else num1 - num2 if operator == '-' else num1 * num2 \
                if operator == '*' else num1 // num2
            print(f"\nQuestion {question_num}/{len(question_history)}: What is {num1} {operator} {num2}?")
            if not is_correct:
                print(f"Your answer: {user_answer} (Correct answer: {correct_answer})")
            else:
                print(f"Your answer: {user_answer}")
            print(f"Result: {result}")

# Statistics function
print()
show_statistics = yes_no("📊 Do you want to see the statistics? 📊 ")
if show_statistics:
    points = difficulty_points[difficulty_str]
    total_questions_answered = len(question_history)
    total_correct = sum(1 for _, _, _, _, _, is_correct in question_history if is_correct)
    total_incorrect = total_questions_answered - total_correct
    percentage_correct = (total_correct / total_questions_answered) * 100 if total_questions_answered else 0

    print("\nStatistics:")
    print(f"Total correct answers: {total_correct}")
    print(f"Total incorrect answers: {total_incorrect}")
    print(f"Total points scored for {difficulty_str} mode: {points}")
    print(f"Percentage of questions correct: {int(percentage_correct)}%")

print()
print("😀 Thanks for attempting the quiz! 😀")
