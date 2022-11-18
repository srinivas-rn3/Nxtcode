#Lists, Tuples, and Sets
#https://www.youtube.com/watch?v=W8KRzm-HUcc

#Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?
''''
nums = [1,3,4,5]
#i_nums = nums.__iter__()
i_nums = iter(nums)
#print(i_nums)
#print(dir(i_nums))
#print(dir(nums))
while True:
    try:
       item = next(i_nums)
       print(item)
    except StopIteration:
        break
    
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
'''
'''
class MyRange:
    def __init__(self,first,end):
        self.value = first
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value  >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,5)
#for i in nums:
#    print(i)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
'''
'''
def My_range(start,end):
    current = start 
    while current < end:
        yield current
        current += 1
mynums = My_range(1,10)
#print(next(mynum))
#print(next(mynum))
#print(next(mynum))
for i in mynums:
    print(i)
        
'''
'''
#https://www.youtube.com/watch?v=C3Z9lJXI6Qw&t=0s
#Python Coding Problem: Creating Your Own Iterators
class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
        self.index = 0
        self.word = self.sentence.split()
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        index = self.index 
        self.index += 1
        return self.word[index]
my_sentences = Sentence('This is a test')
for word in my_sentences:
    print(word)
'''
#using generator
'''
def setn(sentences):
    for word in sentences.split():
        yield word

my_sentences = setn('This is a test')

print(next(my_sentences))
print(next(my_sentences))
print(next(my_sentences))
print(next(my_sentences))
'''
#Python Tutorial: Sorting Lists, Tuples, and Objects
#https://www.youtube.com/watch?v=D3JvDWO-BY4
'''
li = [8,6,0,1,2,66,69,-100,99]
s_li = sorted(li)
print("Sorted variable is :\t",s_li)
#li.sort() #cannot assign to value it gives result 'None'
print("Orginal List is :\t",li)
s_li = sorted(li,reverse=True)
print("reverse List is:\t",s_li)
'''
#tuple 
'''
tuple = (8,6,0,1,2,66,69,-100,99)
s_tuple = sorted(tuple)
print("Tuple:\t",s_tuple)
'''
#dict
'''
dict = {'name':'Srini','job':'Tech Consultant','age':30,'code':'Python'}
s_di = sorted(dict)
print("sorted dict:\t",s_di)
'''
'''
li = [-4,-9,-1,7,1,3]
s_li = sorted(li)
print("sorted list:\t",s_li)
s_li = sorted(li,key=abs)#absolute value of a number
print("absolute value of a number:\t",s_li)
'''
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('Srini',30,80000)
e2 = Employee('Muge',26,55000)
e3 = Employee('Hirbo',32,78800)
emp_list = [e1,e2,e3]
'''
def e_sort_name(emp):
    return emp.name
def e_sort_age(emp):
    return emp.age
def e_sort_salary(emp):
    return emp.salary

S_employee = sorted(emp_list,key=e_sort_name)
print("sorted by name:\t",S_employee)
S_employee = sorted(emp_list,key=e_sort_age)
print("Sorted by age:\t",S_employee)
S_employee = sorted(emp_list,key=e_sort_salary,reverse=True)
print("Sorted by Salary:\t",S_employee)
'''
#above function using lambda
'''
S_employee = sorted(emp_list,key=lambda e: e.name)
print("sorted by name:\t",S_employee)
S_employee = sorted(emp_list,key=lambda e: e.age)
print("Sorted by age:\t",S_employee)
S_employee = sorted(emp_list,key=lambda e: e.salary)
print("Sorted by Salary:\t",S_employee)
'''
#another way of sort
from operator import attrgetter
S_employee = sorted(emp_list,key=attrgetter('name'))
print("sorted by name:\t",S_employee)
S_employee = sorted(emp_list,key=attrgetter('age'))
print("Sorted by age:\t",S_employee)
S_employee = sorted(emp_list,key=attrgetter('salary'))
print("Sorted by Salary:\t",S_employee)