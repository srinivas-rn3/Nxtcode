'''
"Green coding" typically refers to writing code that is efficient, optimized, and environmentally friendly"
'''
def cal_fib(n):
    """Calcaulating the nth fibonacci number."""
    if n <= 0:
        return 0 
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(2,n+1):
            a,b = b,a+b
        return b 
'''
So, when calculating the Fibonacci sequence programmatically, we start iterating from the third number onwards
(index 2 in zero-based indexing), because the first two numbers are already known (0 and 1) and don't need to be recalculated.
'''
'''
for _ in ...:: This is a for loop in Python. 
The _ is a convention in Python to indicate a variable that will
not be used inside the loop. It's essentially a placeholder.
'''
def main():
    """The main function to demostrate green coding"""
    print("Enter the number (n)  of fibbonacci sequence you want to calculate: ")
    n = int(input())

    fib_no = cal_fib(n)
    print(f"The {n}th Fibbonacci number is:{fib_no}")



if __name__ == '__main__':
    main()
