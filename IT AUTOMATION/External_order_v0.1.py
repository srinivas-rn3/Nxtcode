import requests
import json
import sys
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
#api = apiprod

#url = "https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex"

#email = sys.argv[1]
email = "Vishnu.Priyan@microfocus.com"
#common_name = sys.argv[2]
common_name = "content.software.microfocus.com"
#externalcsr = 'MIIDDTCCAfUCAQAwgYoxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEgMB4GA1UEAxMXc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRBsaGEktC/9ruokg8LcBihNOS1/aOpnWEUtQ946wsDlvDO86ClrhUurOE6EDbRTcqEPlAmFOYjqBcEJBeZ1VzH/6xdvcDcNfACLbXCk6i2/sjfodXMAs24UEmuFGFj5XOdl5mc5Fcpztfumg0Ck0aTsuAOSrx8GxN8/DrGKAsiVTTX/NLI3OuagsLOCmhUhcKEhh9cI1E1WQxzwMQcCXhVb5V4e+UeAbcw9wWPpR6DsVP76stEfKzmXkIqWpgRCxr63Z4LhxWXiXI+7XezhEBsdfGgXYUBnDdQsmLVq5+gAsDN3YM7HiKusEe4/5vK8Rl2CsnJpYis/MGwaf3nJlpAgMBAAGgPTA7BgkqhkiG9w0BCQ4xLjAsMCoGA1UdEQQjMCGCH2h0dHBzOi8vc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wDQYJKoZIhvcNAQEFBQADggEBALFzHY0Ruu0PBEyQIKH72Ze2YED1Hts2kbspraZBRxh6zPe32/O4WdP5o3155jKNTl/YqREbC9x+zFbVYWHpwdagXpWmcTkjlEU8p0/faL3Qyl3QTQ3UNRGFR05OAI6Qqwq14VkLwcUmowMcnTtMeL1Iig/jY4UcNv6Ruc74fTiY39ZuhuISVqwlmFOV/qW6MjP1xt/YYaZlObNaBoKYP80JxsE3IUK3J/7yfA2SOzj5zGeH2oetn/7SSev7ol9aIFOvvBmi88AyllJYyvqpisQbAi6Fy5rlvyqVpYZHGzDjtqhPntB41UvLcQ+xB+XRYCU0VHMYb83cBEip52vdGcE='
#externalcsr = sys.argv[3]
externalcsr = "-----BEGIN CERTIFICATE REQUEST-----MIIEIjCCAwoCAQAwgZ8xCzAJBgNVBAYTAkdCMRIwEAYDVQQIDAlCZXJrc2hpcmUxEDAOBgNVBAcMB05ld2J1cnkxJjAkBgNVBAoMHU1pY3JvIEZvY3VzIEludGVybmF0aW9uYWwgcGxjMRgwFgYDVQQLDA9PbmxpbmUgQnVzaW5lc3MxKDAmBgNVBAMMH2NvbnRlbnQuc29mdHdhcmUubWljcm9mb2N1cy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDH41sDzzaUUo1FYRxVKz76ATnLH8Vyq5PLTKBY4SxvvVv1O4ntJmP5t8pPyPch4Os5WMzJ/oLCYxhj+8FTVHUgBmZIoXIxtbFJi15W/TQ0Rx6F2CVqZ8j3hU28ykoq9l6egQsAW68DNbinrTRB8S2SgAzDLCmf0pOK6m0TkZPRZpK+W/fuxuBX1v5ChzSzvEwMAxICIMPWW2QVBm6bCjREd4tp5NmtVZiGlg1NJ6NUp6fV12oQGL+azYOHGU12MPM13gM/tp0sZc10xaKKI9e99xPHC1TgTxUG6FEGPm3WOidPMO7dGKmRdp1zaQgCn+oK22XJHozuGjEHvbCjB7KlAgMBAAGgggE7MIIBNwYJKoZIhvcNAQkOMYIBKDCCASQwCwYDVR0PBAQDAgQwMBMGA1UdJQQMMAoGCCsGAQUFBwMBMIH/BgNVHREEgfcwgfSCIWRhc2hib2FyZC5zb2Z0d2FyZS5taWNyb2ZvY3VzLmNvbYIgYnVpbGQtbWYuc29mdHdhcmUubWljcm9mb2N1cy5jb22CIHJlZ2lzdHJ5LnNvZnR3YXJlLm1pY3JvZm9jdXMuY29tgiFhcnRpZmFjdHMuc29mdHdhcmUubWljcm9mb2N1cy5jb22CH2NvbnRlbnQuc29mdHdhcmUubWljcm9mb2N1cy5jb22CI2Ntcy1zZXJ2aWNlLnNvZnR3YXJlLm1pY3JvZm9jdXMuY29tgiJ1aS1zZXJ2aWNlLnNvZnR3YXJlLm1pY3JvZm9jdXMuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQATJAzM+jklHsoDk4YLmA1/3GsJVuG8i3AYrhAla87qDZ7pNI7/zGi9f3SG26og58kqc5zFTG/8E/MRn/XzdEh7QzCjNu4j6ccXLOWlMNii3WGXbimiB8A23mXl4jGDkgvq5R3/uaOZykxvWG+CeamDJsqp8UzlFxmcLPI9K9UjxqalucNylIjVSThI16ytmN6BCZNS/2R9XIxpY5lVPdD2NKT/BjmGlsBXnH8hSoriquwoeoerwEnA7DrIou0aOcEHyWSr5KbpLdP8J5k2o/uPCiIXiWBl2hUCFjb7lF8+37HhGDMvElqUNw3vMKiSC28L+iQgu9Jkpxjq+8hxAd+b-----END CERTIFICATE REQUEST-----"
#given_name = sys.argv[4]
given_name = "Vishnu"
#surname = sys.argv[5]
surname = "Priyan"
name = given_name+' '+surname
san1 = sys.argv[1]
#san1= "dashboard.software.microfocus.com","build-mf.software.microfocus.com","registry.software.microfocus.com","artifacts.software.microfocus.com","content.software.microfocus.com","cms-service.software.microfocus.com","ui-service.software.microfocus.com"
if san1 == '' or san1 == " ":
     san1 = common_name
else:
     san1 = san1.split(',')
     #print(san1)
#smaxid = sys.argv[7]
smaxid = "7952334"
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
'''
response = requests.request("POST", url, data=payload_new, headers=headers)
print (response)
#res = response.text
#print(res)
resp_dict = json.loads(response.text)
#print (resp_dict)
print(str(resp_dict["id"]) + "is the certificate id")
print(response.status_code)
'''