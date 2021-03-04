

class NewCar:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def value(self):
        print(f'A new {self.model} {self.name} has a starting price of ${self.price}.')


    def testdrive(self, speed):
        pass
        