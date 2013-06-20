# Author: Geoffrey Ranson
# SN# G11002201
# Date: 05/20/2013
# File: convert_table.py
# Description: Converts Celsius to Fahrenheit then prints a table
 

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS

# MAIN FUNCTION

def main():
	print ("////////////////")
	print ("// C ////// F //")
	print ("////////////////")
	for celsius in [0,10,20,30,40,50,60,70,80,90,100]:
		fahrenheit = (((9/5)*celsius)+32)
		if celsius<10:
			space1 = ("  //")
		elif celsius<100:
			space1 = (" //")
		else:
			space1 = ("//")
			
		if fahrenheit<10:
			space2 = ("  /")
		elif fahrenheit<100:
			space2 = (" /")
		else:
			space2 = ("/")
		print ("/",celsius,space1,fahrenheit,space2)
	print ("////////////////")

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

