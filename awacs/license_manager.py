# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS License Manager"
prefix = "license-manager"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptGrant = Action("AcceptGrant")
CheckInLicense = Action("CheckInLicense")
CheckoutBorrowLicense = Action("CheckoutBorrowLicense")
CheckoutLicense = Action("CheckoutLicense")
CreateGrant = Action("CreateGrant")
CreateGrantVersion = Action("CreateGrantVersion")
CreateLicense = Action("CreateLicense")
CreateLicenseAssetGroup = Action("CreateLicenseAssetGroup")
CreateLicenseAssetRuleset = Action("CreateLicenseAssetRuleset")
CreateLicenseConfiguration = Action("CreateLicenseConfiguration")
CreateLicenseConversionTaskForResource = Action(
    "CreateLicenseConversionTaskForResource"
)
CreateLicenseManagerReportGenerator = Action("CreateLicenseManagerReportGenerator")
CreateLicenseVersion = Action("CreateLicenseVersion")
CreateToken = Action("CreateToken")
DeleteGrant = Action("DeleteGrant")
DeleteLicense = Action("DeleteLicense")
DeleteLicenseAssetGroup = Action("DeleteLicenseAssetGroup")
DeleteLicenseAssetRuleset = Action("DeleteLicenseAssetRuleset")
DeleteLicenseConfiguration = Action("DeleteLicenseConfiguration")
DeleteLicenseManagerReportGenerator = Action("DeleteLicenseManagerReportGenerator")
DeleteToken = Action("DeleteToken")
ExtendLicenseConsumption = Action("ExtendLicenseConsumption")
GetAccessToken = Action("GetAccessToken")
GetGrant = Action("GetGrant")
GetLicense = Action("GetLicense")
GetLicenseAssetGroup = Action("GetLicenseAssetGroup")
GetLicenseAssetRuleset = Action("GetLicenseAssetRuleset")
GetLicenseConfiguration = Action("GetLicenseConfiguration")
GetLicenseConversionTask = Action("GetLicenseConversionTask")
GetLicenseManagerReportGenerator = Action("GetLicenseManagerReportGenerator")
GetLicenseUsage = Action("GetLicenseUsage")
GetServiceSettings = Action("GetServiceSettings")
ListAssetsForLicenseAssetGroup = Action("ListAssetsForLicenseAssetGroup")
ListAssociationsForLicenseConfiguration = Action(
    "ListAssociationsForLicenseConfiguration"
)
ListDistributedGrants = Action("ListDistributedGrants")
ListFailuresForLicenseConfigurationOperations = Action(
    "ListFailuresForLicenseConfigurationOperations"
)
ListLicenseAssetGroups = Action("ListLicenseAssetGroups")
ListLicenseAssetRulesets = Action("ListLicenseAssetRulesets")
ListLicenseConfigurations = Action("ListLicenseConfigurations")
ListLicenseConfigurationsForOrganization = Action(
    "ListLicenseConfigurationsForOrganization"
)
ListLicenseConversionTasks = Action("ListLicenseConversionTasks")
ListLicenseManagerReportGenerators = Action("ListLicenseManagerReportGenerators")
ListLicenseSpecificationsForResource = Action("ListLicenseSpecificationsForResource")
ListLicenseVersions = Action("ListLicenseVersions")
ListLicenses = Action("ListLicenses")
ListReceivedGrants = Action("ListReceivedGrants")
ListReceivedGrantsForOrganization = Action("ListReceivedGrantsForOrganization")
ListReceivedLicenses = Action("ListReceivedLicenses")
ListReceivedLicensesForOrganization = Action("ListReceivedLicensesForOrganization")
ListResourceInventory = Action("ListResourceInventory")
ListTagsForResource = Action("ListTagsForResource")
ListTokens = Action("ListTokens")
ListUsageForLicenseConfiguration = Action("ListUsageForLicenseConfiguration")
RejectGrant = Action("RejectGrant")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLicenseAssetGroup = Action("UpdateLicenseAssetGroup")
UpdateLicenseAssetRuleset = Action("UpdateLicenseAssetRuleset")
UpdateLicenseConfiguration = Action("UpdateLicenseConfiguration")
UpdateLicenseManagerReportGenerator = Action("UpdateLicenseManagerReportGenerator")
UpdateLicenseSpecificationsForResource = Action(
    "UpdateLicenseSpecificationsForResource"
)
UpdateServiceSettings = Action("UpdateServiceSettings")
