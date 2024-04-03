class Employee:
    def __init__(self, first,last):
        self.first = first 
        self.last = last 
        #self.email = first + '.'+ last +'@next.com'
    @property
    def email(self):
        return '{}.{}@next.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name!!!")
        self.first = None
        self.last = None

emp1 = Employee("Marnie","Sapraroo")
emp1.first = "Nanoko"
emp1.fullname = "Goku Z"
print(emp1.fullname)
print(emp1.email)
del emp1.fullname