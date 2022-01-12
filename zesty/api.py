import json


def get_ec2_instances(region: str):
    with open(f'storage/{region}.json') as f:
        return json.load(f)
