'''
Python NumPy is a general-purpose array processing package which provides tools for handling 
the n-dimensional arrays. It provides various computing tools such as comprehensive mathematical 
functions, linear algebra routines. NumPy provides both the flexibility of Python and the speed 
of well-optimized compiled C code.

It’s easy to use syntax makes it highly accessible and productive for programmers from any background.

'''

import numpy as np 
'''
arr = np.array([[1,2,3],
               [2,3,50]])
print("Array is of type:",type(arr))
print("No. of dimensions:",arr.ndim)
print("Shape of array:",arr.shape)
print("Size of array:",arr.size)
print("Array stores elements of type:",arr.dtype)
'''
'''
#print(dir(np))
a = np.array([[1,2,3],[3,4,5]],dtype='float')
print("\nArray creaed using passed list:\n",a)

b = np.array((1,2,3,4))
print("\nArray created using tuple:\n", b)

c = np.zeros((3,4))
print("\nArray initialized with all zeros:\n",c)

d = np.full((3,3),6,dtype ='complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)

e = np.random.random((2,3))
print("\nA random array:\n", e)

f = np.arange(0,30,5)
print("\nA Sequential array with step of 5 :\n",f)

g = np.linspace(0,5,10)
print ("\nA sequential array with 10 values between"
                                        "0 and 5:\n", g)
arr = np.array([[2,4,6,8],[10,12,14,16],[20,22,24,26]])
newarr = arr.reshape(2,2,3)

print("\nOriginal array:\n",arr)
print("\nNew array is:\n",newarr)


arr = np.array([[1,2,3],[4,5,6]])
flat = arr.flatten()
print("\nOriginal array:\n",arr)
print("Flatten array:\n",flat)
'''
'''
arr = np.array([[1,2,3,4],
              [3,-2,3,4],
              [-5,-6,6,8],
              [90,5,-8,4]])
# Slicing array
temp = arr[:2,::3]
print(temp)
print("\n")
## Integer array indexing example
temp =arr[[0,1],[1,3]]
print(temp)
print("\n")
# boolean array indexing example
cond = arr > 0
temp = arr[cond]
print(temp)
#https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/
'''
'''
a = np.array([0,np.pi/2,np.pi])
print("Sine values of array elements:",np.sin(a))

a = np.array([0,1,2,3])
print("Exponent of array elements:",np.exp(a))

a1=(np.array([2,3,4]))
a = np.sqrt(a1)
print("Square root of elements:",a)
'''
'''
a = np.array([1,2,5,3])
print("\nOrginal array is:",a)
print("\nAdding 1 to every element:",a+1)
print("\nSubtraction 3 from each number:", a-3)
print("\nMultiplication each elements by 10:", a*10)
print("\nSquaring each elements:", a**2)
a *= 2
print("\nDouble each elements of orginal array:",a)
a2 = np.array([[1,2,3],[3,4,5],[6,7,0]])
print("\nOriginal array is:",a2)
print("\nTranspose of array:",a2.T)
'''
'''
## unary operators in numpy
arr = np.array([[12,14,16],
               [2,4,6],
               [8,10,18]])
print("\nLargest element is:",arr.max())
print("\nRow-wise maximum elements:",arr.max(axis=1))
print("\nColumn-wise minimum elements:",arr.min(axis=1))
print("\nSum of all array elements:",arr.sum())
print("\nCumlative sum  along each row:",arr.cumsum(axis = 1))
'''
'''
# Python program to demonstrate
# binary operators in Numpy
a = np.array([[1,2],[3,4]])

b = np.array([[4,3],[5,6]])

print("\nArray sum is:\n", a+b)
print("Array Multiplication is:\n", a*b) ## multiply arrays (elementwise multiplication)
print("Matrix multiplication is:\n",a.dot(b))
'''
#https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/
a = np.array([[1,4,2],
              [3,4,6],
              [0,-1,-5]])

#Sorted array
print("\nArray elelment is sorted order is:\n",np.sort(a,axis=None))
# sort array row-wise
print("\nRow-wise sorted array:\n",np.sort(a,axis=1))
# specify sort algorithm
print("\nColumn wise sort by applying merge-sort:\n",np.sort(a,axis=0,kind ='mergesort'))
# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
# Creating array
arr = np.array(values,dtype = dtypes)
print("\nArray sorted by names:\n",
      np.sort(arr,order='name'))

print("Array sorted by graduation year and then CGPA:\n",
      np.sort(arr,order=['grad_year','cgpa']))
