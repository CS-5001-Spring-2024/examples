def double_as(word: str) -> str:
	result = ''

	for char in word:
		if char == 'a':
			result += 'aa'
		else:
			result += char

	return result
	# return word.replace('a', 'aa')

def main():
	print(double_as('cat'))
	print(double_as('dog'))
	print(double_as('abra'))

if __name__ == '__main__':
	main()