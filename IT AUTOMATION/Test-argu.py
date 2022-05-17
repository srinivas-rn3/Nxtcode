
import requests
import json
import sys

global common_name
common_name = sys.argv[1]
san1 = sys.argv[2].split(',')
#san1 = "san1.com","san2.com","san3.com"
csr = sys.argv[3]
if san1 == '':
    san1 = common_name
    print(common_name)
    payload={
  "common_name": common_name,
  "dns_value": common_name
 }
    payload_new = json.dumps(payload)
    print(payload_new)
else:
    print(san1)
    payload={
  "common_name": common_name,
  "dns_value": san1,
  "csr": csr
 }
    payload_new = json.dumps(payload)
    print(payload_new)
'''
"""
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
orderid = "131445239"
#url=securesiteov
# SMAX ID sys.argv[2]
#smaxid = sys.argv[2]
smaxid = "6745570"
# Comment from SMAX sys.argv[3]
comment = "renewcerts"
comments = "SMAX Ref:"+smaxid+' - '+comment
# Common Name from SMAX sys.argv[4]
#common_name = sys.argv[4]
common_name = "not-euw.cmx.connected.com"
# SAN from SMAX sys.argv[5]
#san1 = sys.argv[5]
san1 = "not001-euw.cmx.connected.com","not002-euw.cmx.connected.com","not003-euw.cmx.connected.com","not004-euw.cmx.connected.com","not005-euw.cmx.connected.com","not006-euw.cmx.connected.com","not007-euw.cmx.connected.com","not008-euw.cmx.connected.com","not009-euw.cmx.connected.com","cmxnot-uk.connected.com"
#san1 = ''
if san1 == '':
    san1 = common_name
# CSR from SMAX
#csr = 'MIIC+TCCAeECAQAwgYYxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEcMBoGA1UEAxMTd3d3LmVhc3RiYXljYWZlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALwSgqfTpy755SLql+QGnQk67CS510Q+wP8i2w40ncnLHJODaE8zFzw/xyJpItPZYn3Mub9rPbu7H0miDYvVjfikJM1SWQOm1MxEGyEtk17skaedg/y4+XN0335HMNVwfISX25HX4Y6d3cXv/0Kg655utWm4f2gkHG/G0P4RcyBD0f/wOHeNNvQsS48tFJrgotCBQmt7HhY4UkuNXk/xP91pl0eu5O/Yh0SlbShBECL3YgyfYmfwDI338XVdauZbmwgsu1Tq1xrKLN8uSp3C7v9enkNYJXNY55X++pmO+eBpgxOYe9NWsxVeIgQwzTttmJIm0qd9O7cOyQY+9VQ5jCUCAwEAAaAtMCsGCSqGSIb3DQEJDjEeMBwwGgYDVR0RBBMwEYIPZWFzdGJheWNhZmUuY29tMA0GCSqGSIb3DQEBBQUAA4IBAQBywTb6qgPEVMicKAkY5lt+30beWZuSCzl3FUIqMf7fZHrczGD7K24OSDt8zuomgX4JU+18RkCv9V0u2oq8igwWRiLWUkZHYLs1BMl8Hl0sToRItg98h0BRpPztUCm9Dc4ZKvHuoRDLHOhPTV5U22db820oWQPGPfFXa/M+zU/kGmAZhHpIB+1ZKg+SX71bBSkBkyrbNkwW+VgX2dksUDFHuVC8u/nOhOXDuhKOCPiMeq19KJyclhz89E5mzbs2n9KYe7XuTTbpXbXYOo9XtRr6TgsWuh3QXCYn7ZfqtYx7ZU67iXWnSU+0gASsgVtsyOQYn8HmIqvaolIje4sEI79L'
#csr = sys.argv[6]
csr ="-----BEGIN NEW CERTIFICATE REQUEST-----MIID+zCCAuMCAQAwZTELMAkGA1UEBhMCR0IxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UECxMDQzEwMRMwEQYDVQQKEwpNaWNyb2ZvY3VzMSIwIAYDVQQDExlub3QtZXV3LmNteC5jb25uZWN0ZWQuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq99DuYhT9K/+MqCbDrJ9c5iHly6Bdrt/LTf7OIm27l5y9j15vHqkrB23yjHf5U4sCzb8puC9w6lXPMomHwXBEjii+hokYU2wgSEUxikbVNLDxIBQ0Tq35MtjqFFHFMPe9eqjdcS+WLKnE3b3CR6InuQYA4ZQ+v/a4SAQsf/2o0cryqw28HM1wsx/YR9h86P1XSLLts0XXSdVWUmjK2vGnW32xf9ndh8W1z0dvEjmVkkN7BIzS9JJYhJ60+JL7F/rLc4XuNtaWFV/c+EKf8/Eij9hQAhW4BG3ADw1t/3MtOx1eLsWqUkXC4gCTl4gTk+TZMiaZc26NH1O3By6SDB3xQIDAQABoIIBTzCCAUsGCSqGSIb3DQEJDjGCATwwggE4MIIBNAYDVR0RBIIBKzCCASeCHG5vdDAwMS1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwMi1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwMy1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwNC1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwNS1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwNi1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwNy1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwOC1ldXcuY214LmNvbm5lY3RlZC5jb22CHG5vdDAwOS1ldXcuY214LmNvbm5lY3RlZC5jb22CF2NteG5vdC11ay5jb25uZWN0ZWQuY29tMA0GCSqGSIb3DQEBBQUAA4IBAQAcWcWBo/D7+SgREFkK19TWltgJC4r0KNhlyGRt/JyRKsQYncTjTKewbgB8NLiEhJmGN0/LdXEplOFNBuEriXmZ4ZoXe23ugzx0YJ2B+m91Dtna5K8iDv28/qoOsyvwyB0v0vqAM5NUMtIJ0UlTyjiOD9R7EinYO1seHe24HuD9FTfK9wkfPfwqiChePyZbjjgVIxfTr4AqXfir0M2XA8eJIYO0sdnN5JQmdTGKS6aR6r487PyF0lREt//WN8LSMl5JAAIgKsCQdx2aWkY5dl6r6GaYbOiyWhoG2leEXFlTD+MT9FlybrxC7i/d37ZSUOst370oDgTvjgjfMBLcYayO-----END NEW CERTIFICATE REQUEST----- "
# Given Name from SMAX sys.argv[7]
#given_name = sys.argv[7]
given_name = "DILIP"
# Surname/last name from SMAX sys.argv[8]
#surname = sys.argv[8]
surname = "BEHERA"
# Email from SMAX sys.argv[9]
#email = sys.argv[9]
email = "DILIP.BEHERA@microfocus.com"
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
            san1,
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
"""
"""
import requests
import json
import sys

global common_name
common_name = sys.argv[1]
san1 = sys.argv[2]

print (san1)
'''
'''
#san1 = "san1.com","san2.com","san3.com"
csr = sys.argv[3]
if san1 == '':
    san1 = common_name
    print(common_name)
    payload={
  "common_name": common_name,
  "dns_value": common_name
 }
    payload_new = json.dumps(payload)
    print(payload_new)
else:
    print(san1)
    payload={
  "common_name": common_name,
  "dns_value": san1,
  "csr": csr
 }
    payload_new = json.dumps(payload)
    print(payload_new)
"""
'''