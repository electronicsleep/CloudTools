# ct library

import boto3


def ask_continue():
    """ Stop and ask for user input """
    yes = {'yes', 'y'}

    print("Proceed (y/n)?")
    choice = input().lower()
    if choice in yes:
        return True
    else:
        print("Aborting due to user input")
        exit(1)


def aws_list_inst():
    client = boto3.client('ec2', 'us-west-1')
    response = client.describe_instances()
    for r in response['Reservations']:
        for inst in r['Instances']:
            if inst['State']['Name'] == 'running':
                print("%s # %s %s %s" % (inst['PublicIpAddress'], inst['InstanceId'],
                                         inst['Tags'][0]['Value'], inst['State']['Name']))

