
# how to use the INIT method
# data and functions associated to a class are called attributes and methods
# each method takes as 1st argument the istance of the class

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
        # here I want to use the class Employee instead of self
        # because in this case there is no case I can think of in
        # which I want a different number of employees from the istance

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # you cannot access a variable like this below,
        # you need to access trhough the class or an istance of the class
        #self.pay = int(self.pay * raise_amount)
        # this would give the following error:
        # NameError: name 'raise_amount' is not defined

        # by using Employee I change the class
        # self.pay = int(self.pay * Employee.raise_amount)

        # by using self I change the istance of the class
        # self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Argia', 'Rubeo', 35000)

#emp_2.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)
print(emp_2.__dict__)
## A namespace in computer science (sometimes also called a name scope),
## is an abstract container or environment created to hold a logical grouping
## of unique identifiers or symbols (i.e. names). An identifier defined in a
## namespace is associated only with that namespace.

print(Employee.num_of_emps)
