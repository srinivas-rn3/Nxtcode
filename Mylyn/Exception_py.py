'''
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
'''
'''
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def p_exception(self):
        print("User Defined exception:", self.msg)
        
try:
    raise Accident('Crash between two cars')
except Accident as a :
    a.p_exception()
    
#Raise Exception And Finally
'''
'''
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("Accident occured ... Take to Detour")
try:
    raise Accident('crash between two cars')
except Accident as e :
    e.handle()
'''
def process_file():
    try:
        f = open("C:\\Users\\rnsri\\funny-learn.txt")
        x = 1/0
    except FileNotFoundError as e :
        print("inside the exception!!")
        print(e)
    except ZeroDivisionError as e :
        print("divison error")
    finally:
        print("cleaning up file")
        f.close()
process_file()