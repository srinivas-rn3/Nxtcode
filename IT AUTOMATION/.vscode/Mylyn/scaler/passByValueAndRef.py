#https://pythonguides.com/python-pass-by-reference-or-value/
'''

def func(int):
    int +=100
    print("inside the func call",int)

int =100
print("Before the func",int)
func(int)
print("after the func",int)
'''
'''
#Python pass by reference example
student = {'Jim': 12, 'Anna':14,'Preet':18}
def test(student):
    new = {'Sam':20,'Steve':19}
    student.update(new)
    print("inside the fucntion",student)
    return
test(student)
print("Outside the functions",student)
'''
'''
#Python pass by value example
student = {'Jim': 12, 'Anna':14,'Preet':18}
def test(student):
    student={"Steve":23,"Kyle":21}
    student.update(student)
    print("inside the fucntion",student)
    return 
test(student)
print("Outside the fucntion",student)
'''
'''
#Pass by reference vs value in python
def marks_list(list):
    list.append([11,12,12,3,14,15])
    print("Value inside the function", list)
    return 
list = [10,19]
marks_list(list)
print("Vlaue outsode the function:",list)
'''
'''
#Python function arguments pass by reference or value

teacher = {'Peter':110,'John':102,'Suzan':103}
def test(teacher):
    new = {'Kat':123,'Bal':190}
    teacher.update(new)
    print("Inside the function", teacher)
    return 
test(teacher)
print("Outside the functino",teacher)
'''
'''
#Python pass string by value
my_string = "Alpha"
def test(my_string):
    my_string = "Beta"
    print("Inside the func", my_string)
test(my_string)
print("Outside the fuunc",my_string)
'''
my_str = "Alpha"
def test(my_str):
    my_str = my_str + "Beta"
    print('Inside the func',my_str)
    return 
test(my_str)
print("Outside the func",my_str)
