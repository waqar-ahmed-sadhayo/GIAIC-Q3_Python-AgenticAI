class Car:

    def __init__(self, brand, name):
        self.brand = brand  # public instance variable
        self.name = name    # public instance variable

    def start(self):
        print(f"The \"{self.name}\" car is the Product of \"{self.brand}\"")

# Instantiate the class
car1 = Car("Toyota", "Vigo")

# Access the public variable
print(f"Car Brand: {car1.brand}")

# Call the public method
car1.start()