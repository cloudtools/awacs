# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elemental MediaPackage'
prefix = 'mediapackage'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateChannel = Action('CreateChannel')
CreateOriginEndpoint = Action('CreateOriginEndpoint')
DeleteChannel = Action('DeleteChannel')
DeleteOriginEndpoint = Action('DeleteOriginEndpoint')
DescribeChannel = Action('DescribeChannel')
DescribeOriginEndpoint = Action('DescribeOriginEndpoint')
ListChannels = Action('ListChannels')
ListOriginEndpoints = Action('ListOriginEndpoints')
ListTagsForResource = Action('ListTagsForResource')
RotateIngestEndpointCredentials = \
    Action('RotateIngestEndpointCredentials')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateChannel = Action('UpdateChannel')
UpdateOriginEndpoint = Action('UpdateOriginEndpoint')
