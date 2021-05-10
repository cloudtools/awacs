# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Control Tower"
prefix = "controltower"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateManagedAccount = Action("CreateManagedAccount")
DeregisterManagedAccount = Action("DeregisterManagedAccount")
DeregisterOrganizationalUnit = Action("DeregisterOrganizationalUnit")
DescribeAccountFactoryConfig = Action("DescribeAccountFactoryConfig")
DescribeCoreService = Action("DescribeCoreService")
DescribeGuardrail = Action("DescribeGuardrail")
DescribeGuardrailForTarget = Action("DescribeGuardrailForTarget")
DescribeManagedAccount = Action("DescribeManagedAccount")
DescribeManagedOrganizationalUnit = Action("DescribeManagedOrganizationalUnit")
DescribeSingleSignOn = Action("DescribeSingleSignOn")
DisableGuardrail = Action("DisableGuardrail")
EnableGuardrail = Action("EnableGuardrail")
GetAvailableUpdates = Action("GetAvailableUpdates")
GetGuardrailComplianceStatus = Action("GetGuardrailComplianceStatus")
GetHomeRegion = Action("GetHomeRegion")
GetLandingZoneStatus = Action("GetLandingZoneStatus")
ListDirectoryGroups = Action("ListDirectoryGroups")
ListEnabledGuardrails = Action("ListEnabledGuardrails")
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
SetupLandingZone = Action("SetupLandingZone")
UpdateAccountFactoryConfig = Action("UpdateAccountFactoryConfig")
