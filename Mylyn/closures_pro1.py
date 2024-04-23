'''
Closures are a powerful concept in Python (and in many other programming languages) 
that allows functions to retain access to variables from their enclosing scope even 
after the outer function has finished executing.
'''
#Example1
def outer_function(x):
    def inner_function(y):
        return x + y 
    return inner_function
closure = outer_function(10)
result = closure(20)
print(result)

#Example2
def outer_function(message):
    def inner_function(name):
        return message + ", " + name
    return inner_function

mes = outer_function("Hello I'm Exporer!!")

nam = mes("DORA")
nam2 = mes("Alice")

print(nam)
print(nam2)

#Example4

def create_counter():
    count = 0
    
    def increment():
        nonlocal count 
        count += 1
        return count
    
    def decrement():
        nonlocal count 
        count -= 1
        return count 
    
    def get_count():
        return count 
    return increment,decrement,get_count

# Create counter instances
increment_count,decrement_count,get_count = create_counter()
# Increment the counter
print("Incrementing counter:",increment_count())
print("Incrementing counter:",increment_count())
print("Incrementing counter:",increment_count())
# Decrement the counter
print("Decrementing counter:",decrement_count())
print("Decrementing counter:",decrement_count())

# Get the current count
print("Current count:",get_count())