import requests
import json
import sys
from requests.exceptions import HTTPError
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
#api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
# Test Vishak account
api = 'B6IZH3C7KT367TMA54DDNFTABHHTIGJBP5MOXT3UL6OXWXROB6FP4QMZNRK4HW4KBDTKPGAQJ4WBMRHMR'
#api = apiprod

#url = "https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex"

#email = sys.argv[1]
email = "vishak.m@microfocus.com"
#common_name = sys.argv[2]
common_name = "gdc-coffee-shop-laurel.microfocus.com"
externalcsr = '-----BEGIN CERTIFICATE REQUEST-----MIIDVDCCAjwCAQAwgasxCzAJBgNVBAYTAklOMRowGAYDVQQIDBFLYXJuYXRha2EgKEluZGlhKTESMBAGA1UEBwwJYmFuZ2Fsb3JlMRQwEgYDVQQKDAtNaWNybyBmb2N1czEuMCwGA1UEAwwlZ2RjLWNvZmZlZS1zaG9wLWxhdXJlbC5taWNyb2ZvY3VzLmNvbTEmMCQGCSqGSIb3DQEJARYXdmlzaGFrLm1AbWljcm9mb2N1cy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQClPS2mtMwCq76Cnt5iKV05vOk3s2YDnurMMqGLKyF1BGMDEpqBnZPYJHdxz/GEOIMJJXOrO+hiGz2582RCHurW9dgvXNE3kCuA0jo7n3loG/BmFs6ilkWKGUUcEQAHKAja/n9Nr9WWCUkj6lXq5aWtn1gmh6Paj313/n+Bl8y2SrxSFCwIixEqhrFglpQx0mN5vADPFyYK2nf4lv+cjly2hFPoDx/72rA5hELi6gLOyvdKTOkqWpyKm5I7wgIrdWGHa+iXKmzLcJ6AsK9j41hwFsll/zS5w2elwSHocuzp/SRSFBdKpYB0hlTQAqlSusSnFwokXIVevKptEYJaq+/5AgMBAAGgYzBhBgkqhkiG9w0BCQ4xVDBSMFAGA1UdEQRJMEeCFWxhdXJlbC5taWNyb2ZvY3VzLmNvbYIWbGF1cmVsMS5taWNyb2ZvY3VzLmNvbYIWbGF1cmVsMi5taWNyb2ZvY3VzLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAUrM1J0AaaZlyM0DuWzWvb8xTggxECoG2k7zmoJ6R0A71T8YNTgiA5y5A6kUTEeOUwFaH3pV8ozoaqhLPBER7FkgROr6jgbC0mjOxy/e4C56eZQpqOVS7HVLTczJVCUL5uDn8R/iAsIxdX2HVR1Bot61sSWubOBsNFApzdMtRZonsZLp28A+4eYV9jXMTsuse0k9CRLIG2JYCVp8J9h6tjaEUFwipybEjTbFnKdMuVoIfH8wzKV6nsxdfqBsFgwn8InxnLkkuC6mGz3PeGC65iAKEy5SQV0ayGpncFobtzz0aRZIu28Qu2hy9l+6xviSz4+3LQt7yTRYItl4CQXssvQ==-----END CERTIFICATE REQUEST-----'
#externalcsr = sys.argv[3]
#externalcsr = "-----BEGIN CERTIFICATE REQUEST-----MIIEIjCCAwoCAQAwgZ8xCzAJBgNVBAYTAkdCMRIwEAYDVQQIDAlCZXJrc2hpcmUxEDAOBgNVBAcMB05ld2J1cnkxJjAkBgNVBAoMHU1pY3JvIEZvY3VzIEludGVybmF0aW9uYWwgcGxjMRgwFgYDVQQLDA9PbmxpbmUgQnVzaW5lc3MxKDAmBgNVBAMMH2NvbnRlbnQuc29mdHdhcmUubWljcm9mb2N1cy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDH41sDzzaUUo1FYRxVKz76ATnLH8Vyq5PLTKBY4SxvvVv1O4ntJmP5t8pPyPch4Os5WMzJ/oLCYxhj+8FTVHUgBmZIoXIxtbFJi15W/TQ0Rx6F2CVqZ8j3hU28ykoq9l6egQsAW68DNbinrTRB8S2SgAzDLCmf0pOK6m0TkZPRZpK+W/fuxuBX1v5ChzSzvEwMAxICIMPWW2QVBm6bCjREd4tp5NmtVZiGlg1NJ6NUp6fV12oQGL+azYOHGU12MPM13gM/tp0sZc10xaKKI9e99xPHC1TgTxUG6FEGPm3WOidPMO7dGKmRdp1zaQgCn+oK22XJHozuGjEHvbCjB7KlAgMBAAGgggE7MIIBNwYJKoZIhvcNAQkOMYIBKDCCASQwCwYDVR0PBAQDAgQwMBMGA1UdJQQMMAoGCCsGAQUFBwMBMIH/BgNVHREEgfcwgfSCIWRhc2hib2FyZC5zb2Z0d2FyZS5taWNyb2ZvY3VzLmNvbYIgYnVpbGQtbWYuc29mdHdhcmUubWljcm9mb2N1cy5jb22CIHJlZ2lzdHJ5LnNvZnR3YXJlLm1pY3JvZm9jdXMuY29tgiFhcnRpZmFjdHMuc29mdHdhcmUubWljcm9mb2N1cy5jb22CH2NvbnRlbnQuc29mdHdhcmUubWljcm9mb2N1cy5jb22CI2Ntcy1zZXJ2aWNlLnNvZnR3YXJlLm1pY3JvZm9jdXMuY29tgiJ1aS1zZXJ2aWNlLnNvZnR3YXJlLm1pY3JvZm9jdXMuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQATJAzM+jklHsoDk4YLmA1/3GsJVuG8i3AYrhAla87qDZ7pNI7/zGi9f3SG26og58kqc5zFTG/8E/MRn/XzdEh7QzCjNu4j6ccXLOWlMNii3WGXbimiB8A23mXl4jGDkgvq5R3/uaOZykxvWG+CeamDJsqp8UzlFxmcLPI9K9UjxqalucNylIjVSThI16ytmN6BCZNS/2R9XIxpY5lVPdD2NKT/BjmGlsBXnH8hSoriquwoeoerwEnA7DrIou0aOcEHyWSr5KbpLdP8J5k2o/uPCiIXiWBl2hUCFjb7lF8+37HhGDMvElqUNw3vMKiSC28L+iQgu9Jkpxjq+8hxAd+b-----END CERTIFICATE REQUEST-----"
#given_name = sys.argv[4]
given_name = "Vishak"
#surname = sys.argv[5]
surname = "M"
name = given_name+' '+surname
#san1 = sys.argv[1]
san1 ='laurel.microfocus.com, laurel1.microfocus.com, laurel2.microfocus.com'
#san1= "dashboard.software.microfocus.com","build-mf.software.microfocus.com","registry.software.microfocus.com","artifacts.software.microfocus.com","content.software.microfocus.com","cms-service.software.microfocus.com","ui-service.software.microfocus.com"
if san1 == '' or san1 == " ":
     san1 = common_name
