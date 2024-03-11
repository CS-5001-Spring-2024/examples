from inventory_item import Item
from inventory import Inventory

carbs = Inventory()
# approach 1
item = Item('Bread', 25, 4.99, 12345)
carbs.add_new_item(item)
item = Item('Rice', 15, 1.99, 98765)
carbs.add_new_item(item)
item = Item('Pasta', 70, 3.75, 12234)
carbs.add_new_item(item)
print(carbs)

# approach 2
# carbs.add_new_item('Bread', 25, 4.99, 12345)

result = carbs.purchase_item(12345, 5)
print(result)
print(carbs)

result = carbs.purchase_item(12345, 50)
print(result)
print(carbs)


# produce = Inventory()

# canned_goods = Inventory()
