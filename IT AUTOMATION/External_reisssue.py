import requests
import json
import sys
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
#api = apiuser
# Order ID from SMAX
#orderid = sys.argv[1]
orderid = '229828524'
reissueurl = 'https://www.digicert.com/services/v2/order/certificate/'
reissueurlpostfix = '/reissue'
url=reissueurl+orderid+reissueurlpostfix
# Comments from SMAX
#comments = sys.argv[2]
comments = "Urgent Request Please"
# Common Name from SMAX
#common_name = sys.argv[3]
common_name = "prvgwmob01.novell.com"
# SANs from SMAX
#san1 = sys.argv[4]
san1 = "mobility2.novell.com","mobility1.novell.com","mobility3.novell.com"
# CSR from SMAX
#csr = 'MIIDATCCAekCAQAwgYoxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEgMB4GA1UEAxMXc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDKbjDCIxwl8rx9dT45iSuaEU5wgmheruTda4DcZ7WIEpn/2XXiX77LbdYwj78h9F1yLb7Cd6rIi0DAZueosq86epXN/40ySsT3qbTZdFVoS/tGQh3Rl0GO/W6uqI9MaNCZuJTYJ4rRc02FqfDzau/eDq9mqsHdivtGAbyVxtyJ7FmfijOoa+Wu0/0zoBmBtP/SdjPyVmkl3mW0zaHQbFI5WVAjK6nleutnU9G8ZxIeRXinhZ8wn7vU08S2d52YVLlcfjR8L63ZPvJdh5N9pLRgllTj7vEpmpP8DRgdK7/LXvv1BZTxbqQVaJje6ywdeZ/v0+oUTWr82V3iyNFlg2fNAgMBAAGgMTAvBgkqhkiG9w0BCQ4xIjAgMB4GA1UdEQQXMBWCE3d3dy5lYXN0YmF5Y2FmZS5jb20wDQYJKoZIhvcNAQEFBQADggEBAC/Tqtx22wjiZi31ci/zLPFEFk8PaXJM1DzY6L0y8wNX8X4tHqPR7Ex0pbS6qHCbKZeQbddcHdnmj9hIR0DJ+rJ7X7ybUB3ACCNITnBodPPI5xeQ7L0LFv3orU3G9X1gcUhXggtPwrE6Q2uzEOxgUF4yL+HJkp7B1q2uAvLIfILiKvSw5Al37zhcvr7W+tCdCsheei/uM+/z6EdYZlAjUXCJufKewhiTpBGKaaqCKLCGvFQSh3mEdGQvXJPgTd+wysJCekSnhNdqIERgSuhDLV/X9OIJkCH4N3m+xYWeN/p+fG6k2CLt+hY4166rU2DJEkl04p4hnqPjzqfu8E3WWv0='
#csr = sys.argv[5]
csr = "-----BEGIN CERTIFICATE REQUEST-----MIIDLjCCAhYCAQAwgc0xCzAJBgNVBAYTAkdCMRIwEAYDVQQIDAlCZXJrc2hpcmUxEDAOBgNVBAcMB05ld2J1cnkxJjAkBgNVBAoMHU1pY3JvIEZvY3VzIEludGVybmF0aW9uYWwgcGxjMR8wHQYDVQQLDBZJbmZvcm1hdGlvbiBUZWNobm9sb2d5MR4wHAYDVQQDDBVwcnZnd21vYjAxLm5vdmVsbC5jb20xLzAtBgkqhkiG9w0BCQEWIGx1Y2lhbi5rbGVpbnZlbGR0QG1pY3JvZm9jdXMuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwdq5ze9x2Lno/LgykNxehSTc/PSta6Y9IsIYoP8CQesMmeStEGMZsoTAW6n41qcw7RCfm1/DMKeFgRR1UMK4Dg9GXtkLqEPx4mUrKh1V8rmInVE491thj6oq5MeB2SeSAk+6WQKdQ3+SesTm58jaf/yt7a/YRWW9rIQAFBZzDg/ozjF0Q5OHN2q5p07wmp/i16cAVuS04p7STj39rjq+UWnabTMyo2Men8ZWK3oXdHvU2CRhBjJ5uTxpG0GPYIHo1Dyn9eYvVo4BiyMZLkC5mSAWCaZ/YvPiP8DdHq4e1tvj3LxS28y0OOpSp6WGVj6SW7k+kYX8OMshs2goaW9wCwIDAQABoBswGQYJKoZIhvcNAQkHMQwMCkNhcGVUb3duMDEwDQYJKoZIhvcNAQELBQADggEBACp+THdWJuRtbnhwdqp3Qzyg81zJ4594qdHiSCUa+f9Xuv20vkjXitoPVOdb42RrCyykS0LIxqUSMzUTTRKR70Mp7PBQD09G3bELmNVybFMrWfvidF/bh5FESl/CoistJ1iz5b4oSbHVTf4HdKMFQ8LhxBUuhmzHZYd6XfLqvxkh9jH7MbKisBBvvOp1PJ6zhg0SX6EsO6BSFzHbq6vaxLKOeBdT72Z4mcVm7djYl/Bv6ayChWIiyKmckwqBRT9u3KvdWAtq5Dy3sTQcn1tApi2FRIZMdPeqlOlmnZjnEmHg3106C0t5jZrop4NCIriYJSgppoJN0Ot78VqkXX0YV5E=-----END CERTIFICATE REQUEST-----"
if san1 == '':
    san1 = common_name
payload = {
  "certificate": {
    "common_name": common_name,
    "dns_names": san1,
    "csr": csr,
    "server_platform": {
      "id": 2
    },
    "signature_hash": "sha256"
  },
     "skip_approval": "true",
     "order_validity": {
     "days": 365
    },
}
payload_new = json.dumps(payload)
#print(payload_new)
headers = {
    'X-DC-DEVKEY': api,
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload_new, headers=headers)
resp_dict = json.loads(response.text)
print(str(resp_dict["id"])+"is the certificate id")
print(response.status_code)