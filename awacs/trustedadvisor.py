# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Trusted Advisor"
prefix = "trustedadvisor"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DescribeAccount = Action("DescribeAccount")
DescribeAccountAccess = Action("DescribeAccountAccess")
DescribeCheckItems = Action("DescribeCheckItems")
DescribeCheckRefreshStatuses = Action("DescribeCheckRefreshStatuses")
DescribeCheckSummaries = Action("DescribeCheckSummaries")
DescribeChecks = Action("DescribeChecks")
DescribeNotificationPreferences = Action("DescribeNotificationPreferences")
DescribeOrganization = Action("DescribeOrganization")
DescribeOrganizationAccounts = Action("DescribeOrganizationAccounts")
DescribeReports = Action("DescribeReports")
DescribeServiceMetadata = Action("DescribeServiceMetadata")
ExcludeCheckItems = Action("ExcludeCheckItems")
GenerateReport = Action("GenerateReport")
IncludeCheckItems = Action("IncludeCheckItems")
ListAccountsForParent = Action("ListAccountsForParent")
ListOrganizationalUnitsForParent = Action("ListOrganizationalUnitsForParent")
ListRoots = Action("ListRoots")
RefreshCheck = Action("RefreshCheck")
SetAccountAccess = Action("SetAccountAccess")
SetOrganizationAccess = Action("SetOrganizationAccess")
UpdateNotificationPreferences = Action("UpdateNotificationPreferences")
