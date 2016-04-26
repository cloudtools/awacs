# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Kinesis Firehose'
prefix = 'firehose'

CreateDeliveryStream = Action(prefix, 'CreateDeliveryStream')
DeleteDeliveryStream = Action(prefix, 'DeleteDeliveryStream')
DescribeDeliveryStream = Action(prefix, 'DescribeDeliveryStream')
ListDeliveryStreams = Action(prefix, 'ListDeliveryStreams')
PutRecord = Action(prefix, 'PutRecord')
PutRecordBatch = Action(prefix, 'PutRecordBatch')
UpdateDestination = Action(prefix, 'UpdateDestination')
