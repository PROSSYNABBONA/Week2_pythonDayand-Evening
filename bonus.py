# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary
        
#     def cal_bonus(self):
#         return self.salary * 0.15
    
#     def display_details(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Bonus:", self.cal_bonus())

# # Creating objects
# emp1 = Employee("Prossy Nabbona", 150000)
# emp2 = Employee("Morren", 230000)

# emp1.display_details()
# emp2.display_details()

#2
class Temperature:
    def __init__(self, _celsius):
        self.celsius = _celsius
    
    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit
    
# Creating a Temperature object
temp = Temperature(37)

# Converting Celsius to Fahrenheit
fahrenheit_temp = temp.to_fahrenheit()

print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", fahrenheit_temp)

#Bank Account
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # encapsulates the account number attribute
#         self.balance = balance  # encapsulates the balance attribute

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.balance


# # Create BankAccount object
# my_account = BankAccount("1245664766", 1000)

# # Accessing the BankAccount object
# print(my_account.account_number)
# print(my_account.balance)

# my_account.deposit(500)
# print(my_account.balance)

# my_account.withdraw(100)
# print(my_account.balance)


