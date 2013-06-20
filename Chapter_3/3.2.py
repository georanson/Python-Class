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
sos = 1100
mile = 5280

# FUNCTIONS

# MAIN FUNCTION

def main():

	seconds = 0
	result = 0
	seconds = eval(input("How many seconds was it between the lighting flash and the thunder: "))
	result = (seconds*sos)/mile
	print ("The lightning struck",round(result,2),"miles away!")

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