class Product(object):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price 

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.name == other.name and self.price == other.price
        return False

    def getId(self):
        return self.id
         
    def getName(self):
        return self.name 

    def getPrice(self):
        return self.price

    