# checks if users enter yes or no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


def instructions():
    print('''
    
    *** Instructions ***
    
Hey there! Welcome to the Math Quiz. Get ready to have a blast!

Choose Your Challenge:
Decide how many questions you want to tackle. Enter your desired amount of questions or choose
an infinite amount by pressing enter.

Solve the Problems:
Get cracking on those math problems! We're talking addition, subtraction, multiplication, and division!

No pressure, just type in your answers and hit Enter. 

If you answer incorrectly, we'll gently steer you in the right direction with the correct answer.

Check Your Progress:
Curious to see how you did? Look at your progress at the end of the game with the Quiz History option.

Ready to dive into the fun? Let's get started!
    
    ''')


# Main routine
print()
print('''
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
   ✦   ➕➖✖️➗ Welcome to the Math Quiz! ➗✖️➖➕   ✦
 ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦
  ''')
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()

print("program continues")

