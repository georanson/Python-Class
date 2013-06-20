# Author: Geoffrey Ranson
# SN# G11002201
# Date: mm/dd/yyyy
# File: chaos_working.py
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
    x=float(input("Enter a number between 0 and 1: "))
    for i in range(10):
            x = 3.9 * x * (1.0-x)
            print (x)
	

main()