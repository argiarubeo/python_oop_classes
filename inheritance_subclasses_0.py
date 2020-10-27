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

# subclass Developer inherits methods and attributes from the parent class Employee
# we can add functionality without altering the parent class
class Developer(Employee):
    raise_amt = 1.10

    # in order to add an attribute (prog_lang) I need to define the __init__ method
    # pass the additional argument
    def __init__(self, first, last, pay, prog_lang):
        # there is no need to copy and paste the same method
        # we can just inherit it using 'super().__init__('arguments of parent class')'
        super().__init__(first, last, pay)

        # we could also call the parent class to obtain the same result
        ## Employee.__init__(self, first, last, pay)
        # but using super() is necessary when using multiple inheritance


        self.prog_lang = prog_lang

# by using the help function you can resolve the method order
## print(help(Developer))

dev_1 = Developer('Argia', 'Rubeo', 35000, 'Python')
dev_2 = Developer('Corey', 'Schafer', 50000, 'Java')

print(dev_1.email)
print(dev_2.email)
print(dev_1.prog_lang)
print(dev_2.prog_lang)
