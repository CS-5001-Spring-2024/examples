"""
Implement a guess my number program. The computer will 
randomly generate a secret number and ask the user for 
a guess. If the user's number is the same as the secret
number a winner message will be printed. Otherwise, a 
try again message will be printed.

Phase 2:
- allow the user to keep guessing until the number is
found

Phase 3:
- keep track of the number of guesses too high and the
number of guesses too low
"""

# see: https://www.w3schools.com/python/ref_random_randint.asp
import random

def main():
	secret_number = random.randint(1, 10)
	guessed = False
	while not guessed:
		user_guess = int(input('Guess my number! '))	
		if user_guess > 10 or user_guess < 1:
			print('Guess must be between 1 and 10')
		elif user_guess == secret_number:
			print('Winner winner chicken dinner')
			guessed = True
		else:
			print(f'Try again...')

if __name__ == '__main__':
	main()