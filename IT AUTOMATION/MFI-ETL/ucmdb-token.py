import requests
import json
#creation of the ucmdb token
def ucmdb_token():
    url = "https://cms.us2-smax.saas.microfocus.com/ucmdb-server/rest-api/authenticate"

    payload = json.dumps({
    "username": "mfit_prod_vertica_intuser",
    "password": "6@f4xKYe9P",
    "repository": "UCMDB",
    "clientContext": 973580388
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    #token = response.json()
    response_json = response.text
    response_json1 = json.loads(response_json)
    ucmdb_token = response_json1['token']
    print(ucmdb_token)
ucmdb_token()
