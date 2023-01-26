#https://www.youtube.com/watch?v=QVdf0LgmICw&t=#283s&ab_channel=CoreySchafer
'''
A variable is only available from inside the region it is created. This is called scope.
The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes.
'''
#x = 'global x'
'''
def test(z):
    #global x
    x = 'local x'
    #print(y)
    print(z)
test('local z')
#print(x)
print(z)
#9:24
'''
# = 'global x'
'''
def test():
    global x
    x = 'local x'
    print(x)
test()
print(x)
''' 
#m = min([3,3,41,0,8,8])
#print(m)
#import builtins
#print(dir(builtins))
'''
def my_min():
    pass

m = min([3,3,41,1,8,8])
print(m)    
#12:51
'''
x = 'global x'
def outer():
    #x = 'outer x'

    def inner():
        #nonlocal x
        #x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()
print(x)