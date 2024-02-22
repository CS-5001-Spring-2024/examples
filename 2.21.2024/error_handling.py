# See: https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/os.html
import os

def convert(value, target_type):
	"""
	Write a function to convert value into the target type. 
	Valid type for target_type is int or float.
	If the value is already the target_type
		return the value without conversion
	If the target_type is not int or float
		generate a TypeError
	If the value cannot be converted
		return a ValueError
	"""
	# '5'
	# int

	if target_type != int and target_type != float:
		raise TypeError(f'Cannot convert to type {target_type}')

	if isinstance(value, target_type):
		return value

	if target_type == int:
		int_value = int(value)
		return int_value

	if target_type == float:
		float_value = float(value)
		return float_value


def read_file(filename: str):
	"""
	Write a function to display the contents of a file.
	The function will throw an exception if the file is
	not found.
	"""
	with open(filename, 'r') as input_file:
		for line in input_file:
			print(line)

def search_replace(search:str, 
	replace:str, 
	infilename:str, 
	outfilename:str):
	"""
	Write a function that will replace all instances of a search
	term in a given file with a replace term. The result will be 
	saved to a new file.
	
	Parameters:
	search : str
		the string to replace
	replace : str
		the replacement string
	infilename : str
		the name of the original file
	outfilename : str
		the name of the file where the result will be saved
	"""
	with open(infilename, 'r') as input_file, open(outfilename, 'w') as output_file:
		for line in input_file:
			result = line.replace(search, replace)
			print(result)
			output_file.write(result)


def find_py_files(root: str):
	# /Users/srollins/teaching/cs5001-f23 
	'''
	Write a recursive function to list all files in any
	descendant directory of a given root.
	'''
	if os.path.isfile(root) and root.endswith('py'):
		print(f'Python file: {root}')
	elif os.path.isdir(root):
		results = os.listdir(root)
		for result in results:
			find_py_files(os.path.join(root, result))

def main():


	# try :
	# 	search_replace('class', 'CS 5001', 'class_file.txt', 'out.txt')
	# except FileNotFoundError as fnf:
	# 	print(fnf)

	# try :
	# 	convert('123a', int)
	# except TypeError as te:
	# 	print(te)
	# except ValueError as ve:
	# 	print(ve)
	# print('next line...')

	# i = 0
	# while i < 10:
	# 	print(i)
	# 	if i % 3 == 0:
	# 		i += 1
	# 		continue
	# 	i += 2


	# success = False
	# while not success:
	# 	number_str = input('enter a floating point number: ')
	# 	try:
	# 		number_float = float(number_str)
	# 	except ValueError as ve:
	# 		print(ve)
	# 		continue
	# 	except TypeError as te:
	# 		print(te)

	# 	success = True
	# print(f'you said {number_float}')	














if __name__ == '__main__':
	main()