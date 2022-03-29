import requests
import json
import sys
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
#api = apiuser
#securesiteov = "https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex"
# Order ID from SMAX sys.argv[1]
#orderid = sys.argv[1]
orderid = "126441049"
#url=securesiteov
# SMAX ID sys.argv[2]
#smaxid = sys.argv[2]
smaxid = "6192572"
# Comment from SMAX sys.argv[3]
comment = "renewcerts"
comments = "SMAX Ref:"+smaxid+' - '+comment
# Common Name from SMAX sys.argv[4]
#common_name = sys.argv[4]
common_name = "www.voltage.com"
# SAN from SMAX sys.argv[5]
#san1 = sys.argv[5]
san1 = "voltage.com"
san1 = ''
if san1 == '':
    san1 = common_name
# CSR from SMAX
#csr = 'MIIC+TCCAeECAQAwgYYxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEcMBoGA1UEAxMTd3d3LmVhc3RiYXljYWZlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALwSgqfTpy755SLql+QGnQk67CS510Q+wP8i2w40ncnLHJODaE8zFzw/xyJpItPZYn3Mub9rPbu7H0miDYvVjfikJM1SWQOm1MxEGyEtk17skaedg/y4+XN0335HMNVwfISX25HX4Y6d3cXv/0Kg655utWm4f2gkHG/G0P4RcyBD0f/wOHeNNvQsS48tFJrgotCBQmt7HhY4UkuNXk/xP91pl0eu5O/Yh0SlbShBECL3YgyfYmfwDI338XVdauZbmwgsu1Tq1xrKLN8uSp3C7v9enkNYJXNY55X++pmO+eBpgxOYe9NWsxVeIgQwzTttmJIm0qd9O7cOyQY+9VQ5jCUCAwEAAaAtMCsGCSqGSIb3DQEJDjEeMBwwGgYDVR0RBBMwEYIPZWFzdGJheWNhZmUuY29tMA0GCSqGSIb3DQEBBQUAA4IBAQBywTb6qgPEVMicKAkY5lt+30beWZuSCzl3FUIqMf7fZHrczGD7K24OSDt8zuomgX4JU+18RkCv9V0u2oq8igwWRiLWUkZHYLs1BMl8Hl0sToRItg98h0BRpPztUCm9Dc4ZKvHuoRDLHOhPTV5U22db820oWQPGPfFXa/M+zU/kGmAZhHpIB+1ZKg+SX71bBSkBkyrbNkwW+VgX2dksUDFHuVC8u/nOhOXDuhKOCPiMeq19KJyclhz89E5mzbs2n9KYe7XuTTbpXbXYOo9XtRr6TgsWuh3QXCYn7ZfqtYx7ZU67iXWnSU+0gASsgVtsyOQYn8HmIqvaolIje4sEI79L'
#csr = sys.argv[6]
csr = "-----BEGIN CERTIFICATE REQUEST-----MIIC7jCCAdYCAQAwbzELMAkGA1UEBhMCR0IxETAPBgNVBAgTCEJlcmtzaXJlMRAwDgYDVQQHEwdOZXdidXJ5MSEwHwYDVQQKExhNaWNybyBGb2N1cyAoSVApIExpbWl0ZWQxGDAWBgNVBAMTD3d3dy52b2x0YWdlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMTtyn5NKgKAnjQg7wy9KAe+W5FFjwylUJqcVes/ugHTy5ugPDx6JhYMRzBupG2wmvTdCI+o+JOTuM+zIeq2eyMtl80VmmoZTHW1/wWoauL9WrhVeuoUZolDD7ETqF/DVy9vxFlJOiri6Qm9YYRahDHHbqlD9VcUX1mUef5LJZ+BfHOXTiT5gs3K2nFrcDGyqOct2i9eiRqnk9LmmUkKs4ZcLj95s30XfvAMIIaSblqXrwdnTJboZoYr3Laec3cVe3BQgrZfZ3Boa7T9sP1gNHCFE7HhdpPzGDUhih8Pmsq5vRSrvrvqHT2RWT8HokJikL3cZzYGoxDSUyaC0Q6+vPkCAwEAAaA6MDgGCSqGSIb3DQEJDjErMCkwJwYDVR0RBCAwHoILdm9sdGFnZS5jb22CD3d3dy52b2x0YWdlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAwq2xUGsqnNBFzrSjLT0kBDqHZCzsVcwkcu30LmxXMg4WazlJOLBn6B0GxphuQIh8m9CwvMhxeYLKFFAYMOF/lrPspFXmkoh4HaCenP4U6GU0exMEukeo4Cn111OYmG1CRHPc0S+7BIQKQNhxH5NDMMvuJpxH/otJjxX7b96Q//g2sSdG742Q23FNbLFqBmFc1yNgRzpTlQbQL/EuHOuB2SRECyHwbjn8NZAV0HvPPfGvyN++my5ytH0eBxFKHS91b0O1SAy+XBKQZ4TlD6uD/fs/fBXWaCZlz0eU4/gWgXZ9q/F4u1qHXUA/xx76EeX51NyHNpZE6j+U23RdNdqzXA==-----END CERTIFICATE REQUEST----- "
# Given Name from SMAX sys.argv[7]
#given_name = sys.argv[7]
given_name = "Antonio"
# Surname/last name from SMAX sys.argv[8]
#surname = sys.argv[8]
surname = "Macias"
# Email from SMAX sys.argv[9]
#email = sys.argv[9]
email = "John.Wardle@microfocus.com"
#external_cert_type = sys.argv[10] 
external_cert_type = "BasicOV_c"
if external_cert_type == "BasicOV_c":
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_basic'
elif external_cert_type == "BasicEV_c":
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_ev_basic'
else:
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex'
payload = {
    "certificate": {
        "common_name": common_name,
        "dns_names": 
            san1
        ,
        "csr": csr,
        "signature_hash": "sha256",
    },
    "comments": comments,
    "renewal_of_order_id":orderid,
    "skip_approval": "true",
    "auto_renew": 0,
    "organization": {
        "id": 153574,
            "contacts": [
            {
                "contact_type": "ev_approver",
                "user_id": 1522870
            },
            {
                "contact_type": "technical_contact",
                "first_name": given_name,
                "last_name": surname,
                "job_title": "Project Manager",
                "email": email
            }
        ]
    },
    "order_validity": {
      "days": 365
    },
    "payment_method": "balance"
}

payload_new = json.dumps(payload)
print(payload_new)

headers = {
    'X-DC-DEVKEY': api,
    'Content-Type': "application/json"
    }
response = requests.request("POST", url, data=payload_new, headers=headers)
print (response)
resp_dict = json.loads(response.text)
#print(str(resp_dict["id"])+"is the certificate id")
#print(str(resp_dict['id'])+"is the certificate id")
print(response.status_code)