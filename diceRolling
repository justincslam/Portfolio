import random
total = 0
playAgain = 'y'

while playAgain == 'y':
    print('How many dice?')
    number = int(input())

    for i in range(number):
        roll = random.randint(1,6)
        print('You rolled a ' + str(roll) + '!')
        total = total + roll
    
    print('The sum of your rolls is ' + str(total) + '.')
    total = 0
    
    playAgain = 0
    
    while playAgain not in ['y','n']:
        print('Roll again? (y/n)')
        playAgain = input()
        playAgain = playAgain.lower()
        
        if playAgain not in ['y','n']:
            print(playAgain + ' is not an option.')
            
        if playAgain == 'n':
            print('Okay bye!')
            exit()
        
