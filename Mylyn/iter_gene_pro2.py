import random 
class RandomNumberIter:
    def __init__(self,length,min_val,max_val):
        self.length = length 
        self.min_val = min_val
        self.max_val = max_val
        self.count = 0 

    def __iter__(self):
        return self 

    def __next__(self):
        if self.count >= self.length:
            raise StopIteration
        self.count += 1
        return random.randint(self.min_val,self.max_val)

#Test the Iterator
random_iter = RandomNumberIter(5,1,100)
for num in random_iter:
    print(num)
    
    
#Using Generators
def random_number_generator(length,min_val,max_val):
    count = 0 
    while count < length:
        yield random.randint(min_val,max_val)
        count += 1

#test the generator 
print(" ")
random_gen = random_number_generator(5,1,200)
for num in random_gen:
    print(num)
