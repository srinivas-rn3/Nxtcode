import sys

service = sys.argv[1]
if service == "servicecomponentcontainsdevice":
    first_index = "device_globalid"
    second_index = "servicecomponent_globalid"
    
elif service == "systemelementcontainsdevice":
    first_index = "device_globalid"
    second_index = "systemelement_globalid"
    
elif service == "servicecomponentcontainssystemelement":
    first_index = "systemelement_globalid"
    second_index = "servicecomponent_globalid"
    
elif service == "actualservicecontainsservicecomponent":
    first_index = "servicecomponent_globalid"
    second_index = "actualservice_globalid"
    
else:
    first_index = "device_globalid"
    second_index = "servicecomponent_globalid"
    
print("service Name is :", service)
print("First Index:" ,first_index, end = " " )
print("Second Index is :",second_index , end= " ")