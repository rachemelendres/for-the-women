# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        age_of_car = 2019 - self.year
        return age_of_car

# car_1 = Car(1994, 'Toyota', 'Camry' )
# car_2 = Car(2019, 'Ferrari', '488 Pista')

# print(car_1.year)
# print(car_1.age())
