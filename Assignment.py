class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary

    def give_raise(self, increment):
        if increment > 0:
            self._salary += increment


# Create an Employee object
employee = Employee("Nabbona Prossy", 850000)

# Get the current salary
current_salary = employee.get_salary()
print("Current Salary:", current_salary)

# # Set a new salary
# new_salary = 1000000
# employee.set_salary(new_salary)
# print("New Salary:", employee.get_salary())

# Give a raise
increment = 150000
employee.give_raise(increment)
print("Updated Salary after Raise:", employee.get_salary())
