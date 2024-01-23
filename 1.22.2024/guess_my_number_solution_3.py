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
	guess =	int(input('Guess my number! '))	
	while guess < LOW or guess > HIGH:
		print('Guess must be between 1 and 10')
		guess =	int(input('Guess my number! '))	
	return guess

def has_won(secret_number: int, user_guess: int) -> bool:
	return user_guess == secret_number

def print_win_message(too_low: int, too_high: int):
	print('Winner winner chicken dinner')
	print(f'You had {too_low} guesses that were too low')
	print(f'and {too_high} guesses that were too high')

def print_try_again_message():
	print('Try again...')

def main():	
	secret_number = get_secret_number()
	winner = False
	too_high = 0
	too_low = 0
	while not winner:
		user_guess = get_user_guess()
		winner = has_won(secret_number, user_guess)
		if winner:
			print_win_message(too_low, too_high)
		else:
			if user_guess < secret_number:
				too_low += 1
			else:
				too_high += 1
			print_try_again_message()
			
if __name__ == '__main__':
	main()