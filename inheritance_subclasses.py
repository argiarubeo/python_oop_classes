class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # there is no need to copy and paste the same method
        # we can just inherit it using 'super().__init__('arguments of parent class')'
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    # we pass as last argument a list of employees that the manager supervises
    # but we do not want to pass a mutable object so we set it to 'None'
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Argia', 'Rubeo', 35000, 'Python')
dev_2 = Developer('Corey', 'Schafer', 50000, 'Java')

print(dev_1.email)
print(dev_2.email)
print(dev_1.prog_lang)
print(dev_2.prog_lang)

mgr_1 = Manager('Test', 'Man', 90000, [dev_1])
mgr_1.add_emp(dev_2)
print(mgr_1.email)
mgr_1.print_emps()
print('--------\n')
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()
print('--------\n')
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
