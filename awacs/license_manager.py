# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS License Manager'
prefix = 'license-manager'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateLicenseConfiguration = Action('CreateLicenseConfiguration')
DeleteLicenseConfiguration = Action('DeleteLicenseConfiguration')
GetLicenseConfiguration = Action('GetLicenseConfiguration')
GetServiceSettings = Action('GetServiceSettings')
ListAssociationsForLicenseConfiguration = \
    Action('ListAssociationsForLicenseConfiguration')
ListLicenseConfigurations = Action('ListLicenseConfigurations')
ListLicenseSpecificationsForResource = \
    Action('ListLicenseSpecificationsForResource')
ListResourceInventory = Action('ListResourceInventory')
ListTagsForResource = Action('ListTagsForResource')
ListUsageForLicenseConfiguration = \
    Action('ListUsageForLicenseConfiguration')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateLicenseConfiguration = Action('UpdateLicenseConfiguration')
UpdateLicenseSpecificationsForResource = \
    Action('UpdateLicenseSpecificationsForResource')
UpdateServiceSettings = Action('UpdateServiceSettings')
