
# def count_ing_words() -> int:
# 	count = 0
# 	word = ''
# 	while word != 'quit':
# 		word = input('Enter word: ')
# 		word = word.lower()
# 		if word.endswith('ing'):
# 			count += 1
# 	return count

def count_ing_words() -> int:
	count = 0
	word = input('Enter word: ').lower()
	while word != 'quit':				
		if word.endswith('ing'):
			count += 1
		word = input('Enter word: ').lower()

	return count


def main():
	result = count_ing_words()
	print(result)

if __name__ == '__main__':
	main()
