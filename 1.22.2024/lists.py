"""
Practice with lists!
"""

def fun_with_lists():
	"""
	What can you do with a list?!
	"""
	# Lists are mutable!
	# Creating a list
	names = ['Jerry', 'Jon', 'Soojin']
	# print(names)
	names.append('Promise')
	# print(names)

	# Accessing elements of a list
	# print(names[0])


	# Modifying lists
	names[0] = 'Joel'
	# print(names)	
	# print(names)
	# print(type(names))

	# Appending to a list
	# Lists of mixed types
	# class_list = [['CS 5001', 8], ['CS 5004', 3]]
	# print(class_list[1][0])

	# Slicing a list
	print(names)
	print(names[1:3])
	print(len(names))

def list_to_string(list_of_string: list[str]) -> str:
	"""
	A function that takes a list of strings and
	combines them into a single string with 
	spaces between each word. Returns the string.		
	"""
	result = ''
	i = 0	
	while i < len(list_of_string):
		result = result + list_of_string[i] + ' '
		i += 1
	return result
	
def greater_than_100(values: list[int]) -> int:
	"""
	A function that takes as input a list of ints
	and returns the number of ints in the list that
	are greater than 100.
	"""
	i = len(values)-1
	# i = -1
	result = 0
	while i >= 0:
		if values[i] > 100:
			result += 1
		i -= 1
	return result

def main():
	# fun_with_lists()
	values = [101, 2, 44, 533, 4, 222, 49, 243, 501]	
	print(values[-3])
	result = greater_than_100(values)
	print(result)
	# months = ['may', 'june', 'august', 'september']
	# result = list_to_string(months)
	# print(result)

if __name__ == '__main__':
	main()