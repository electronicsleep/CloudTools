#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# ct library

import boto3
import subprocess
import pprint
import requests
import logging
from datetime import datetime


# log.setLevel(logging.INFO)
logging.basicConfig(filename='ct.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
log = logging.getLogger("ct_lib")
log.info("run ct_lib")


def ask_continue():
    """Ask for user confirmation"""
    yes = {'yes', 'y'}

    print("Proceed (y/n)?")
    choice = input().lower()
    if choice in yes:
        return True
    else:
        print("Aborting due to user input")
        exit(1)


def check_sites(server_list: list[str], verbose: bool):
    """Check websites using requests"""
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


def aws_li(region: str, verbose: bool):
    """AWS list instances li (list instances)"""
    if verbose:
        print(f"verbose: region: {region}")
    log.info("run aws_li")
    print(date_ymd())

    client = boto3.client('ec2', region)
    response = client.describe_instances()
    for r in response['Reservations']:
        for inst in r['Instances']:
            if inst['State']['Name'] == 'running':
                print("%s # %s %s %s" % (inst['PublicIpAddress'], inst['InstanceId'],
                                         inst['Tags'][0]['Value'], inst['State']['Name']))


def gcp_li(project: str, verbose: bool):
    """GCP list instances li (list instances) """
    format = '--format="value(name,zone,status,id,kind,INTERNAL_IP,EXTERNAL_IP,id)"'
    if verbose:
        print(f"verbose: project: {project}")
    cmd = f"gcloud compute instances list --project={project} {format}"
    run_cmd(cmd)


def aws_udns(verbose: bool):
    """AWS update route53"""
    if verbose:
        print("Verbose on")
    print("Updating r53 now")


def run_cmd(cmd: str):
    """Run command using subprocess"""
    print("run_cmd", cmd)
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if pipe.stdout is not None:
        for line in pipe.stdout:
            line = line.decode("utf-8")
            print(line.strip())


def date_ymd():
    """Return standard date format"""
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    return f"Date: {current_year}-{current_month}-{current_day}"


def add_dict(map: dict, s: str, count: int = 1):
    """Increment dict key string"""
    if s in map:
        map[s] += count
    else:
        map[s] = 1
