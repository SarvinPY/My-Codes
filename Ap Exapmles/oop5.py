class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first+'.'+last+"@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary*Employee.raise_amount)


emp1 = Employee("Ali", "Karimi", 5000)
emp2 = Employee("Karim", "Bagheri", 6000)

print(emp1.salary)
print(emp2.salary)
print("----------")
# emp1.apply_raise()
# print(emp1.salary)
# print(emp2.salary)

emp1.raise_amount = 1.05
emp2.raise_amount = 1.06
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
emp1.apply_raise()
print(emp1.salary)

