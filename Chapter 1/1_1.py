#!/usr/bin/env python3
# Author: Geoffrey Ranson
#
# Date: mm/dd/yyyy
# File: nameOfProgram.py
# Description: Brief description of what this program does

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

1. Print a welcome statement.
2. Ask the user to input their name.
3. Call the greet() function to update the visitor count and print
   a statement to greet the user.
4. Print an exit statement.
5. End the program

"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES
gTotal = 0

# FUNCTIONS
def greet(person):
    global gTotal

    gTotal = gTotal + 1
    print("Hello " + person + ", you are visitor number " + str(gTotal) + " today.")

# MAIN FUNCTION
def main():
    
    print("Welcome to the Greeter program.")
    name = (input("Please enter your name: "))
    greet(name)
    print("End of program.")

main()

