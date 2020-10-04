# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elastic Container Service'
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


CreateCapacityProvider = Action('CreateCapacityProvider')
CreateCluster = Action('CreateCluster')
CreateService = Action('CreateService')
CreateTaskSet = Action('CreateTaskSet')
DeleteAccountSetting = Action('DeleteAccountSetting')
DeleteAccountSettings = Action('DeleteAccountSettings')
DeleteAttributes = Action('DeleteAttributes')
DeleteCapacityProvider = Action('DeleteCapacityProvider')
DeleteCluster = Action('DeleteCluster')
DeleteService = Action('DeleteService')
DeleteTaskSet = Action('DeleteTaskSet')
DeregisterContainerInstance = Action('DeregisterContainerInstance')
DeregisterTaskDefinition = Action('DeregisterTaskDefinition')
DescribeCapacityProviders = Action('DescribeCapacityProviders')
DescribeClusters = Action('DescribeClusters')
DescribeContainerInstances = Action('DescribeContainerInstances')
DescribeServices = Action('DescribeServices')
DescribeTaskDefinition = Action('DescribeTaskDefinition')
DescribeTaskSets = Action('DescribeTaskSets')
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
PutClusterCapacityProviders = Action('PutClusterCapacityProviders')
RegisterContainerInstance = Action('RegisterContainerInstance')
RegisterTaskDefinition = Action('RegisterTaskDefinition')
RunTask = Action('RunTask')
StartTask = Action('StartTask')
StartTelemetrySession = Action('StartTelemetrySession')
StopTask = Action('StopTask')
SubmitAttachmentStateChanges = Action('SubmitAttachmentStateChanges')
SubmitContainerStateChange = Action('SubmitContainerStateChange')
SubmitTaskStateChange = Action('SubmitTaskStateChange')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateClusterSettings = Action('UpdateClusterSettings')
UpdateContainerAgent = Action('UpdateContainerAgent')
UpdateContainerInstancesState = Action('UpdateContainerInstancesState')
UpdateService = Action('UpdateService')
UpdateServicePrimaryTaskSet = Action('UpdateServicePrimaryTaskSet')
UpdateTaskSet = Action('UpdateTaskSet')
