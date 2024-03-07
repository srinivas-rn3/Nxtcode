
'''
It's important to note that pickle is Python-specific, meaning that the serialized data 
can only be read by Python programs. 
Additionally, while pickle is convenient for storing and loading basic Python 
objects, it's not recommended for serializing objects that contain code 
(such as functions or class instances with custom methods), 
as this can lead to security vulnerabilities. For more complex data types or
interoperability with other programming languages, 
alternative serialization libraries like JSON or protocol buffers may be more suitable.

'''
import pickle 
# Create a Python dictionary
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize the dictionary and save it to a file
with open('data.pkl','wb')as file:
    pickle.dump(data,file)

# Deserialize the dictionary from the file
with open('data.pkl','rb') as file:
    loaded_data = pickle.load(file)

# Print the deserialized dictionary
print(loaded_data)