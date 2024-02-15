'''
Practice with recursion!
'''

def factorial_iterative(n: int) -> int:
	"""
	A function that takes as input an integer and returns the 
	factorial of that number.
	"""
	# result = 1
	# while n > 0:
	# 	result = result * n
	# 	n -= 1
	# return result

	result = 1
	current = 1
	while current <= n:
		result *= current
		current += 1
	return result

def factorial_recursive(n: int) -> int:
	"""
	A function that takes as input an integer and returns the 
	factorial of that number.
	This implementation does not use a loop.
	"""
	# base case
	if n == 1:
		return 1

	# recursive case
	return n * factorial_recursive(n-1)


def print_string(string: str):
	"""
	Implement a recursive function that takes as input 
	a str and prints the characters of the str one per 
	line *without using a loop*. 
	"""
	# base case -- empty string
	# 		stop...return...nothing
	if string == '':
		return

	# print a letter
	print(string[0])

	# recursively call
	print_string(string[1:])


def print_string_backward(string: str):
	"""
	Implement a recursive function that takes as input 
	a str and prints the characters of the str *in 
	reverse* one per line *without using a loop*. 
	"""
	# base case -- empty string
	# 		stop...return...nothing
	if string == '':
		return

	# recursively call
	print_string_backward(string[1:])		

	# print a letter
	print(string[0])


def print_nums_iterative(n: int):
	"""
	A function that takes as input a number and prints 
	from 1 to the number (inclusive).
	"""
	pass

def print_nums_recursive(n: int):
	"""
	Implement print_nums_iterative above without using a loop.
	There are several ways to do this. We will look at how to
	use a helper function.
	"""
	# if n == 0:
	# 	return
	
	# print(n)
	# print_nums_recursive(n-1)
	
	if n == 0:
		return
	print_nums_helper(1, n)

def print_nums_helper(current: int, n: int):
	if current == n:
		print(current)
		return
	print(current)
	print_nums_helper(current + 1, n)


def find_char_a(string: str) -> int:
	"""
	Implement a function that returns the number of times the 
	character "a" appears in a str without using a loop. 
	You may not use the count function.
	"""
	if len(string) == 0:
		return 0
	if string[0] == 'a':
		return 1 + find_char_a(string[1:])
	else:
		return find_char_a(string[1:])


def num_to_word(number: int) -> str:
	# if number == 0:
	# 	return 'zero'
	# if number == 1:
	# 	return 'one'
	match number:
		case 0:
			return 'zero'
		case 1:
			return 'one'
		case 2:
			return 'two'
		case 3:
			return 'three'
		case 4:
			return 'four'
		case 5:
			return 'five'
		case 6:
			return 'six'
		case 7:
			return 'seven'
		case 8:
			return 'eight'
		case 9:
			return 'nine'			

def in_english(number: int) -> str:
	"""
	Write a recursive function called in_english that takes a 
	integer value as input and returns a string containing 
	the digits of the number in English. For example, 
	in_english(153) would return "one five three".
	"""
	if number >= 0 and number <= 9:
		return num_to_word(number)		

	return in_english(number // 10) + ' ' + num_to_word(number % 10)
	# return num_to_word(number % 10) + ' ' + in_english(number // 10)
 

def binarysearch(list: list[int], target: int) -> bool:
 	"""
 	Write a recursive function that returns True if the target
 	exists in the list and False otherwise.
 	"""
 	if len(list) == 0:
 		return False
 	if len(list) == 1:
 		return list[0] == target
 	# slice
 	# //
 	mid_index = len(list) // 2
 	if list[mid_index] == target:
 		return True
 	if list[mid_index] < target:
 		return binarysearch(list[mid_index+1:], target)
 	return binarysearch(list[:mid_index], target)


def main():
	# print(factorial_recursive(3))
	# print(factorial_recursive(5))
	# print_string_backward('computer')
	# print_nums_recursive(5)
	# print(find_char_a('dog'))
	# print(in_english(4259))
	# print(in_english(6))
	# print(in_english(0))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],0))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],1))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],2))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],4))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],16))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],73))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],89))
	print(binarysearch([1, 2, 4, 16, 73, 89, 450],95))

	# pass

if __name__ == '__main__':
	main()