def is_prime(num):
    """Check number is prime"""
    if num < 2:
        return False 
    for i in range(2,int(num**0.5) +1):
        if num * i == 0:
            return False 
    return True 
def generate_primes_in_range(start,end):
    """Generate a list of prime numbers withing a specified range"""
    return [num for num in range(start,end+1) if is_prime(num)]


def main():
    """Get the user inputs in range"""
    start_range = int(input("Enter the starting number of the reange: "))
    end_range = int(input("Enter the the ending number of the range: "))

    """Genrtate and display the list of prime number"""
    primes = generate_primes_in_range(start_range,end_range)
    print(f"Prime number between {start_range} and {end_range}: {primes}")

if __name__ =='__main__':
    main()