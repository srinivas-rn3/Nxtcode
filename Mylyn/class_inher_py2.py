'''
class emp:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 =  emp('Srini','RN',50000)
emp_2 = emp('Marnie','Satiro',70000)

#print(emp_1)
#print(emp_2)
#print('{} {}'.format(emp_2.first,emp_1.last))
print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())
#https://www.youtube.com/watch?v=BJ-VvGyQxho
'''
'''
# Class Variables
class Employee:
    raise_amnt = 1.04
    no_of_emp = 0
    def __init__(self, first ,last, pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first+'.'+last+'@company.com'
        Employee.no_of_emp += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)
print(Employee.no_of_emp)
emp1 = Employee('Srini',"RN",60000)
emp2 = Employee('Marnie','Sapparo',70000)
print(Employee.no_of_emp)

print(emp1.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp2.fullname())
print(emp2.pay)
emp2.apply_raise()
print("after raise",end='\n')
print(emp1.pay)
print(emp2.pay)

emp1.raise_amnt = 1.7
print(emp1.raise_amnt)
print(emp1.__dict__)
print(emp1.raise_amnt)
print(emp2.raise_amnt)
print(Employee.raise_amnt)
'''
#classmethods and staticmethods
#https://www.youtube.com/watch?v=rq8cL2XMM5M
'''
def outer_func(msg):
    message = msg

    def inner_func():

       print(message)
    return inner_func
my_fucn1 = outer_func('Hi')
my_fucn2 = outer_func('Fuck You')
my_fucn1(); my_fucn2()
'''
'''
def decorator_functions(message):
    def wrapper_function():
        print(message)
    return wrapper_function
'''
'''
def decorator_function(orginal_function):
    def wrapper_function(*args,**kwargs):
        print("Wrapper fucntion is executed first {}". format(orginal_function.__name__))
        return orginal_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran!!')

@decorator_function
def display_info(name, age):
    print('Display info with two arguments ({},{})'.format(name, age))

#def1 = decorator_function(display)

display_info('Sri', 30)
display()
'''
'''
class decorator_class(object):
    def __init__(self,orginal_function):
        self.orginal_function = orginal_function
    def __call__(self, *args,**kwargs):
         print("class fucntion is executed first {}". format(self.orginal_function.__name__))
         return self.orginal_function(*args,**kwargs)
@decorator_class
def display():
    print('display function ran!!')

@decorator_class
def display_info(name, age):
    print('Display info with two arguments ({},{})'.format(name, age))

display()
display_info('Sri', 30)
'''
'''
import time
from functools import wraps
def my_logger(orgi_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orgi_func.__name__),level=logging.INFO)
    @wraps(orgi_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {} , and kwargs:{}'.format(args,kwargs)
        )
        return orgi_func(*args, **kwargs)
    return wrapper

def my_timer(orgi_func):
    import time
    @wraps(orgi_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result =  orgi_func(*args , **kwargs) 
        t2 = time.time() - t1
        print('{} ran in: {} sec'. format(orgi_func.__name__, t2))
        return result 
    return wrapper
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(5)
    print('Display info with two arguments ({}, {})'.format(name, age))
dis = my_timer(display_info)
print(dis.__name__)
display_info("kylie", 30)
'''

class Employee:
    no_of_emps = 0
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.pay = pay 
        self.last = last 
        self.email = first + '.' + last + '@comp.com'

        Employee.no_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls,emp_):
        first,last,pay = emp_.split('-')
        return cls(first, last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

'''
emp1 = Employee('Srini', 'RN',100000)
emp2 = Employee('Marnie', 'saperro', 900000)

Employee.set_raise_amount(1.08)

print(emp2.apply_raise())
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
'''
'''
emp_1 = 'John-Dee-70000'
emp_2 = 'Srini-RN-70000'
emp_3 =  'Marnie-Sapparo-80000'

#first,last,pay = emp_1.split('-')
#new_emp_1 = Employee(first,last,pay)
new_emp_1 = Employee.from_string(emp_1)
print(new_emp_1.email)
print(new_emp_1.pay)
'''
import datetime
my_date = datetime.date(2022,10,30)

print(Employee.is_workday(my_date))