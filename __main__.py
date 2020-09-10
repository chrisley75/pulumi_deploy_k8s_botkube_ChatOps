#https://www.pulumi.com/docs/get-started/kubernetes/modify-program/

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts

# Deploy BOTKube chatops

botkube = Chart(
   'botkube', 
   ChartOpts(
     repo='infracloudio',
     chart='botkube',
     version='v0.10.0',
     namespace='botkube',
#     fetch_opts=FetchOpts(
#         repo="https://infracloudio.github.io/charts",
#     ),
     values={
       'communications.slack.enabled': 'true',
       'communications.slack.channel': 'chatops',
       'communications.slack.token': 'xoxb-1349221428866-1361852017825-hmvgOOdtb71FmCPWngAjjN9H',
       'config.settings.clustername': 'akspulu',
       'config.settings.allowkubectl': 'true' 
     },
    ),
   )



pulumi.export("name", deployment.metadata["name"])
