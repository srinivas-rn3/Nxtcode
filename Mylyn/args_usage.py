#argparse module

import sys,argparse
'''
n = len(sys.argv)
print("Total arguemnt passed:",n)

print("Name of the python script",sys.argv[0])

print("No. of arguments passed:",end= " ")
for i in range (1,n):
    print(sys.argv[i],end= " ")
Sum = 0
for i in range(1,n):
    Sum += int(sys.argv[i])

print("\n\nResult:",Sum)
'''
'''
#Adding description to the help message.
msg ="Adding description"
parser = argparse.ArgumentParser(description=msg)
parser.parse_args()
'''
'''
# Defining optional value
parser = argparse.ArgumentParser()
## Adding optional argument
parser.add_argument('-o','--Output',help='Show Output')
#Read arguments from command line
args = parser.parse_args()
if args.Output:
    print("Displaying Output as:% s" % args.Output)
'''
def main():
    parser = argparse.ArgumentParser() 
    parser.add_argument('--x',type=float,default=1.0,help='What is the first number')
    parser.add_argument('--y',type=float,default=1.0,help='What is the second number')
    parser.add_argument('--operation',type=str,default='add',help='What operation? can choose add,sub,mul,div')
    
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))
def calc(args):
    if args.operation == 'add':
        return args.x + args.y 
    elif args.operation == 'sub':
        return args.x - args.y 
    elif args.operation == 'mul':
        return args.x * args.y 
    elif args.operation == 'div':
        return args.x / args.y
    
if __name__ == '__main__':
    main()
    