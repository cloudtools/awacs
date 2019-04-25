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
DeleteAccountSettings = Action('DeleteAccountSettings')
DeleteAttributes = Action('DeleteAttributes')
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
ListAccountSettings = Action('ListAccountSettings')
ListAttributes = Action('ListAttributes')
ListClusters = Action('ListClusters')
ListContainerInstances = Action('ListContainerInstances')
ListServices = Action('ListServices')
ListTagsForResource = Action('ListTagsForResource')
ListTaskDefinitionFamilies = Action('ListTaskDefinitionFamilies')
ListTaskDefinitions = Action('ListTaskDefinitions')
ListTasks = Action('ListTasks')
Poll = Action('Poll')
PutAccountSetting = Action('PutAccountSetting')
PutAccountSettingDefault = Action('PutAccountSettingDefault')
PutAttributes = Action('PutAttributes')
RegisterContainerInstance = Action('RegisterContainerInstance')
RegisterTaskDefinition = Action('RegisterTaskDefinition')
RunTask = Action('RunTask')
StartTask = Action('StartTask')
StartTelemetrySession = Action('StartTelemetrySession')
StopTask = Action('StopTask')
SubmitContainerStateChange = Action('SubmitContainerStateChange')
SubmitTaskStateChange = Action('SubmitTaskStateChange')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateContainerAgent = Action('UpdateContainerAgent')
UpdateContainerInstancesState = Action('UpdateContainerInstancesState')
UpdateService = Action('UpdateService')
