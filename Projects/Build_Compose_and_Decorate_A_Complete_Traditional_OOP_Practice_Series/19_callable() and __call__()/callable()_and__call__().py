# Define the class
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Create an instance of the class
double = Multiplier(2)
triple = Multiplier(3)

# Test if the objects are callable
print("Is 'double' callable?", callable(double))  # True
print("Is 'triple' callable?", callable(triple))  # True

# Use the objects like functions
print("double(5) =", double(5))  # Output: 10
print("triple(4) =", triple(4))  # Output: 12
