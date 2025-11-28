
def calculator():
    try:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        
        print("\nSelect an operator:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        
        choice = input("Enter your choice (1/2/3/4): ")

        
        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == '4':
            
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("\nInvalid operator choice. Please select 1, 2, 3, or 4.")

    except ValueError:
        
        print("\nError: Please enter numeric values only!")


calculator()