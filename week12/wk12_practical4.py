# Employee and Manager using inheritance

class Employee:
    def __init__(self, name, salary):
        # Save the employee's name and salary
        self.name = name
        self.salary = salary

    def __str__(self):
        # Return a readable description of the employee
        return f'{self.name} earns ${self.salary}'


class Manager(Employee):  # Manager inherits from Employee

    def __init__(self, name, salary, department):
        # Call the Employee constructor
        super().__init__(name, salary)

        # Save the manager's department
        self.department = department

    def __str__(self):
        # Return a readable description of the manager
        return f"{self.name} earns ${self.salary} and manages {self.department}"


# Create an Employee object
e = Employee("Peter", 3000)

# Create a Manager object
m = Manager("Mary", 5000, "IT")

# Print the Employee object
print(e)  # Peter earns $3000

# Print the Manager object
print(m)  # Mary earns $5000 and manages IT


# Create a list of Employee and Manager objects
employees = [
    Employee("Peter", 3000),
    Manager("Mary", 5000, "IT"),
    Manager("John", 6000, "Finance")
]

# Go through each object in the list
for e in employees:
    # Print the current object
    print(e)

# OUTPUT:
# Peter earns $3000
# Mary earns $5000 and manages IT
# John earns $6000 and manages Finance