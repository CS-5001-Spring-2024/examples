ACTUAL_PASSWORD = 'hello123'

def login():
	"""Implement a function that prompts a 
	user for a password until the actual 
	password is entered and the user is 
	authenticated.

	Step 2: allow a maximum of three attempts.

	"""
	matched = False
	attempts = 0

	while not matched and attempts < 3: # there is a match or attempts is 3
	# while attempts < 3: # there is a match or attempts is 3
		password = input('password: ')
		attempts = attempts + 1

		if password == ACTUAL_PASSWORD:
			# success
			matched = True
		else:
			print('wrong password...')

	if matched:
		print('Welcome!')
	else:
		print('Contact your sysadmin...locked out!')


def main():

	login()
	# flag = True
	# while flag:
	# 	# do something
	# 	# update flag


	# # control variable
	# count = 10 # initialize the control variable
	# while count >= 0: # condition
	# 	print(count)
	# 	count -= 1
	# 	# update control variable




if __name__ == '__main__':
	main()