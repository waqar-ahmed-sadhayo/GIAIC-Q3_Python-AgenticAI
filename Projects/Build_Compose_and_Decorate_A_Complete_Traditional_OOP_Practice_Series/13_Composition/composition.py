class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def start(self):
        return f"Engine with {self.horse_power} HP is starting..."

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine   # Composition: Engine is part of Car

    def strat_car(self):
        return f"{self.brand} car: {self.engine.start()}"

# Create an Engine object
my_engine = Engine(150)

# Pass the Engine object to the Car
my_car = Car("Toyota", my_engine)

# Access the Engine's method through the Car class
print(my_car.strat_car())
