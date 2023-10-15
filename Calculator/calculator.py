# Define the calculator function
def calculator():
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the operation
    op = input("Enter the operation (+, -, *, /): ")
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Calculate the result based on the operation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by 0")
            return
        else:
            result = num1 / num2
    
    # Print the result
    print(f"{num1} {op} {num2} = {result}")

# Call the calculator function
calculator()
