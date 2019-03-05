# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Kinesis Video Streams'
prefix = 'kinesisvideo'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateStream = Action('CreateStream')
DeleteStream = Action('DeleteStream')
DescribeStream = Action('DescribeStream')
GetDataEndpoint = Action('GetDataEndpoint')
GetHLSStreamingSessionURL = Action('GetHLSStreamingSessionURL')
GetMedia = Action('GetMedia')
GetMediaForFragmentList = Action('GetMediaForFragmentList')
ListFragments = Action('ListFragments')
ListStreams = Action('ListStreams')
ListTagsForStream = Action('ListTagsForStream')
PutMedia = Action('PutMedia')
TagStream = Action('TagStream')
UntagStream = Action('UntagStream')
UpdateDataRetention = Action('UpdateDataRetention')
UpdateStream = Action('UpdateStream')
