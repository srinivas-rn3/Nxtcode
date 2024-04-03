#https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5
#Python OOP Tutorial 5: Special (Magic/Dunder) Methods
class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay  
        self.email = first.lower()+'.'+last.lower()+'@xxx.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    def __str__(self):
        return'{} - {}'.format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Marnie','Chan',75000)
emp2 = Employee('Nuzuko','Superno',80000)
#print(emp1)
#print(emp1.fullname());print(emp1.email);print(emp1.apply_raise())
#print(emp2.fullname());print(emp2.email);print(emp2.apply_raise())

#print(repr(emp1))
#print(str(emp1))
#print(emp1.__repr__())
#print(emp1.__str__())
#print(int.__add__(1,2))
#print(str.__add__('a','b'))
#print(emp1 + emp2) #this is beacuse of dunder function __add__
#print(len('test'))
#print('test'.__len__())
print(len(emp1))