from math import *

num1 = float(input("Enter first number: "))
op = input("Enter you operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
elif op == "*":
    result = num1 * num2
else:
    result = "Enter a valid operator"

print(result)

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor