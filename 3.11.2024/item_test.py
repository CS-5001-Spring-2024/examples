from inventory_item import Item

item1 = Item('Bread', 25, 2.99, 12345)
item2 = Item('Rice', 10, 1.99, 98766)
item3 = Item('Pasta', 15, 3.75, 88776)

print(item1)
# item1.price
# item1.get_price()
item1.buy(5)
print(item1)
item1.add_stock(50)
print(item1)


# print(item2)
# print(item3)
