def log1(func):
    def wrapper(*args,**kwargs):
        if isinstance(args[0],Calc):
            instance = args[0]
        print(f"Calling function {func.__name__} with arguments ({instance.a},{instance.b})") 
        return func(*args,**kwargs)
    return wrapper 

class Calc:
    def __init__(self,a,b):
        self.a ,self.b = a,b
        
    @log1
    def add(self):
        return self.a + self.b 
    
    @log1
    def sub(self):
        return self.a  - self.b 
    
    @log1
    def mul(self):
        return self.a * self.b 
    
    @log1
    def div(self):
        '''
        try:
            return self.a / self.b
        except ZeroDivisionError as e:
            print("Divison cannot allow",e)
        '''
        if self.b == 0:
            raise ValueError ("Cannot divide by zero")
        return self.a / self.b
    
    def __str__(self):
        return f"Calc:({self.a} ,{self.b})"

if __name__ == '__main__':
    calc = Calc(10,1)
    
    print("Add:",calc.add())
    print("Sub:",calc.sub())
    print("Mul:",calc.mul())
    print("Div:",calc.div())
    
           