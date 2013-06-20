# Author: Geoffrey Ranson
# S# G11002201
# Date: 06/03/2013
# File: template.py
# Description: Brief description of what this program does

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

"""

# IMPORT STATEMENTS
import math

# GLOBAL VARIABLES

# FUNCTIONS

# MAIN FUNCTION
def main():

	radius = 0.0
	volume = 0.0
	area = 0.0
	unit = ("unit")
	radius = eval(input("Please input the radius of the circle: "))
	unit = input("What unit is the radius in: ")
	volume = ((4/3) * math.pi * (radius**3))
	area = 4*math.pi*(radius**2)
	print ("For a circle with a radius",radius,"the volume is",round(volume,3),unit+"^3","and the area is",round(area,3),unit+"^2")


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