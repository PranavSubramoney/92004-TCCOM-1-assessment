import random

# Global variable to store round history
round_history = []

# Global dictionary to store total points scored for each difficulty level
difficulty_points = {'Easy': 0, 'Normal': 0, 'Hard': 0, 'Extra Hard': 0}


# Function to update total points scored for each difficulty level if the answer is correct
def update_difficulty_points(difficulty, points):
    difficulty_points[difficulty] += points


# Function to choose difficulty level
def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. 🟩 Easy (1-10)")
    print("2. ⬜ Normal (1-20)")
    print("3. 🟨 Hard (1-100)")
    print("4. 🟥 Extra Hard (1-1000)")

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


# Function to get the difficulty name based on the range
def difficulty_name(difficulty_range):
    if difficulty_range == 10:
        return 'Easy'
    elif difficulty_range == 20:
        return 'Normal'
    elif difficulty_range == 100:
        return 'Hard'
    elif difficulty_range == 1000:
        return 'Extra Hard'


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
def check_answer(operator, user_answer, correct_answer):
    if operator in ['+', '-', '*', '/']:
        return user_answer == correct_answer
    else:
        return False  # Handle unknown operation


# Function to determine the number of tries based on difficulty mode
def determine_num_tries(difficulty_name):
    if difficulty_name == 'Easy':
        return 1
    elif difficulty_name == 'Normal':
        return 2
    elif difficulty_name == 'Hard':
        return 3
    elif difficulty_name == 'Extra Hard':
        return 4


# Main routine
def math_quiz(num_questions, operations, num_range):
    print(f"You've chosen {operations} operation(s) with numbers in the range {num_range}.\n")
    correct_answers = 0
    round_history.clear()  # Clear round history for each new round

    # Determine points per question based on difficulty
    points_per_question = determine_num_tries(difficulty_name(num_range[1]))

    # If num_questions is infinite, set a large number as a placeholder
    if num_questions == "infinite":
        num_questions = 10**9  # Or any sufficiently large number
    else:
        num_questions = int(num_questions)  # Convert to integer

    for i in range(num_questions):
        num1, operator, num2, correct_answer = generate_question(operations, num_range)
        print(f"\nQuestion {i + 1}: What is {num1} {operator} {num2}?")

        # Get number of tries based on difficulty
        num_tries = points_per_question

        while num_tries > 0:
            user_answer = input("Your answer: ")
            if user_answer.lower() == "quit":  # Check if user wants to quit
                print("You have quit the quiz.")
                total_points = correct_answers * points_per_question
                update_difficulty_points(difficulty_name(num_range[1]), total_points)
                return False
            try:
                user_answer = int(user_answer)  # Convert user input to integer
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue  # Ask for input again if it's not a valid integer
            if check_answer(operator, user_answer, correct_answer):
                print("✅ Correct!")
                correct_answers += 1
                break  # Break the loop if the answer is correct
            else:
                num_tries -= 1
                if num_tries == 0:
                    print(f"❌ Incorrect! The correct answer is {correct_answer}")
                else:
                    print(f"❌ Incorrect! You have {num_tries} tries left.")
                if num_tries > 0:  # If there are remaining tries, prompt the user to answer again
                    continue  # Continue to prompt the user for an answer
                break  # Break the loop if there are no remaining tries

        # Add round history after each question
        round_history.append((i + 1, num1, operator, num2, user_answer, check_answer(operator, user_answer, correct_answer)))

    total_questions = "infinite" if num_questions == 10**9 else num_questions
    score = correct_answers * points_per_question  # Calculate total score
    update_difficulty_points(difficulty_name(num_range[1]), score)  # Update points for the current round
    percentage_correct = (correct_answers / num_questions) * 100 if num_questions != 10**9 else 0
    print()
    print(f"You scored {score} out of {total_questions * points_per_question} points.")
    if num_questions != 10**9:
        print(f"You answered {correct_answers} questions correctly out of {num_questions}. You got "
              f"{int(percentage_correct)}% questions correct.\n")
    return True


