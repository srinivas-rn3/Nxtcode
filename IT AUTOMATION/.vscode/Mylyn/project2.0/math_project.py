'''
Math exercises are a good place to get comfortable with Python’s syntax and style. 
Write some code to conduct simple math calculations (addition, subtraction, etc.) but with caveats.

For instance, write a short program that asks the computer to request and add two variable inputs. 
Then, adjust the program to perform a specific task based on the result. For example, print a 
specific statement if the sum is between 10 and 20, above 100, or print “no negative numbers”
if a subtraction problem delivers a corresponding result. 
You can gradually expand the program to make it more elaborate and the tasks more complex.
'''
import math

def math_cals(choice,A,B):
    """
    This perform basic math operations such as :
    1. Add
    2. Subtraction
    3. Multiplication
    4. Divion
    5. Sum
    and print the resepective value of math operation
    """
    match choice:
            case 'Add':
                C = A + B
                print(f"Add value is: {C}")
            case 'Sub':
                C = A - B
                print(f"Subtraction value is: {C}")
            case 'Mul':
                C = A * B 
                print(f"Multiplication value is: {C}")
            case 'Div':
                try:
                    C = A / B
                    print(f"Division value is: {C}")
                except ZeroDivisionError as e:
                    print("Error cannot divide by zero!!!")
            case 'Sum':
                try:
                    d =[A,B]
                    C = sum(d)
                except ValueError as e:
                    print("Invlaid values of sum!!!",e)
                if C >= 0:
                    print(f"Sum value is +ve number")
                    print(f"Sum value is: {C}")
            case default:
                print("Invalid math operation!!!")
print("Using__doc__:")
print("Using help")
help(math_cals)
'''
def main():
    print("Math expreseesion test.Enter the numbers followed by option" ,end='\n')
    A = int(input("enter the first number:"))
    B = int(input("enter the second number:"))
    options = ['Add','Sub','Mul','Div']
    for i,option in enumerate(options):
        print("{}.{}".format(i+1,option))
    choice = input("Enter the choice: ")
    if choice in['1','2','3','4']:
        print("you have selected option {}".format(options[int(choice)-1]))
        print("Performaing math oprtation",end='\n')
        math_cals(choice,A,B)

    else:
        print("Invalid Choice!!!")
'''
if __name__=="__main__":
     print("Math expreseesion test.Enter the numbers followed by option" ,end='\n')
     
     A = int(input("enter the first number:"))
     B = int(input("enter the second number:"))

     options = ['Add','Sub','Mul','Div','Sum']
     
     for i,option in enumerate(options):
        print("{}.{}".format(i+1,option))
        
     choice = input("Enter the choice: ")
     
     if choice in['1','2','3','4','5']:
        op = options[int(choice)-1]
        print("you have selected option {}".format(op))
        print("Performaing math operation",end='\n')
        print(f"First Value is: {A}")
        print(f"Second Value is: {B}")
        math_cals(op,A,B)
     else:
        print("Invalid Choice!!!")