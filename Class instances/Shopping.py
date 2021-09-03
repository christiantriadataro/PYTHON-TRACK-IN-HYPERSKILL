# Find the mistakes in the __init__ method of the class Store
# and fix them so that the attributes of the object shop would 
# be printed out correctly.

class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category

shop = Store("GAP", "clothes")
print(shop.name, shop.category)