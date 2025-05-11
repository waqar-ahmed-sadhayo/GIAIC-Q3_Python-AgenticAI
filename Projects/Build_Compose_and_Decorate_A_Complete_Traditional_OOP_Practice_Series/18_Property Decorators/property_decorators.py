class Product:
    # Constructor to initialize the product with a price
    def __init__(self, price):
        self._price = price  # Use a private attribute to store the price

    # Getter method to access the price
    @property
    def price(self):
        print("Getting price...")  # Message indicating getter is called
        return self._price         # Return the stored price

    # Setter method to update the price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")  # Validate input
        print("Setting price...")   # Message indicating setter is called
        self._price = value         # Update the private _price attribute

    # Deleter method to delete the price
    @price.deleter
    def price(self):
        print("Deleting price...")  # Message indicating deleter is called
        del self._price             # Delete the _price attribute

# Example usage
p = Product(100)           # Create a Product object with initial price 100
print(p.price)             # Calls the getter method

p.price = 150              # Calls the setter method to update the price
print(p.price)             # Calls the getter method to confirm update

del p.price                # Calls the deleter method to delete the price
