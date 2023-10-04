from random import randint

name = input('What should I call you?: ')
max_number = int(input('Difficulty (max number): '))

secret_number = randint(1,max_number)
guess = int(input('Your guess: '))

guesses = 1

while guess != secret_number:
	if guess > secret_number:
		print("Too hight guess again!")
	else:
		print("Too low guess again!")
	guess = int(input('Your guess: '))
	guesses = guesses + 1
score = max_number / guesses

print("Lucky guess {}!. Your score is {}".format(name, score))

f = open('highscores.txt', 'w+')
print("{}\t{}".format(name, score), file=f)