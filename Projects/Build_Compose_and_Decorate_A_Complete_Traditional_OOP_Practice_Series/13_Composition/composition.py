class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def start(self):
        return f"Engine with {self.horse_power} HP is starting..."

class Car:
    def __init__(self, brand, horse_power):
        self.brand = brand
        self.engine = Engine(horse_power)    # Composition: Engine is created inside Car

    def strat_car(self):
        return f"{self.brand} car: {self.engine.start()}"


# Now we don't create Engine separately
my_car = Car("Toyota", 150)   # Create object for Car Class

# Access the Engine's method through the Car class
print(my_car.strat_car())

