#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# ct library

import boto3
import subprocess
import pprint
import requests


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


def check_sites(server_list, verbose):
    if verbose:
        print(f"ec: verbose: {verbose}")
        pprint.pprint(server_list)
    for url in server_list:
        print(f"check_sites cmd: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            print("200 ok")
        if verbose:
            pprint.pprint(response.content)
            pprint.pprint(response.text)
            pprint.pprint(response.headers)
            pprint.pprint(response.status_code)


def aws_list_inst(region, verbose):
    """ idea is to keep commands consistent use list-inst for aws/gcp """
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
    """ idea is to keep commands consistent use list-inst for aws/gcp """
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
