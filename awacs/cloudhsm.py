# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CloudHSM'
prefix = 'cloudhsm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToResource = Action('AddTagsToResource')
CreateLunaClient = Action('CreateLunaClient')
CreateHapg = Action('CreateHapg')
CreateHsm = Action('CreateHsm')
DeleteLunaClient = Action('DeleteLunaClient')
DeleteHapg = Action('DeleteHapg')
DeleteHsm = Action('DeleteHsm')
DescribeLunaClient = Action('DescribeLunaClient')
DescribeHapg = Action('DescribeHapg')
DescribeHsm = Action('DescribeHsm')
GetConfig = Action('GetConfig')
ListAvailableZones = Action('ListAvailableZones')
ListLunaClients = Action('ListLunaClients')
ListHapgs = Action('ListHapgs')
ListHsms = Action('ListHsms')
ListTagsForResource = Action('ListTagsForResource')
ModifyLunaClient = Action('ModifyLunaClient')
ModifyHapg = Action('ModifyHapg')
ModifyHsm = Action('ModifyHsm')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
