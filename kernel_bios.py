import os
import sys
from os import*

print("Booting From a Drive....")

def print_words(sentence):
    words = sentence.split()
    for word in words:
        print(word)

while True:
    user_input = input("$ ")
    print_words(user_input)
