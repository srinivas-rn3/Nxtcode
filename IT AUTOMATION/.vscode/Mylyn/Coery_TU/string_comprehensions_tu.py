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
my_list = map(lambda n : n*n, nums)
print(list(my_list))
#5:29