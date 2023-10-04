from random import randint
secret_number = randint(1,100)

guess = int(input('Your guess: '))
print(guess, secret_number)

while guess != secret_number:
	print("Ha! wrong!")
	guess = int(input('Your guess: '))

print("Lucky guess!")













# nr_guesses = 1
# while guess != secret_number:
# 	if guess > secret_number:
# 		guess = int(input('Too high. Try again: '))
# 	else:
# 		guess = int(input('Too low. Try again: '))
# 	nr_guesses += 1
# print("Got it in {} tries".format(nr_guesses))