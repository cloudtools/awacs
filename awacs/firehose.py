# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, BaseARN

service_name = 'Amazon Kinesis Firehose'
prefix = 'firehose'


class ARN(BaseARN):
    def __init__(self, resource, region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class FirehoseAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action

CreateDeliveryStream = Action(prefix, 'CreateDeliveryStream')
DeleteDeliveryStream = Action(prefix, 'DeleteDeliveryStream')
DescribeDeliveryStream = Action(prefix, 'DescribeDeliveryStream')
ListDeliveryStreams = Action(prefix, 'ListDeliveryStreams')
PutRecord = Action(prefix, 'PutRecord')
PutRecordBatch = Action(prefix, 'PutRecordBatch')
UpdateDestination = Action(prefix, 'UpdateDestination')
