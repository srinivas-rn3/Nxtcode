'''
# Merge Two Dictionaries
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}
dict3 = {**dict1,**dict2}
print(dict3)
dict_u = dict1 | dict2 
print(dict_u)


#Check if a Key Exists in a Dictionary
dict1 = {"a":1,"b":2,"c":4}
print('a' in dict1)
print("d" in dict1)

#Add and change items
my_dict = {"name":"Max", "age":28, "city":"New York"}
my_dict2 = dict(name='Lisa',age=27,city='Boston')
print(my_dict)
print(my_dict2)
name_dict = my_dict['name']
name_dict= my_dict2['name']
print(name_dict)

my_dict['email'] = "xxx@zzz.com"
print(my_dict)
my_dict['email'] ="xxxx@zzzz.com"
print(my_dict)
#https://www.python-engineer.com/courses/advancedpython/03-dict/
#Delete items
del my_dict['email']
print(my_dict)
print("Popped item",my_dict.pop(("age")))
print(my_dict)

# return and removes the last inserted key-value pair 
print("popped item",my_dict.popitem())
print(my_dict)
my_dict.clear()
print(my_dict)
'''
#Check for keys
my_dict = {"name":"Max", "age":28, "city":"New York"}
'''
if "name" in my_dict:
    print(my_dict["name"])
try:
    print(my_dict['first_name'])
except KeyError:
    print("No Key found!!!!")
'''
'''
if "name" in my_dict:
    print(my_dict['name'])
else:
    print("No name found!!!")
'''
'''
#Looping through dictionary
for key in my_dict: ## loop over keys
    print(key,my_dict[key])
# loop over keys
for key in my_dict.keys():
    print(key)
# loop over values
for value in my_dict.values():
    print(value)
# loop over keys and values
for key,value in my_dict.items():
    print(key,value)
'''
'''
#Copy a dictionary
dict_org = {"name":"Max", "age":28, "city":"New York"}
# this just copies the reference to the dict, so be careful
dict_copy = dict_org
print(dict_copy)
dict_copy['name'] ='Lisa'
print(dict_copy)
print(dict_org)
# use copy(), or dict(x) to actually copy the dict
dict_org = {"name":"Max", "age":28, "city":"New York"}
dict_copy = dict_org.copy()
#dict_copy = dict(dict_org)
# now modifying the copy does not affect the original
dict_copy['name'] = 'Lisa'
print(dict_copy)
print(dict_org)
'''
'''
#Merge two dictionaries
# Use the update() method to merge 2 dicts
# existing keys are overwritten, new keys are added
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
my_dict.update(my_dict_2)
print(my_dict)
'''
'''
#Possible key types

# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[6])
# use a tuple with immutable elements (e.g. number, string)
my_tuple =(8,7)
my_dict = {my_tuple:15}

print(my_dict[my_tuple])
#print(my_dict[8,7])
# a list is not possible because it is not immutable
# this will raise an Error:
my_list = [8,7]
my_dict = {my_list:15}
'''
#Nested dictionaries
my_dict_1 = {"name": "Max", "age": 28}
my_dict_2 = {"name": "Alex", "age": 25}
nested_dict = {"dictA":my_dict_1,
               "dictB":my_dict_2}
print(nested_dict)