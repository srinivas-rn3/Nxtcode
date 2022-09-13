import sys
import json
#san1= '"dashboard.software.microfocus.com","build-mf.software.microfocus.com","registry.software.microfocus.com","artifacts.software.microfocus.com","content.software.microfocus.com","cms-service.software.microfocus.com","ui-service.software.microfocus.com"'
#san1 = "xyx.com","xxo.com"
san1 = sys.argv[1]

#arr = san1.split()
#print(arr)
common_name = "mf.com"
if san1 == '' or san1 == " ":
     san1 = common_name
else:
     list1 = list(san1.split(" "))
     print(list1)
     for i in list1:
     #san1 = san1.split(',')
        i = i.replace(i,',')
        print (i)
        print(i.split())
