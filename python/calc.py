"""Basic calculator module.

Author: Ethan Adams
GitHub: epadams
Email: epaadams2002@gmail.com
"""
import sys
def add(x, y):
    """Basic add function."""
    return x + y

def sub(x, y):
    """Basic subtraction function."""
    return x - y

def mul(x, y):
    """Basic multiplication function."""
    return x * y

def div(x, y):
    """Basic division function."""
    return x / y

print("\033[1;36mWelcome to the Basic Calculator!")
while True:
    answer = int(input("Please select:\n1) Addition\n2) Subtraction\n3) Multiplication"
    + "\n4) Division\n5) Quit\n"))
    if answer == 5:
        sys.exit()
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    match answer:
        case 1:
            print(add(num1, num2))
        case 2:
            print(sub(num1, num2))
        case 3:
            print(mul(num1, num2))
        case 4:
            print(div(num1, num2))
        case default:
            print("Invalid selection, try 1/2/3/4/5")
