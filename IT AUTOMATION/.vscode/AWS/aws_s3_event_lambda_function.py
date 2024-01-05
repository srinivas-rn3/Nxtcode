import json 

def lambda_handler(event,context):
    """
    Lambda Function  handler dor S3 event. 
    """
    #log incoming event for debugging process 
    print("Received S3 event: "+ json.dumps(event,indent=2))
    #Process the S3 event
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        #perform the custom logic here based on the s3 event
        print(f"New object is created in bucekt '{bucket} with key {key}'")
    return{
        'statusCode':200,
        'body':'S3 event is  processed successfully '
    }