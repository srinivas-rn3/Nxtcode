response = client.create_cluster(
    name='string',
    version='string',
    roleArn='string',
    resourcesVpcConfig={
        'subnetIds': [
            'string',
        ],
        'securityGroupIds': [
            'string',
        ],
        'endpointPublicAccess': True|False,
        'endpointPrivateAccess': True|False,
        'publicAccessCidrs': [
            'string',
        ]
    },
    kubernetesNetworkConfig={
        'serviceIpv4Cidr': 'string',
        'ipFamily': 'ipv4'|'ipv6'
    },
    logging={
        'clusterLogging': [
            {
                'types': [
                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                ],
                'enabled': True|False
            },
        ]
    },
    clientRequestToken='string',
    tags={
        'string': 'string'
    },
    encryptionConfig=[
        {
            'resources': [
                'string',
            ],
            'provider': {
                'keyArn': 'string'
            }
        },
    ],
    outpostConfig={
        'outpostArns': [
            'string',
        ],
        'controlPlaneInstanceType': 'string'
    }
)