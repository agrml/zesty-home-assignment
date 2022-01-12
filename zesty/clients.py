import boto3

import settings


def get_ec2_instances(region_name) -> list:
    ec2 = boto3.client(
        service_name='ec2',
        region_name=region_name,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        aws_session_token=settings.AWS_SESSION_TOKEN,
    )
    data = ec2.describe_instances()
    instances = []
    for reservation in data['Reservations']:
        instances.extend(reservation['Instances'])
    return instances
