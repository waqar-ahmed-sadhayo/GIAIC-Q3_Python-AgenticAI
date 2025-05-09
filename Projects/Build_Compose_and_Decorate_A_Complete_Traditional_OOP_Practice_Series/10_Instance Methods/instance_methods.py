class Dog:
    def __init__(self, name, breed):
        self.name = name     # instance variable
        self.breed = breed   # instance variable

    def bark(self):   # instance Method
        print(f"{self.name}: {self.breed}")

# create object dog1
dog1 = Dog("Max", "German Shepherd")
dog1.bark()

# create object dog2
dog2 = Dog("Buddy", "Beagle")
dog2.bark()