#https://www.youtube.com/watch?v=k9TUPpGqYTo&ab_channel=CoreySchafer
#string
#message = "Hole's is big"
#msg = '''Hi I'm black hole.
#I can eat your planet.'''
#print(len(msg))
#print(msg[6:])
#print(msg.lower())
#print(msg.upper())
#print(msg.count('o'))
#print(msg.find('planet'))
#msg = msg.replace('planet','Universe')
#print(msg)
#12:49
#greetings = 'Hello'
#name = 'Srini'
#message = greetings +','+ name + '.Welcome!'
#message = '{},{}.Welcome!!!'.format(greetings,name)
#message = f'{greetings.lower()},{name.upper()}.Welcome!!!'
#print(message)
#print(dir(name))
#print(help(str))
#print(help(str.upper))
#Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates
#https://www.youtube.com/watch?v=ajrtAuDg3yw&ab_channel=CoreySchafer
'''
my_list = [0,1,2,3,4,5,6,7,8,9]
#          0,1,2,3,4,5,6,7,8,9
#          -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
#list[start:end:step]
#print(my_list[1:8:3])
print(my_list[::5])
url_sample ='https://next-think.com'
print(url_sample[:-7])
'''
#https://www.youtube.com/watch?v=3dt4OGnU5sM&ab_channel=CoreySchafer
#Python Tutorial: Comprehensions - How they work and why you should be using them
nums = [1,2,3,4,5,6,7,8,9,10]
#my_list = [] # for loop way
#for i in nums:
#    my_list.append(i)
#print(my_list)
#Comprehensions way
#my_list = [n for n in nums]
#print(my_list)
#for way
#my_list = []
#for i in nums:
#    my_list.append(i*i)
#print(my_list)
##Comprehensions way
#my_list = [n*n for n in nums]
#print(my_list)
#Using lambda + map
#my_list = map(lambda n : n*n, nums)
#print(list(my_list))
#5:29
#my_list = [n for n in nums if n%2 ==0]
#print(my_list)
#using filter + lambda 
#my_list = filter(lambda n:n%2 ==0,nums)
#print(list(my_list))
# I want a (letter , num)pair for each letter in 'abcd' and each number in '0123'
#my_list = []
#for letter in 'abcd':
#    for num in range(4):
#        my_list.append((letter,num))
#print(my_list)
#comprehensial
#my_list = [(letter,num)for letter in 'abcd' for num in range(4)]
#print(my_list)
#11:09
names = ['Bruce','Clark','Peter','Logan','Diana']
heros = ['Batman','Super Man','Spider Man','Wolverine','Wonder women']
# I want dict('name','heros') for each name , hero  in zip(names,heros)
#print1 =zip(heros,names)
#print(dict(print1))
'''
#The dict() function creates a dictionary.
my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)
'''
# using comprehncee
#my_dict1 = {name: hero for name, hero in zip(heros,names) if hero != 'Spider Man'}
#print(my_dict1)
#my_dict = {}
#for hero,name in zip(heros,names):
#    if name != 'Peter':
#        my_dict[name] = hero
#print(my_dict)
#13:49
#sets : unique values
#nums = [1,2,3,4,4,4,5,5,6,6,7,7,8,9,9,9,0,0,0,]
#my_set = set()
#for i in nums:
#    my_set.add(i)
#print(my_set)
#my_set = {i for i in nums}
#print(my_set)
#genreator expression
n = [1,2,3,4,5,6,7,8,9,10,11]
#def gen_func(n):
#    for n in nums:
#        yield n * n
#my_gen = gen_func(nums)
#for i in my_gen:
# print(i)
my_gen = (n*n for n in n)
for i in my_gen:
    print(i)