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
def check_answer(operator, user_answer, correct_answer):
    if operator in ['+', '-', '*', '/']:
        return user_answer == correct_answer
    else:
        return False  # Handle unknown operation


# Main routine
def math_quiz(num_questions, operations, num_range, round_number):
    print(f"You've chosen {operations} operation(s) with numbers in the range {num_range}.\n")
    correct_answers = 0
    round_history.clear()  # Clear round history for each new round

    # Determine points per question based on difficulty
    if num_range[1] == 10:
        points_per_question = 1
    elif num_range[1] == 20:
        points_per_question = 2
    elif num_range[1] == 100:
        points_per_question = 3
    elif num_range[1] == 1000:
        points_per_question = 4

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

        is_correct = check_answer(operator, user_answer, correct_answer)
        round_history.append((round_number, i + 1, num1, operator, num2, user_answer, is_correct))  # Add round history

        if is_correct:
            print("✅Correct!\n")
            correct_answers += 1
        else:
            print(f"❌Incorrect! The correct answer is {correct_answer}\n")

    total_questions = num_questions
    score = correct_answers * points_per_question  # Calculate total score
    update_difficulty_points(difficulty_name(num_range[1]), score)  # Update points for the current round
    percentage_correct = (correct_answers / num_questions) * 100 if num_questions > 0 else 0
    print()
    print(f"You scored {score} out of {total_questions * points_per_question} points.")
    print(
        f"You answered {correct_answers} questions correctly out of {num_questions}, which is {percentage_correct:.2f}%.\n")
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

Hey there! Welcome to the Math Quiz. Here's how to play:

1. Choose the Number of Rounds:
Decide how many rounds you want to answer. You can choose a specific number or test 
yourself in infinite mode by pressing enter.

2. Choose the Number of Questions per Round:
Select the number of questions you'd like to answer in each round.

3. Select the Operation:
For each round, choose one of the four basic operations: addition (+), subtraction (-), 
multiplication (*), or division (/). You can also choose the random option to answer a mix
of all operations.

4. Choose the Difficulty Level:
You'll be asked to select a difficulty level for each round:
- 🟩 Easy: Numbers from 1 to 10, suitable for beginners.
- ⬜ Normal: Numbers from 1 to 20, ideal for players with some math experience.
- 🟨 Hard: Numbers from 1 to 100, challenging for confident players.
- 🟥 Extra Hard: Numbers from 1 to 1000, for advanced players seeking a significant challenge.    

5. Solve the Problems:
Once you've chosen your preferences, you'll be presented with math problems based on your choices. 
Answer the questions by just inputting the correct number and pressing enter.
You will receive instant feedback on each answer. If you answer incorrectly you will be presented
with the correct answer. If answered correctly, you will receive points based on your chosen difficulty.

6. Check your progress:
After each round see how many points you scored, including the percentage of questions you got correct.   

7. Quit Anytime:
Exit the quiz at any time by entering "quit" as your answer to a question.

8. Scoring system:
View all the questions you you answered by entering yes or y for short when asked to see your round history.
You will be shown whether you got the questions correct or incorrect with the correct answers.    
Also see how many points you scored in total with the statistics option.
The point system is based on difficulty. This is how it works:
🟩 Easy - 1 point
⬜ Normal - 2 points
🟨 Hard - 3 points
🟥 Extra Hard - 4 points

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
        operation_choice = input("Which operation do you want? (➕,➖,✖️,➗, random): ").lower()
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
show_history = yes_no("⏱️ Do you want to see the round history? ⏱️ ")
if show_history:
    if len(all_round_history) == 0:
        print("There is no history to show.")
    else:
        print("\n⏪ Round History ⏪:")
        current_round = 0
        for round_data in all_round_history:
            round_number, question_number, num1, operator, num2, user_answer, is_correct = round_data
            if round_number != current_round:
                print(f"\nRound {round_number}:")
                current_round = round_number
            result = "✅Correct" if is_correct else "❌Incorrect"
            print(f"Question {question_number}: ({result}) {num1} {operator} {num2} = {user_answer}")

# Ask user if they want to see the statistics
print()
show_statistics = yes_no("📊 Do you want to see the statistics? 📊 ")
if show_statistics:
    # Print statistics section under round history
    print("\nStatistics:")
    for difficulty, points in difficulty_points.items():
        print(f"Total points scored for {difficulty}: {points}")
    print(f"Total points altogether: {sum(difficulty_points.values())}")

print()
print("Thanks for playing!👋🏻")