else:
    san1 = san1.split(',')
     #print(san1)
#smaxid = sys.argv[7]
smaxid = "79523344"
comment = ""
comments = "SMAX Ref:"+smaxid+' - '+comment
#External_Cert_Type = "dev"
#external_cert_type = sys.argv[9]
external_cert_type = "BasicOV_c"
#external_cert_type = "Basic OV" 
if external_cert_type == "BasicOV_c":
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_basic'
elif external_cert_type == "BasicEV_c":
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_ev_basic'
else:
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex'

payload = {
    "certificate": {
        "common_name": common_name,
        "dns_names": san1,
        "csr": externalcsr,
        "signature_hash": "sha256",
    },
    "comments": comments,
    "skip_approval": "true",
    "auto_renew": 0,
    "organization": {
        "id": 1719333,
            "contacts": [
             {
                "contact_type": "ev_approver",
                "user_id": 2582963 
            },
            {
                "contact_type": "technical_contact",
                "first_name": given_name,
                "last_name": surname,
                "email": email
            }
        ]
    },
    "order_validity": {
      "days": 5
    },
    "payment_method": "balance"
}
try:
    payload_new = json.dumps(payload)
    #print(payload_new)
    headers = {
        'X-DC-DEVKEY': api,
        'Content-Type': "application/json"
     }
    #print ("Headers are : " ,headers)

    response = requests.request("POST", url, data=payload_new, headers=headers)
    #print (response)
    #res = response.text
    #print(res)
    resp_dict = json.loads(response.text)
    status_code = response.status_code
    response.raise_for_status()
except HTTPError as http_err:
    print(status_code)
    print(resp_dict)

except Exception as err:
    print(f'Other error occurred: {err}') 
    print(status_code)
else:
     print(str(resp_dict["id"]) + " is the certificate Id")
     print (status_code)
