'''
book ={}
book['tom'] = {
    "name": "Tom",
    "address": "1 red street, NY" ,
    "phone no": "899893773"
    
}
book['bob'] = {
    "name":"Bob",
    "address" : "1 green street,NY",
    "phone no" : "786537392"
    
}
'''
import json ,sys
'''
s= json.dumps(book)
#print(s)
with open("c:\\Users\\rnsri\\myjson12.txt","w") as f:
    f.write(s)
    print(sys.exit(0))

'''
f = open("c:\\Users\\rnsri\\myjson12.txt","r")
s = f.read()
print(s)
print(type(s))
book = json.loads(s)
print(book)
print(type(book))
phone = book['bob']['phone no']
print(phone)
for person in book:
    print(book[person])
#https://www.youtube.com/watch?v=YgI94IRXySk&ab_channel=codebasics