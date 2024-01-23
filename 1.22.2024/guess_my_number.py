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

LOW = 1
HIGH = 10

def get_secret_number() -> int:
	return random.randint(LOW, HIGH)

def get_user_guess() -> int:
	return int(input('Guess my number: '))

def check_winner(secret:int, user_guess:int) -> bool:
	if secret == user_guess:
		print('Winner winner')
		return True
	else:		
		print('Try again...')
		return False

def main():
	secret = get_secret_number()
	print(secret)
	guessed = False
	too_low = 0
	too_high = 0
	while not guessed:
		user_guess = get_user_guess()
		if user_guess < secret:
			too_low += 1
		elif user_guess > secret:
			too_high += 1
		guessed = check_winner(secret, user_guess)
	print(f'You had {too_low} guesses that were too low and {too_high}') 
	print(f'guesses that were too high.')


if __name__ == '__main__':
	main()








