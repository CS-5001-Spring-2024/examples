def func(x: list):
	x.append('cat')

def main():
	x = ['dog', 'horse', 'bird']
	func(x)
	print(x)

if __name__ == '__main__':
	main()