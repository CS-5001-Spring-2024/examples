inventory_item = []
inventory_quantity = []


def add_new_item(new_item, number_available: int):
	"""
	Add a new item to the inventory with quantity number_available.
	Raises an exception if the item is already in the 
	inventory.
	"""
	if new_item in inventory_item:
		raise Exception('We already sell that.')
	inventory_item.append(new_item)
	inventory_quantity.append(number_available)

def get_number_available(item_to_find) -> int:
	"""
	Return the number of the given item that are available
	in the inventory.
	Raises a KeyError if the item is not found in the inventory.
	"""
	for index, item in enumerate(inventory_item):
		if item_to_find == item:
			return inventory_quantity[index]
	raise KeyError(f'Key {item_to_find} not found.')		
			
def update_number_available(item_to_find, number_purchased: int):	
	"""
	Update the number of the given item that are available in 
	the inventory.
	Raises an Exception if there is not a sufficient quantity 
	of the item available. 
	"""
	found = False
	for index, item in enumerate(inventory_item):
		if item == item_to_find:
			if inventory_quantity[index] >= number_purchased:
				inventory_quantity[index] -= number_purchased
				found = True
			else:
				raise Exception('Insufficient quantity.')
	if not found:
		raise KeyError(f'Key {item_to_find} not found.')

def show_inventory():
	"""
	Display the item names and amounts for all items in the
	inventory.
	"""
	print(inventory_item)
	print(inventory_quantity)

def main():
	try:
		add_new_item('bread', 10)
		add_new_item('rice', 15)
		show_inventory()
		print(get_number_available('rice'))		
		# update_number_available('bread', 5)
		show_inventory()
		# update_number_available('bread', 6)
		# show_inventory()
	except KeyError as ke: 
		print('exception...')


if __name__ == '__main__':
	main()