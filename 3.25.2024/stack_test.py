from stack import Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
try:
	print(stack.pop())
except:
	print('trying to pop from empty stack')
stack.push(4)
try:
	print(stack.pop())
except:
	print('trying to pop from empty stack')

try:
	print(stack.pop())
except:
	print('trying to pop from empty stack')

try:
	print(stack.pop())
except:
	print('trying to pop from empty stack')

try:
	print(stack.pop())
except:
	print('trying to pop from empty stack')

try:
	print(stack.pop())
except:
	print('trying to pop from empty stack')

