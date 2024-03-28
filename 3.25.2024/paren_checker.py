
# from: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/#

"""
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {{[]{()}}
Output : Unbalanced

Input : {[]{()}}
Output : Balanced

Input : [{}{})
Output : Unbalanced
"""
from stack import Stack

OPEN_CHARS = ['(', '[', '{']
CLOSE_CHARS = [')', ']', '}']

def match(open_char, close_char) -> bool:
	# if (open_char == '(' and close_char == ')'
	# 	 or open_char == '[' and close_char == ']'
	# 	 or open_char == '{' and close_char == '}'):
	# 	return True
	# return False

	return OPEN_CHARS.index(open_char) == CLOSE_CHARS.index(close_char)


# print(match('(', '}'))

def check(paren_string) -> bool:
	stack = Stack(10)

	for char in paren_string:
		if char in OPEN_CHARS:
			# if you see a left bracket - push
			stack.push(char)
		elif char in CLOSE_CHARS:
			# if you see a right bracket - pop						
			if stack.size() == 0:
				# when we see a close -- there has to be something on the stack
				return False
			else:
				# when we see a close -- the top item on the stack has to match
				if not match(stack.pop(), char):
					return False
				
	# when we have looked at all chars the stack must be empty
	return stack.size() == 0

print(check('{{[]{()}}'))
print(check('{[]{()}}'))
print(check('[{}{})'))


