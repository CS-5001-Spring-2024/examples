
# This import is not strictly necessary if
# we aren't instantiating an Item in this 
# class. We can still call methods on an
# Item object passed to the class through
# a method.
from inventory_item import Item

class Inventory:

	def __init__(self):
		
		# key: sku: str
		# value: item object
		self.items = {}

	# add new items
	# approach 1
	def add_new_item(self, item):
		if item.sku in self.items:
			raise Exception('We already sell that.')
		self.items[item.sku] = item

	# add new items
	# approach 2
	# def add_new_item(self, name, quantity, price, sku):
	# 	item = Item(name, quantity, price, sku)
	# 	self.items[sku] = item

	# remove item

	# combine items

	# purchase item
	def purchase_item(self, sku, number_to_purchase):
		if sku not in self.items:
			raise Exception('We don\'t sell that')
		return self.items[sku].purchase_item(number_to_purchase)

	def __str__(self):
		result = f''
		for item in self.items.values():
			result += f'{item}' + '\n'
		return result













