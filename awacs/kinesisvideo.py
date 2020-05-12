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


ConnectAsMaster = Action('ConnectAsMaster')
ConnectAsViewer = Action('ConnectAsViewer')
CreateSignalingChannel = Action('CreateSignalingChannel')
CreateStream = Action('CreateStream')
DeleteSignalingChannel = Action('DeleteSignalingChannel')
DeleteStream = Action('DeleteStream')
DescribeSignalingChannel = Action('DescribeSignalingChannel')
DescribeStream = Action('DescribeStream')
GetClip = Action('GetClip')
GetDASHStreamingSessionURL = Action('GetDASHStreamingSessionURL')
GetDataEndpoint = Action('GetDataEndpoint')
GetHLSStreamingSessionURL = Action('GetHLSStreamingSessionURL')
GetIceServerConfig = Action('GetIceServerConfig')
GetMedia = Action('GetMedia')
GetMediaForFragmentList = Action('GetMediaForFragmentList')
GetSignalingChannelEndpoint = Action('GetSignalingChannelEndpoint')
ListFragments = Action('ListFragments')
ListSignalingChannels = Action('ListSignalingChannels')
ListStreams = Action('ListStreams')
ListTagsForResource = Action('ListTagsForResource')
ListTagsForStream = Action('ListTagsForStream')
PutMedia = Action('PutMedia')
SendAlexaOfferToMaster = Action('SendAlexaOfferToMaster')
TagResource = Action('TagResource')
TagStream = Action('TagStream')
UntagResource = Action('UntagResource')
UntagStream = Action('UntagStream')
UpdateDataRetention = Action('UpdateDataRetention')
UpdateSignalingChannel = Action('UpdateSignalingChannel')
UpdateStream = Action('UpdateStream')
