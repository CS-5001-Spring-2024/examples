"""
Write a program (remember that programs have a main() function) to print the lyrics of the song "Old MacDonald." Your program should print the lyrics for five different animals (five verses), similar to the example verse below:
"""

# Old MacDonald had a farm, ee-igh, ee-igh, oh!
# And on that farm he had a cow, ee-igh, ee-igh, oh!
# With a moo, moo here and a moo, moo there.
# Here a moo, there a moo, everywhere a moo, moo.
# Old MacDonald had a farm, ee-igh, ee-igh, oh!

# TODO: discuss the string split function

def sing(animal: str, sound: str):
# def sing(animal_and_sound: tuple[str, str]):	
	# animal = animal_and_sound[0]
	# sound = animal_and_sound[1]

	print('Old MacDonald had a farm, ee-igh, ee-igh, oh!')
	print(f'And on that farm he had a {animal}, ee-igh, ee-igh, oh!')
	print(f'With a {sound}, {sound} here and a {sound}, {sound} there.')
	print(f'Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.')
	print('Old MacDonald had a farm, ee-igh, ee-igh, oh!')

# ask for an input
def ask_animal_and_sound() -> tuple[str, str]:
	# animal = input('Enter animal name: ')
	# sound = input('Enter sound: ')
	result = input('Give me an animal and a sound: ')
	animal, sound = result.split()
	return animal, sound

def main():

	i = 0
	while i < 5:
		animal, sound = ask_animal_and_sound()
		sing(animal, sound)
		i += 1



	# sing('pig', 'oink')
	# sing('cow', 'moo')

	# ('pig', 'oink')
	# print(ask_animal_and_sound())

	# sing(ask_animal_and_sound())

	animal, sound = ask_animal_and_sound()
	sing(animal, sound)

	# animal, sound = ask_animal_and_sound()
	# sing(animal, sound)

	# animal, sound = ask_animal_and_sound()
	# sing(animal, sound)

	# animal, sound = ask_animal_and_sound()
	# sing(animal, sound)

	# animal, sound = ask_animal_and_sound()
	# sing(animal, sound)


if __name__ == '__main__':
	main()
