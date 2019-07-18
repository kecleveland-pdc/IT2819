# This is a guess the number game
import random
import array
print("Program Written by Keaunna ", end="")
print("Cleveland")

def display_guesses(n: array) -> str:
    input = "You already guessed "
    
    for guess in n:
        if str(guess) in input:
            continue
        else:
            input += str(guess) + " "
    return input

print ('Hello, what is your name?')
name = input()
guesses = []

print ('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)
print ('secretNumber = ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print('Take a guess.\n')
    guess = int(input())
    guesses.append(guess)

    if guessesTaken > 1:
        print(display_guesses(guesses))
    
    if guess < secretNumber:
        print ('Your guess is too low.')
    elif guess > secretNumber:
        print ('Your guess is too high.')
    else:
        break # this indicates a correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