# Integer checker function
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more, or push enter for infinite questions:"

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
You'll be asked to select a difficulty level for your questions:
- 🟩 Easy: Numbers from 1 to 10, suitable for beginners.
- ⬜ Normal: Numbers from 1 to 20, ideal for students with some math experience.
- 🟨 Hard: Numbers from 1 to 100, challenging for confident students.
- 🟥 Extra Hard: Numbers from 1 to 1000, for advanced students seeking a significant challenge.    

4. Solve the Problems:
Once you've chosen your preferences, you'll be presented with math problems based on your choices. 
Answer the questions by just inputting the correct number and pressing enter.
You will receive instant feedback on each answer. If you answer incorrectly you will be presented
with the correct answer. You will also be given extra attempts at questions based on your chosen difficulty.
If answered correctly, you will receive points based on your chosen difficulty.

5. Quit Anytime:
Exit the quiz at any time by entering "quit" as your answer to a question.

6. Quiz history and Scoring system:
View all the questions you you answered by entering yes or y for short when asked to see your quiz history.
You will be shown whether you got the questions correct or incorrect with the correct answers.    
Also see how many points you scored in total with the statistics option.
The point system is based on difficulty. This is how it works:
🟩 Easy mode - 1 point
⬜ Normal mode - 2 points
🟨 Hard mode - 3 points
🟥 Extra Hard mode - 4 points

Have fun and good luck with the Math Quiz! 🎉

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

operations = ['+', '-', '*', '/']

# Ask for the number of questions
print()
num_questions = int_check("How many questions would you like? Enter a number or push enter for an infinite amount: ")
if num_questions == "":
    print("You chose infinite questions.")
else:
    print(f"You chose {num_questions} questions.")
# Asking for operation
operation_choice = input("Which operation do you want? (➕,➖,✖️,➗, random): ").lower()
if operation_choice in ['+', '-', '*', '/', 'random']:
    if operation_choice == 'random':
        operations = ['+', '-', '*', '/']  # Include all operations
    else:
        operations = [operation_choice]
else:
    print("Invalid operation! Please choose either +, -, *, /, or random.")

num_range = (1, choose_difficulty())  # Ask for difficulty

# Start quiz directly without rounds
math_quiz(num_questions, operations, num_range)

# Ask user if they want to see the quiz history
print()
show_quiz_history = yes_no("⏱️ Do you want to see the quiz history? ⏱️ ")
if show_quiz_history:
    if len(round_history) == 0:
        print("There is no quiz history to show.")
    else:
        print("\n⏪ Quiz History ⏪:")
        num_correct = 0
        num_incorrect = 0
        for question_num, num1, operator, num2, user_answer, is_correct in round_history:
            result = "✅ Correct" if is_correct else f"❌ Incorrect"
            correct_answer = num1 + num2 if operator == '+' else num1 - num2 if operator == '-' else num1 * num2 if operator == '*' else num1 // num2
            print(f"\nQuestion {question_num}/{len(round_history)}: What is {num1} {operator} {num2}?")
            if not is_correct:
                print(f"Your answer: {user_answer} (Correct answer: {correct_answer})")
                num_incorrect += 1
            else:
                print(f"Your answer: {user_answer}")
                num_correct += 1
            print(f"Result: {result}")

        # Print summary
        print("\nSummary:")
        print(f"Total correct answers: {num_correct}")
        print(f"Total incorrect answers: {num_incorrect}")

# Rest of the code remains the same

# Ask user if they want to see the statistics
print()
show_statistics = yes_no("📊 Do you want to see the statistics? 📊 ")
if show_statistics:
    # Print statistics section under round history
    print("\nStatistics:")
    for difficulty, points in difficulty_points.items():
        print(f"Total points scored for {difficulty} mode: {points}")
    print(f"Total points altogether: {sum(difficulty_points.values())}")

print()
print("Thanks for playing!👋🏻")
