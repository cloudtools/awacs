# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Kinesis'
prefix = 'kinesis'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToStream = Action('AddTagsToStream')
CreateStream = Action('CreateStream')
DecreaseStreamRetentionPeriod = Action('DecreaseStreamRetentionPeriod')
DeleteStream = Action('DeleteStream')
DescribeLimits = Action('DescribeLimits')
DescribeStream = Action('DescribeStream')
DisableEnhancedMonitoring = Action('DisableEnhancedMonitoring')
EnableEnhancedMonitoring = Action('EnableEnhancedMonitoring')
GetRecords = Action('GetRecords')
GetShardIterator = Action('GetShardIterator')
IncreaseStreamRetentionPeriod = Action('IncreaseStreamRetentionPeriod')
ListStreams = Action('ListStreams')
ListTagsForStream = Action('ListTagsForStream')
MergeShards = Action('MergeShards')
PutRecord = Action('PutRecord')
PutRecords = Action('PutRecords')
RemoveTagsFromStream = Action('RemoveTagsFromStream')
SplitShard = Action('SplitShard')
StartStreamEncryption = Action('StartStreamEncryption')
StopStreamEncryption = Action('StopStreamEncryption')
UpdateShardCount = Action('UpdateShardCount')
