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
smaxid = "5896553"
# Comment from SMAX sys.argv[3]
comment = "renewcerts"
comments = "SMAX Ref:"+smaxid+' - '+comment
# Common Name from SMAX sys.argv[4]
#common_name = sys.argv[4]
common_name = "www.cyberres.com"
# SAN from SMAX sys.argv[5]
#san1 = sys.argv[5]
san1 = "cyberres.com","cyberresilient.com","www.cyberresilient.com"
if san1 == '':
    san1 = common_name
# CSR from SMAX
#csr = 'MIIC+TCCAeECAQAwgYYxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEcMBoGA1UEAxMTd3d3LmVhc3RiYXljYWZlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALwSgqfTpy755SLql+QGnQk67CS510Q+wP8i2w40ncnLHJODaE8zFzw/xyJpItPZYn3Mub9rPbu7H0miDYvVjfikJM1SWQOm1MxEGyEtk17skaedg/y4+XN0335HMNVwfISX25HX4Y6d3cXv/0Kg655utWm4f2gkHG/G0P4RcyBD0f/wOHeNNvQsS48tFJrgotCBQmt7HhY4UkuNXk/xP91pl0eu5O/Yh0SlbShBECL3YgyfYmfwDI338XVdauZbmwgsu1Tq1xrKLN8uSp3C7v9enkNYJXNY55X++pmO+eBpgxOYe9NWsxVeIgQwzTttmJIm0qd9O7cOyQY+9VQ5jCUCAwEAAaAtMCsGCSqGSIb3DQEJDjEeMBwwGgYDVR0RBBMwEYIPZWFzdGJheWNhZmUuY29tMA0GCSqGSIb3DQEBBQUAA4IBAQBywTb6qgPEVMicKAkY5lt+30beWZuSCzl3FUIqMf7fZHrczGD7K24OSDt8zuomgX4JU+18RkCv9V0u2oq8igwWRiLWUkZHYLs1BMl8Hl0sToRItg98h0BRpPztUCm9Dc4ZKvHuoRDLHOhPTV5U22db820oWQPGPfFXa/M+zU/kGmAZhHpIB+1ZKg+SX71bBSkBkyrbNkwW+VgX2dksUDFHuVC8u/nOhOXDuhKOCPiMeq19KJyclhz89E5mzbs2n9KYe7XuTTbpXbXYOo9XtRr6TgsWuh3QXCYn7ZfqtYx7ZU67iXWnSU+0gASsgVtsyOQYn8HmIqvaolIje4sEI79L'
#csr = sys.argv[6]
csr = "-----BEGIN NEW CERTIFICATE REQUEST-----MIICuzCCAaMCAQAwdjEZMBcGA1UEAxMQd3d3LmN5YmVycmVzLmNvbTEmMCQGA1UEChMdTWljcm8gRm9jdXMgSW50ZXJuYXRpb25hbCBwbGMxEDAOBgNVBAcTB05ld2J1cnkxEjAQBgNVBAgTCUJlcmtzaGlyZTELMAkGA1UEBhMCR0IwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDSoICXzcuvqH9PM/m2pDU6l1eKzwtC23WnJfddHYVZzqQwalLwql8o2a08JBI9B5BL7u9S6qIpMjUJOeSJZtCcJZB/Sm75mYWva9cBSTjZHDvL/6HbjokpHlGs/vjaS1IOorJ6wdGZf5vdtBuSzicfgbd3e+GYiy8IFj6E+NSEWFiebE3OST3Hvu1DA64toSWvO7K8Eu5RjQKwdnAvU5nYIWe3U3W61jIOiiVAbaFWSqkSh4adPlgVrsH6F3mOjU1kSTbUGHTi5TOD3gTW8YawnW+pqqCxr4xs4X0Is9HdM8mCYoc3n9alQZTtBFuhtfxgEKjCfgLuflATtTSO+4fPAgMBAAGgADANBgkqhkiG9w0BAQsFAAOCAQEAAfYbOrPTY+Q0R3ltLJKVE2nTXEdLtDhPEG3jWf3ORNvJbM/7yxZtzfEQ1u7cXwxe5Rbth26+O3DjJglbCg4dQUBp403yqYuCKAuX5DWG2Mn5nQjvmz3CJGzdfTF/zYpPOgQDiAOE7qFuREfvC3Oxn8Tpw8fXt+ORHWZnqks0U9To0fiN3UHbv9sNQwVovVlK3vge5akuvpaGRlOpBipM271KPAxDwlS/duUM+N/is/ThzOv9+RRx25yaDA1WKR6mici8CN4lK2AbUv+bs6Y6pJUib9h/9r19RYB5ZKyPrDNbr0IJXl6Tle5fI8oZ7ZLoq4WkzbRjZqw4UXHqLRC30A==-----END NEW CERTIFICATE REQUEST-----"
# Given Name from SMAX sys.argv[7]
#given_name = sys.argv[7]
given_name = "john"
# Surname/last name from SMAX sys.argv[8]
#surname = sys.argv[8]
surname = "Wardle"
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
        "dns_names": [
            san1
        ],
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
resp_dict = json.loads(response.text)
#print(str(resp_dict["id"])+"is the certificate id")
#print(str(resp_dict['id'])+"is the certificate id")
print(response.status_code)
