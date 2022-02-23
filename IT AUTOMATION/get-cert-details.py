import requests
import json
import datetime
import time
import sys

from requests.models import Response
#To get the current date & Time
from datetime import date
today = date.today()
issuedate= (f'{today}T00:00:00.000Z')

#api22 = '01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
# prod api
api22 = '017d1f0298ca0b9c02_89F736A27B08E31A6919E8DC72F54DC69F5B53C6D0B0E7690564A50D6A4D976A'
url = "https://pki-ws-rest.symauth.com/mpki/api/v1/searchcert"
#SerialNumber = '0bd02e5f385f9701a9835fcd99ca5984'
# Common Name retrived from SMAX
#common_name = sys.argv[1]
common_name = "*.cross.admlabs.aws.swinfra.net"
# Common Name retrived from SMAX
seat_id = common_name
#certificateoid = "2.16.840.1.113733.1.16.1.5.3.5.1.1298715434"
certificateoid = '2.16.840.1.113733.1.16.1.5.3.5.1.1361541783'
#certificateoid = '2.16.840.1.113733.1.16.1.5.3.1.1.483560546'
payload = {
  "common_name" : common_name,
  "profile_id" : certificateoid,
  "valid_from" : issuedate,
  "status" : "VALID",
  "start_index" : 1
}
headers = {
    'X-API-Key': api22,
    'Content-Type': "application/json"
    }

payload_new = json.dumps(payload)
print(payload_new)
resp = requests.post(url, data=payload_new, headers=headers)
print(resp)
resp_dict = json.loads(resp.text)
print(resp_dict)
'''
for i in resp_dict["certificates"]:
  date_time = i["valid_to"]
  pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
  datem = datetime.datetime.strptime(date_time, pattern)
  Day = datem.day
  Month = datem.month
  Year = datem.year
  epoch = int(time.mktime(time.strptime(date_time, pattern)))*1000
  #epoch = int(time.mktime(time.strptime(date_time, pattern)))
  print("Issuername:Microfocus Infrastructure Issuing CA,Serial_number:"+str(i['serial_number'])+",Valid_to:"+str(epoch)+",Day:"+str(Day)+",Month:"+str(Month)+",Year:"+str(Year))
#print(resp.text)
#print(resp.status_code)
'''