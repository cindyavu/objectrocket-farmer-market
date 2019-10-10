class Product(object):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price 

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.name == other.name and self.price == other.price
        return False

    def get_id(self):
        return self.id
         
    def get_name(self):
        return self.name 

    def get_price(self):
        return self.price

    