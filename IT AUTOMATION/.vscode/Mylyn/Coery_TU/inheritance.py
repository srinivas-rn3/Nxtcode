#https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4&ab_channel=CoreySchafer
# Inheritance - Creating Subclasses
class Employee:
    raise_amt = 1.05
    def __init__(self,first,last,pay):
        self.first,self.last,self.pay = first,last,pay
        self.email = first+ '.' +last+'@xxx.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.20
    '''
    The Python super() function returns objects represented in the parent’s class and is very useful
    in multiple and multilevel inheritances to find which class the child class is extending first.

    '''
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
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

dev1 = Developer('Srini','RN',65000,'Python');dev2 = Developer('Nezuko','Sue',75000,'Go Lang')

#print(dev1.email);print(dev1.prog_lang)
#print(dev2.email);print(dev2.prog_lang)
#print(help(Developer))
#print(dev1.pay)
#dev1.apply_raise()
#print(dev1.pay)
mgnr1 = Manager('Susy','Jane',90000,[dev1])
print(mgnr1.email)
mgnr1.add_emp(dev1)
mgnr1.add_emp(dev2)
mgnr1.print_emp()
print("After removing",end='\n')
mgnr1.remove_emp(dev1)
mgnr1.print_emp()

'''
Python isinstance() function returns True if the object is specified types, and it will not match then return False

Parameters : 

obj : The object that need to be checked as a part of class or not.
class : class/type/tuple of class or type, against which object is needed to be checked.

Returns : True, if object belongs to the given class/type if single class 
is passed or any of the class/type if tuple of class/type is passed, else returns False. Raises
'''
print(isinstance(mgnr1,Developer))
'''
Python issubclass() is built-in function used to check if a class is a subclass of another class or not.
This function returns True if the given class is the subclass of given class else it returns False.
Syntax: issubclass( object, classinfo ) 

Parameters: 

Object: class to be checked
classinfo: class, types or a tuple of classes and types 
Return Type: True if object is subclass of a class, or any element of the tuple, otherwise False.
'''
print(issubclass(Developer,Employee))