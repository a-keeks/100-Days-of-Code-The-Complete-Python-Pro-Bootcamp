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
    return n1 ^ n2

operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/" : divide,
    "^" : exponent
}

num1 = int(input("What is your first number?: "))

for operation in operations:
    print(operation)

operation_symbol = input ("Pick a symbol from the line above: ")
calculation_fuction = operations[operation_symbol]
num2 = int(input("What is your second number?: "))

answer = calculation_fuction(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")