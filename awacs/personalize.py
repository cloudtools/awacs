# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Personalize'
prefix = 'personalize'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateBatchInferenceJob = Action('CreateBatchInferenceJob')
CreateCampaign = Action('CreateCampaign')
CreateDataset = Action('CreateDataset')
CreateDatasetGroup = Action('CreateDatasetGroup')
CreateDatasetImportJob = Action('CreateDatasetImportJob')
CreateEventTracker = Action('CreateEventTracker')
CreateFilter = Action('CreateFilter')
CreateSchema = Action('CreateSchema')
CreateSolution = Action('CreateSolution')
CreateSolutionVersion = Action('CreateSolutionVersion')
DeleteCampaign = Action('DeleteCampaign')
DeleteDataset = Action('DeleteDataset')
DeleteDatasetGroup = Action('DeleteDatasetGroup')
DeleteEventTracker = Action('DeleteEventTracker')
DeleteFilter = Action('DeleteFilter')
DeleteSchema = Action('DeleteSchema')
DeleteSolution = Action('DeleteSolution')
DescribeAlgorithm = Action('DescribeAlgorithm')
DescribeBatchInferenceJob = Action('DescribeBatchInferenceJob')
DescribeCampaign = Action('DescribeCampaign')
DescribeDataset = Action('DescribeDataset')
DescribeDatasetGroup = Action('DescribeDatasetGroup')
DescribeDatasetImportJob = Action('DescribeDatasetImportJob')
DescribeEventTracker = Action('DescribeEventTracker')
DescribeFeatureTransformation = Action('DescribeFeatureTransformation')
DescribeFilter = Action('DescribeFilter')
DescribeRecipe = Action('DescribeRecipe')
DescribeSchema = Action('DescribeSchema')
DescribeSolution = Action('DescribeSolution')
DescribeSolutionVersion = Action('DescribeSolutionVersion')
GetPersonalizedRanking = Action('GetPersonalizedRanking')
GetRecommendations = Action('GetRecommendations')
GetSolutionMetrics = Action('GetSolutionMetrics')
ListBatchInferenceJobs = Action('ListBatchInferenceJobs')
ListCampaigns = Action('ListCampaigns')
ListDatasetGroups = Action('ListDatasetGroups')
ListDatasetImportJobs = Action('ListDatasetImportJobs')
ListDatasets = Action('ListDatasets')
ListEventTrackers = Action('ListEventTrackers')
ListFilters = Action('ListFilters')
ListRecipes = Action('ListRecipes')
ListSchemas = Action('ListSchemas')
ListSolutionVersions = Action('ListSolutionVersions')
ListSolutions = Action('ListSolutions')
PutEvents = Action('PutEvents')
UpdateCampaign = Action('UpdateCampaign')
