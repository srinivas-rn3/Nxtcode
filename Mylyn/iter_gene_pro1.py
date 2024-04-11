'''
Project Overview:

We'll create an iterator to generate Fibonacci numbers up to a certain limit.
Then, we'll create a generator function to achieve the same.
Finally, we'll compare both approaches in terms of simplicity and efficiency.

'''

class FibanacciIterator:
    def __init__(self,limit):
        self.limit = limit 
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self 

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        result = self.a 
        self.a,self.b = self.b, self.a + self.b 
        return result 

fib_iter = FibanacciIterator(50)
for num in fib_iter:
    print(num)


#Now, let's implement the same functionality using a generator:

def fiba_generator(limit):
    a,b = 0,1
    while a <= limit:
        yield a 
        a,b = b,a + b
fib_gen = fiba_generator(50)
for num in fib_gen:
    print(num)