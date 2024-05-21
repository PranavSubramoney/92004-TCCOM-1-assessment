import random

# Stores question history
question_history = []

# Stores total points scored for each difficulty level
difficulty_points = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Diabolic': 0}

# Stores total number of questions answered for each difficulty level
difficulty_questions_answered = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Diabolic': 0}


# Updates total points for each difficulty level if correct
def update_difficulty_points(difficulty_level, points):
    # Increases points for difficulty level
    difficulty_points[difficulty_level] += points


# Updates questions answered
def update_difficulty_questions(difficulty_level):
    # Increases total questions answered
    difficulty_questions_answered[difficulty_level] += 1


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


# Function to choose difficulty level
def choose_difficulty():
    # Prompts users to choose difficulty
    print("Choose a difficulty level:")
    print("🟩 Easy (1-10)")
    print("🟨 Normal (1-20")
    print("🟥 Hard (1-100)")
    print("💀 Diabolic (1-1000)")

    while True:
        choice = input("Enter the difficulty level: ").strip().lower()

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


# Generates a random math question based on chosen operation and number range
def generate_question(ops, num_range):
    operation = random.choice(ops)
    # Generates numbers based on operation
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
        max_quotient = num_range[1] // num2
        num1 = random.randint(num_range[0], max_quotient) * num2  # num1 is a multiple of num2
        correct_answer = num1 // num2  # Calculate correct answer using integer division
    return num1, operation, num2, correct_answer


# Checks if user's answer is correct
def check_answer(op, user_answer, correct_answer):
    if op in ['+', '-', '*', '/']:
        return user_answer == correct_answer
    else:
        return False


# Determines number tries based on chosen difficulty
def determine_num_tries(difficulty_level):
    # Assigns number of tries
    if difficulty_level == 'Easy':
        return 1
    elif difficulty_level == 'Normal':
        return 2
    elif difficulty_level == 'Hard':
        return 3
    elif difficulty_level == 'Diabolic':
        return 4


