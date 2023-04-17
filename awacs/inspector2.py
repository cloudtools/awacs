# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Inspector2"
prefix = "inspector2"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateMember = Action("AssociateMember")
BatchGetAccountStatus = Action("BatchGetAccountStatus")
BatchGetCodeSnippet = Action("BatchGetCodeSnippet")
BatchGetFreeTrialInfo = Action("BatchGetFreeTrialInfo")
BatchGetMemberEc2DeepInspectionStatus = Action("BatchGetMemberEc2DeepInspectionStatus")
BatchUpdateMemberEc2DeepInspectionStatus = Action(
    "BatchUpdateMemberEc2DeepInspectionStatus"
)
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
GetConfiguration = Action("GetConfiguration")
GetDelegatedAdminAccount = Action("GetDelegatedAdminAccount")
GetEc2DeepInspectionConfiguration = Action("GetEc2DeepInspectionConfiguration")
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
UpdateConfiguration = Action("UpdateConfiguration")
UpdateEc2DeepInspectionConfiguration = Action("UpdateEc2DeepInspectionConfiguration")
UpdateFilter = Action("UpdateFilter")
UpdateOrgEc2DeepInspectionConfiguration = Action(
    "UpdateOrgEc2DeepInspectionConfiguration"
)
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
