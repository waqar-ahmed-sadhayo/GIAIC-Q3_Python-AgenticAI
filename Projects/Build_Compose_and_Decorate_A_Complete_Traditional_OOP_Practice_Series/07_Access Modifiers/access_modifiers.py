class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable


# Create object of Employee
emp = Employee("Waqar Ahmed", 150000, "123-45-6789")

# Access public variable
print(f"Public (name): {emp.name}")

# Access protected variable
print(f"Protected (_salary): {emp._salary}")  # Works, but not recommended outside the class

# Access private variable
try:
    print(f"Private (__ssn): {emp.__ssn}")  # Raises AttributeError
except AttributeError:
    print("Private (__ssn): Cannot access directly (AttributeError)")

# Access private variable via name mangling
print("Private (__ssn) via name mangling:", emp._Employee__ssn)