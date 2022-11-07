#Python Tutorial: Generators - How to use them and the benefits you receive
#https://www.youtube.com/watch?v=bD05uGo_sVI
'''
def square_num(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

nu_nums = square_num([1,3,5,7,9,11])

print(nu_nums)
'''
'''
def square_num(nums):
    for i in nums:
        yield(i*i)

my_num = square_num([1,3,5,7,9,11])
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
#for num in my_num:
#    print (num)
'''
'''
my_num = (x*x for x in [1,3,5,7,9,11])

print(list(my_num))

##for i in my_num:
#   print (i)
'''
'''
import random
import time 
import mem_profile 

names = ['Marnie','Goku','Bulma','Krelin','Yamcha']
subject = ['Physco','Karate','Device Engineer','Karate','Hunting Karate']

print ('Memory (Before): {}Mb'.format(mem.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major' : random.choice(subject)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(subject)

        }
    yield person 

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

#t1 = time.clock()
#people = people_generator(1000000)
#t2 = time.clock()

print ('Memory (After) : {}Mb'.format(mem.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))
'''
#https://www.youtube.com/watch?v=3dt4OGnU5sM