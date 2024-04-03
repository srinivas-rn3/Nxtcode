def my_function():
    """
    This is the docstring for my_function.
    It describes what the function does.
    """
    pass
#Access doctring using help()
#help(my_function)
print(my_function.__doc__)

import argparse 

def main():
    parser = argparse.ArgumentParser(description = 'Checking two numbers')
    parser.add_argument('--option1',help="Value of options1")
    parser.add_argument('--option2',help="Value of options2")
    
    args = parser.parse_args()
    
    if args.option1:
        print(f"Option1 value: {args.option1}")
    if args.option2:
        print(f"Option2 value: {args.option2}")

if __name__ =='__main__':
    main()