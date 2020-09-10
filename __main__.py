## Python Pulumi program to Create K8s namesaoce and to deploy ChatOps in the K8s cluster
## Christopher LEY - Sept 2020 
## https://github.com/chrisley75/pulumi_deploy_k8s_botkube_ChatOps
## https://www.pulumi.com/docs/get-started/kubernetes/modify-program/

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts
import pulumi_kubernetes as kubernetes

# Recuperation et declaration des variables qui ont été configurées dans pulumi (ex: pulumi config set CLUSTER_NAME k8schrisley)
config = pulumi.Config()
ALLOW_KUBECTL = config.require("ALLOW_KUBECTL")
CLUSTER_NAME = config.require("CLUSTER_NAME")
SLACK_API_TOKEN = config.require_secret("SLACK_API_TOKEN")
SLACK_CHANNEL_NAME = config.require("SLACK_CHANNEL_NAME")

# Create a K8s namespace.
# Create dedicated namespace for ChatOps
botkube_namespace = kubernetes.core.v1.Namespace(
    "botkube",
    metadata={
        "name": "botkube",
    })

# Deploy BOTKube chatops
botkube = Chart(
   'botkube',
   ChartOpts(
   ## Si on utilise un repo local helm ($ helm repo list), utiliser le nom du repo avec cette entree repo='<repo_name>'
   # repo='infracloudio',
     chart='botkube',
     version='v0.10.0',
     namespace='botkube',
   ## Si on fetch directement un repo helm distant
     fetch_opts=FetchOpts(
         repo="https://infracloudio.github.io/charts/",
     ),
     values={
       "communications": {
          "slack": {
             "enabled": True,
             "channel": SLACK_CHANNEL_NAME,
             "token": SLACK_API_TOKEN,
          },
       },
       "config": {
           "settings": {
             "clustername": CLUSTER_NAME,
             "allowkubectl": ALLOW_KUBECTL,
           },
       },
     },
   )
)

# DEBUG VARS
print(ALLOW_KUBECTL)
print(config.require("ALLOW_KUBECTL"))
print(SLACK_API_TOKEN)
print(config.require_secret("SLACK_API_TOKEN"))
print(CLUSTER_NAME)
print(config.require("CLUSTER_NAME"))

