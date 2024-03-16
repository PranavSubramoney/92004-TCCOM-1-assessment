# Checks that users enter an integer
# that is more than 1
def int_check():
    while True:
        error = "Please enter an integer that is or more than / equal to 1."

        try:
            response = int(input("Enter an integer: "))

            # checks that the umber is more / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine goes here
target_score = int_check()
print(target_score)
