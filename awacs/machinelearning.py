# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Machine Learning'
prefix = 'machinelearning'


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
CreateBatchPrediction = Action('CreateBatchPrediction')
CreateDataSourceFromRDS = Action('CreateDataSourceFromRDS')
CreateDataSourceFromRedshift = Action('CreateDataSourceFromRedshift')
CreateDataSourceFromS3 = Action('CreateDataSourceFromS3')
CreateEvaluation = Action('CreateEvaluation')
CreateMLModel = Action('CreateMLModel')
CreateRealtimeEndpoint = Action('CreateRealtimeEndpoint')
DeleteBatchPrediction = Action('DeleteBatchPrediction')
DeleteDataSource = Action('DeleteDataSource')
DeleteEvaluation = Action('DeleteEvaluation')
DeleteMLModel = Action('DeleteMLModel')
DeleteRealtimeEndpoint = Action('DeleteRealtimeEndpoint')
DeleteTags = Action('DeleteTags')
DescribeBatchPredictions = Action('DescribeBatchPredictions')
DescribeDataSources = Action('DescribeDataSources')
DescribeEvaluations = Action('DescribeEvaluations')
DescribeMLModels = Action('DescribeMLModels')
DescribeTags = Action('DescribeTags')
GetBatchPrediction = Action('GetBatchPrediction')
GetDataSource = Action('GetDataSource')
GetEvaluation = Action('GetEvaluation')
GetMLModel = Action('GetMLModel')
Predict = Action('Predict')
UpdateBatchPrediction = Action('UpdateBatchPrediction')
UpdateDataSource = Action('UpdateDataSource')
UpdateEvaluation = Action('UpdateEvaluation')
UpdateMLModel = Action('UpdateMLModel')
