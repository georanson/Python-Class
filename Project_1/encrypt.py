# Author: Geoffrey Ranson
# S# G11002201
# Date: 06/10/2013
# File: encrypt.py
# Description: Encrypts a message

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

1. Input Message
2. Break up message into individual caracters
3. Turn each caracter into unicode
4. Procces unicode through equation
5. Print results to file

"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS

# MAIN FUNCTION


def main():

	unencrypted = ("")
	unencrypted = input("Please input the string you wish to encrypt: ")
	
	file = open("EncryptedMessage.txt", "w")
	
	encryptedstring = ("")
	unencryptedarray = list(unencrypted)
	for encrypt in unencryptedarray:
		unencrypted = ord(encrypt)
		encryptednum = (5*unencrypted)+6
		encryptedstring = (encryptedstring + str(encryptednum) + " ")
	print (encryptedstring)
	print (encryptedstring, file=file)
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