def sum_greater_than(values: list[int], target: int) -> int:
	# sum = 0
	# for value in values:
	# 	if value > target:
	# 		sum += value
	# return sum

	sum = 0
	i = 0
	while i < len(values):
		if values[i] > target:
			sum += values[i]
		i += 1
	return sum


def main():
	values = [1, 2, 3, 4, 5]
	target = 3
	print(f'expected: 9 -- actual: {sum_greater_than(values, target)}')

	values = [5, 4, 2, 1, 18]
	target = 19
	print(f'expected: 0 -- actual: {sum_greater_than(values, target)}')

	values = [8, 3, 1, 5, 5]
	target = 4
	print(f'expected: 18 -- actual: {sum_greater_than(values, target)}')


if __name__ == '__main__':
	main()