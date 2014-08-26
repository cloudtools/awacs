# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Kinesis'
prefix = 'kinesis'

CreateStream = Action(prefix, 'CreateStream')
DeleteStream = Action(prefix, 'DeleteStream')
DescribeStream = Action(prefix, 'DescribeStream')
ListStreams = Action(prefix, 'ListStreams')
PutRecord = Action(prefix, 'PutRecord')
GetShardIterator = Action(prefix, 'GetShardIterator')
GetRecords = Action(prefix, 'GetRecords')
MergeShards = Action(prefix, 'MergeShards')
SplitShard = Action(prefix, 'SplitShard')
