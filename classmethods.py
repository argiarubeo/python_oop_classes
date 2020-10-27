# (regular)method -modifies an istance of the class (self)
# classmethod -modifies the class (cls)
# staticmethod -does not modify either the istance or the class,
#               it acts on the variable we want to modify

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    ## In object-oriented programming, the decorator pattern is a design pattern
    ## that allows behavior to be added to an individual object, dynamically, without
    ## affecting the behavior of other objects from the same class.
    @classmethod
    def set_raise_amt(cls, amount): # cls as class
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Argia', 'Rubeo', 35000)

emp_str_1 = 'Corey-Schafer-60000'
emp_str_2 = 'Argia-Rubeo-35000'
emp_str_3 = 'Daniele-Desanctis-50000'

#first, last, pay = emp_str_2.split('-')
# new_emp_2 = Employee(first, last, pay)
new_emp_2 = Employee.from_string(emp_str_2)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.num_of_emps)
print(new_emp_2.first)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
