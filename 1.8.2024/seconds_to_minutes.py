"""
A program to prompt a user to enter a number of seconds and 
covert that to minutes.

Examples:

Enter a number of seconds: 60
You entered 60 seconds.
60 seconds is 1.0 minutes

Enter a number of seconds: 90
You entered 90 seconds.
90 seconds is 1.5 minutes

# https://docs.python.org/3/tutorial/inputoutput.html

"""

def main():
	# get a number from the user
	seconds = int(input('Enter a number of seconds: '))
	# print(type(seconds))

	# * make sure what we got is a positive integer
	# < > <= >= == 
	
	# seconds > 0 -- turn seconds into minutes
	# seconds between -100 and 0 -- seconds is slightly negative
	# seconds is smaller than -100 -- seconds is very negative

	if seconds > 0:	
		# turn seconds into minutes
		# -- divide seconds by 60 and store in a new variable
		# -- + - * / //
		minutes = seconds / 60

		# output our result
		print(f'{seconds} seconds is {minutes} minutes')
	else:
		print(f'Seconds is negative...but...')
		if seconds > -100:
			print(f'Seconds is slightly negative.')
		elif seconds > -200:
			print(f'Seconds is pretty negative.')
		else:
			print(f'Seconds is very negative.')

















if __name__ == '__main__':
	main()	