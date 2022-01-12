from datetime import datetime

import json

import pytz as pytz

from zesty.clients import get_ec2_instances


def get_region_names() -> list[str]:
    with open('config/regions.txt') as f:
        regions_string = f.readline().strip()
        return regions_string.split(', ')


def save_instances(instances: list, filename: str) -> None:
    make_json_serializable_inplace(instances)
    with open(f'storage/{filename}', 'w') as f:
        json.dump(instances, f)


def make_json_serializable_inplace(instances: list):
    for instance in instances:
        # review note: bonus task :)
        active_time = datetime.utcnow().replace(tzinfo=pytz.utc) - instance['LaunchTime']
        instance['DaysActive'] = active_time.days

        instance['LaunchTime'] = instance['LaunchTime'].isoformat()

        # review note: we would provide a proper serialization in real life,
        # but we don't have time now
        instance.pop('BlockDeviceMappings')
        instance.pop('NetworkInterfaces')
        instance.pop('UsageOperationUpdateTime')


regions = get_region_names()
for region_name in regions:
    ec2_instances = get_ec2_instances(region_name)
    ec2_instances = sorted(ec2_instances, key=lambda instance: instance['LaunchTime'])
    save_instances(instances=ec2_instances, filename=f'{region_name}.json')
