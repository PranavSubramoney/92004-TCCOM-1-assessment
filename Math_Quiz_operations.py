def ask_for_operation():
    operations = ['+', '-', '*', '/']
    while True:
        operation_choice = input("Which operation do you want? (➕,➖,✖️,➗, random): ").lower()
        if operation_choice in ['+', '-', '*', '/', 'random']:
            if operation_choice == 'random':
                selected_operations = ['+', '-', '*', '/']
                chosen_operation = '+', '-', '*', '/'
            else:
                selected_operations = [operation_choice]
                chosen_operation = operation_choice
            break
        else:
            print("Invalid operation! Please choose either +, -, *, /, or random.")
    return selected_operations, chosen_operation


# Example usage:
operations, chosen_operation = ask_for_operation()
print(f"You chose {chosen_operation} operation(s).")
