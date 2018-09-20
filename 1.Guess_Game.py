from random import randint
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

	
