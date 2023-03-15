from car import Car
# 可以导入父类

class fuel_tank():
    """燃油车类"""
    def __init__(self, capacity):
        self.capacity = capacity

    def describe(self):
        print(f"fuel tank capacity is {self.capacity} L")


class FuelCar(Car):
    def __init__(self, maker, model, year, mileage = 0, fuel_tank_capacity = 100):
        super.__init__(maker, model, year, mileage)
        self.fuel_tank = fuel_tank(fuel_tank_capacity)

    def describe_fuel_tank(self):
        self.fuel_tank.describe()
