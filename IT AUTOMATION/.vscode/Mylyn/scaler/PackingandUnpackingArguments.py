'''
def eligibility_check(name,age):
    if (age>=18):
        print(f"Hey {name},you are eligible to vote.")
    else:
        print(f"Hey {name},you are not eligible to vote.")

eligibility_check("Srinu",29)
eligibility_check("Anu",10)
eligibility_check(name ="bim",age=17)
#Python Example to Understand Packing with * Operator

# A Python program to demonstrate packing
# All arguments passed to fun2 are packed into tuple *args.
def fun2(*args):
    # Accessing the elements just like we access then from a tuple
    print(args[0])
    #Convert args tuple to a list so we can modify it
    args = list(args)

    #modfying args
    args[0] = "Srinu"
    args[1] = "Academy"
    print(args)
#driver Code
fun2('Python','coding','preparation')
'''
'''
def add_num(*args):
    total = 0 
    for n in args:
        total += n
    return total

print(add_num(2,3))
print(add_num(3,4,5))
'''
'''
#Python example to understand packing with ** operator
# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    #Printing dictionary items
    print(kwargs)
fun(name = "srinu",ID=27,lang="python")
## A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # Printing dictionary items
    for key in kwargs:
        print("%s=%s"%(key,kwargs[key]))
fun(name="s",ID=3,lang="python")
'''
#Unpacking Arguments
#Supposing 1, 2, 3, 4, 5 are going to be function parameters
# We want to add these numbers
'''
val = (1,2,3,4,5,6)
def add_number(*args):
    total = 0
    for n in args:
        total += n 
    print(total)
    return total
add_number(*val)
'''
'''
details = ('1',"Aryan","EC")
def f(roll_no,name,branch):
    print(f"roll number {roll_no} is {name} from {branch} branch of engineering")
f(*details)
'''
'''
#Example of unpacking with ** operator:
def f(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)
    
## Using **kwargs to pass arguments to this function :
kwargs = {"arg1":"S","arg2":2,"arg3":4}
f(**kwargs)
'''
#Working of Packing and Unpacking simultaneously
def eligible(name, age,eligbilty):
    print(f"Hey {name},you are {eligbilty} to vote")
def check_eligible(*args):
    args = list(args)
    if args[1] >=18:
        elig = 'eligible'
    else:
        elig = 'not eligible'
        
    args.append(elig)
    eligible(*args)
check_eligible('anu',19)
