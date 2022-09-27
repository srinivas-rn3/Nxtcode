x = input("Enter the number: ")
y = input("Enter the number: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("Divison error occured: ",e)
    z = None
except TypeError as  e :
    print("Type Error Exception")
    z = None
print("Divison is: ", z)