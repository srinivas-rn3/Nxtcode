import json 
try:
    with open(r'C:\Users\srini\git\Nxtcode\IT AUTOMATION\.vscode\Mylyn\project2.0\PythonProjects\requestsAPI\sample_AWS_S3_Event.json','r') as jd:
        json_data = json.load(jd)
    print(json_data)
    bucket_name = [record['s3']['bucket']['name'] for record in json_data['Records']]
    print(bucket_name)
except FileNotFoundError:
    print(f"Error: File not found")    