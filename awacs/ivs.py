# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Interactive Video Service'
prefix = 'ivs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetChannel = Action('BatchGetChannel')
BatchGetStreamKey = Action('BatchGetStreamKey')
CreateChannel = Action('CreateChannel')
CreateStreamKey = Action('CreateStreamKey')
DeleteChannel = Action('DeleteChannel')
DeletePlaybackKeyPair = Action('DeletePlaybackKeyPair')
DeleteStreamKey = Action('DeleteStreamKey')
GetChannel = Action('GetChannel')
GetPlaybackKeyPair = Action('GetPlaybackKeyPair')
GetStream = Action('GetStream')
GetStreamKey = Action('GetStreamKey')
ImportPlaybackKeyPair = Action('ImportPlaybackKeyPair')
ListChannels = Action('ListChannels')
ListPlaybackKeyPairs = Action('ListPlaybackKeyPairs')
ListStreamKeys = Action('ListStreamKeys')
ListStreams = Action('ListStreams')
ListTagsForResource = Action('ListTagsForResource')
PutMetadata = Action('PutMetadata')
StopStream = Action('StopStream')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateChannel = Action('UpdateChannel')
