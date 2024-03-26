from student import Student
from students import Students

import json


all_students = Students()
filename = 'students.json'
with open(filename) as students_data:
	students = json.load(students_data)
	for item in students['students']:
		student = Student(item['name'], item['id'], item['grades'])
		all_students.students.append(student)

print(all_students)

# student1 = Student('Sue', 12345)
# student2 = Student('Joe', 98765)

# student1.grades.append(90)
# print(student2.grades)