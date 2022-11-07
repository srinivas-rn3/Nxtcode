#https://www.youtube.com/watch?v=RSl87lqOXDE
#Inheritance - Creating Subclasses
'''
class Employee:
    raise_amt = 1.04
    def __init__(self, first , last ,pay):
        self.first = first 
        self.last = last 
        self.email = first+'.'+last+'@next-think.com'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_riase(self):
        self.pay = int(self.pay  *self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees  is  None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())
    
dev1 = Developer('Srini','RN',89000,'Python')
dev2 = Developer('Marnie','Sapparo',78888,'Julia')
#print(dev1.prog_lang)
#print(dev2.prog_lang)
mgr_1 = Manager('Bella','Hadid',100000,[dev1])

print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev2)
mgr_1.print_emp()
mgr_1.remove_emp(dev2)
print('after removal',end='\n')
mgr_1.print_emp()
#print(dev1.fullname())
#print(help(Developer))
#print(dev1.pay)
#dev1.apply_riase()
#print(dev1.pay)

print(isinstance(mgr_1,Employee))
print(issubclass(Developer,Manager))
'''
#Python OOP Tutorial 5: Special (Magic/Dunder) Methods
#https://www.youtube.com/watch?v=3ohzBxoFHAY

class Employee:
    raise_amt = 1.04
    def __init__(self, first , last ,pay):
        self.first = first 
        self.last = last 
        self.email = first+'.'+last+'@next-think.com'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_riase(self):
        self.pay = int(self.pay  *self.raise_amt)
    def __repr__(self) -> str:
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

dev1 = Employee('Srini','RN',89000)
dev2 = Employee('Marnie','Sapparo',78888)

#print(dev1)

##rint(repr(dev1))
print(str(dev1))
#print(dev1.__repr__())
#print(dev1.__str__())

#print(int.__add__(1,3))
#print(int.__str__('a'+'c'))
#print(dev1 + dev2)
#print(len(dev1))
#print('test'.__len__())