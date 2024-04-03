def Square(x):

    return (x * x)

def SumofSquare(Array ,n):
    Sum = 0
    for i in range(n):
        SquaredValues = Square(Array[i])
        Sum += SquaredValues
    return Sum

Array = [1,2,3,4,5,6,7,8,9,10]
n = len(Array)
Total = SumofSquare(Array ,n)
print("{}:Sum of Sqaures of list of numbers".format(Total))