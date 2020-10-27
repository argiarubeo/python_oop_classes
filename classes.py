
# how to use the INIT method
# data and functions associated to a class are called attributes and methods
# each method takes as 1st argument the istance of the class

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Argia', 'Rubeo', 35000)

# print(emp_1)
# print(emp_2)
# print(emp_2.email)
# print(emp_2.fullname())

# applying to an istance the class method
print(emp_2.fullname())
# calling the method of the class and passing an istance
print(Employee.fullname(emp_2))
