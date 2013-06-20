# Author: Geoffrey Ranson
# SN# G11002201
# Date: mm/dd/yyyy
# File: chaos_mod.1.py
# Description: Deomstrates a chotic function

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

1.Ask user for input 0<=x<=1
2.Process variable through equation
3.Return result

"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS

# MAIN FUNCTION
def main():
    x=0.0
    print ("This program demonstrates a chaotic funtion")
    x=eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
            x = 3.9 * x * (1-x)
            print (x)
	

main()
