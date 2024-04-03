#Command line argument processing using argparse [Python 3 Programming Tutorials]
import argparse 
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #postional arugement
    #optional arugument need to add (--) in front of th arguments
    parser.add_argument("--number1",help ="first number")
    parser.add_argument("--number2",help = "second number")
    parser.add_argument("--operation",help = "operation", \
                        choices=["add","subtract","multiply"])
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    result = None
    #print(args.operation)
    n1 = int(args.number1)
    n2 = int(args.number2)
    if args.operation == "add":
        print("add is selected as a operation")
        result = n1 + n2
    elif args.operation == "subtract":
        print("Subtract is selected as aoperation")
        result = n1 - n2
    elif args.operation == "multiply":
        print("Multiply is selected as aoperation")
        result = n1 * n2 
    else:
        print("un-supported operations!!!")

    print(result)
'''
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("--physics",help = "physics")
    p.add_argument("--chemistry",help= "chemistry")
    p.add_argument("--math", help = "math")
    args = p.parse_args()
    #avg = None
    ph = (args.physics)
    ch = (args.chemistry)
    ma =  (args.math)
    print("physics subject marks is :",ph)
    print("chemistry subject marks is :", ch)
    print("math subject marks is :", ma)
    avg = (int(ph)+int(ch)+int(ma))/3
    print("The average is :", avg)