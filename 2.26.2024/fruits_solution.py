fruits_by_color = {}

def go_again() -> bool:
	go_again = ''
	while go_again != 'y' and go_again != 'n':
		go_again = input('Go again? (y/n) ')
	return go_again == 'y'

def show_fruits_by_color(fruits_by_color: dict):
	for color in fruits_by_color:
		fruits = fruits_by_color[color]
		print(color)
		for fruit in fruits:
			print(f'\t{fruit}')

def build_fruits_by_color() -> dict:
	fruits_by_color = {}
	again = True
	while again:
		color = input('Give me a color: ')
		if color in fruits_by_color:
			fruits = fruits_by_color[color]
		else:
			fruits = []
			fruits_by_color[color] = fruits
		fruit = ''
		while fruit != 'q':
			fruit = input(f'Give me a {color} fruit - q to end: ')
			if fruit != 'q':
				fruits.append(fruit)
		# fruits_by_color[color] = fruits
		again = go_again()
	return fruits_by_color

fruits_by_color = build_fruits_by_color()
show_fruits_by_color(fruits_by_color)