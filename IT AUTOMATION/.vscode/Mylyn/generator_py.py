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
    