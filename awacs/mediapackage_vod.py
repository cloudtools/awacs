# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elemental MediaPackage VOD'
prefix = 'mediapackage-vod'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAsset = Action('CreateAsset')
CreatePackagingConfiguration = Action('CreatePackagingConfiguration')
CreatePackagingGroup = Action('CreatePackagingGroup')
DeleteAsset = Action('DeleteAsset')
DeletePackagingConfiguration = Action('DeletePackagingConfiguration')
DeletePackagingGroup = Action('DeletePackagingGroup')
DescribeAsset = Action('DescribeAsset')
DescribePackagingConfiguration = Action('DescribePackagingConfiguration')
DescribePackagingGroup = Action('DescribePackagingGroup')
ListAssets = Action('ListAssets')
ListPackagingConfigurations = Action('ListPackagingConfigurations')
ListPackagingGroups = Action('ListPackagingGroups')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
