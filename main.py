import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="ap-south-1")
ec2_resource = boto3.client('ec2', region_name="ap-south-1")

# reservations = ec2_client.describe_instances()
# for reservation in reservations['Reservations']:
#     instances = reservation['Instances']
#     for instance in instances:
#         print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")

def check_instance_status():
    instance_statuses = ec2_client.describe_instance_status()
    for instance_status in instance_statuses['InstanceStatuses']:
        ins_status = instance_status['InstanceStatus']
        sys_status = instance_status['SystemStatus']
        print(f"Instance {instance_status['InstanceId']} is {instance_status['InstanceState']['Name']}")
        # print(f"\nInstance {instance_status['InstanceId']}")
        print(f"Instance status: {ins_status['Status']}")
        print(f"System status: {sys_status['Status']}\n")

schedule.every(10).minutes.do(check_instance_status)
# schedule.every(30).seconds.do(check_instance_status)
schedule.every().day.at('10:30').do(check_instance_status)

while True:
    schedule.run_pending()