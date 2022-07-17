#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# ct library

import boto3
import subprocess


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


def aws_list_ec2(region, verbose):
    if verbose:
        print(f"verbose: region: {region}")
    client = boto3.client('ec2', region)
    response = client.describe_instances()
    for r in response['Reservations']:
        for inst in r['Instances']:
            if inst['State']['Name'] == 'running':
                print("%s # %s %s %s" % (inst['PublicIpAddress'], inst['InstanceId'],
                                         inst['Tags'][0]['Value'], inst['State']['Name']))


def gcp_list_inst(project, verbose):
    format = '--format="value(name,status,zone,id,kind)"'
    if verbose:
        print(f"verbose: project: {project}")
    cmd = 'gcloud compute instances list --project=' + project + ' ' + format
    run_cmd(cmd)


def aws_update_r53(verbose):
    if verbose:
        print("Verbose on")
    print("Updating r53 now")


def run_cmd(cmd):
    print("run_cmd", cmd)
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in pipe.stdout:
        line = line.decode("utf-8")
        print(line.strip())
