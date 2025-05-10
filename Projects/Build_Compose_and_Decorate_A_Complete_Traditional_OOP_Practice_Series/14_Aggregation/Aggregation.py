# Employee class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee   # Aggregation: using an existing Employee object

    def display(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()


# Create an Employee object independently
emp1 = Employee(1, "Waqar")

# Pass the existing Employee object to Department (Aggregation)
dept1 = Department("Development", emp1)

# Display Department info
dept1.display()

# Show that Employee still exists independently
print("\nEmployee still accessible outside the department:")
emp1.display()