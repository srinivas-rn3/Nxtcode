'''
Python has predefined functions for many mathematical, logical, relational, 
bitwise etc operations under the module “operator”. Some of the basic functions 
are covered in this article.

1. add(a, b) :- This functions returns addition of the given arguments.
Operation – a + b.

2. sub(a, b) :- This functions returns difference of the given arguments.
Operation – a – b.

3. mul(a, b) :- This functions returns product of the given arguments.
Operation – a * b.

'''
'''
import operator

a =10; b = 34;
print("The addition of number is :", end="")
print(operator.add(a , b))
print("The sub of numner is :", end="" )
print(operator.sub(a ,b))
print("The multiplication of number is :", end="")
print(operator.mul(a ,b))
'''
'''
4. truediv(a,b) :- This function returns division of the given arguments.
Operation – a / b.

5. floordiv(a,b) :- This function also returns division of the given arguments. But the value is floored value i.e. returns greatest small integer.
Operation – a // b.

6. pow(a,b) :- This function returns exponentiation of the given arguments.
Operation – a ** b.

7. mod(a,b) :- This function returns modulus of the given arguments.
Operation – a % b.
'''
'''
import operator

a = 19; b = 23;

print(operator.truediv(a,b))
print(operator.floordiv(a,b))
print(operator.pow(a,b))
print(operator.mod(a,b))
'''
'''
8. lt(a, b) :- This function is used to check if a is less than b or not. Returns true if a is less than b, else returns false.
Operation – a < b.

9. le(a, b) :- This function is used to check if a is less than or equal to b or not. Returns true if a is less than or equal to b, else returns false.
Operation – a <= b.

10. eq(a, b) :- This function is used to check if a is equal to b or not. Returns true if a is equal to b, else returns false.
Operation – a == b.
'''
'''
import operator

a =3; b= 30;

if(operator.lt(a ,b)):
    print("3 less than 3")
else:
    print("3 is not less than 3")
if(operator.gt(a,b)):
    print("a is GREATER")
else: 
    print("b is GREATER")
if(operator.le(a,b)):
    print(" a is less than b")
else:
    print("b is less than a")
if(operator.eq(a,b)):
    print("a is equal to b")
else:
    print("b is not equal to a")
'''
'''
1. setitem(ob, pos, val) :- This function is used to assign the value at a particular position in the container. 
Operation – ob[pos] = val

2. delitem(ob, pos) :- This function is used to delete the value at a particular position in the container. 
Operation – del ob[pos]

3. getitem(ob, pos) :- This function is used to access the value at a particular position in the container. 
Operation – ob[pos]
'''
import operator

li=[1,2,3,4,6]

print("The original list is :",end=" ")
for i1 in range(0,len(li)):
    print(li[i1], end=" ")
print("\r")

# using setitem() to assign 3 at 4th position
operator.setitem(li,3,90)

print("The Modified list is :", end=" ")
for i in range(0,len(li)):
    print(li[i],end=" ")
    
print("\r")

# printing modified list after delitem()
operator.delitem(li,3)
print("The deleted list is :", end = " ")
for i in range(len(li)):
    print(li[i], end=" ")
print("\r")
    
# using getitem() to access 4th element
print("To get the 3rd position value from list :", end=" ")
print(operator.getitem(li,3))
#https://www.geeksforgeeks.org/operator-functions-python-set-2/