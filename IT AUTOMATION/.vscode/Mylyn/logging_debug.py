#https://www.youtube.com/watch?v=-ARI4Cz-awo
#Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting

import logging
import logging.handlers

#logging.basicConfig(filename='test_1110.log',level=logging.DEBUG,
#                     format ='%(asctime)s:%(levelname)s:%(message)s')
'''
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y

num_1 = 1000;num_2 = 2000
add_result = add(num_1,num_2)
#print('{} + {} = {}'.format(num_1,num_2,add_result))
logging.debug('Add:{} + {} = {}'.format(num_1,num_2,add_result))
#logging.warning('Add:{} + {} = {}'.format(num_1,num_2,add_result))

sub_result = sub(num_1,num_2)
#print('{} - {} = {}'.format(num_1,num_2,sub_result))
logging.debug('Sub:{} - {} = {}'.format(num_1,num_2,sub_result))
#logging.warning('Sub:{} - {} = {}'.format(num_1,num_2,sub_result))
mul_result = mul(num_1,num_2)
#print('{} * {} = {}'.format(num_1,num_2,mul_result))
logging.debug('Mul:{} * {} = {}'.format(num_1,num_2,mul_result))
#logging.warning('Mul:{} * {} = {}'.format(num_1,num_2,mul_result))

div_result = div(num_1,num_2)
#print('{} / {} = {}'.format(num_1,num_2,div_result))
logging.debug('Div:{} / {} = {}'.format(num_1,num_2,div_result))
#logging.warning('Div:{} / {} = {}'.format(num_1,num_2,div_result))
'''
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
#https://github.com/CoreyMSchafer/code_snippets/blob/master/Logging-Basics/snippets.txt
#https://docs.python.org/3/library/logging.html

logging.basicConfig(filename = 'test_1110.log',level=logging.INFO,format = '%(levelname)s:%(message)s')
class Employee:
    def __init__(self,first,last):
        self.first = first 
        self.last = last
        #print("Created Employee:{} - {}".format(self.fullname,self.email))
        logging.info("Created Employee:{} - {}".format(self.fullname,self.email))
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
emp1 = Employee ('John','Wick')
emp2 = Employee ('Marie','Saparro')

#https://www.youtube.com/watch?v=jxmzY9soFXg