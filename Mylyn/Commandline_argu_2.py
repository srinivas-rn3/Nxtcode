import argparse as a
'''
p = a.ArgumentParser()
p.add_argument("--str1", help ="Enter the string1")
p.add_argument("--str2", help = "enter the string2")
p.add_argument("--case",help ="enter the case", choices=["upper","lower"])
args = p.parse_args()

s1 = args.str1
s2 = args.str2
print("Before conversion: " , end ='\n')
print(s1)
print(s2)
if args.case == "upper":
    print("Converted string to 'upper' case:", end = "\n")
    print("str1:",s1.upper())
    print("str2 :",s2.upper())

elif args.case == "lower":
    print("Converted string to 'lower' case:", end = "\n")
    print("str1: ",s1.lower())
    print("str2: ",s2.lower())
'''
'''
p = a.ArgumentParser()
p.add_argument("--num1", help ="Enter the integer value1")
p.add_argument("--num2",help="Enter the integer value2")
p.add_argument("--math_operator",help="Enter the math operator",choices=['Add','Sub','Mul','Div'])
args = p.parse_args()

int1 = int(args.num1)
int2 = int(args.num2)
print("the numbers are {} {}".format(int1,int2))

try :
    if args.math_operator == "Add":
        print("Addtion is :")
        print(int1 + int2)
    elif args.math_operator =="Sub":
        print("Subtraction is :")
        print(int1 - int2)
    elif args.math_operator == "Mul":
        print("Multiplication is : ")
        print(int1 * int2)
    elif args.math_operator == "Div":
        print("Division is : ")
        print(int1 / int2)
except ZeroDivisionError as e :
    print(e)
'''
# Create the parser
p = a.ArgumentParser()
# Add an argument
p.add_argument('--name',type = str ,required=True,help = "enter the string value")
# Parse the argument
args = p.parse_args()
print("Hello",args.name)
