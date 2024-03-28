class Queue:

	def __init__(self, max_size=10):
		self.max_size = max_size
		self.items = []

	def enqueue(self, item):
		# TODO: handle list full

		# option 1
		self.items.append(item)

		# option 2
		self.items.insert(0, item)

	def dequeue(self):
		# TODO: handle list empty

		# option 1
		return self.items.pop(0)

		# option 2
		return self.items.pop()

