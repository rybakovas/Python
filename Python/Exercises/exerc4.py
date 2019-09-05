# Receive user full name by input and do a simple analise on the string
# print the full name in uppercase
# print the full name in lowercase
# print the full name total letters
# print the first name and how many letters it have
from time import *

name = input("Enter your Full name: ")
print("Analyzing your name...")
sleep(1.5)  # Just for "loading"
print("Your full name in uppercase {}".format(name.upper()))
print("Your full name in lowercase {}".format(name.lower()))
print("Your full name have {} letters".format(len(name) - name.count(' ')))
fname= name.split()
print("Your first name is {} and have {} letters".format(fname[0], len(fname[0])))

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor