#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Example use kubernetes API to automate finding and investigate issues

from kubernetes import client, config


def check_pods(verbose):
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()
        pods = v1.list_pod_for_all_namespaces(watch=False)
    except Exception as e:
        print(f"Error with client connect {e}")
        return "Connection Error"
    for pod in pods.items:
        if "ErrImagePull" in str(pod.status):
            print("ERROR: %s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name))
        if verbose:
            print("%s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name))


def check_events(verbose):
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()
        events = v1.list_event_for_all_namespaces()
    except Exception as e:
        print(f"Error with client connect {e}")
        return "Connection Error"
    for event in events.items:
        if "ErrImagePull" in str(event.message):
            print("ERROR:", event.message)
        if "Failed" in str(event.message):
            print("ERROR:", event.message)
        if verbose:
            print(event.message)
