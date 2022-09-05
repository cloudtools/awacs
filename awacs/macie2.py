# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Macie"
prefix = "macie2"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptInvitation = Action("AcceptInvitation")
ArchiveFindings = Action("ArchiveFindings")
BatchGetCustomDataIdentifiers = Action("BatchGetCustomDataIdentifiers")
CreateAllowList = Action("CreateAllowList")
CreateClassificationJob = Action("CreateClassificationJob")
CreateCustomDataIdentifier = Action("CreateCustomDataIdentifier")
CreateFindingsFilter = Action("CreateFindingsFilter")
CreateInvitations = Action("CreateInvitations")
CreateMember = Action("CreateMember")
CreateSampleFindings = Action("CreateSampleFindings")
DeclineInvitations = Action("DeclineInvitations")
DeleteAllowList = Action("DeleteAllowList")
DeleteCustomDataIdentifier = Action("DeleteCustomDataIdentifier")
DeleteFindingsFilter = Action("DeleteFindingsFilter")
DeleteInvitations = Action("DeleteInvitations")
DeleteMember = Action("DeleteMember")
DescribeBuckets = Action("DescribeBuckets")
DescribeClassificationJob = Action("DescribeClassificationJob")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
DisableMacie = Action("DisableMacie")
DisableOrganizationAdminAccount = Action("DisableOrganizationAdminAccount")
DisassociateFromAdministratorAccount = Action("DisassociateFromAdministratorAccount")
DisassociateFromMasterAccount = Action("DisassociateFromMasterAccount")
DisassociateMember = Action("DisassociateMember")
EnableMacie = Action("EnableMacie")
EnableOrganizationAdminAccount = Action("EnableOrganizationAdminAccount")
GetAdministratorAccount = Action("GetAdministratorAccount")
GetAllowList = Action("GetAllowList")
GetBucketStatistics = Action("GetBucketStatistics")
GetClassificationExportConfiguration = Action("GetClassificationExportConfiguration")
GetCustomDataIdentifier = Action("GetCustomDataIdentifier")
GetFindingStatistics = Action("GetFindingStatistics")
GetFindings = Action("GetFindings")
GetFindingsFilter = Action("GetFindingsFilter")
GetFindingsPublicationConfiguration = Action("GetFindingsPublicationConfiguration")
GetInvitationsCount = Action("GetInvitationsCount")
GetMacieSession = Action("GetMacieSession")
GetMasterAccount = Action("GetMasterAccount")
GetMember = Action("GetMember")
GetRevealConfiguration = Action("GetRevealConfiguration")
GetSensitiveDataOccurrences = Action("GetSensitiveDataOccurrences")
GetSensitiveDataOccurrencesAvailability = Action(
    "GetSensitiveDataOccurrencesAvailability"
)
GetUsageStatistics = Action("GetUsageStatistics")
GetUsageTotals = Action("GetUsageTotals")
ListAllowLists = Action("ListAllowLists")
ListClassificationJobs = Action("ListClassificationJobs")
ListCustomDataIdentifiers = Action("ListCustomDataIdentifiers")
ListFindings = Action("ListFindings")
ListFindingsFilters = Action("ListFindingsFilters")
ListInvitations = Action("ListInvitations")
ListManagedDataIdentifiers = Action("ListManagedDataIdentifiers")
ListMembers = Action("ListMembers")
ListOrganizationAdminAccounts = Action("ListOrganizationAdminAccounts")
ListTagsForResource = Action("ListTagsForResource")
ListTagsForResources = Action("ListTagsForResources")
PutClassificationExportConfiguration = Action("PutClassificationExportConfiguration")
PutFindingsPublicationConfiguration = Action("PutFindingsPublicationConfiguration")
SearchResources = Action("SearchResources")
TagResource = Action("TagResource")
TestCustomDataIdentifier = Action("TestCustomDataIdentifier")
UnarchiveFindings = Action("UnarchiveFindings")
UntagResource = Action("UntagResource")
UpdateAllowList = Action("UpdateAllowList")
UpdateClassificationJob = Action("UpdateClassificationJob")
UpdateFindingsFilter = Action("UpdateFindingsFilter")
UpdateMacieSession = Action("UpdateMacieSession")
UpdateMemberSession = Action("UpdateMemberSession")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
UpdateRevealConfiguration = Action("UpdateRevealConfiguration")
