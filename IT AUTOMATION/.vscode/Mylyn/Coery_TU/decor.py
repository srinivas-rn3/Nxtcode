#https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
#Property Decorators - Getters, Setters, and Deleter
#%%
'''
class Employee:
    def __init__(self,first,last):
        self.first = first 
        self.last = last 
        #self.email = first.lower() +'.' +last.lower()+'@xxx.com'
    @property
    def email(self):
        return "{}.{}.@xxx.com".format(self.first.lower(),self.last.lower())
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first 
        self.last = last
    
    
    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None 
        self.last = None
emp1 = Employee('Nezuko','Chan')
#emp1.first = 'Narutho'
emp1.fullname = 'Goku Uran'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
'''
#in above ex. Whne we changed emp1.first only first name is changed but not the email. because email is not method

#Decorators:Dynamically Alter The Functionality Of Your Functions
#https://www.youtube.com/watch?v=FsAPt_9Bf3U

#Closures
#https://www.youtube.com/watch?v=swU3c34d2NQ

'''
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

It is a record that stores a function together with an environment: a mapping associating each free variable of 
the function (variables that are used locally but defined in an enclosing scope) with the value or reference 
to which the name was bound when the closure was created.

A closure—unlike a plain function—allows the function to access those captured variables through the 
closure’s copies of their values or references, even when the function is invoked outside their scope
'''
'''
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func
my_func = outer_func()
#print(my_func.__name__)
my_func()
my_func()
'''
'''
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')
hi_func()
hello_func()
'''

'''
import logging as log
from datetime import datetime
cur_date_time = datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
log.basicConfig(filename='test1902.log',level=log.INFO)
#log.basicConfig(filename='mylog.log',level=log.INFO)
def loger(func):
    def loger_func(*args):
        log.info(
            'Running "{}" with arguments{}'.format(func.__name__,args)
        )
        print(func(*args))
    # Necessary for closure to
    # work (returning WITHOUT parenthesis)
    return loger_func
def add(x,y):
    return x + y
def sub(x,y):
    return x - y

add_logger = loger(add)
sub_logger = loger(sub)

add_logger(2,3)
sub_logger(7,5)
# Python program to illustrate
# closures
'''
#%%
#Decorators:Dynamically Alter The Functionality Of Your Functions\
'''
def outer_func(msg):
    #message = msg
    def inner_func():
        print(msg)
    return inner_func
hi_func = outer_func('Hi')
bye_func = outer_func('Bye')
hi_func()
bye_func()
'''
'''
def decorator_func(original_func):
    def wrapper_fucn():
        print('wrapper Execute this before {}'.format(original_func.__name__))
        return original_func()
    return wrapper_fucn
@decorator_func
def display():
    print('display function ran!!!')

#decor_display = decorator_func(display)
#decor_display()
display()
'''
#https://www.youtube.com/watch?v=FsAPt_9Bf3U
#10.18
#%%

def decorator_(orginal_func):
    def wrapper_func(*args, **kwargs):
         print('wrapper executed this before {}'.format(orginal_func.__name__))
         return orginal_func(*args,**kwargs)
    return wrapper_func

@decorator_
def display():
    print('Display function ran')
@decorator_
def display_info(name, age):
    print("display_info ran with arguments ({},{})".format(name , age))

display_info('Mia','32')
display()


# %%
#13.21