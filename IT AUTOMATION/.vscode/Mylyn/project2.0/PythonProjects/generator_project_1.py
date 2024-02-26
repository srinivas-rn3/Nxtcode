'''
Generators are a powerful concept in Python used for creating iterators. 
They allow you to generate a sequence of values on-the-fly, rather than storing them in memory all at once. 
This can be particularly useful when dealing with large datasets or infinite sequences.
'''
def my_generator():
    yield 1
    yield 2 
    yield 3
'''
In this example, my_generator is a generator function because it contains one or more yield statements. '
When you call this function, it returns a generator object. Each time the next() function is
called on this generator object, the function runs until it reaches a yield statement, at 
which point it yields the value and pauses its execution. When next() is called again, it resumes 
execution from where it left off.

'''
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

'''
Generators can also be used in for loops, as they automatically handle the 
StopIteration exception that is raised when the generator is exhausted.
'''
gen1_ = my_generator()
for values in gen:
    print(values)
'''
Generators are memory-efficient because they produce values on-the-fly, which means 
they only need to store the current state of the iteration, rather than the entire 
sequence of values. This makes them particularly useful for working with large datasets or infinite sequences.
'''
'''
print("\n")
def infinte_sequence():
    num = 0 
    while True: 
        yield num 
        num += 1
gen = infinte_sequence()
#for i in gen:
#    print(i)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''
'''
def fibonacci_gen():
    a,b=0,1
    while True:
        yield a 
        a,b = b,a+b
# Using the generator to print the first 10 Fibonacci numbers
fib_ = fibonacci_gen()
for _ in range(10):
    print(next(fib_))
    
def my_gen3():
    yield 1 
    yield 2 
    yield 3
gen_ = my_gen3()
print(next(gen_))
'''
def even_number():
    num = 0
    while True:
        yield num 
        num += 2
even_gen = even_number()
for _ in range(10):
    print(next(even_gen))