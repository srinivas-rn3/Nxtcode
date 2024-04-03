#Python Tutorial: Using Try/Except Blocks for Error Handling
#https://www.youtube.com/watch?v=NIWwJbo-9_8

try:
    f = open('wrapper.log')
    if f.name == 'wrapper.log':
        raise Exception
    #var  = bad_var
except FileNotFoundError as e:
    print(e) 
except Exception as e:
    print("Holy Cow, no such file!!")
else:
    print(f.read())
    f.close()
finally:
    print("executing Finally.....")

