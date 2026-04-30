try:
    x = int(input("Enter number 1: "))
    y=int(input("Enter Number 2: "))
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")