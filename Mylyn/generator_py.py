'''
def remote_control_next():
    yield "cnn"
    yield "espn"

itr = remote_control_next()
print(itr)
print(next(itr))

for i in remote_control_next():
    print(i)
'''
def fib():
    a, b = 0, 1
    while True:
        yield a 
        a, b = b ,a+b
for i in fib():
    if i > 100:
        break 
    print(i)

#yield
'''
In Python, yield is a keyword used in the context of generators. 
Generators are a convenient way to generate a sequence of values
dynamically without needing to allocate memory for the entire 
sequence at once. They are defined like regular functions but 
use the yield statement to return values one at a time, suspending 
their state in between each value until the next one is requested.
'''
def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1
#Using the generator
counter = count_up_to(5)
for c in counter:
    print(c)