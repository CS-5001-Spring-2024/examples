class Item:

	def __init__(self, name, quantity, price, sku):
		self.name = name
		self.quantity = quantity
		self.price = price
		self.sku = sku

	def purchase_item(self, number_to_purchase):
		if self.quantity >= number_to_purchase:
			self.quantity -= number_to_purchase
			return True
		return False

	def add_stock(self, number_to_add):
		if number_to_add > 0:
			self.quantity += number_to_add
			return True
		return False

	# change_price
	# change_sku???

	def get_price(self):
		return self.price

	def __str__(self):
		return f'{self.name} - {self.quantity}'


