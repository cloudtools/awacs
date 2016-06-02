# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Cognito Sync'
prefix = 'cognito-sync'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BulkPublish = Action('BulkPublish')
DeleteDataset = Action('DeleteDataset')
DescribeDataset = Action('DescribeDataset')
DescribeIdentityUsage = Action('DescribeIdentityUsage')
DescribeIdentityPoolUsage = Action('DescribeIdentityPoolUsage')
GetBulkPublishDetails = Action('GetBulkPublishDetails')
GetCognitoEvents = Action('GetCognitoEvents')
GetIdentityPoolConfiguration = Action('GetIdentityPoolConfiguration')
ListDatasets = Action('ListDatasets')
ListIdentityPoolUsage = Action('ListIdentityPoolUsage')
ListRecords = Action('ListRecords')
RegisterDevice = Action('RegisterDevice')
SetCognitoEvents = Action('SetCognitoEvents')
SetIdentityPoolConfiguration = Action('SetIdentityPoolConfiguration')
SubscribeToDataset = Action('SubscribeToDataset')
UpdateRecords = Action('UpdateRecords')
UnsubscribeFromDataset = Action('UnsubscribeFromDataset')
