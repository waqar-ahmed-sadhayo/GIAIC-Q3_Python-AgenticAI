class Logger:
    def __init__(self, name):  # Constructor
        self.name = name
        print(f"Looger object created for {name}.")

    def __del__(self):  # Destructor
        print(f"Logger object destroyed for {self.name}.")

# Creating the object
obj1 = Logger("Waqar")

# Force the destructor to run immediately
del obj1  # This will trigger the __del__ method