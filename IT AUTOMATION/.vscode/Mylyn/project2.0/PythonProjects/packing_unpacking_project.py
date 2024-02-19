#packing and unpacking Demo

#packing 
'''
def pack_value(*args):
    return args 

packed_values = pack_value(1,2,3,4)
print("Packing Values",packed_values)

#Unpacking
def unpack_values(a,b,c,d):
    return a,b,c,d 
unpack_values = unpack_values(*packed_values)
print("Unpacked values:",unpack_values)
'''
#packing and unpacking with dictionaries
def pack_dict(**kwargs):
    return kwargs 
packed_dict = pack_dict(name = "Alice", age = 30, city = "Wonderland")
print("Packed dicitionary:",packed_dict)


def unpack_dict(name,age,city):
    return name,age,city 
unpacked_dict = unpack_dict(**packed_dict)
print("Unpacked dictionary:",unpacked_dict)
