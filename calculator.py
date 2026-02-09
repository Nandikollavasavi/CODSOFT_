# Simple Calculator in Python

def calculator():
    print("=== Simple Calculator ===")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter choice (1/2/3/4 or + - * /): ")
        
        if choice in ("1", "+"):
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice in ("2", "-"):
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice in ("3", "*"):
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice in ("4", "/"):
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a valid operation.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()

