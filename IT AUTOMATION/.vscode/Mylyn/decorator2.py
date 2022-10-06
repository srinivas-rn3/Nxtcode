'''
def greet():
    print("Hello I'm IO",end = '\n')
def mydecor(fn):
    fn()
    print("I'm one of the moon of Jupiter planet")
mydecor(greet)
'''
def mydecor(fn):
    def inner_function():
        fn()
        print("I'm IO moon of the Juipter")
    return inner_function

@mydecor
def greet():
    print("Hello Interstellar!!!", end = "\n")

greet()
