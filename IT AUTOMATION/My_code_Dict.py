'''
Dictionary in Python is an unordered collection of data values,
used to store data values like a map, which, unlike other Data
Types that hold only a single value as an element, Dictionary holds key:value pair.
Key-value is provided in the dictionary to make it more optimized.
'''
'''
# Creating a Dictionary
# with Integer Keys
DICT = {1:'Srini',2:'Nova', 3:'Giant'}
print("\nDictionary with the use od Integer Keys: ")
print(DICT)
DICT1 = {'Name':'Srini',1:[3,5,7,9]}
print("\nDictionary with the use f Mixed keys: ")
print(DICT1)
#Dictionary can also be created by the built-in function dict().
#An empty dictionary can be created by just placing to curly braces{}.
# Creating an empty Dictionary
DICT3 = {}
print("Empty dict. : ")
print(DICT3)
# Creating a Dictionary
# with dict() method
DICT4 = dict({1:'srini', 2:'Nova', 3:678})
print("\nDict function use")
print(DICT4)
# Creating a Dictionary
# with each item as a Pair
DICT5 = dict([(1 ,'Srini'),(2,'Nova'),(3,'er45YT')])
print("Dict. with each pair\n")
print(DICT5)
#https://www.geeksforgeeks.org/python-dictionary/?ref=lbp
'''
'''
DICT = {1:'Srini',2:"Nova",3:{'A':"Alpha", 'B': 'Milky way', 'C':'330Ly'}}
print(DICT)
'''
'''
Adding elements to a Dictionary

In Python Dictionary, the Addition of elements can be done in multiple ways.
One value at a time can be added to a Dictionary by defining value along with
the key e.g. Dict[Key] = ‘Value’. Updating an existing value in a Dictionary c
an be done by using the built-in update() method. Nested key values can also be 
added to an existing Dictionary.

Note- While adding a value, if the key-value already exists,
the value gets updated otherwise a new Key with the value is added to the Dictionary.
'''
'''
# Creating an empty Dictionary
DICT = {}
print("Empty dict.:")
print(DICT)
# Adding elements one at a time
DICT[0] = 'Srini'
DICT[1] = 'Nova'
DICT[3] = 'Star'
DICT[4] = 56
print("\nDictionary after filling the data:")
print(DICT)
# Adding set of values
# to a single Key
DICT['value_set'] = 2,3,4
print("\nDictionary after adding three elements:")
print(DICT)
# Updating existing Key's Value
DICT[3] = 'DarkNova'
print("\nAfter updating the dictionary")
print(DICT)
# Adding Nested Key value to Dictionary
DICT[5] = {'Nested':{'1':'Hyper', '2':'Loop','3':'Sonic'}}
print("\nAfter update with nesting")
print(DICT)
'''
'''
Accessing elements from a Dictionary

In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets.
'''
'''
#creating Dict
DICT = {1:'Srini', 'type':'Nova',3:'Sonic',4:'Boom'}
print("\nNew dict")
print(DICT)
# accessing a element using key
print("\nAccessing a element using key:")
print(DICT['type'])
# accessing a element using key
print("\nAccessing another element using key:")
print(DICT[1])
#There is also a method called get() that will also help in accessing the element from a dictionary.
print("\nAccessing a element using 'get'")
print(DICT.get(3))
'''
'''
Accessing an element of a nested dictionary

In order to access the value of any key in the nested dictionary, use indexing [] syntax.
'''
'''
DICT = {1:2344,'type':"Nova star",'distance':{1:'5555Lyt',2:'19000lyt',3:'10000lyt'}}
print("\nNested dict")
print(DICT)
print("\nAccessing the dict values:")
print(DICT[1])
print(DICT['type'])
print(DICT['distance'][1])
print(DICT['distance'][3])
'''
'''
Delete Dictionary
The Python Dictionary is a data structure used in Python that accepts elements in key-value pair form. In this article,
we will be understanding different Ways of deleting a key-value pair from a Python Dictionary.
The dict.clear() to delete a dictionary in Python

Python has in-built clear() method to delete a dictionary in Python. The clear()
method deletes all the key-value pairs present in the dict and returns an empty dict.
'''
'''
DICT = {"A":"Sonic", "B":"Nova",3:44555}
print("\nValue of dict")
print(DICT)
print("\nAfter performing deletion")
DICT.clear()
print(DICT)
'''
'''
Techniques to delete a key-value pair from a Python Dictionary

The following techniques can be used to delete a key-value pair from a dictionary:

    ->Python pop() function
    ->Python del keyword
    ->In-built Python popitem() method
    ->Dictionary Comprehension along with Python items() method
'''
'''
Using pop() method

Python pop() method can be used to delete a key and a value associated with it i.e. a key-value pair from a dictionary.
'''
'''
DICT = {1:222,2:4555,3:6999,4:8999}
print("\nDict values")
print(DICT)
a = DICT.pop(4)
print("\nDeleted element")
print(a)
print(DICT)
'''
'''
Python del keyword

Python del is actually a keyword which is basically used for the deletion of
objects. As we all are aware that Python considers everything as an object,
that is why we can easily use del to delete a dictionary in Python by deleting elements individually.

Python del keyword can also be used to delete a key-value pair from the input dictionary values.

Syntax: del dict[key]
'''
'''
DICT = {1:222,2:4555,3:6999,4:8999}
print("\nDict values")
print(DICT)
del DICT[1]
print("\nAfter deleting the dictionary value")
print(DICT)
'''
'''
DICT = {1:12,2:32,3:45,5:{1:10,2:32,4:67}}
print(DICT)
del DICT[5][2]
print(DICT)
'''
'''
Python popitem() method

Python popitem() function can be used to delete a random or an arbitrary key-value pair from a Python dict.
The popitem() function accepts no arguments and returns the deleted key-value pair from the dictionary.dict.popitem()
'''
'''
DICT = {"A":"Python","B":"Java","C":"Fortan","D":"Javascript"}
print("\mElements of dict")
print(DICT)
print("\nRandom item deleted:")
popItem = DICT.popitem()
print(popItem)
print("\nAfter random deletion")
print(DICT)
'''
'''
Python Dict Comprehension along with items() method

Python items() method along with Dict Comprehension can be used to delete a dictionary in Python.

Python items() method basically takes no arguments and returns an object containing
a list of all the key-value pairs in the particular dictionary.

Syntax:
dict.items()

Python Dict Comprehension can be used to create a dictionary by accepting the key-value pairs from a particular iterable.

Syntax:
{key: value for key, value in iterable}
'''
'''
DICT = {"A":"Set","B":"Dict","C":"Tuple","D":"List","1":"Java","2":"Fortan"}
print("\n Before deletion")
print(DICT)
dictDel = {key:value for key, value in DICT.items() if key != "1"}
dictDel1 = {key:value for key ,value in DICT.items() if key != "2"}
print("\element after deletion is ")
print(dictDel)
'''