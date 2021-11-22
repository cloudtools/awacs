# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Inspector2"
prefix = "inspector2"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateMember = Action("AssociateMember")
BatchGetAccountStatus = Action("BatchGetAccountStatus")
BatchGetFreeTrialInfo = Action("BatchGetFreeTrialInfo")
CancelFindingsReport = Action("CancelFindingsReport")
CreateFilter = Action("CreateFilter")
CreateFindingsReport = Action("CreateFindingsReport")
DeleteFilter = Action("DeleteFilter")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
Disable = Action("Disable")
DisableDelegatedAdminAccount = Action("DisableDelegatedAdminAccount")
DisassociateMember = Action("DisassociateMember")
Enable = Action("Enable")
EnableDelegatedAdminAccount = Action("EnableDelegatedAdminAccount")
GetDelegatedAdminAccount = Action("GetDelegatedAdminAccount")
GetFindingsReportStatus = Action("GetFindingsReportStatus")
GetMember = Action("GetMember")
ListAccountPermissions = Action("ListAccountPermissions")
ListCoverage = Action("ListCoverage")
ListCoverageStatistics = Action("ListCoverageStatistics")
ListDelegatedAdminAccounts = Action("ListDelegatedAdminAccounts")
ListFilters = Action("ListFilters")
ListFindingAggregations = Action("ListFindingAggregations")
ListFindings = Action("ListFindings")
ListMembers = Action("ListMembers")
ListTagsForResource = Action("ListTagsForResource")
ListUsageTotals = Action("ListUsageTotals")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFilter = Action("UpdateFilter")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
