import secrets
options = ['paper', 'rock', 'scissors']
computer = secrets.choice(options)

while True:
	player = input("player: pick rock, paper or scissors ")
	if player == "exit":
		print("Thanks for playing friend! see you later.")
		break
	if player == computer:
		print("it's a draw!")
	elif player == "paper" and computer == "rock":
		print("player1 winsss!")
		print("computer picked " + computer)
		print("If you want to quit, type 'exit' ")
	elif player == "rock" and computer == "scissors":
		print("player1 winsss!")
		print("computer picked " + computer)
		print("If you want to quit, type 'exit' ")
	elif player == "scissors" and computer == "paper":
		print("player1 winsss!")
		print("computer picked " + computer)
		print("If you want to quit, type 'exit' ")
	else:
		print("computer winsss!")
		print("computer picked " + computer)
		print("If you want to quit, type 'exit'")

	import random
	options = ['paper', 'rock', 'scissors']
	computer = random.choice(options)
