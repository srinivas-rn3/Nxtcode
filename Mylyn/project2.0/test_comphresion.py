
def com(start,end):
    return [num for num in range(start,end+1) if if_prime(num)]

def if_prime(num):
    if num < 2:
        return False 
    sq = int((num ** 0.5)+1)
    #print(f"Square root of {num} is {sq}")
    for i in range(2,sq):
        #print(i)
        if num * i == 0:
            return False  
    return True 

def main():
    A = int(input("Enter the interger value of start : "))
    B = int(input("Enter the integer value of end : "))
    prime = com(A,B)
    print(prime)
if __name__ == "__main__":
    main()