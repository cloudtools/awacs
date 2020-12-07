# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Forecast'
prefix = 'forecast'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateDataset = Action('CreateDataset')
CreateDatasetGroup = Action('CreateDatasetGroup')
CreateDatasetImportJob = Action('CreateDatasetImportJob')
CreateForecast = Action('CreateForecast')
CreateForecastExportJob = Action('CreateForecastExportJob')
CreatePredictor = Action('CreatePredictor')
CreatePredictorBacktestExportJob = \
    Action('CreatePredictorBacktestExportJob')
DeleteDataset = Action('DeleteDataset')
DeleteDatasetGroup = Action('DeleteDatasetGroup')
DeleteDatasetImportJob = Action('DeleteDatasetImportJob')
DeleteForecast = Action('DeleteForecast')
DeleteForecastExportJob = Action('DeleteForecastExportJob')
DeletePredictor = Action('DeletePredictor')
DeletePredictorBacktestExportJob = \
    Action('DeletePredictorBacktestExportJob')
DescribeDataset = Action('DescribeDataset')
DescribeDatasetGroup = Action('DescribeDatasetGroup')
DescribeDatasetImportJob = Action('DescribeDatasetImportJob')
DescribeForecast = Action('DescribeForecast')
DescribeForecastExportJob = Action('DescribeForecastExportJob')
DescribePredictor = Action('DescribePredictor')
DescribePredictorBacktestExportJob = \
    Action('DescribePredictorBacktestExportJob')
GetAccuracyMetrics = Action('GetAccuracyMetrics')
ListDatasetGroups = Action('ListDatasetGroups')
ListDatasetImportJobs = Action('ListDatasetImportJobs')
ListDatasets = Action('ListDatasets')
ListForecastExportJobs = Action('ListForecastExportJobs')
ListForecasts = Action('ListForecasts')
ListPredictorBacktestExportJobs = \
    Action('ListPredictorBacktestExportJobs')
ListPredictors = Action('ListPredictors')
ListTagsForResource = Action('ListTagsForResource')
QueryForecast = Action('QueryForecast')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDatasetGroup = Action('UpdateDatasetGroup')
