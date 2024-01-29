"""
Practice with for loops!
"""
VOWELS = ('a', 'e', 'i', 'o', 'u')

def fun_with_for_loops():
	list = ["hello", "there", "cs", "5001", "class"]
	# i = 0
	# while i < len(list):
	# 	item = list[i]		
	# 	print(f'{i} {item}')
	# 	i += 1

	# Iterating over a list is easier with a for loop!

	# Accessing the index using range()

	# Accessing the index using enumerate

	# Using zip to iterate over two lists at once

def multiples_of_5(number: int):
	"""
	A function that takes as input a positive integer and
	uses a for loop to print the multiples of 5 that are 
	less than or equal to the number that was entered.
	"""
	pass

def generate_user_names(first_names: list[str], 
	last_names: list[str]) -> list[str]:
	"""
	A function that takes as input a list of strings
	representing first names and a list of strings representing
	last names and returns a list of usernames where the ith username
	is the first initial of the first name stored at the ith position
	of the first_names list concatenated with the first 7 characters 
	of the last name stored at the ith position of the last_names
	list.
	"""
	pass

def nested_loops():
	board = [
				['x', '-', 'x'], 
				['o', '-', '-'],
				['-', '-', '-']
			]


def gradebook():
	grades  = [
				[95, 99, 82],
				[90.5, 92, 84],
				[85, 79, 82],
				]

	# student 1: XXX
	# student 2: YYY
	# student 3: ZZZ


def is_vowel(char: str) -> bool:	
	return char in VOWELS

	# if (char == 'a' 
	# 	or char == 'e'
	# 	or char == 'i'
	# 	or char == 'o'
	# 	or char == 'u'):
	# 	return True
	# return False

def count_vowels(sentence: str) -> int:
	"""
	A function that takes as input a string and returns the number
	of vowels (a, e, i, o, u) that are found in the sentence.
	"""
	pass

def main():
	pass

if __name__ == '__main__':
	main()