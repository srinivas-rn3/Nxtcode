import requests
import json
import sys

#URL
order_id = sys.argv[1]
print(order_id)
#Status
#status = "renewed"
url = f"https://www.digicert.com/services/v2/order/certificate/{order_id}/status"
print(url)
#api = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
#headers
headers = {
    'X-DC-DEVKEY': api,
    'Content-Type': "application/json"
    }
#API Payload
payload = {
  "status": "renewed"
}
payload_new = json.dumps(payload)
print(payload_new)
#API Call
try:
  response = requests.request("PUT",url,data=payload_new,headers=headers)
  print(response.text)
  print(response.status_code)
except requests.exceptions.HTTPError as error:
    print(error)
    print(response.status_code)