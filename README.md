# Description

pulumi program written in python to create a namespace in a K8s cluster and deploy a bot in it for ChatOps communication (Slack, Mattermost)

## What is ChatOps
ChatOps is a way to execute DevOps tasks, such as deployments, monitoring and system management using chat messages. For example sending a logs message to a chatbot retrieves the latest log messages. Or a deployment could be triggered from a chat message.

This offers a few important advantages:

* A very human way to manage your infrastructure, by chatting with a bot.
* It can be part of a shared chat, so that people can collaborate and share information. This also offers a record of executed commands and actions.
* It can help safely overcome network and firewall restrictions to make working from home or on the go possible.
* A unified interface over DevOps tools, manage Kubernetes and OpenShift with the same interfaceIt can simplify and secure infrastructure tasks, so they can be done by the developers themselves.

## BotKube Backend Architecture

source: [BotKube](https://www.botkube.io/architecture/)

![HLD ChatOps BotKube](docs/botkube_architecture.png)

- **Informer Controller:** Registers informers to kube-apiserver to watch events on the configured Kubernetes resources. It forwards the incoming Kubernetes event to the Event Manage
- **Event Manager:** Extracts required fields from Kubernetes event object and creates a new BotKube event struct. It passes BotKube event struct to the Filter Engine
- **Filter Engine:** Takes the Kubernetes object and BotKube event struct and runs Filters on them. Each filter runs some validations on the Kubernetes object and modifies the messages in the BotKube event struct if required.
- **Event Notifier:** Finally, notifier sends BotKube event over the configured communication channel.
- **Bot Interface:** Bot interface takes care of authenticating and managing connections with communication mediums like Slack, Mattermost. It reads/sends messages from/to commucation mediums.
- **Executor:** Executes BotKube or kubectl command and sends back the result to the Bot interface.

## BotKube ChatOps interaction in multi-environment

![HLD ChatOps BotKube](docs/botkube.png)

## Prerequisites
- Install [BotKube App](https://www.botkube.io/installation/) in your Slack/Mattermost and remember to keep the associated token when creating the app.
- Create a dedicated channel in Slack/Mattermost.
- Have access to a kubernete cluster with privileges access.
- Have a valid [pulumi](https://app.pulumi.com/) account

## Installation
Clone this Git Repository
```bash
$git clone https://github.com/chrisley75/pulumi_deploy_k8s_botkube_ChatOps
```

## Manual installation
Create a folder

```bash
$mkdir <folder> && cd <folder>
```

Init a new pulumi stack and configure as a new kubernetes-python 
```bash
$pulumi stack init
$pulumi new kubernetes-python
```

Replace __main__.py with the one in this Github repository


## Configuration
Set pulumi environment variables with your environment information.
```bash
$pulumi config set SLACK_CHANNEL_NAME <SLACK_CHANNEL>
$pulumi config set CLUSTER_NAME <Cluster_Name>
$pulumi config set ALLOW_KUBECTL True
$pulumi config set --secret SLACK_API_TOKEN <TOKEN>
```

Check the configured variables
```bash
$ pulumi config
KEY                 VALUE
ALLOW_KUBECTL       True
CLUSTER_NAME        <Cluster_Name>
SLACK_API_TOKEN     <TOKEN>
SLACK_CHANNEL_NAME  <SLACK_CHANNEL>
```
or to visualize encrypt vars
```bash
$pulumi config --show-secrets
```

## Deploy the ChatOps BotKube with Pulumi
```bash
$ pulumi up
Previewing update (dev)

View Live: https://app.pulumi.com/chrisley75/k8s-apps-chatops-botkube/dev/previews/397a3c49-d785-4ca2-aed7-e082b7565dcd

     Type                                                           Name                                  Plan       Info
 +   pulumi:pulumi:Stack                                            k8s-apps-chatops-botkube-dev          create     6 messages
 +   ├─ kubernetes:helm.sh:Chart                                    botkube                               create     
 +   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRole         botkube-clusterrole                   create     
 +   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRoleBinding  botkube-clusterrolebinding            create     
 +   │  ├─ kubernetes:core:ServiceAccount                           botkube/botkube-sa                    create     
 +   │  ├─ kubernetes:core:Secret                                   botkube/botkube-communication-secret  create     
 +   │  ├─ kubernetes:core:ConfigMap                                botkube/botkube-configmap             create     
 +   │  └─ kubernetes:apps:Deployment                               botkube/botkube                       create     
 +   └─ kubernetes:core:Namespace                                   botkube                               create     
 
Diagnostics:
  pulumi:pulumi:Stack (k8s-apps-chatops-botkube-dev):
    True
    True
    <pulumi.output.Output object at 0x109c7f160>
    <pulumi.output.Output object at 0x10b2104f0>
    k8schrisley
    k8schrisley
 

Do you want to perform this update? yes
Updating (dev)

View Live: https://app.pulumi.com/chrisley75/k8s-apps-chatops-botkube/dev/updates/41

     Type                                                           Name                                  Status      Info
 +   pulumi:pulumi:Stack                                            k8s-apps-chatops-botkube-dev          created     6 messages
 +   ├─ kubernetes:helm.sh:Chart                                    botkube                               created     
 +   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRole         botkube-clusterrole                   created     
 +   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRoleBinding  botkube-clusterrolebinding            created     
 +   │  ├─ kubernetes:core:ServiceAccount                           botkube/botkube-sa                    created     
 +   │  ├─ kubernetes:core:Secret                                   botkube/botkube-communication-secret  created     
 +   │  ├─ kubernetes:core:ConfigMap                                botkube/botkube-configmap             created     
 +   │  └─ kubernetes:apps:Deployment                               botkube/botkube                       created     
 +   └─ kubernetes:core:Namespace                                   botkube                               created     
 
Diagnostics:
  pulumi:pulumi:Stack (k8s-apps-chatops-botkube-dev):
    True
    True
    <pulumi.output.Output object at 0x10cddcf10>
    <pulumi.output.Output object at 0x10e374430>
    k8schrisley
    k8schrisley
 
Resources:
    + 9 created

Duration: 12s
```

If everything went well, the deployment appears directly in your ChatOps and it is now possible to view and manage the cluster (or several clusters) from the channel.
![k8s cluster appears in the channel](docs/deploy_ok.png)

## Manage Kubernetes cluster with Chat

Check cluster is ready:

![k8s ping from chat](docs/ping.png)

Kubectl command to get namespace on the cluster:
![k8s get namespace](docs/getns.png)

Get state of the creation on resource in the cluster:
![Resource creation monitor](docs/creation.png)

be automatically alerted in case of a problem on the cluster:
![Resource creation monitor](docs/errors.png)

and so many other possibilities.....


## Delete and remove app
This action will delete the app and the namespace in the K8s cluster (Only resources created by this program), but not the stack in pulumi
```bash
$ pulumi destroy
Previewing destroy (dev)

View Live: https://app.pulumi.com/chrisley75/k8s-apps-chatops-botkube/dev/previews/834376a4-587b-46e8-9838-5b5666f18b03

     Type                                                           Name                                  Plan       
 -   pulumi:pulumi:Stack                                            k8s-apps-chatops-botkube-dev          delete     
 -   ├─ kubernetes:helm.sh:Chart                                    botkube                               delete     
 -   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRole         botkube-clusterrole                   delete     
 -   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRoleBinding  botkube-clusterrolebinding            delete     
 -   │  ├─ kubernetes:core:ServiceAccount                           botkube/botkube-sa                    delete     
 -   │  ├─ kubernetes:core:ConfigMap                                botkube/botkube-configmap             delete     
 -   │  ├─ kubernetes:core:Secret                                   botkube/botkube-communication-secret  delete     
 -   │  └─ kubernetes:apps:Deployment                               botkube/botkube                       delete     
 -   └─ kubernetes:core:Namespace                                   botkube                               delete     
 
Resources:
    - 9 to delete

Do you want to perform this destroy? yes
Destroying (dev)

View Live: https://app.pulumi.com/chrisley75/k8s-apps-chatops-botkube/dev/updates/40

     Type                                                           Name                                  Status      
 -   pulumi:pulumi:Stack                                            k8s-apps-chatops-botkube-dev          deleted     
 -   ├─ kubernetes:helm.sh:Chart                                    botkube                               deleted     
 -   │  ├─ kubernetes:core:ConfigMap                                botkube/botkube-configmap             deleted     
 -   │  ├─ kubernetes:core:Secret                                   botkube/botkube-communication-secret  deleted     
 -   │  ├─ kubernetes:core:ServiceAccount                           botkube/botkube-sa                    deleted     
 -   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRole         botkube-clusterrole                   deleted     
 -   │  ├─ kubernetes:rbac.authorization.k8s.io:ClusterRoleBinding  botkube-clusterrolebinding            deleted     
 -   │  └─ kubernetes:apps:Deployment                               botkube/botkube                       deleted     
 -   └─ kubernetes:core:Namespace                                   botkube                               deleted     
 
Resources:
    - 9 deleted

Duration: 18s

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained. 
If you want to remove the stack completely, run 'pulumi stack rm dev'.
```

# Author
**Christopher LEY**
SRE and MultiCloud Architect at IBM - IBM Services - christopher.ley@ibm.com
