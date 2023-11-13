'''
def avg(marks):
    assert len(marks) != 0 
    return sum(marks)/len(marks)
#mark1 =[]
#print("Avg.  of mark1:",avg(mark1)) #assertionError

marks2 = [99,89,100,78,90,88]
print(f"avg. marks2:{round(avg(marks2),2)}")
'''
'''
number = -42
assert number > 0, f"Number is greater than zero expected. got:{number}" 
#AssertionError: Number is greater than zero expected. got:-42
'''
number = -0.42 
assert number > 0  and isinstance(number,int),\
    f"Number is greater than 0 expected , got {number}"