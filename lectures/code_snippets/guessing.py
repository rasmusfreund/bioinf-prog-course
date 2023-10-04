from random import randint
from math import log
secret_number = randint(1,10)

print(log(256, 2))

max_guesses = 4

guess = int(input('Your guess: '))
while guess != secret_number and max_guesses:
	if guess < secret_number:
		guess = int(input('Too low try again: '))
	else:
		guess = int(input('Too high try again: '))

	max_guesses = max_guesses - 1

print('Correct')
