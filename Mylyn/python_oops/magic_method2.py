class Fraction:
    def __init__(self,numerator, denominator):
        
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        
        return f"Fraction({self.numerator},{self.denominator})"
    def __add__(self,other):
         # Adding two fractions: a/b + c/d = (a*d + b*c) / (b*d)
         new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
         new_denomitor = self.denominator * other.denominator
         return Fraction(new_numerator,new_denomitor)
     
    def __eq__(self,other):
        # Two fractions are equal if a/b == c/d
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __lt__(self,other):
        # Comparing two fractions a/b < c/d
        return self.numerator * other.denominator < self.denominator * other.numerator

# Usage
f1 = Fraction(1,2)
f2 = Fraction(2,3)
f3 = Fraction(3,4)
f4 = Fraction(1,2)

# Print the fractions
print(f1)
print(f2)
print(f3)
print(f4)
print("\n")
# Adding two fractions
f1_sum = f1 + f2
print(f1_sum)
f2_sum = f3 +f4
print(f2_sum)
print("\n")
# Comparing fractions
print(f1 < f2)
print(f2 < f3)
print(f3 < f1)
print("\n")
# Checking equality
print(f1 == f2)
print(f1 == f4)

#Example 2
class Student:
    def __init__(self,name,age):
        self.name = name  
        self.age = age  
    
    def __repr__(self):
        return f"Student(name = '{self.name}',age = '{self.age}')"
    
    def __gt__(self,other):
        if not isinstance(other,Student):
            raise ValueError("Can only compare Student Objebcts") 
        return self.age > other.age
       
#usage
S1 = Student("Alice",20)
S2 = Student("Bob",30)
S3 = Student("Charlie",18)

# Greater than checks
print(S1 > S2)
print(S2 > S3)

#Printing the student objects
print(S1)
print(S2)
print(S3)