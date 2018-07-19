# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon SageMaker'
prefix = 'sagemaker'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTags = Action('AddTags')
CreateEndpoint = Action('CreateEndpoint')
CreateEndpointConfig = Action('CreateEndpointConfig')
CreateModel = Action('CreateModel')
CreateNotebookInstance = Action('CreateNotebookInstance')
CreatePresignedNotebookInstanceUrl = \
    Action('CreatePresignedNotebookInstanceUrl')
CreateTrainingJob = Action('CreateTrainingJob')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteEndpointConfig = Action('DeleteEndpointConfig')
DeleteModel = Action('DeleteModel')
DeleteNotebookInstance = Action('DeleteNotebookInstance')
DeleteTags = Action('DeleteTags')
DescribeEndpoint = Action('DescribeEndpoint')
DescribeEndpointConfig = Action('DescribeEndpointConfig')
DescribeModel = Action('DescribeModel')
DescribeNotebookInstance = Action('DescribeNotebookInstance')
DescribeTrainingJob = Action('DescribeTrainingJob')
InvokeEndpoint = Action('InvokeEndpoint')
ListEndpointConfigs = Action('ListEndpointConfigs')
ListEndpoints = Action('ListEndpoints')
ListModels = Action('ListModels')
ListNotebookInstances = Action('ListNotebookInstances')
ListTags = Action('ListTags')
ListTrainingJobs = Action('ListTrainingJobs')
StartNotebookInstance = Action('StartNotebookInstance')
StopNotebookInstance = Action('StopNotebookInstance')
StopTrainingJob = Action('StopTrainingJob')
UpdateEndpoint = Action('UpdateEndpoint')
UpdateEndpointWeightsAndCapacities = \
    Action('UpdateEndpointWeightsAndCapacities')
UpdateNotebookInstance = Action('UpdateNotebookInstance')
