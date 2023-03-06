# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Control Tower"
prefix = "controltower"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateManagedAccount = Action("CreateManagedAccount")
DeleteLandingZone = Action("DeleteLandingZone")
DeregisterManagedAccount = Action("DeregisterManagedAccount")
DeregisterOrganizationalUnit = Action("DeregisterOrganizationalUnit")
DescribeAccountFactoryConfig = Action("DescribeAccountFactoryConfig")
DescribeCoreService = Action("DescribeCoreService")
DescribeGuardrail = Action("DescribeGuardrail")
DescribeGuardrailForTarget = Action("DescribeGuardrailForTarget")
DescribeLandingZoneConfiguration = Action("DescribeLandingZoneConfiguration")
DescribeManagedAccount = Action("DescribeManagedAccount")
DescribeManagedOrganizationalUnit = Action("DescribeManagedOrganizationalUnit")
DescribeRegisterOrganizationalUnitOperation = Action(
    "DescribeRegisterOrganizationalUnitOperation"
)
DescribeSingleSignOn = Action("DescribeSingleSignOn")
DisableControl = Action("DisableControl")
DisableGuardrail = Action("DisableGuardrail")
EnableControl = Action("EnableControl")
EnableGuardrail = Action("EnableGuardrail")
GetAccountInfo = Action("GetAccountInfo")
GetAvailableUpdates = Action("GetAvailableUpdates")
GetControlOperation = Action("GetControlOperation")
GetGuardrailComplianceStatus = Action("GetGuardrailComplianceStatus")
GetHomeRegion = Action("GetHomeRegion")
GetLandingZoneDriftStatus = Action("GetLandingZoneDriftStatus")
GetLandingZoneStatus = Action("GetLandingZoneStatus")
ListDirectoryGroups = Action("ListDirectoryGroups")
ListDriftDetails = Action("ListDriftDetails")
ListEnabledControls = Action("ListEnabledControls")
ListEnabledGuardrails = Action("ListEnabledGuardrails")
ListExtendGovernancePrecheckDetails = Action("ListExtendGovernancePrecheckDetails")
ListExternalConfigRuleCompliance = Action("ListExternalConfigRuleCompliance")
ListGuardrailViolations = Action("ListGuardrailViolations")
ListGuardrails = Action("ListGuardrails")
ListGuardrailsForTarget = Action("ListGuardrailsForTarget")
ListManagedAccounts = Action("ListManagedAccounts")
ListManagedAccountsForGuardrail = Action("ListManagedAccountsForGuardrail")
ListManagedAccountsForParent = Action("ListManagedAccountsForParent")
ListManagedOrganizationalUnits = Action("ListManagedOrganizationalUnits")
ListManagedOrganizationalUnitsForGuardrail = Action(
    "ListManagedOrganizationalUnitsForGuardrail"
)
ManageOrganizationalUnit = Action("ManageOrganizationalUnit")
PerformPreLaunchChecks = Action("PerformPreLaunchChecks")
SetupLandingZone = Action("SetupLandingZone")
UpdateAccountFactoryConfig = Action("UpdateAccountFactoryConfig")
