# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject

# Create object
teacher1 = Teacher("Mr. Waqar Ahmed", "Programming")
print(f"Name: {teacher1.name}")
print(f"Subject: {teacher1.subject}")