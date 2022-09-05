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
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfc2FsdCI6InBvc3RncmVzcWxfY21zX3VjbWRiX2RiIiwiZXhwIjoxNjYyMzk2MDY5LCJyZXBvc2l0b3J5IjoiVUNNREIiLCJjdXN0b21lciI6OTczNTgwMzg4LCJ1c2VybmFtZSI6Im1maXRfcHJvZF92ZXJ0aWNhX2ludHVzZXIifQ.csK3JgEQ1DYPWtAq8--HFAstRqEaZQvBvN9jdTrSvTY'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)

        status = response.status_code
        if status == 200:
            print("OK!")
            print("status code :" ,status)
        else :
            print("Boo!!!")
            print("status code :" ,status)
        file = open(final_output, "wb")
        file.write(response.content)
        file.close()
    except requests.exceptions.RequestException as e:
        print(e)
ucmdb_tql("Node_InstalledSoftware_EUC_adobe")