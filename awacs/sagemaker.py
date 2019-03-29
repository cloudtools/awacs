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
CreateHyperParameterTuningJob = Action('CreateHyperParameterTuningJob')
CreateLabelingJob = Action('CreateLabelingJob')
CreateModel = Action('CreateModel')
CreateNotebookInstance = Action('CreateNotebookInstance')
CreatePresignedNotebookInstanceUrl = \
    Action('CreatePresignedNotebookInstanceUrl')
CreateTrainingJob = Action('CreateTrainingJob')
CreateTransformJob = Action('CreateTransformJob')
CreateWorkteam = Action('CreateWorkteam')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteEndpointConfig = Action('DeleteEndpointConfig')
DeleteModel = Action('DeleteModel')
DeleteNotebookInstance = Action('DeleteNotebookInstance')
DeleteTags = Action('DeleteTags')
DeleteWorkteam = Action('DeleteWorkteam')
DescribeEndpoint = Action('DescribeEndpoint')
DescribeEndpointConfig = Action('DescribeEndpointConfig')
DescribeHyperParameterTuningJob = Action('DescribeHyperParameterTuningJob')
DescribeLabelingJob = Action('DescribeLabelingJob')
DescribeModel = Action('DescribeModel')
DescribeNotebookInstance = Action('DescribeNotebookInstance')
DescribeSubscribedWorkteam = Action('DescribeSubscribedWorkteam')
DescribeTrainingJob = Action('DescribeTrainingJob')
DescribeTransformJob = Action('DescribeTransformJob')
DescribeWorkteam = Action('DescribeWorkteam')
InvokeEndpoint = Action('InvokeEndpoint')
ListEndpointConfigs = Action('ListEndpointConfigs')
ListEndpoints = Action('ListEndpoints')
ListHyperParameterTuningJobs = Action('ListHyperParameterTuningJobs')
ListLabelingJobs = Action('ListLabelingJobs')
ListLabelingJobForWorkteam = Action('ListLabelingJobForWorkteam')
ListModels = Action('ListModels')
ListNotebookInstances = Action('ListNotebookInstances')
ListSubscribedWorkteams = Action('ListSubscribedWorkteams')
ListTags = Action('ListTags')
ListTrainingJobs = Action('ListTrainingJobs')
ListTrainingJobsForHyperParameterTuningJob = \
    Action('ListTrainingJobsForHyperParameterTuningJob')
ListTransformJobs = Action('ListTransformJobs')
ListWorkteams = Action('ListWorkteams')
StartNotebookInstance = Action('StartNotebookInstance')
StopLabelingJob = Action('StopLabelingJob')
StopHyperParameterTuningJob = Action('StopHyperParameterTuningJob')
StopNotebookInstance = Action('StopNotebookInstance')
StopTrainingJob = Action('StopTrainingJob')
StopTransformJob = Action('StopTransformJob')
UpdateEndpoint = Action('UpdateEndpoint')
UpdateEndpointWeightsAndCapacities = \
    Action('UpdateEndpointWeightsAndCapacities')
UpdateNotebookInstance = Action('UpdateNotebookInstance')
UpdateWorkteam = Action('UpdateWorkteam')
