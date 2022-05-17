import requests
import json
import sys

global common_name
common_name = sys.argv[1]
san1 = sys.argv[2]
csr = sys.argv[3]
if san1 == '' or san1 == " ":
    san1 = common_name
    print(common_name)
    payload={
  "common_name": common_name,
  "dns_value": common_name,
  "csr": csr
 }
    payload_new = json.dumps(payload)
    print(payload_new)
else:
    san1 = san1.split(',')
    print(san1)
    payload={
  "common_name": common_name,
  "dns_value": san1,
  "csr": csr
 }
    payload_new = json.dumps(payload)
    print(payload_new)