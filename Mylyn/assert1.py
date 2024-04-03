#https://www.geeksforgeeks.org/python-assert-keyword/
'''
a = 4
b = 0
print("The value of a /b is =")
assert b != 0,"Zero division error!!!"
print(a/b)
'''
'''
def cal_rectangle_area(length,width):
    assert length > 0  and width > 0, "Length and width " + \
        "Must be +ve"
    area = length * width 
    print("Area of rectangle:",area)
    
a1 = cal_rectangle_area(5,6)
a1
a2 = cal_rectangle_area(8,0)
'''
'''
#Assert with boolean Condition
x = 30 ; y = 20
assert x > y 
print("x = ",x);print("y = ",y)
'''
'''
#Assert Type of Variable in Python
a = "hello"
b = 42
assert type(a) == str 
assert type(b) == int

print("a =", a)
print("b = ",b)
'''
'''
#Asserting dictionary values
my_dict = {"apple":1,"banana":2,"cherry":3}
assert my_dict["apple"] == 1
assert my_dict["banana"] == 2
assert my_dict["cherry"] == 3

print(my_dict)
'''
'''
#Practical Application
batch = [40,26,39,30,25,21]
cut = 26 
for i in batch:
    assert i >= 26,"Batch is rejected"
    print(str(i) + "is O.K")
'''