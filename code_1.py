HISTORY_FILE = "history.txt"

def show_history():
    # Open the history file in read mode to fetch previous entries
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        # Print each line in reverse order so the most recent history appears first
        for line in reversed(lines):
            print(line.strip())
    file.close()  # Ensure the file is closed after reading

def clear_history():
    # Open the history file in write mode to clear its content
    file = open(HISTORY_FILE, "w")
    file.write("")  # Write an empty string to clear file content
    file.close()  # Close the file after clearing

def save_to_history(equation, result):
    # Open the history file in append mode to add a new calculation record
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()  # Close the file after writing the new record

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: operand1 operator operand2")
        return None
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if  operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return None
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return None
    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")
    save_to_history(user_input, result)

def main():
    print("Welcome to the calculator!")
    while True:
        user_input = input("Enter calculation(+,-,/,*) (or type 'history' to view history, 'clear' to clear history, or 'exit' to quit): ")
        if user_input == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
            print("History cleared.")
        else:
            calculate(user_input)
        
main()

    



