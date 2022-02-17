import sys
'''
print ("No. of arguments", len(sys.argv),"arguments")
print ("arguments list is :", str(sys.argv))
'''

if len(sys.argv) >= 2:
        print("argument is :", str(sys.argv))
else:
    print("No arguments is found... exiting code!!!")
    sys.exit(2)

'''
try:
    print(sys.argv[1])
    print(sys.argv[2])
except IndexError:
    print("empty arugument!!!")
    sys.exit(2)
var1 = sys.argv[1]
var2 = sys.argv[2]

print(var1)
print(var2)

'''