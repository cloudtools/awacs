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
CreateAlgorithm = Action('CreateAlgorithm')
CreateCodeRepository = Action('CreateCodeRepository')
CreateCompilationJob = Action('CreateCompilationJob')
CreateEndpoint = Action('CreateEndpoint')
CreateEndpointConfig = Action('CreateEndpointConfig')
CreateHyperParameterTuningJob = Action('CreateHyperParameterTuningJob')
CreateLabelingJob = Action('CreateLabelingJob')
CreateModel = Action('CreateModel')
CreateModelPackage = Action('CreateModelPackage')
CreateNotebookInstance = Action('CreateNotebookInstance')
CreateNotebookInstanceLifecycleConfig = \
    Action('CreateNotebookInstanceLifecycleConfig')
CreatePresignedNotebookInstanceUrl = \
    Action('CreatePresignedNotebookInstanceUrl')
CreateTrainingJob = Action('CreateTrainingJob')
CreateTransformJob = Action('CreateTransformJob')
CreateWorkteam = Action('CreateWorkteam')
DeleteAlgorithm = Action('DeleteAlgorithm')
DeleteCodeRepository = Action('DeleteCodeRepository')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteEndpointConfig = Action('DeleteEndpointConfig')
DeleteModel = Action('DeleteModel')
DeleteModelPackage = Action('DeleteModelPackage')
DeleteNotebookInstance = Action('DeleteNotebookInstance')
DeleteNotebookInstanceLifecycleConfig = \
    Action('DeleteNotebookInstanceLifecycleConfig')
DeleteTags = Action('DeleteTags')
DeleteWorkteam = Action('DeleteWorkteam')
DescribeAlgorithm = Action('DescribeAlgorithm')
DescribeCodeRepository = Action('DescribeCodeRepository')
DescribeCompilationJob = Action('DescribeCompilationJob')
DescribeEndpoint = Action('DescribeEndpoint')
DescribeEndpointConfig = Action('DescribeEndpointConfig')
DescribeHyperParameterTuningJob = \
    Action('DescribeHyperParameterTuningJob')
DescribeLabelingJob = Action('DescribeLabelingJob')
DescribeModel = Action('DescribeModel')
DescribeModelPackage = Action('DescribeModelPackage')
DescribeNotebookInstance = Action('DescribeNotebookInstance')
DescribeNotebookInstanceLifecycleConfig = \
    Action('DescribeNotebookInstanceLifecycleConfig')
DescribeSubscribedWorkteam = Action('DescribeSubscribedWorkteam')
DescribeTrainingJob = Action('DescribeTrainingJob')
DescribeTransformJob = Action('DescribeTransformJob')
DescribeWorkteam = Action('DescribeWorkteam')
GetSearchSuggestions = Action('GetSearchSuggestions')
InvokeEndpoint = Action('InvokeEndpoint')
ListAlgorithms = Action('ListAlgorithms')
ListCodeRepositories = Action('ListCodeRepositories')
ListCompilationJobs = Action('ListCompilationJobs')
ListEndpointConfigs = Action('ListEndpointConfigs')
ListEndpoints = Action('ListEndpoints')
ListHyperParameterTuningJobs = Action('ListHyperParameterTuningJobs')
ListLabelingJobs = Action('ListLabelingJobs')
ListLabelingJobsForWorkteam = Action('ListLabelingJobsForWorkteam')
ListModelPackages = Action('ListModelPackages')
ListModels = Action('ListModels')
ListNotebookInstanceLifecycleConfigs = \
    Action('ListNotebookInstanceLifecycleConfigs')
ListNotebookInstances = Action('ListNotebookInstances')
ListSubscribedWorkteams = Action('ListSubscribedWorkteams')
ListTags = Action('ListTags')
ListTrainingJobs = Action('ListTrainingJobs')
ListTrainingJobsForHyperParameterTuningJob = \
    Action('ListTrainingJobsForHyperParameterTuningJob')
ListTransformJobs = Action('ListTransformJobs')
ListWorkteams = Action('ListWorkteams')
RenderUiTemplate = Action('RenderUiTemplate')
Search = Action('Search')
StartNotebookInstance = Action('StartNotebookInstance')
StopCompilationJob = Action('StopCompilationJob')
StopHyperParameterTuningJob = Action('StopHyperParameterTuningJob')
StopLabelingJob = Action('StopLabelingJob')
StopNotebookInstance = Action('StopNotebookInstance')
StopTrainingJob = Action('StopTrainingJob')
StopTransformJob = Action('StopTransformJob')
UpdateCodeRepository = Action('UpdateCodeRepository')
UpdateEndpoint = Action('UpdateEndpoint')
UpdateEndpointWeightsAndCapacities = \
    Action('UpdateEndpointWeightsAndCapacities')
UpdateNotebookInstance = Action('UpdateNotebookInstance')
UpdateNotebookInstanceLifecycleConfig = \
    Action('UpdateNotebookInstanceLifecycleConfig')
UpdateWorkteam = Action('UpdateWorkteam')
