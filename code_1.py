HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")

    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.write("")  # Clear the file by writing an empty string
    file.close()

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

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

    



