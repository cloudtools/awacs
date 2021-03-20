# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

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


AcceptGrant = Action('AcceptGrant')
CheckInLicense = Action('CheckInLicense')
CheckoutBorrowLicense = Action('CheckoutBorrowLicense')
CheckoutLicense = Action('CheckoutLicense')
CreateGrant = Action('CreateGrant')
CreateGrantVersion = Action('CreateGrantVersion')
CreateLicense = Action('CreateLicense')
CreateLicenseConfiguration = Action('CreateLicenseConfiguration')
CreateLicenseVersion = Action('CreateLicenseVersion')
CreateToken = Action('CreateToken')
DeleteGrant = Action('DeleteGrant')
DeleteLicense = Action('DeleteLicense')
DeleteLicenseConfiguration = Action('DeleteLicenseConfiguration')
DeleteToken = Action('DeleteToken')
ExtendLicenseConsumption = Action('ExtendLicenseConsumption')
GetAccessToken = Action('GetAccessToken')
GetGrant = Action('GetGrant')
GetLicense = Action('GetLicense')
GetLicenseConfiguration = Action('GetLicenseConfiguration')
GetLicenseUsage = Action('GetLicenseUsage')
GetServiceSettings = Action('GetServiceSettings')
ListAssociationsForLicenseConfiguration = \
    Action('ListAssociationsForLicenseConfiguration')
ListDistributedGrants = Action('ListDistributedGrants')
ListFailuresForLicenseConfigurationOperations = \
    Action('ListFailuresForLicenseConfigurationOperations')
ListLicenseConfigurations = Action('ListLicenseConfigurations')
ListLicenseSpecificationsForResource = \
    Action('ListLicenseSpecificationsForResource')
ListLicenseVersions = Action('ListLicenseVersions')
ListLicenses = Action('ListLicenses')
ListReceivedGrants = Action('ListReceivedGrants')
ListReceivedLicenses = Action('ListReceivedLicenses')
ListResourceInventory = Action('ListResourceInventory')
ListTagsForResource = Action('ListTagsForResource')
ListTokens = Action('ListTokens')
ListUsageForLicenseConfiguration = \
    Action('ListUsageForLicenseConfiguration')
RejectGrant = Action('RejectGrant')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateLicenseConfiguration = Action('UpdateLicenseConfiguration')
UpdateLicenseSpecificationsForResource = \
    Action('UpdateLicenseSpecificationsForResource')
UpdateServiceSettings = Action('UpdateServiceSettings')
