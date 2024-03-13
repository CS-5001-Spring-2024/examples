from inventory_item import Item
import unittest

class InventoryItemTest(unittest.TestCase):

	def test_constructor(self):
		item = Item('Bread', 25, 2.99, 12345)
		self.assertEqual(item.name, 'Bread')
		self.assertEqual(item.quantity, 25)
		self.assertAlmostEqual(item.price, 2.99)
		self.assertEqual(item.sku, 12345)

	def test_purchase_item_number_gt_quantity_return_value(self):
		item = Item('Bread', 25, 2.99, 12345)
		result = item.purchase_item(30)
		self.assertFalse(result)

	def test_purchase_item_number_gt_quantity_quantity_result(self):
		item = Item('Bread', 25, 2.99, 12345)
		result = item.purchase_item(30)
		self.assertEqual(item.quantity, 25)

	def test_purchase_item_number_not_gt_quantity_return_value(self):
		item = Item('Bread', 25, 2.99, 12345)
		result = item.purchase_item(20)
		self.assertTrue(result)

	def test_purchase_item_number_not_gt_quantity_quantity_result(self):
		item = Item('Bread', 25, 2.99, 12345)
		result = item.purchase_item(20)
		self.assertEqual(item.quantity, 5)



if __name__ == '__main__':
	unittest.main()


# item1 = 
# item2 = Item('Rice', 10, 1.99, 98766)
# item3 = Item('Pasta', 15, 3.75, 88776)

# print(item1)
# # item1.price
# # item1.get_price()
# result = item1.purchase_item(5)
# print(f'expected: True - actual: {result}') # True


# # print(item1)
# # item1.add_stock(50)
# # print(item1)


# # # print(item2)
# # # print(item3)
