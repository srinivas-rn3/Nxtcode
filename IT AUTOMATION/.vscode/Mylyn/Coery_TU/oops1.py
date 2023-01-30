#https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer
#OOP
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
#https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2&ab_channel=CoreySchafer