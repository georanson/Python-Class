# Author: Geoffrey Ranson
# S# G11002201
# Date: mm/dd/2013
# File: template.py
# Description: Brief description of what this program does

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES
ppp = 10.50
spp = 0.86
fixed = 1.50

# FUNCTIONS

# MAIN FUNCTION

def main():

	pounds = 0
	result = 0
	pounds = eval(input("How many pounds of coffee are you buying today? "))
	result = (ppp*pounds)+(spp*pounds)+fixed
	print ("Thank you for shopping with us. Today your order of",pounds,"pounds of coffee will cost you",result+".")


main()

"""
Black Knight: 'Tis but a scratch!
King Arthur:  A scratch? Your arm's off!
Black Knight: No, it isn't!
King Arthur:  Well, what's that then?
King Arthur:  I've had worse.
King Arthur:  You liar!
Black Knight: Come on, you pansy!
[they fight again. Arthur cuts off the Knight's right arm]

"""