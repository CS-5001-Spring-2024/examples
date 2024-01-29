"""
Practice with strings!
"""

def fun_with_strings():
	"""
	What can you do with a string?!
	https://docs.python.org/3/library/stdtypes.html#string-methods
	"""	
	name = 'The cat in the hat'
	# Accessing individual characters	
	# print(name[3])
	# Strings are immutable!
	# name[0] = 'X' # ERROR!
	# Slicing strings
	# print(name[2:7])

	# Calling string methods -- like replace!
	# print(name.capitalize())	
	print(f'BEFORE: {name}')
	name = name.replace('cat', 'dog')
	print(f'AFTER: {name}')

def reverse(phrase: str) -> str:
	"""
	A function to reverse the string passed as input.
	"""
	result = ''
	i = len(phrase) - 1
	while i >= 0:
		# print(phrase[i])
		result = result + phrase[i]
		i -= 1

	return result

def is_palindrome(word: str) -> bool:
	"""
	A palindrome is a word that is the same forward
	and backward. Examples are madam, racecar, and deed.
	This function takes as input a word and returns True
	if the word is a palindrome and False otherwise.
	You may assume that the string does not contain spaces.
	Consider two different approaches to implementing 
	this function.
	"""
	# if word == reverse(word):
	# 	return True
	# return False
	
	return word == reverse(word)


def main():
	# fun_with_strings()
	# print(reverse('computer'))
	print(is_palindrome('deed'))
	print(is_palindrome('racecar'))
	print(is_palindrome('computer'))

if __name__ == '__main__':
	main()