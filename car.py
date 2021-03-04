import random

class Car:

    def __init__(self, name, color, gas_type, year):
        self.name = name
        self.color = color
        self.gas_type = gas_type
        self.year = year

    def __str__(self):
        # Representing Object as String
        return f'{self.name}, {self.color}, {self.gas_type}, {self.year}'

    def drive(self, location):
        # Method to drive to certain location
        return f'Driving to {location}.'

    def get_color(self):
        # Method to get car color
        return self.color
    
    def get_gas_type(self):        
        #  Method to get the cars gas type
        return self.gas_type




class Ford(Car):

    def __init__(self, name, color, gas_type, year, car_type):
        super().__init__(name, color, gas_type, year)
        self._car_type = car_type
    
    def get_car_type(self):
        # Method to get the protected _car_type, but only avilible to it's class and subclasses 
        return f'This Ford is a {self._car_type}'

    def drive(self, location, resting_point):
        # Overriding the parent method
        return f'Driving to {location} & taking a pit stop at {resting_point}'

    def __get_vin(self):
        # A private method, only accessble within the class
        self.vin = random.randint(10000000000000, 99999999999999)
        return self.vin

    def show_vin(self):
        # calling the private method inside it's class
        print(self.__get_vin())


  


class Mercedes(Car):
    def __init__(self, name, color, gas_type, year, car_type):
        super().__init__(name, color, gas_type, year)
        self.car_type = car_type

    def get_car_type(self):
        # Method to get car type
        return f'This car is a BMW {self.car_type}'

    def make_noise(self, noise="brrum brrum"):
        # Method returns the car noise it makes
        return f'This car is about to peel out: (car noise {noise})'

    def drive(self, location, resting_point):
        # Overriding the parent method
        return f'Driving to {location} & taking a pit stop at{resting_point}'


        

class Maintenance:
    def __init__(self):
        self.wash_fee = 10
        self.ford = list()
        self.mercedes = list()

    def mechanic(self, fee):
        self.fee = fee

    def wash(self, ford, mercedes):
        # implementing composition logic for classes
        self.ford.append(ford)
        self.mercedes.append(mercedes)
        total_cars = int(len(self.ford)) + int(len(self.mercedes))
        earnings = total_cars * self.wash_fee
        return earnings





maint_earning = Maintenance()
her_car = Ford('fusion', 'blue', 'gasoline', 2010, 'sedan')
his_car = Mercedes('Benz', 'white', 'gasoline', 2011, 'Suv')
print(maint_earning.wash(her_car, his_car))


# her_car.__get_vin()
her_car.show_vin()   

# Avalon = Car('red', 'gasoline', 2009)
# print(Avalon)


mycar = Ford('Escape', 'Black', 'Diesel', 2008, 'Suv')
# mycar._get_type()
print(mycar.drive('Miami', 'Dallas'))
print(mycar.get_car_type())

