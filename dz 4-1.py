class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        return "Engine started with power: " + str(self.power)

class Wheels:
    def __init__(self, size):
        self.size = size

    def rotate_wheels(self):
        return "Wheels are rotating with size: " + str(self.size)

class Car(Engine, Wheels):
    def __init__(self, power, size, color):
        Engine.__init__(self, power)
        Wheels.__init__(self, size)
        self.color = color

    def car_details(self):
        return f"Car with {self.power} power, {self.size} inch wheels, and color {self.color}"

# Использование
car = Car(150, 18, "red")
print(car.start_engine())
print(car.rotate_wheels())
print(car.car_details())
