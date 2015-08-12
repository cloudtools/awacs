# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Kinesis'
prefix = 'kinesis'


class KinesisAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action

AddTagsToStream = KinesisAction('AddTagsToStream')
CreateStream = KinesisAction('CreateStream')
DeleteStream = KinesisAction('DeleteStream')
DescribeStream = KinesisAction('DescribeStream')
GetShardIterator = KinesisAction('GetShardIterator')
GetRecords = KinesisAction('GetRecords')
ListStreams = KinesisAction('ListStreams')
ListTagsForStream = KinesisAction('ListTagsForStream')
MergeShards = KinesisAction('MergeShards')
PutRecord = KinesisAction('PutRecord')
PutRecords = KinesisAction('PutRecords')
RemoveTagsFromStream = KinesisAction('RemoveTagsFromStream')
SplitShard = KinesisAction('SplitShard')
