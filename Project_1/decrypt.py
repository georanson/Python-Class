# Author: Geoffrey Ranson
# S# G11002201
# Date: 06/10/2013
# File: decrypt.py
# Description: Decrypts a message

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

1. Import encrypted message file
2. Split encrypted message up by spaces
3. Process each number through reversed equation
4. Convert the resulting number back to a character
5. Print the message

"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS

# MAIN FUNCTION

def main():
	string= ("")

	file = open("EncryptedMessage.txt", "r")
	decryptnum = ("")
	string = file.read()
	for decrypt in string:
		if decrypt == " ":
			numchar = (eval(decryptnum))
			decryptednum = (numchar-6)/5
			decryptednum = int(decryptednum)
			decryptnum = ("")
			print (chr(decryptednum), end="")
		else:
			decryptnum = decryptnum + decrypt
			
	print ("")
	file.close

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