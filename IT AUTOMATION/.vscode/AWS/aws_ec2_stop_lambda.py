#Lambda Function to Stop EC2 Instances:
'''
import boto3

def lambda_handler(event, context):
    # Define the region where your EC2 instances are located
    region = 'your_region'

    # Specify the EC2 instance IDs that you want to stop
    instance_ids_to_stop = ['instance_id_1', 'instance_id_2']

    # Create EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    # Stop EC2 instances
    ec2_client.stop_instances(InstanceIds=instance_ids_to_stop)

    return {
        'statusCode': 200,
        'body': 'EC2 instances stopped successfully.'
    }
'''
import boto3

def lambda_handler(event, context):
    # Extract parameters from the event
    region = event['region']
    instance_ids_to_stop = event['instance_ids']

    # Create EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    # Stop EC2 instances
    ec2_client.stop_instances(InstanceIds=instance_ids_to_stop)

    return {
        'statusCode': 200,
        'body': 'EC2 instances stopped successfully.'
    }
'''
aws lambda invoke \
    --function-name StartEC2LambdaFunction \
    --payload '{"region": "your_region", "instance_ids": ["instance_id_1", "instance_id_2"]}' \
    output.json
Replace "your_region" with the actual AWS region, and ["instance_id_1", "instance_id_2"]
'''