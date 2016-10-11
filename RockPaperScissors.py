import random

playerScore = 0
computerScore = 0
playAgain = 'y'
playerChoice = 0


print('Hi! What is your name?')
playerName = input()
print('Nice to meet you, ' + playerName + '!')
print('.')
print('.')
print('.')

while playAgain == 'y':
	
	while playerChoice not in ['rock','paper','scissors']:
		print('Choose "rock", "paper", or "scissors."')

		playerChoice = input()
		playerChoice = playerChoice.lower()
		

		if playerChoice not in ['rock','paper','scissors']:
			print('.')
			print('.')
			print(playerChoice + ' is not an option.')
		elif playerChoice == 'rock':
			playerChoice = 0
			break
		elif playerChoice == 'paper':
			playerChoice = 1
			break
		elif playerChoice == 'scissors':
			playerChoice = 2
			break


	computerChoices = ['Rock','Paper','Scissors'] 
	computerChoice = random.choice(computerChoices)

	print('.')
	print('.')
	print('Computer chose ' + computerChoice)
	print('.')
	print('.')
	

	if computerChoice == 'Rock':
		computerChoice = 0
	elif computerChoice == 'Paper':
		computerChoice = 1
	else:
		computerChoice = 2
	

	result = playerChoice - computerChoice
	if result == 0:
		print("It's a Tie!")
	elif result == -1 or result == 2:
		print('You Lose!')
		computerScore = computerScore + 1
	else:
		print('You Win!')
		playerScore = playerScore + 1
	
	print('The score is: ' + playerName + ': ' + str(playerScore) + '      Computer: ' + str(computerScore))
	
	playAgain = 0

	while playAgain not in ['y','n']:
		print('Would you like to play again, ' + playerName + '?  (y/n)')
		playAgain = input()
		playAgain = playAgain.lower()
		
		if playAgain not in ['y','n']:
			print('.')
			print('.')
			print(playAgain + ' is not an option.')
	
		if playAgain == 'n':
			print('Okay bye!')
			exit()
		


	
