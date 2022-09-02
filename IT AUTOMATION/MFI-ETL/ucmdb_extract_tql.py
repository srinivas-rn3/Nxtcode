import requests
import json
def ucmdb_tql(tql):
    url = "https://cms.us2-smax.saas.microfocus.com/rest-api/topology?chunkSize=100000"

    output_file ="C://Users//rnsri//Software-ucmdb//SEP1//"
    #output_name = "Node_InstalledSoftware_EUC1"
    output_name = tql
    final_output = output_file+output_name + ".json"
    print(final_output)

    payload = json.dumps(tql)
    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfc2FsdCI6InBvc3RncmVzcWxfY21zX3VjbWRiX2RiIiwiZXhwIjoxNjYyMTA1MjgwLCJyZXBvc2l0b3J5IjoiVUNNREIiLCJjdXN0b21lciI6OTczNTgwMzg4LCJ1c2VybmFtZSI6Im1maXRfcHJvZF92ZXJ0aWNhX2ludHVzZXIifQ.qyyy_u2lHOkUhsINJ4TZ7osLWIUkamIK_ql5AjFE7Ts'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)

        #print(response.text)
        file = open(final_output, "wb")
        file.write(response.content)
        file.close()
    except requests.exceptions.RequestException as e:
        print(e)
ucmdb_tql("Node_InstalledSoftware_EUC2")