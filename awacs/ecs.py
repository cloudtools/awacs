# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EC2 Container Service'
prefix = 'ecs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateCluster = Action('CreateCluster')
CreateService = Action('CreateService')
DeleteCluster = Action('DeleteCluster')
DeleteService = Action('DeleteService')
DeregisterContainerInstance = Action('DeregisterContainerInstance')
DeregisterTaskDefinition = Action('DeregisterTaskDefinition')
DescribeClusters = Action('DescribeClusters')
DescribeContainerInstances = Action('DescribeContainerInstances')
DescribeServices = Action('DescribeServices')
DescribeTaskDefinition = Action('DescribeTaskDefinition')
DescribeTasks = Action('DescribeTasks')
DiscoverPollEndpoint = Action('DiscoverPollEndpoint')
ListClusters = Action('ListClusters')
ListContainerInstances = Action('ListContainerInstances')
ListServices = Action('ListServices')
ListTaskDefinitionFamilies = Action('ListTaskDefinitionFamilies')
ListTaskDefinitions = Action('ListTaskDefinitions')
ListTasks = Action('ListTasks')
Poll = Action('Poll')
RegisterContainerInstance = Action('RegisterContainerInstance')
RegisterTaskDefinition = Action('RegisterTaskDefinition')
RunTask = Action('RunTask')
StartTask = Action('StartTask')
StopTask = Action('StopTask')
StartTelemetrySession = Action('StartTelemetrySession')
SubmitContainerStateChange = Action('SubmitContainerStateChange')
SubmitTaskStateChange = Action('SubmitTaskStateChange')
UpdateContainerAgent = Action('UpdateContainerAgent')
UpdateService = Action('UpdateService')
