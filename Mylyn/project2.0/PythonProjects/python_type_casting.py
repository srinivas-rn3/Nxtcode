''''
Type casting in Python refers to the process of converting a variable from
one data type to another. Python provides built-in functions to perform type 
casting, allowing you to convert variables between different data types as 
needed. Here's an overview of the most common type casting functions in Python:
'''
#int(): This function converts a variable into an integer data type.
# Converting a string to an integer
num_str = '10'
print(num_str)
print(type(num_str))
num_int = int(num_str)
print(num_int)
print(type(num_int))

sep = "#############################"
print(sep)
# Converting a floating-point number to an integer
num_float = 10.5
print(num_float)
print(type(num_float))
num_int1 = int(num_float)
print(num_int1)
print(type(num_int1))
print(sep)

#float(): This function converts a variable into a floating-point number.
#Converting an integer to a float
num_int2 = 10 
print(num_int2)
print(type(num_int2))
num_float2 = float(num_int2)
print(num_float2)
print(type(num_float2))
print(sep)

# Converting a string representing a number to a float
num_str2 = "10.5"
print(num_str2)
print(type(num_str2))
num_float3 = float(num_str2)
print(num_float3)
print(type(num_float3))
print(sep)

#str(): This function converts a variable into a string.
# Converting an integer to a string
num_int3 = 10 
num_str3 = str(num_int3)
print(num_str3)
print(type(num_str3))
## Converting a floating-point number to a string
num_float4 = 10.5
print(type(num_float4))
print(num_float4)
num_str4 = str(num_float4)
print(num_str4)
print(type(num_str4))
print(sep)
'''
bool(): This function converts a variable into a Boolean value.
It returns False if the value is zero, an empty sequence
(e.g., "", (), []), or None. Otherwise, it returns True.
'''
# Converting an integer to a Boolean
num_int4 = 1
bool_value = bool(num_int4)
print(type(bool_value))
print(bool_value)

# Converting a non-zero integer to a Boolean
num_int5 = 10
print(type(num_int5))
print(num_int5)
bool_value1 = bool(num_int5)
print(bool_value1)
print(type(bool_value1))

# Converting a string to a Boolean
str_value4 = "FUCK"
print(type(str_value4))
print(str_value4)
bool_value4 = bool(str_value4)
print(bool_value4)
print(type(bool_value4))
print(sep)
float4 = 0.0
b = bool(float4)
print(b)