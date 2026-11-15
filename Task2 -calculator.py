def main():
    print("--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nOperations:")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")

        operation = input("\nChoose an operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation selected.")
            return

        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
