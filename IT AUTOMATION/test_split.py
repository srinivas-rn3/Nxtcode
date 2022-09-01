import sys
import json
#san1= "dashboard.software.microfocus.com","build-mf.software.microfocus.com","registry.software.microfocus.com","artifacts.software.microfocus.com","content.software.microfocus.com","cms-service.software.microfocus.com","ui-service.software.microfocus.com"
#san1 = "xyx.com","xxo.com"
san1 = sys.argv[1]
print(type(san1))
common_name = "mf.com"
if san1 == '' or san1 == " ":
     san1 = common_name
else:
    print(san1)
