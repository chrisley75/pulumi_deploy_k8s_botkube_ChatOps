#https://www.pulumi.com/docs/get-started/kubernetes/modify-program/

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts
import pulumi_kubernetes as kubernetes

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
#     repo='infracloudio',
     chart='botkube',
     version='v0.10.0',
     namespace='botkube',
## Si on fetch directement un repo helm distant
     fetch_opts=FetchOpts(
         repo="https://infracloudio.github.io/charts/",
     ),
     values={
       'communications.slack.enabled': 'true',
       'communications.slack.channel': '<SLACK_CHANNEL_NAME>',
       'communications.slack.token': '<SLACK_API_TOKEN_FOR_THE_BOT>',
       'config.settings.clustername': '<CLUSTER_NAME>',
       'config.settings.allowkubectl': 'true'
     },
    ),
   )

#pulumi.export(botkube_namespace.metadata["name"])
