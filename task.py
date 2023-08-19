def get_valid_number(prompt):
    max_trials = 5
    trial_count = 0

    while trial_count < max_trials:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            trial_count += 1

    print("Maximum number of trials reached. Using default value.")
    return 0 


def get_valid_operation():
    valid_operations = ["1", "2", "3", "4"]
    max_trials = 5
    trial_count = 0

    while trial_count < max_trials:
        user_input = input("Enter operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
        if user_input in valid_operations:
            return user_input
        else:
            print("Invalid operation. Please enter a valid operation.")
            trial_count += 1

    print("Maximum number of trials reached. Using default operation.")
    return "1"  

def main():
    num_1 = get_valid_number("Enter the first number: ")
    num_2 = get_valid_number("Enter the second number: ")
    operation = get_valid_operation()

    if operation == "4" and num_2 == 0:
        print("Division by zero is not allowed.")
    else:
        if operation == "1":
            result = num_1 + num_2
            operation_str = "addition"
        elif operation == "2":
            result = num_1 - num_2
            operation_str = "subtraction"
        elif operation == "3":
            result = num_1 * num_2
            operation_str = "multiplication"
        elif operation == "4":
            result = num_1 / num_2
            operation_str = "division"

        print(f"Result of {operation_str}: {result}")

if __name__ == "__main__":
    main()
