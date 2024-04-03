#https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer
#OOP

'''
class Employee:
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay 
        self.email = first.lower()+'.'+last.lower()+'@xxx.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
#instance variable
emp1 = Employee('Srini','RN',7000)
emp2 = Employee('Nezko','Chan',8000)
#print(emp1)
#print(emp2)


#print(emp1.email)
#print(emp2.email)
#print(emp1.fullname())
#print(emp2.fullname())
#8:58
#print('{} {}'.format(emp1.first,emp1.last))
print(Employee.fullname(emp1))
'''
#https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2&ab_channel=CoreySchafer
# Class Variables
'''
class Employee:
    
    raise_amount = 1.04
    no_of_employee = 0
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay 
        self.email = first.lower()+'.'+last.lower()+'@xxx.com'

        Employee.no_of_employee += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)#self.raise_amount alos works
#instance variable
print(Employee.no_of_employee)
emp1 = Employee('Srini','RN',7000)
emp2 = Employee('Nezuko','Chan',8000)
'''
'''
#Employee.raise_amount = 1.05
emp1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)
#print(Employee.__dict__)
#emp1.apply_raise()
#print(emp1.pay)
print(Employee.no_of_employee)
'''
#https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3&ab_channel=CoreySchafer
#: classmethods and staticmethods
class Employee:
    raise_amount = 1.04
    no_of_employee = 0
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay 
        self.email = first.lower()+'.'+last.lower()+'@xxx.com'

        Employee.no_of_employee += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)#self.raise_amount alos works
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
       first,last,pay = emp_str.split('-')
       return cls(first,last,pay)
    @staticmethod #9:14
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

print(Employee.no_of_employee)
emp1 = Employee('Srini','RN',7000)
emp2 = Employee('Nezuko','Chan',8000)
Employee.set_raise_amount(2.50)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str_1 = 'Srini-R-80000'
emp_str_2 = 'Nezuko-Chan-86000'
emp_str_3 = 'Tanjiro-Chan-90000'

#first,last,pay = emp_str_1.split('-')
new_emp1 = Employee.from_string(emp_str_1)

    
print(new_emp1.email)
print(new_emp1.pay)

import datetime
my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))

