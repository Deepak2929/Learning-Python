'''This code is a guessing-game program.The program keep asking the user for an answer while the current
guess is wrong. It keeps running until the user guesses the correct answer.--
from random import randint'''


secret=randint(1,10)
choice="yes"
while choice =="yes":
	print("Welcome to the guess game ")
	d=input("Enter any number to guess")
	if secret==int(d):
		print("Right, the secret key is ",secret)
		secret=randint(1,10)
		
		choice=input("Do you want to try again?")
	else:
		if secret<int(d):
			print("Too high")
			print("the secret key is :")
			print(secret)
			choice=input("Do you want to try again?")
			secret=randint(1,10)
		else:
			print("Too low")
			print("the secret key is :")
			print(secret)
			choice=input("Do you want to try again?")
			secret=randint(1,10)
print("Game over")

'''
Python Tools used:
* if/else branches
* while loops
* = assignment operator
* == equality operator
* != inequality operator
* > greater than operator
* print() displays a message on screen
* input() gets and returns user input
* int() converts characters to numbers
* randint() produces a random number
'''
	
