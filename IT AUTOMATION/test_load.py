import json
import sys
a = {
    "id": 217742929,
    "domains": [
     {
      "id": 4076689,
      "name": "mfidmz-houston-adgc.houston.softwaregrp.com",
      "dns_name": "mfidmz-houston-adgc.houston.softwaregrp.com"
     },
     {
      "id": 4076690,
      "name": "mfidmz-houston-ad.houston.softwaregrp.com",
      "dns_name": "mfidmz-houston-ad.houston.softwaregrp.com"
     },
     {
      "id": 4076687,
      "name": "m4w0329g.mfidmz.net",
      "dns_name": "m4w0329g.mfidmz.net"
     },
     {
      "id": 4076691,
      "name": "m4w0329g.houston.softwaregrp.com",
      "dns_name": "m4w0329g.houston.softwaregrp.com"
     },
     {
      "id": 4076688,
      "name": "m4w0330g.mfidmz.net",
      "dns_name": "m4w0330g.mfidmz.net"
     },
     {
      "id": 4076692,
      "name": "m4w0330g.houston.softwaregrp.com",
      "dns_name": "m4w0330g.houston.softwaregrp.com"
     }
    ],
    "certificate_id": 219246317
   }
resp_dict1 = json.dumps(a)
resp_dict = json.loads(resp_dict1)
print (resp_dict)
print(resp_dict["id"])
"""
"json.loads"take a string as input and returns a dictionary as output.
"json.dumps" take a dictionary as input and returns a string as output.
"""