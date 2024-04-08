import random
# insertion sort
# bubble sort
# selection sort

# [5, 2, 67, 8, 2, 8, 1, 9, 3, 2]

# [1, 2, 67, 8, 2, 8, 5, 9, 3, 2]

# [1, 2, 2, 8, 67, 8, 5, 9, 3, 2]

# [1, 2, 2, 2, 67, 8, 5, 9, 3, 8]

# [1, 2, 2, 2, 3, 8, 5, 9, 67, 8]

# [1, 2, 2, 2, 3, 5, 8, 9, 67, 8]

# [1, 2, 2, 2, 3, 5, 8, 9, 67, 8]

# [1, 2, 2, 2, 3, 5, 8, 8, 67, 9]

# [1, 2, 2, 2, 3, 5, 8, 8, 9, 67]

def selection_sort(things: list):
	for i in range(len(things)-1):
		min = i
		for j in range(i+1, len(things)):
			if things[j] < things[min]:
				min = j
		
		temp = things[i]
		things[i] = things[min]
		things[min] = temp

		# things[i], things[min] = things[min], things[i]
	return things


def main():
	my_list = [i for i in range(100)]
	random.shuffle(my_list)
	print(my_list)
	sorted_list = selection_sort(my_list)
	print(sorted_list)

main()