# Main routine
def math_quiz(num_questions, ops, num_range):
    # Starts quiz based on user parameter choices
    print(f"You've chosen {ops} operation(s) with numbers in the range {num_range}.\n")
    correct_answers = 0
    num_correct = 0
    num_incorrect = 0
    question_history.clear()
    difficulty_name_str = difficulty_name(num_range[1])
    points_per_question = determine_num_tries(difficulty_name_str)

    # placeholder number for infinite questions
    if num_questions == "infinite":
        num_questions_placeholder = 10 ** 9
    else:
        num_questions_placeholder = int(num_questions)

    difficulty_questions_answered[difficulty_name_str] += num_questions_placeholder

    # Iterates through each question
    for i in range(num_questions_placeholder):
        num1, operator, num2, correct_answer = generate_question(ops, num_range)
        print(f"\nQuestion {i + 1}: What is {num1} {operator} {num2}?")

        num_tries = points_per_question
        attempted_numbers = set()
        user_answer = None  # Initialize user_answer
        # Loops for multiple tries if user does not input an integer
        while num_tries > 0:
            user_input = input("Your answer: ")

            if user_input.lower() == "quit":
                # Allows user to quit the quiz
                if i == 0:
                    print("You've barely started and you're already retiring? Retirement goals, I like it!")
                    raise SystemExit
                else:
                    print("You have quit the quiz.")
                    total_points = correct_answers * points_per_question
                    update_difficulty_points(difficulty_name_str, total_points)
                    return True, num_correct, num_incorrect

            # Handles invalid integer inputs
            try:
                user_answer = int(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue

            if user_answer in attempted_numbers:
                # Handles duplicate integer inputs
                print("You have already tried this number. Please enter a different one.")
                continue

            attempted_numbers.add(user_answer)

            if check_answer(operator, user_answer, correct_answer):
                # updates / notifies user if their answer is correct
                if num_tries == 1 and difficulty_name_str != 'Easy':
                    print("✅ Correct!")
                    print("Phew! You got it on the last try.")
                else:
                    print("✅ Correct!")
                # Update correct_answers regardless of try count
                correct_answers += 1
                num_correct += 1
                # If correct, update question history with correct answer
                question_history.append((i + 1, num1, operator, num2, correct_answer, True))
                if difficulty_name_str != 'Easy' and num_tries != 1:
                    tries_str = "try" if num_tries == points_per_question else "tries"
                    print(f"You got the answer in {points_per_question - num_tries + 1} {tries_str}.")
                break
            else:
                num_tries -= 1
                num_incorrect += 1
                if num_tries == 0:
                    # displays correct answer is user answer is incorrect
                    print(f"❌ Incorrect! The correct answer is {correct_answer}")
                    # Update question history with incorrect answer
                    question_history.append((i + 1, num1, operator, num2, user_answer, False))
                elif num_tries > 0:
                    print(f"❌ Incorrect! You have {num_tries} tries left.")
                if num_tries == 0:
                    break

    total_questions = "infinite" if num_questions == "infinite" else num_questions_placeholder
    score = correct_answers * points_per_question
    update_difficulty_points(difficulty_name_str, score)
    (correct_answers / num_questions_placeholder) * 100 if num_questions != "infinite" else 0
    print()
    # displays points and questions correct at end of quiz (not infinite mode)
    print(f"You scored {score} out of {total_questions * points_per_question} points.")
    if num_questions != "infinite":
        print(f"You answered {correct_answers} questions correctly out of {num_questions_placeholder}.\n")
    return True, num_correct, num_incorrect


# Integer checker function
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more, or push enter for infinite questions."

        to_check = input(question)

        # check for infinite mode
        if to_check.strip() == "":
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


# checks user enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if user doesn't enter yes or no
        if response == "yes" or response == "y":
            return True
        if response == "no" or response == "n":
            return False
        else:
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
- Extra Hard: 4 attempts

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

# Display instructions if user wants to see them
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions:
    instructions()

operations = ['+', '-', '*', '/']

# Ask for the number of questions
print()
num_questions = int_check("How many questions would you like? Enter a number or push enter for an infinite amount: ")
if num_questions == "":
    print("You chose infinite questions.")
else:
    print(f"You chose {num_questions} questions.")
# Asks for operation
while True:
    operation_choice = input("Which operation do you want? (➕,➖,✖️,➗, random): ").lower()
    if operation_choice in ['+', '-', '*', '/', 'random']:
        if operation_choice == 'random':
            operations = ['+', '-', '*', '/']  # Includes all operations
        else:
            operations = [operation_choice]
        break
    else:
        print("Invalid operation! Please choose either +, -, *, /, or random.")
difficulty_value, difficulty_str = choose_difficulty()  # Asks for difficulty
num_range = (1, difficulty_value)

# Starts quiz
result, num_correct, num_incorrect = math_quiz(num_questions, operations, num_range)

# Quiz history section
# Displays quiz history if they choose to see it
print()
show_quiz_history = yes_no("⏱️ Do you want to see the quiz history? ⏱️ ")
if show_quiz_history:
    if len(question_history) == 0:
        print("There is no quiz history to show.")
    else:
        print("\n⏪ Quiz History ⏪:")
        for question_num, num1, operator, num2, user_answer, is_correct in question_history:
            # shows result of questions with correct answers
            result = "✅ Correct" if is_correct else f"❌ Incorrect"
            correct_answer = num1 + num2 if operator == '+' else num1 - num2 if operator == '-' else num1 * num2 if (
                    operator == '*') else num1 // num2
            print(f"\nQuestion {question_num}/{len(question_history)}: What is {num1} {operator} {num2}?")
            if not is_correct:
                print(f"Your answer: {user_answer} (Correct answer: {correct_answer})")
            else:
                print(f"Your answer: {user_answer}")
            print(f"Result: {result}")

# Statistics function
# Displays statistics if user choose to see it
print()
show_statistics = yes_no("📊 Do you want to see the statistics? 📊 ")
if show_statistics:
    # Print statistics section for the chosen difficulty
    points = difficulty_points[difficulty_str]
    total_questions_answered = 0
    total_correct = 0
    total_incorrect = 0
    for _, _, _, _, user_answer, is_correct in question_history:
        total_questions_answered += 1
        if is_correct:
            total_correct += 1
        else:
            total_incorrect += 1

    percentage_correct = (total_correct / total_questions_answered) * 100 if total_questions_answered != 0 else 0

    print("\nStatistics:")
    print(f"Total correct answers: {total_correct}")
    print(f"Total incorrect answers: {total_incorrect}")
    print(f"Total points scored for {difficulty_str} mode: {points}")
    print(f"Percentage of questions correct: {int(percentage_correct)}%")

print()
print("😀 Thanks for attempting the quiz! 😀")
