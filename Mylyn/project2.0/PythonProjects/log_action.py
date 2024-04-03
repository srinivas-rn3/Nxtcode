def log_functions(action):
    def decorator(func):
        def wrapper(self,*args,**kwargs):
            print(f"{action}:{func.__name__}({args},{kwargs})")
            return func(self,*args,**kwargs)
        return wrapper
    return decorator


class DataStore:
    def __init__(self):
        self.data = {}

    @log_functions("Set")
    def set_value(self,key,value):
        self.data[key] = value 

    @log_functions("Get")
    def get_value(self,key):
        value = self.data.get(key,None)
        if value is not None:
            return value 
        else:
            print("Value is not found!!!")
        #return self.data.get(key,None)

    @log_functions("Delete")
    def delete_value(self,key):
        if key in self.data:
            del self.data[key]
#Example usage
if __name__=='__main__':
    ##create  an instance  of Datastore
    my_data_store = DataStore()
    
    #Set values
    my_data_store.set_value("name","Kylie")
    my_data_store.set_value("age",26)
    
    #Get Value
    name = my_data_store.get_value("name")
    city = my_data_store.get_value("city")#This key doesn't exit
    '''
    if name is not None:
        print(f"Get result:{name}")
    else:
        print("Key is not found!!")
    '''
    
    #Delete the vaules
    my_data_store.delete_value('age')
    my_data_store.delete_value('city') #This key is not found
    
    #Print final value
    print(" Final Data:",my_data_store.data)