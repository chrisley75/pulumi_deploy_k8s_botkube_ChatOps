# Description

pulumi program written in python to create a namespace in a K8s cluster and deploy a bot in it for ChatOps communication (Slack, Mattermost)

## Prerequisites
- Install [BotKube App](https://www.botkube.io/installation/) in your Slack/Mattermost and remember to keep the associated token when creating the app.
- Create a dedicated channel in Slack/Mattermost.
- Have access to a kubernete cluster with privileges access.
- Have a valid [pulumi](https://app.pulumi.com/) account

## Installation
Clone this Git Repository
’’’bash
git clone https://github.com/chrisley75/pulumi_deploy_k8s_botkube_ChatOps
’’’

## Manual installation
Create a folder
’’’bash
mkdir <folder> && cd <folder>
’’’

Init a new pulumi stack and configure as a new kubernetes-python 
’’’bash
pulumi stack init
pulumi new kubernetes-python
’’’bash

Replace __main__.py with the one in this Github repository


## Configuration
Set pulumi environment variables with your environment information.
’’’bash
pulumi config set SLACK_CHANNEL_NAME <SLACK_CHANNEL>
pulumi config set CLUSTER_NAME <Cluster_Name>
pulumi config set ALLOW_KUBECTL True
pulumi config set --secret SLACK_API_TOKEN <TOKEN>
’’’

Check the configured variables
’’’bash
$ pulumi config
KEY                 VALUE
ALLOW_KUBECTL       True
CLUSTER_NAME        <Cluster_Name>
SLACK_API_TOKEN     <TOKEN>
SLACK_CHANNEL_NAME  <SLACK_CHANNEL>
’’’
or to visualize encrypt vars
’’’bash
pulumi config --show-secrets
’’’

## Deploy the ChatOps BotKube with Pulumi
’’’bash
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
’’’

## Delete and remove app
This action will delete the app and the namespace in the K8s cluster (Only resources created by this program), but not the stack in pulumi
’’’bash
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
’’’


