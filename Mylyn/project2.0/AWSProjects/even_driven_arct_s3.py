import json

def lambda_handler(event, context):
    # Print the event details for debugging
    print("Received event: " + json.dumps(event, indent=2))

    # Process the S3 event
    for record in event['Records']:
        # Extract bucket and key from the event record
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Perform your processing logic here, such as reading the object from S3, processing it, etc.
        print(f"New object created in bucket '{bucket}' with key '{key}'")
        # Add your processing logic here
        
    # Return a response if needed
    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
