inventory = {}

def add_new_item(new_item, number_available: int):
	"""
	Add a new item to the inventory with quantity number_available.
	Raises an exception if the item is already in the 
	inventory.
	"""
	if new_item in inventory:
		raise Exception('We already sell that.')
	inventory[new_item] = number_available

def get_number_available(item_to_find) -> int:
	"""
	Return the number of the givenword_counts[word] item that are available
	in the inventory.
	Raises a KeyError if the item is not found in the inventory.
	"""
	return inventory[item_to_find]

def update_number_available(item_to_find, number_purchased: int):	
	"""
	Update the number of the given item that are available in 
	the inventory.
	Raises an Exception if there is not a sufficient quantity 
	of the item available. 
	"""
	if inventory[item_to_find] < number_purchased:
		raise Exception('Insufficient quantity.')
	else:
		inventory[item_to_find] -= number_purchased

def show_inventory():
	"""
	Display the item names and amounts for all items in the
	inventory.
	"""
	for item in inventory:
		print(f'\t{item} - {inventory[item]}')

def main():
	try:
		add_new_item('bread', 10)
		add_new_item('rice', 15)
		show_inventory()
		print(get_number_available('rice'))		
		update_number_available('bread', 5)
		show_inventory()
		update_number_available('bread', 6)
		show_inventory()
	except: 
		print('exception...')

if __name__ == '__main__':
	main()



# inventory = {}

# inventory['rice'] = 10
# inventory['pasta'] = 25
# inventory['bread'] = 3
# inventory['ramen'] = 2

# for item in inventory.items():
# 	print(item)

# inventory.pop('bread')

# for item in inventory.items():
# 	print(item)
