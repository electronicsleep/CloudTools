#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Use kubernetes API to automate finding and investigate issues

from kubernetes import client, config


def check_pods(verbose):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if "ErrImagePull" in str(i.status):
            print("ERROR: %s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        if verbose:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def check_events(verbose):
    """Show events with failed status"""
    config.load_kube_config()
    v1 = client.CoreV1Api()
    events = v1.list_event_for_all_namespaces()
    for event in events.items:
        if "ErrImagePull" in str(event.message):
            print("ERROR:", event.message)
        if "Failed" in str(event.message):
            print("ERROR:", event.message)
        if verbose:
            print(event.message)
