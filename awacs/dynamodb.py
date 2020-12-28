# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon DynamoDB'
prefix = 'dynamodb'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetItem = Action('BatchGetItem')
BatchWriteItem = Action('BatchWriteItem')
ConditionCheckItem = Action('ConditionCheckItem')
CreateBackup = Action('CreateBackup')
CreateGlobalTable = Action('CreateGlobalTable')
CreateTable = Action('CreateTable')
CreateTableReplica = Action('CreateTableReplica')
DeleteBackup = Action('DeleteBackup')
DeleteItem = Action('DeleteItem')
DeleteTable = Action('DeleteTable')
DeleteTableReplica = Action('DeleteTableReplica')
DescribeBackup = Action('DescribeBackup')
DescribeContinuousBackups = Action('DescribeContinuousBackups')
DescribeContributorInsights = Action('DescribeContributorInsights')
DescribeExport = Action('DescribeExport')
DescribeGlobalTable = Action('DescribeGlobalTable')
DescribeGlobalTableSettings = Action('DescribeGlobalTableSettings')
DescribeKinesisStreamingDestination = \
    Action('DescribeKinesisStreamingDestination')
DescribeLimits = Action('DescribeLimits')
DescribeReservedCapacity = Action('DescribeReservedCapacity')
DescribeReservedCapacityOfferings = \
    Action('DescribeReservedCapacityOfferings')
DescribeStream = Action('DescribeStream')
DescribeTable = Action('DescribeTable')
DescribeTableReplicaAutoScaling = \
    Action('DescribeTableReplicaAutoScaling')
DescribeTimeToLive = Action('DescribeTimeToLive')
DisableKinesisStreamingDestination = \
    Action('DisableKinesisStreamingDestination')
EnableKinesisStreamingDestination = \
    Action('EnableKinesisStreamingDestination')
ExportTableToPointInTime = Action('ExportTableToPointInTime')
GetItem = Action('GetItem')
GetRecords = Action('GetRecords')
GetShardIterator = Action('GetShardIterator')
ListBackups = Action('ListBackups')
ListContributorInsights = Action('ListContributorInsights')
ListExports = Action('ListExports')
ListGlobalTables = Action('ListGlobalTables')
ListStreams = Action('ListStreams')
ListTables = Action('ListTables')
ListTagsOfResource = Action('ListTagsOfResource')
PartiQLDelete = Action('PartiQLDelete')
PartiQLInsert = Action('PartiQLInsert')
PartiQLSelect = Action('PartiQLSelect')
PartiQLUpdate = Action('PartiQLUpdate')
PurchaseReservedCapacityOfferings = \
    Action('PurchaseReservedCapacityOfferings')
PutItem = Action('PutItem')
Query = Action('Query')
RestoreTableFromBackup = Action('RestoreTableFromBackup')
RestoreTableToPointInTime = Action('RestoreTableToPointInTime')
Scan = Action('Scan')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateContinuousBackups = Action('UpdateContinuousBackups')
UpdateContributorInsights = Action('UpdateContributorInsights')
UpdateGlobalTable = Action('UpdateGlobalTable')
UpdateGlobalTableSettings = Action('UpdateGlobalTableSettings')
UpdateItem = Action('UpdateItem')
UpdateTable = Action('UpdateTable')
UpdateTableReplicaAutoScaling = Action('UpdateTableReplicaAutoScaling')
UpdateTimeToLive = Action('UpdateTimeToLive')
