from kubernetes import client, config


def check_pods(verbose=False):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def check_events(verbose=False):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    events = v1.list_event_for_all_namespaces()
    for event in events.items:
        print(event.message)
