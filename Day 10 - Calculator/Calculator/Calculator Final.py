from art import logo
import math

#Add
def add(n1, n2):
    """add n1 and n2 together"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """subtracts n2 from n1"""
    return n1 - n2

#Multipy
def multiply(n1, n2):
    """Multiplies n1 and n2 together"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """divides n1 by n2"""
    return n1 / n2

def exponent(n1, n2):
    """returns n1 to the power of n2"""
    return n1 ** n2

operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/" : divide,
    "^" : exponent
}

def calculator():
    print(logo)
    n1 = float(input("What is your first number?: "))

    for operation in operations:
        print(operation)

    operation_symbol = input("What operation would you like to use?: ")
    calculation_fuction = operations[operation_symbol]
    n2 = float(input("What is your second number?: "))

    answer = calculation_fuction(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")

    keep_calculating = True
    while keep_calculating:
        continue_calculation = input(f'Type "y" to continue calculating with the number {answer}, or type "n" to exit.:')
        if continue_calculation == "y":
            operation_symbol = input("Pick another operation: ")
            n3 = float(input("What is the next number?: "))
            calculation_fuction = operations[operation_symbol]
            second_answer = calculation_fuction(answer, n3)
            print(f"{answer} {operation_symbol} {n3} = {second_answer}")
        else:
            keep_calculating = False
            break

calculator()