def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def subtract(x, y):
    """Returns the difference between x and y"""
    return x - y

def multiply(x, y):
    """Return the product of x and y"""
    return x * y

def divide(x, y):
    """Return the quotient of x divided by y"""
    if y == 0:
        raise ValueError("Cannot divide by Zero")
    return x / y

def calculator():
    print("Simple Calculator Program")
    
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        
        choice = input("Enter your choice(1-5): ")
        if choice in ['1', '2', '3', '4']:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            
            if choice == "1":
                print(f"The result of {x} and {y} is {add(x, y)}")
            elif choice == "2":
                print(f"The result of {x} and {y} is {subtract(x, y)}")
            elif choice == "3":
                print(f"The result of {x} and {y} is {multiply(x, y)}")
            elif choice == "4":
                try:
                    print(f"The result of {x} / {y} is: {divide(x, y)}")
                except ValueError as e:
                    print(str(e))
            elif choice == "5":
                break
        else:
            print("Invalid choice. Please choose again.")
            
if __name__ == "__main__":
    calculator()