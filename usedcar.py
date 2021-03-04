from newcar import NewCar

class UsedCar(NewCar):
    def __init__(self, name, model, price, color):
        super(UsedCar, self).__init__(name, model, price)
        self.color = color

    def value(self):
        print(f'The starting price for a {self.color} {self.model} {self.name} is ${self.price}.')

    def __repr__(self):
        return f" {self.name}, {self.model}, {self.price}, {self.color}"

    
    def custom_paint(self, paint=200):
        new_price = self.price + paint
        print(f'Price for this car after paint will be ${new_price}')


mycar = UsedCar('Fusion', 'Ford', 5000, 'Blue')
print(mycar)
mycar.custom_paint()
