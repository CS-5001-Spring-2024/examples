def go_again() -> bool:
	go_again = ''
	while go_again != 'y' and go_again != 'n':
		go_again = input('Go again? (y/n) ')
	return go_again == 'y'

def show_fruits_by_color(fruits_by_color: dict):
	for color in fruits_by_color:
		print(color)
		fruits = fruits_by_color[color]
		for fruit in fruits:
			print(f'\t{fruit}')

def build_fruits_by_color() -> dict:
	fruits_by_color = {}
	while go_again():
		color = input('Give me a color: ')

		if color in fruits_by_color:
			fruits = fruits_by_color[color]
		else:
			fruits = []
			fruits_by_color[color] = fruits		

		fruit = input(f'Give me a {color} fruit - q to end: ')
		while fruit != 'q':
			fruits.append(fruit)
			fruit = input(f'Give me a {color} fruit - q to end: ')			
		
	return fruits_by_color

def main():
	fruits_by_color = build_fruits_by_color()
	show_fruits_by_color(fruits_by_color)

if __name__ == '__main__':
	main()

