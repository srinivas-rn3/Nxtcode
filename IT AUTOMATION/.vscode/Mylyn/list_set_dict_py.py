# List Set Dict Comprehensions
#https://www.youtube.com/watch?v=fz2PKpPdlRo&ab_channel=codebasics

numbers = [1,2,3,4,5,6,7,8,9,10]
'''
even = []
odd = []
for i in numbers:
    if i%2 == 0:
        #print(i, "is even")
        even.append(i)
    else:
        #print(i, "is not even")
        odd.append(i)
print(even)
print(odd)
'''
'''
even = [i for i in numbers if i%2 == 0]
print(even)
odd = [j for j in numbers if j%2 != 0]
print(odd)
sqr_root = [i*i for i in numbers]
print(sqr_root)
'''
'''
set = set([1,2,3,3,4,5,6,6,7,8,8,9,9,10,10])
print(set)
even = {i for i in  set if i%2 == 0}
print(even)
'''
cities = ["Ney York", "London", "Paris","Tokiyo"]
country = ["USA", "England", "France", "Japan"]
'''
z = zip(country,cities)
print(z)
for i in z:
    print(i)
'''
'''
d = {country:cities  for country,cities in zip(country,cities)}
print(d)
'''
#Sets and Frozen Sets
'''
fruits = {"Apple","Mango ","Orange","Apple","Banana","Orange"}
print(type(fruits))
print(fruits)
'''
'''
a =set()
a.add(1)
a.add("orange")
print(a)
print (type(a))
b = {'alpha'}
print(type(b))
'''
numbers = [1,1,2,2,4,5,3,3,7,8,9,10,1,3]
'''
print(numbers)
unique_ = set(numbers)
print(unique_)
unique_.add(20)
print(unique_)
'''
'''
fs = frozenset(numbers)
print(fs)
print(type(fs))
fs.add(33)
'''
x = {"a","b","c","d"}
print("a" in x)
print("z" in x)
for i in x:
    print(i)
    
y = {"q","a","b","e","d"}
union = x | y
intersection = x & y
diff = x - y
sub_set = y < x
print("union:" ,end=" ")
print(union)
print("intersection:", end=" ")
print(intersection)
print("diffreence: ",end=" ")
print(diff)
print("subset: ", end=" ")
print(sub_set)