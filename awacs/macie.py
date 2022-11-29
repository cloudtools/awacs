# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Macie Classic"
prefix = "macie"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptInvitation = Action("AcceptInvitation")
ArchiveFindings = Action("ArchiveFindings")
AssociateMemberAccount = Action("AssociateMemberAccount")
AssociateS3Resources = Action("AssociateS3Resources")
BatchGetCustomDataIdentifiers = Action("BatchGetCustomDataIdentifiers")
CreateClassificationJob = Action("CreateClassificationJob")
CreateCustomDataIdentifier = Action("CreateCustomDataIdentifier")
CreateFindingsFilter = Action("CreateFindingsFilter")
CreateInvitations = Action("CreateInvitations")
CreateMember = Action("CreateMember")
CreateSampleFindings = Action("CreateSampleFindings")
DeclineInvitations = Action("DeclineInvitations")
DeleteCustomDataIdentifier = Action("DeleteCustomDataIdentifier")
DeleteFindingsFilter = Action("DeleteFindingsFilter")
DeleteInvitations = Action("DeleteInvitations")
DeleteMember = Action("DeleteMember")
DescribeBuckets = Action("DescribeBuckets")
DescribeClassificationJob = Action("DescribeClassificationJob")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
DisableMacie = Action("DisableMacie")
DisableOrganizationAdminAccount = Action("DisableOrganizationAdminAccount")
DisassociateFromMasterAccount = Action("DisassociateFromMasterAccount")
DisassociateMember = Action("DisassociateMember")
DisassociateMemberAccount = Action("DisassociateMemberAccount")
DisassociateS3Resources = Action("DisassociateS3Resources")
EnableMacie = Action("EnableMacie")
EnableOrganizationAdminAccount = Action("EnableOrganizationAdminAccount")
GetBucketStatistics = Action("GetBucketStatistics")
GetClassificationExportConfiguration = Action("GetClassificationExportConfiguration")
GetCustomDataIdentifier = Action("GetCustomDataIdentifier")
GetFindingStatistics = Action("GetFindingStatistics")
GetFindings = Action("GetFindings")
GetFindingsFilter = Action("GetFindingsFilter")
GetInvitationsCount = Action("GetInvitationsCount")
GetMacieSession = Action("GetMacieSession")
GetMasterAccount = Action("GetMasterAccount")
GetMember = Action("GetMember")
GetUsageStatistics = Action("GetUsageStatistics")
GetUsageTotals = Action("GetUsageTotals")
ListClassificationJobs = Action("ListClassificationJobs")
ListCustomDataIdentifiers = Action("ListCustomDataIdentifiers")
ListFindings = Action("ListFindings")
ListFindingsFilters = Action("ListFindingsFilters")
ListInvitations = Action("ListInvitations")
ListMemberAccounts = Action("ListMemberAccounts")
ListMembers = Action("ListMembers")
ListOrganizationAdminAccounts = Action("ListOrganizationAdminAccounts")
ListS3Resources = Action("ListS3Resources")
ListTagsForResources = Action("ListTagsForResources")
PutClassificationExportConfiguration = Action("PutClassificationExportConfiguration")
TagResource = Action("TagResource")
TestCustomDataIdentifier = Action("TestCustomDataIdentifier")
UnarchiveFindings = Action("UnarchiveFindings")
UntagResource = Action("UntagResource")
UpdateClassificationJob = Action("UpdateClassificationJob")
UpdateFindingsFilter = Action("UpdateFindingsFilter")
UpdateMemberSession = Action("UpdateMemberSession")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
UpdateS3Resources = Action("UpdateS3Resources")
UpdateSession = Action("UpdateSession")
