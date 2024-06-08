class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first+'.'+last+"@company.com"
        # self.num_of_employees += 1
        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary*self.raise_amount)


print(Employee.num_of_employees)
emp1 = Employee("Ali", "Karimi", 5000)
print(emp1.num_of_employees)
emp2 = Employee("Karim", "Bagheri", 6000)
print(emp2.num_of_employees)
print(Employee.num_of_employees)
