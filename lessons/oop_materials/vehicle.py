class Vehicle:
    def __init__(self, mileage, gas_level):
        self.mileage = mileage
        self.gas_level = gas_level

    def add_gas(self, gallons):
        self.gas_level += gallons
    

class Bus(Vehicle):
    def __init__(self, mileage, gas_level, seating_capacity):
        super().__init__(mileage, gas_level)
        self.seating_capacity = seating_capacity

class Car(Vehicle):
    def __init__(self, mileage, gas_level):
        super().__init__(mileage, gas_level)

def add_gas(vehicle):
    vehicle.add_gas(5)
    print("The vehicle's gas level is " + str(vehicle.gas_level))

bus = Bus(100, 5, 50)
car = Car(200, 0)

add_gas(bus)
add_gas(car)




