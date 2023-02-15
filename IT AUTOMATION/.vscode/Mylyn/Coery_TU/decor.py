#https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
#Property Decorators - Getters, Setters, and Deleter
#%%

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
    '''
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first 
        self.last = last
    '''
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
#in above ex. Whne we changed emp1.first only first name is changed but not the email. because email is not method
#%%
#Decorators
#https://www.youtube.com/watch?v=FsAPt_9Bf3U
