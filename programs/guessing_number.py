import random
# Get the user to guess a random number between 0 and 100
# Handle error if the user's input is not an integer


def testingNumberType():
    print('Guess a number between 0 and 100!')
    randomNumber = random.randrange(0, 100)

    while True:
        while True:
            guess = input('What is your guess?: ')
            try:
                guess = int(guess)
                break
            except ValueError:
                print(f'{guess} is not a number.\n')
        if guessingNumber(guess, randomNumber):
            break


def guessingNumber(guess, randomNumber):
    while guess != randomNumber:
        if guess < randomNumber:
            print('Go bigger!\n')
            return False

        elif guess > randomNumber:
            print('Go smaller!\n')
            return False
    else:
        print(f'Congratulation, the number to guess was {randomNumber}')
        return True


testingNumberType()
