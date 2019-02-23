# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Kinesis Firehose'
prefix = 'firehose'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateDeliveryStream = Action('CreateDeliveryStream')
DeleteDeliveryStream = Action('DeleteDeliveryStream')
DescribeDeliveryStream = Action('DescribeDeliveryStream')
ListDeliveryStreams = Action('ListDeliveryStreams')
ListTagsForDeliveryStream = Action('ListTagsForDeliveryStream')
PutRecord = Action('PutRecord')
PutRecordBatch = Action('PutRecordBatch')
StartDeliveryStreamEncryption = Action('StartDeliveryStreamEncryption')
StopDeliveryStreamEncryption = Action('StopDeliveryStreamEncryption')
TagDeliveryStream = Action('TagDeliveryStream')
UntagDeliveryStream = Action('UntagDeliveryStream')
UpdateDestination = Action('UpdateDestination')
