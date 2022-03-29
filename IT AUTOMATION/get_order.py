import requests
import json
import sys

global common_name
#api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
# prod api
api22 = '017d1f0298ca0b9c02_89F736A27B08E31A6919E8DC72F54DC69F5B53C6D0B0E7690564A50D6A4D976A'
certurl = 'https://pki-ws-rest.symauth.com/mpki/api/v1/certificate'
# Email retrived from SMAX
#email = sys.argv[1]
email = "sivakumar.av@microfocus.com"
# Common Name retrived from SMAX
#common_name = sys.argv[2]
common_name = "megam.swinfra.net"
#common_name = "mc4w01851.itcs.softwaregrp.net"
sid = common_name
#country = "GB"
#locality = "Berkshire"
#organisationname = "Micro Focus International plc"
#department = "IT"
#csr = 'MIIDDTCCAfUCAQAwgZExCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEnMCUGA1UEAxMebWM0dzAxODUxLml0Y3Muc29mdHdhcmVncnAubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvATAqwt/IaU+UKZCHbGy2RZ15keGktP83YlEN5uupqh2SMeF0LqRcGZXsEbTIeM/fS44GEk/BdNYaucY0jEA39JTERWWpyzjPJL968+mPSNwg7YEcUtwWKTUgbxaDpEyuc8KfT/+g70yCryAfAJnx4G24izyiAZWQMoQ10uMs4QyT1oL6TFF0bGj0rAXsoQhQ1MpKOvx/DTUavnloXILLMBTk3OR7lqWmB+JB8EA3kQsKb31LrBxhHY2c4CTJ0bvdwmdkCttyvMHwWnJad4Fa60VDpj6X6gnFueLUHmEg7aMVASrF+4TtiRVgnzYtwofvrM6wUqfs5A7SoCrsGWX5QIDAQABoDYwNAYJKoZIhvcNAQkOMScwJTAjBgNVHREEHDAaghhtYzR3MDE4NTEubWljcm9mb2N1cy5jb20wDQYJKoZIhvcNAQEFBQADggEBAF/kOIR1wxN2qlrf0+owUVGdl0fDfA/pXeFh80BfQpfZkAZI4vbAr2pztxG5xoBO1/sWuEdIr5QyM06EXwn8AM+z+DuibyyHTocFnvqWeM8wqkFo6pMwc/5OHFuUAJKX8QpqeYQKhCLh0BdxOIbZTCTAst7LMQjgPGRdTAkZqI2Vjk3n99LlhEf/K8GmhH2j3xfwITlEDoMcLAlu6chfp5D2afFIpF3m/IiRPO4GSaUKpM6XqgpbWtQKSUTZ0fZ6PbbyefqOnf703IRFlbhZ8xm+XRX7I6QWUEYEEyEMx4rrHi6KLUcAHKxkfwiEjgGk7FRLmxSsoNGwl4hrPSCd73c='
# CSR retrived from SMAX
#csr = sys.argv[3]
csr = "MIIFLDCCAxQCAQAwdjELMAkGA1UEBhMCSU4xEzARBgNVBAgTCkthcmFuYXRha2ExEjAQBgNVBAcTCUJhbmdhbG9yZTENMAsGA1UECxMESVRPTTETMBEGA1UEChMKTWljcm9mb2N1czEaMBgGA1UEAxMRbWVnYW0uc3dpbmZyYS5uZXQwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC81r30u4QzIs+85kNLwEdTypaozdlJvIv0obd0YgHEz/oGEbnYkmmifD2sO4WWD2AmGI9jCaAAYcFMTfhWltz5crR+MzX/9Me0qVzFB8Oty+oTTUgxtQGjrGa9NjY+O4B1AYjGD2Me8a1A4BLQydsIkMRkYvWkDH+MeI3NynAZKWJSwjkxjcro+1Aono1wgcXrm5c1EBkgi8XWhfRUx+Ekx3mU2shXuucUI0EK5Je/srqxg7rbGmlEL3+rTLcYukYWpxqjvtsIxWq6XrbbNnRG6eRUizBt73bGrWfPvYQexe1QJD2YFuwdEWAswYbxU6pM+qSYD+rrA/hk8aH38LTefd7yMXoWs9UGjIZuGw722j0UoB2EDtyeWYSv2QvNgUuhMUk/eYtIzVWBHEVMDDPHp+nrrwEHUbh1xmE18xzcC/UNU0MmNWqTtUXlvUZ7pJroHHWHlDEInCiCusH7BdZpwPfFGkEvN6/95aGwGjpPWpxF8GheBR/d2N/XHMl/jigj2PdyfxaEj1nU6hjhxhlOghKa9ra/d/5wVBpMTYZbTAX+s55HV6AXPymL4V7BMD3W4cQHwLLN3uYYxZjiEUsqS+5UxVi5J2Y0bUKvGCs0Qvws64UEbaCR8Oj7y1a0L3Eu/RiUdBaK9I3ne1dgI9YDMRst2RUN6BtvZKD7RxgDcQIDAQABoHEwbwYJKoZIhvcNAQkOMWIwYDBeBgNVHREEVzBVghFtZWdhbS5zd2luZnJhLm5ldIIUbWVnYW0tbTEuc3dpbmZyYS5uZXSCFG1lZ2FtLW0yLnN3aW5mcmEubmV0ghRtZWdhbS1tMy5zd2luZnJhLm5ldDANBgkqhkiG9w0BAQUFAAOCAgEAI7Y2QJvtpAVm7T+xL0RwUDUASlp/XHISlwOSSsv+vlG+ENhF10GWFgWzYh8qisWnW6s0ZHl/VXUa2Vl9IQVT3UmjfaSIwE7QMbzIy3oh2+RU+gXQrpqCPVeITqHyZchogC/j6D9ND7earYEj8IPyHP0eW04/dgT8LMGeSwoOV9cxGXUIVoOcqwYMWVm/9uSfmuZTMFr9VdUaekmlrIZIjGTLIQaeAmMluXuNxW1T6iN9DjcvkMDIHS+oSG792N/dLQQSVtzHFV8sodFoOcIOvyeYtE+at4WzA4LNJK4ZFdqsgPa0USsQVUOD9/C9Ym7sX1F1+rE7cFZegnlwxR4arR6NVwcuHeE6ZhBrZPI8W8HY+/oIJ75/3ppAEImojrRC+ltM72/pdgZKlMlZ4jm0yKU3XJs0cJr1R8aglyJkDAtmkX8CmeFQYpV6fB/Oyj9J32hqpW6VrE/GrC7ULk10W6EX24Uzkkg2mDAp8VTO1vLPabB8uLQgyx06gS5A82uSssao0SbOiTpxNfV1oU0L300mcmUZRpG7fOizH3R5zeUV0fLVYpXANxjksQ7pIhX0p5s7WXV/Nu0nU9MkaAvc5iBj9HUhxyymrtr/3k/6QZRKhSNl38YhNxKyHfDMrmJKOUIcWhJc6A+nLOhLpJTXT5Rfs9D6jqXXDs3rUkiiZgw=" 
#certificateoid = "2.16.840.1.113733.1.16.1.5.2.5.1.1279460975"
#certificateoid = '2.16.840.1.113733.1.16.1.5.3.5.1.1298715434'
# prod profile id 
certificateoid = '2.16.840.1.113733.1.16.1.5.3.1.1.483560546'
profilename =  "SSL"
#duration = "10"
#validityunit = "Days"
# Given Name retrived from SMAX
#given_name = sys.argv[4]
given_name = "sivakumar"
# Surname retrived from SMAX
#surname = sys.argv[5]
surname = "A V"
# SAN1 retrived from SMAX
#san1 = sys.argv[6]
san1  = "megam.swinfra.net,megam-m1.swinfra.net,megam-m2.swinfra.net,megam-m3.swinfra.net"
#if san1 == '':
#  san1 = common_name
#SMAX ID retrieved from SMAX
#smaxid = sys.argv[7]
smaxid = "6084798"
#comments retrieved from SMAX
#comment = sys.argv[8]
comment = ""
comments = "SMAX Ref:"+smaxid+' - '+comment
#adding manager
#manager = sys.argv[9]
manager = "smomtaj@dxc.com"
#san1 = "mc4w01851.microfocus.com"
payload ={
  "attributes": {
    "common_name": common_name,
    "dnsName":common_name,
    "given_name":given_name,
    "surname":surname,
    "custom_encode_dnsName":common_name,
    "custom_encode_dnsName_multi":san1
    },
    "email": email,
  "csr": csr,
  "profile": {
    "id": certificateoid,
    "name": profilename
  },
  "seat": {
    "email": email,
    "seat_id": common_name,
    "seat_name": common_name
  },
  "authentication" : {
    "auth_comments" : comment,
    "auth_first_name": given_name,
    "auth_last_name": surname,
    "auth_custom_attr_15419815760502719": manager
   },
}

payload_new = json.dumps(payload)
#print(payload_new)
headers = {
    'X-API-Key': api22,
    'Content-Type': "application/json"
    }

resp = requests.post(certurl, data=payload_new, headers=headers)
print(resp.text)
print(resp.status_code)