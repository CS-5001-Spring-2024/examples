"""
A python program to demonstrate how to use functions.
"""

def welcome():
	"""Exercise 1: 
	A function to print a multi-line welcome message.
	You can print this documentation using 
	print(welcome.__doc__)
	"""
	print('Hello class.')
	print('Thanks for coming back today!')
	print('Looking forward to a fun semester.')

def greet_by_name(name: str):
	"""Exercise 2:
	A function to greet a user by name.
	Parameters
	name: str
		name of the user
	"""
	print('Hello ' + name)

def get_greeting() -> str:
	"""Exercise 3:
	A function to get a specific greeting from the user.
	Returns:
	str 
		greeting provided by the user
	"""
	greeting = input('What greeting would you like to use? ')
	return greeting

def welcome_by_name_with_greeting(name: str, greeting: str=None):
	"""Exercise 4:
	A function to welcome a user by name with a 
	specific greeting.
	Parameters:
	name: str
		name of the user
	greeting: str
		greeting to use
	"""
	if greeting == None:
		greeting = get_greeting()
	# print(f'{greeting} {name}')
	print(greeting + ' ' + name)


def main():
	welcome_by_name_with_greeting(3, 'Hello')

if __name__ == '__main__':
	main()




