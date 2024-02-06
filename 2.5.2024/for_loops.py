
def get_names() -> list[str]:
	names = []
	name = input('Enter a name, quit to end input: ')
	while name != 'quit':
		names.append(name)
		name = input('Enter a name, quit to end input: ')
	return names

def names_starting_with_s(names: list[str]) -> int:
	count = 0
	for name in names:
		if name.lower().startswith('s'):
		# if name.startswith('s') or name.startswith('S'):
			count += 1
	return count

def main():
	names = get_names()
	print(names)
	count_of_s_names = names_starting_with_s(names)
	print(count_of_s_names)

if __name__ == '__main__':
	main()
