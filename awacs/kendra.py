# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Kendra'
prefix = 'kendra'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchDeleteDocument = Action('BatchDeleteDocument')
BatchPutDocument = Action('BatchPutDocument')
CreateDataSource = Action('CreateDataSource')
CreateFaq = Action('CreateFaq')
CreateIndex = Action('CreateIndex')
DeleteDataSource = Action('DeleteDataSource')
DeleteFaq = Action('DeleteFaq')
DeleteIndex = Action('DeleteIndex')
DescribeDataSource = Action('DescribeDataSource')
DescribeFaq = Action('DescribeFaq')
DescribeIndex = Action('DescribeIndex')
ListDataSourceSyncJobs = Action('ListDataSourceSyncJobs')
ListDataSources = Action('ListDataSources')
ListFaqs = Action('ListFaqs')
ListIndices = Action('ListIndices')
ListTagsForResource = Action('ListTagsForResource')
Query = Action('Query')
StartDataSourceSyncJob = Action('StartDataSourceSyncJob')
StopDataSourceSyncJob = Action('StopDataSourceSyncJob')
SubmitFeedback = Action('SubmitFeedback')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDataSource = Action('UpdateDataSource')
UpdateIndex = Action('UpdateIndex')
