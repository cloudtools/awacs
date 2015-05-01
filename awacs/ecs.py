# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, BaseARN

service_name = 'AWS Elastic Container Service'
prefix = 'ecs'


class ARN(BaseARN):
    def __init__(self, resource="*", region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class ECSAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


CreateCluster = ECSAction('CreateCluster')
CreateService = ECSAction('CreateService')
DeleteCluster = ECSAction('DeleteCluster')
DeleteService = ECSAction('DeleteService')
DeregisterContainerInstance = ECSAction('DeregisterContainerInstance')
DeregisterTaskDefinition = ECSAction('DeregisterTaskDefinition')
DescribeClusters = ECSAction('DescribeClusters')
DescribeContainerInstances = ECSAction('DescribeContainerInstances')
DescribeServices = ECSAction('DescribeServices')
DescribeTaskDefinition = ECSAction('DescribeTaskDefinition')
DescribeTasks = ECSAction('DescribeTasks')
DiscoverPollEndpoint = ECSAction('DiscoverPollEndpoint')
ListClusters = ECSAction('ListClusters')
ListContainerInstances = ECSAction('ListContainerInstances')
ListServices = ECSAction('ListServices')
ListTaskDefinitionFamilies = ECSAction('ListTaskDefinitionFamilies')
ListTaskDefinitions = ECSAction('ListTaskDefinitions')
ListTasks = ECSAction('ListTasks')
RegisterContainerInstance = ECSAction('RegisterContainerInstance')
RegisterTaskDefinition = ECSAction('RegisterTaskDefinition')
RunTask = ECSAction('RunTask')
StartTask = ECSAction('StartTask')
StopTask = ECSAction('StopTask')
SubmitContainerStateChange = ECSAction('SubmitContainerStateChange')
SubmitTaskStateChange = ECSAction('SubmitTaskStateChange')
UpdateService = ECSAction('UpdateService')

# Not in the API docs, but listed here for Container hosts:
# http://docs.aws.amazon.com/AmazonECS/latest/developerguide/IAM_policies.html#instance_IAM_role
Poll = ECSAction('Poll')
