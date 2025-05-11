# Define the class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the decorator to the class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance and call the added method
p = Person("Waqar")
print(p.greet())
