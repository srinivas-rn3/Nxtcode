class Datastore:
    def __init__(self):
        self.data = {}

    def set_value(self,key,value):
        self.data[key] = value
        print(f"Set:{key}=>{value}")

    def get_value(self,key):
        value = self.data.get(key)
        if value is not None:
            print(f"Get:{key} =>{value}")
        else:
            print(f"Key'{key}' not found")

    def delete_value(self,key):
        if key in self.data:
            del self.data[key]
            print(f"Deleted :{key}")
        else:
            print(f"Key '{key}' not found")

# Example usage
if __name__ == '__main__':
    my_data_store = Datastore()

    #Set value 
    my_data_store.set_value("name","john")
    my_data_store.set_value("age",25)

    #Get Value
    my_data_store.get_value("name")
    my_data_store.get_value("city")

    #Delete value
    my_data_store.delete_value("age")
    my_data_store.delete_value("city")