# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT Analytics'
prefix = 'iotanalytics'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateChannel = Action('CreateChannel')
CreateDataset = Action('CreateDataset')
CreateDatasetContent = Action('CreateDatasetContent')
CreateDatastore = Action('CreateDatastore')
CreatePipeline = Action('CreatePipeline')
DeleteChannel = Action('DeleteChannel')
DeleteDataset = Action('DeleteDataset')
DeleteDatasetContent = Action('DeleteDatasetContent')
DeleteDatastore = Action('DeleteDatastore')
DeletePipeline = Action('DeletePipeline')
DescribeChannel = Action('DescribeChannel')
DescribeDataset = Action('DescribeDataset')
DescribeDatastore = Action('DescribeDatastore')
DescribePipeline = Action('DescribePipeline')
GetDatasetContent = Action('GetDatasetContent')
ListChannels = Action('ListChannels')
ListDatasets = Action('ListDatasets')
ListDatastores = Action('ListDatastores')
ListPipelines = Action('ListPipelines')
UpdateDataset = Action('UpdateDataset')
UpdatePipeline = Action('UpdatePipeline')
