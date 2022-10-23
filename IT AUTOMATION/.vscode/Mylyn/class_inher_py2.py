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
