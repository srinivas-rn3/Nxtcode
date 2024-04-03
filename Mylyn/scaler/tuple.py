nestedTuple = ('hello', [1 ,2, 3], (4, 5, 6))
print(nestedTuple[1][2])
## concatenating two different tuples
a = ('app','dev','test')
b = (1,2,3)
c = a + b
print(c)

tempTuple = (1, 2, 3, 4, 5)
print(tempTuple)
del tempTuple
print(tempTuple)## throws NameError: name 'tempTuple' is not defined