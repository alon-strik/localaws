import boto3


stack = cloudformation.create_stack(
    StackName='string',
    TemplateBody='string',
    TemplateURL='string',
    Parameters=[
        {
            'ParameterKey': 'string',
            'ParameterValue': 'string',
            'UsePreviousValue': True|False
        },
    ],
    DisableRollback=True|False,
    TimeoutInMinutes=123,
    NotificationARNs=[
        'string',
    ],
    Capabilities=[
        'CAPABILITY_IAM',
    ],
    ResourceTypes=[
        'string',
    ],
    OnFailure='DO_NOTHING'|'ROLLBACK'|'DELETE',
    StackPolicyBody='string',
    StackPolicyURL='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
