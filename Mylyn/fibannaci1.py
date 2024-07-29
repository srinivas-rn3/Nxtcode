#Iterative Approach
def fib_it(n):
    a,b,= 0,1
    fib_se = []
    for _ in range(n):
        fib_se.append(a)
        a,b = b,a+b 
    return fib_se 

n = 10
print(fib_it(n))

#Using Generator
def fib_gen(n):
    a,b = 0,1
    while True:
        yield a
        a,b = b ,a+b 

fib_ = fib_gen(10)
for _ in range(10):
    print(next(fib_))

# Simple Generator
def simple_generator():
    yield 1
    yield 2
    yield 3
# Using the generator
gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))