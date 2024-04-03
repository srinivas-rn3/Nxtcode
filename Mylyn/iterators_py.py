#https://www.youtube.com/watch?v=ffFRuB03qLE&t=126s&ab_channel=codebasics
'''
a = ["hey","bro","you'r","awesome"]
for i in a :
    print(i)

#print(dir(a))
itr = iter(a)
itr1 = reversed(a)
print(itr)
print(next(itr))
print(next(itr1))
'''
'''
def stars(n):
    for i in range(n):
        for j in range(i):
            print(i, end=" ")
        print("")
      
stars(10)
'''
class RemoteControl():
    def __init__(self):
        self.channels = ['HBO','CNN','Nick','ABC','Nat Geo']
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))