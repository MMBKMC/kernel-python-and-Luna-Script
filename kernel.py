import os
import sys
from os import*

cpu = 13
ram = 234

print("Booting From A Drive....")
input("$ ")

print("Loading...")

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

while True:
    user_input = input("$ ")
    answer = evaluate_expression(user_input)
    print("$", answer)
