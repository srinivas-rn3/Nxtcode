import requests
import json
import sys
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
#api = apiprod

#url = "https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex"

#email = sys.argv[1]
email = "anand.david@microfocus.com"
#common_name = sys.argv[2]
common_name = "mfidmz-houston-adgc.houston.softwaregrp.com"
#externalcsr = 'MIIDDTCCAfUCAQAwgYoxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEgMB4GA1UEAxMXc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRBsaGEktC/9ruokg8LcBihNOS1/aOpnWEUtQ946wsDlvDO86ClrhUurOE6EDbRTcqEPlAmFOYjqBcEJBeZ1VzH/6xdvcDcNfACLbXCk6i2/sjfodXMAs24UEmuFGFj5XOdl5mc5Fcpztfumg0Ck0aTsuAOSrx8GxN8/DrGKAsiVTTX/NLI3OuagsLOCmhUhcKEhh9cI1E1WQxzwMQcCXhVb5V4e+UeAbcw9wWPpR6DsVP76stEfKzmXkIqWpgRCxr63Z4LhxWXiXI+7XezhEBsdfGgXYUBnDdQsmLVq5+gAsDN3YM7HiKusEe4/5vK8Rl2CsnJpYis/MGwaf3nJlpAgMBAAGgPTA7BgkqhkiG9w0BCQ4xLjAsMCoGA1UdEQQjMCGCH2h0dHBzOi8vc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wDQYJKoZIhvcNAQEFBQADggEBALFzHY0Ruu0PBEyQIKH72Ze2YED1Hts2kbspraZBRxh6zPe32/O4WdP5o3155jKNTl/YqREbC9x+zFbVYWHpwdagXpWmcTkjlEU8p0/faL3Qyl3QTQ3UNRGFR05OAI6Qqwq14VkLwcUmowMcnTtMeL1Iig/jY4UcNv6Ruc74fTiY39ZuhuISVqwlmFOV/qW6MjP1xt/YYaZlObNaBoKYP80JxsE3IUK3J/7yfA2SOzj5zGeH2oetn/7SSev7ol9aIFOvvBmi88AyllJYyvqpisQbAi6Fy5rlvyqVpYZHGzDjtqhPntB41UvLcQ+xB+XRYCU0VHMYb83cBEip52vdGcE='
#externalcsr = sys.argv[3]
externalcsr = "-----BEGIN NEW CERTIFICATE REQUEST-----MIIDmTCCAoECAQAwazELMAkGA1UEBhMCVVMxETAPBgNVBAsTCFNlY3VyaXR5MRMwEQYDVQQKEwpNaWNyb2ZvY3VzMTQwMgYDVQQDEyttZmlkbXotaG91c3Rvbi1hZGdjLmhvdXN0b24uc29mdHdhcmVncnAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuT6i7x9ydOQ8Qa22Bq8iA6pMZ6nWeSzVmuSh4LWzFLQKVKPl/vQLPKHflkLn5rQf+RPO/uoj0ZoxDerJwJCBD++XsAaBqum6FsDEd78m1Lt6azbb1fadym3kTefdRdOuNpokcqZyjg+bZLi/XXFy4JAsQLc4r9QxNoBmX7Aqv7U+PMNo8RseWOGub0KHjCN2JRVEOvFPx383ikIz33t2YYuUGACF6y7f4zL0T8Or/W48aarKN9/69zTuvRMZd64HJsLMIbq5cQ1DAkQeNGrQkfSoBxn5slXTmzMacleJPB0wTY9lHB/gZfE+TrZO095tnefnRcQr92qst+8QynADXQIDAQABoIHoMIHlBgkqhkiG9w0BCQ4xgdcwgdQwgdEGA1UdEQSByTCBxoIgbTR3MDMzMGcuaG91c3Rvbi5zb2Z0d2FyZWdycC5jb22CE200dzAzMzBnLm1maWRtei5uZXSCIG00dzAzMjlnLmhvdXN0b24uc29mdHdhcmVncnAuY29tghNtNHcwMzI5Zy5tZmlkbXoubmV0giltZmlkbXotaG91c3Rvbi1hZC5ob3VzdG9uLnNvZnR3YXJlZ3JwLmNvbYIrbWZpZG16LWhvdXN0b24tYWRnYy5ob3VzdG9uLnNvZnR3YXJlZ3JwLmNvbTANBgkqhkiG9w0BAQUFAAOCAQEAUnPy5g1o6aaIQ3C6p/ccmbxX1rF8AQgpJRLl/LGfbzFPWF+SZowbdWfwBoIHZ5G6ccpsJySxNv1rqmZ/S9eFlF0PcZicvh5vzGS49U80STs/KOo5nH0t6GK6zgaGGTPu/o5AsudgayBCDjXHpsEKFy/Nyt7rn/ud43Fk06egsQXXmfyIs5w9y8/6yAzAoOhG1S/9T1yXrEmkvccZJp1OhXyiUNNql9SO5ujAFCDVRqOeLo+d/78TaZv5Pny6IV1xtEJrpsJPuLNbBeCfEyIigL4hvptISLdshoWvxTR90+xo0Jxo/8GBllEV3Hb+NEfMCivj+Xfbw9Nz49QwLkGEgQ==-----END NEW CERTIFICATE REQUEST-----"
#given_name = sys.argv[4]
given_name = "Anand"
#surname = sys.argv[5]
surname = "David"
name = given_name+' '+surname
#san1 = sys.argv[6]
san1= "mfidmz-houston-adgc.houston.softwaregrp.com","mfidmz-houston-adgc.houston.softwaregrp.com","mfidmz-houston-ad.houston.softwaregrp.com","m4w0329g.mfidmz.net","m4w0329g.houston.softwaregrp.com","m4w0330g.mfidmz.net","m4w0330g.houston.softwaregrp.com"
if san1 == '':
    san1 = common_name
#smaxid = sys.argv[7]
smaxid = "6503320"
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

response = requests.request("POST", url, data=payload_new, headers=headers)
print (response)
#res = response.text
#print(res)
resp_dict = json.loads(response.text)
#print (resp_dict)
print(str(resp_dict["id"]) + "is the certificate id")
print(response.status_code)
