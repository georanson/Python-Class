# Author: Geoffrey Ranson
# SN# G11002201
# Date: mm/dd/2013
# File: avg3.py
# Description: Averages 3 test scores

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

1.Ask user to input test scores
2.Average the test scores
3.Output the results

"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS

# MAIN FUNCTION
def main():
	print("This program computes the average of two exam scores.")
	
	score1,score2,score3 = eval(input("Enter three scores seperated by a comma: "))
	average = ((score1 + score2 + score3)/3)
	
	print("The average of the scores is:",average)
	
main()

"""
Black Knight: 'Tis but a scratch!
King Arthur: A scratch? Your arm's off!
Black Knight: No, it isn't!
King Arthur: Well, what's that then?
King Arthur: I've had worse.
King Arthur: You liar!
Black Knight: Come on, you pansy!
[they fight again. Arthur cuts off the Knight's right arm]

"""