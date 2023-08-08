'''
class Alphabet:
    def __init__(self,value):
        self.__value = value 
    def getValue(self):
        print("Getting the value")
        return self.__value
    def setValue(self,value):
        print('Setting the value to ' +value)
        self.__value = value
    def delValue(self):
        print("Deleting the value")
        del self.__value
    value = property(getValue,setValue,delValue,)

x = Alphabet('GeekforGeek')
print(x.value)
x.value = 'GFG'

del x.value
'''

##################
#example -2 ######
##################
'''
class Alphabet:
    def __init__(self,value):
        self.__value = value

    @property
    def value(self):
        print("Getting value")
        return self.__value
    
    @value.setter 
    def value(self,value):
        print("Setting the value to "+value)
        self.__value  = value 
    @value.deleter 
    def value(self):
        print("Deleting the value")
        del self.__value
x = Alphabet('Peter')
print(x.value)
x.value = 'Mia'
x.value = 'Hmm'
del x.value
'''
###############
## Example -3##
###############
'''
class Employee:
    count = 0 
    
    def increase(self):
        Employee.count += 1
        
a1 = Employee()
a1.increase

print(a1.count)

a2 = Employee()
a2.increase()
print(a2.count)
print(Employee.count)

a3 = Employee()
a3.increase()
print(a3.count)
print(Employee.count)
'''
################
# Example -4 ##
###############
class Stars:
    def __init__(self,value):
        self.__value = value 
        
    def getter(self):
        print("Getting the value")
        return self.__value 
    def setter(self,value):
        print("The Settng the value to " +value)
        self.__value = value
    def deleter(self):
        print("Deleting the value")
        del self.__value
    
    value = property(getter,setter,deleter,)

x = Stars('Proxima Centauri')
print(x.value)
x.value = "Alpha Centauri"
del x.value
