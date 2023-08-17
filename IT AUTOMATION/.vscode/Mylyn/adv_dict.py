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
'''
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