class Students:

	def __init__(self):
		self.students = []

	def __str__(self):
		result = ''
		for student in self.students:
			result += str(student) + '\n'
		return result