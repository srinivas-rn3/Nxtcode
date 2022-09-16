import boto3
import requests 
import json
import sys
from botocore.exceptions import ClientError
import http.client as client
response = client.create_nodegroup(
    clusterName='WebServices-app',
    nodegroupName='WebServices-NG',
    scalingConfig={
        'minSize': 1,
        'maxSize': 2,
        'desiredSize': 2
    },
    diskSize=15,
    subnets=[
        'subnet-689a8125',
    ],
    instanceTypes=[
        't2.medium',
    ],
    amiType='AL2_x86_64'
    remoteAccess={
        'ec2SshKey': 'web_app',
        'sourceSecurityGroups': [
            'Node-group-Lin',
        ]
    },
    nodeRole='arn:aws:iam::012345678910:role/NodeInstanceRole',
    labels={
        'string': 'web-app-role'
    },
    taints=[
        {
            'key': 'dedicated-apps',
            'value': 'webAppGroup',
            'effect': 'NO_SCHEDULE'
        },
    ],
    tags={
        'Name': 'simple-app'
    },
    clientRequestToken='454g6yyjjh-45tryyhd-scvr45-tg56h7-xase34590fhj,
    launchTemplate={
        'name': 'Latest-app',
        'version': $Latest,
        'id': 'Latest-app'
    },
    updateConfig={
        'maxUnavailable': 2,
        'maxUnavailablePercentage': 2
    },
    capacityType='ON_DEMAND',
    version='1.13',
    releaseVersion='1.13'
)
url = "eks.us-east-1.amazonaws.com/clusters/prod/node-groups"
headers = { 
            "Accept-Encoding": "identity",
            "User-Agent": "aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34",
            "X-Amz-Date": "20200812T151423Z",
            "Authorization": "AUTHPARAMS",
            "Content-Length": 454

            }
try:

    response = requests.request("POST", url, headers=headers, data=response)
    response_json = response.text
    response_status = response.status_code()

except requests.RequestException as e:
        print(e)
except EKS.Client.exceptions.ClientException as e:
        print(e)
except EKS.Client.exceptions.InvalidRequestException as e:
      print(e)
