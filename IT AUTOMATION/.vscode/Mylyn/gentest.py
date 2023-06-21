
# def first_n(n):
#     '''Build and return list'''
#     num,nums= 0,[]
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums 

# sum= sum(first_n(10000))
# print(sum)

# class first_n(object):
#     def __init__(self,n):
#         self.n = 0 
#         self.num = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return self.next()
#     def next(self):
#         if self.num < self.n:
#             cur,self.num = self.num,self.num+1
#             return cur 
#         raise StopIteration()
# sym= sum(first_n(10000))
# print(sym)

# def gen_fun():
#     yield 10
#     yield 20
#     yield 30 
# for i in gen_fun():
#     print(i)

# def seq(x):
#     for i in range(x):
#         yield i  
# range_ = seq(10)
# for i in range_:
#     print(next.i)
# print(next(range_))
# print(next(range_))
# print(next(range_))
# print(next(range_))
# print(next(range_))
# print(next(range_))
# print(next(range_))
# print(next(range_))

# x = 10
# gen = (i for i in range(x) if i % 2 == 0)

# list_ = [i for i in range(x) if i %2 == 0]

# print(gen)
# print(list_)
# for j in gen:
#     print(j)

def infi():
    n = 0 
    while True:
        yield n  
        n +=1 
for i in infi():
    if i%4 == 0:
        continue
    elif i  == 13:
        break
    else:
        print(i)
        