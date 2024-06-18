'''
class Number: 
    
    def __init__(self,value):
        self.value = value
     
    def __eq__(self,other):
        return self.value  == other.value 
    
    def __ne__(self,other):
        return self.value  != other.value 
    
    def __lt__(self,other):
        return self.value >= other.value 
    
    def __le__(self,other):
        return self.value <= other.value 
    
    def __gt__(self,other):
        return self.value > other.value
    
    def __ge__(self,other):
        return self.value >= other.value 
'''
class Number: 
    def __init__(self,value):
        self.value = value
        
    def __eq__(self,other):
        if isinstance(other,Number):
            if self.value ==other.value
            return f"{self.value} is equal to {other.value}"
        else:
            raise ValueError("Can only compare with another Number object")
    
    def __ne__(self,other):
        if isinstance(other,Number):
            return f"{self.value} is not equal to {other.value}"
        else:
            raise ValueError("Can only compare with another Number object")
    
    def __lt__(self,other):
        if isinstance(other,Number):
            return f"{self.value} is less than {other.value}"
        else:
            raise ValueError("Can only compare with another Number object")
    
    def __le__(self,other):
        if isinstance(other,Number):
            return f"{self.value} is less than or equal to {other.value}"
        else:
            raise ValueError("Can only compare with another Number object")
    
    def __gt__(self,other):
        if isinstance(other,Number):
            return f"{self.value} is greater than {other.value}"
        else:
            raise ValueError("Can only compare with another Number object")
    
    def __ge__(self,other):
        if isinstance(other,Number):
            return f"{self.value} is grether than or equal to {other.value}"
        else:
            raise ValueError("Can only compare with another Number object")
        
        
num1 = Number(5)
num2 = Number(10)

# Equality operator (==)
print(num1 == num2)

# Not equal operator (!=)
print(num1 != num2)

# Less than operator (<)
print(num1 < num2)

# Less than or equal to operator (<=)
print(num1 <= num2) 

# Greater than operator (>)
print(num1 > num2)

# Greater than or equal to operator (>=)
print(num1 >= num2)