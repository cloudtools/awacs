# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon GuardDuty"
prefix = "guardduty"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAdministratorInvitation = Action("AcceptAdministratorInvitation")
AcceptInvitation = Action("AcceptInvitation")
ArchiveFindings = Action("ArchiveFindings")
CreateDetector = Action("CreateDetector")
CreateFilter = Action("CreateFilter")
CreateIPSet = Action("CreateIPSet")
CreateMalwareProtectionPlan = Action("CreateMalwareProtectionPlan")
CreateMembers = Action("CreateMembers")
CreatePublishingDestination = Action("CreatePublishingDestination")
CreateSampleFindings = Action("CreateSampleFindings")
CreateThreatEntitySet = Action("CreateThreatEntitySet")
CreateThreatIntelSet = Action("CreateThreatIntelSet")
CreateTrustedEntitySet = Action("CreateTrustedEntitySet")
DeclineInvitations = Action("DeclineInvitations")
DeleteDetector = Action("DeleteDetector")
DeleteFilter = Action("DeleteFilter")
DeleteIPSet = Action("DeleteIPSet")
DeleteInvitations = Action("DeleteInvitations")
DeleteMalwareProtectionPlan = Action("DeleteMalwareProtectionPlan")
DeleteMembers = Action("DeleteMembers")
DeletePublishingDestination = Action("DeletePublishingDestination")
DeleteThreatEntitySet = Action("DeleteThreatEntitySet")
DeleteThreatIntelSet = Action("DeleteThreatIntelSet")
DeleteTrustedEntitySet = Action("DeleteTrustedEntitySet")
DescribeMalwareScans = Action("DescribeMalwareScans")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
DescribePublishingDestination = Action("DescribePublishingDestination")
DisableOrganizationAdminAccount = Action("DisableOrganizationAdminAccount")
DisassociateFromAdministratorAccount = Action("DisassociateFromAdministratorAccount")
DisassociateFromMasterAccount = Action("DisassociateFromMasterAccount")
DisassociateMembers = Action("DisassociateMembers")
EnableOrganizationAdminAccount = Action("EnableOrganizationAdminAccount")
GetAdministratorAccount = Action("GetAdministratorAccount")
GetCoverageStatistics = Action("GetCoverageStatistics")
GetDetector = Action("GetDetector")
GetFilter = Action("GetFilter")
GetFindings = Action("GetFindings")
GetFindingsStatistics = Action("GetFindingsStatistics")
GetIPSet = Action("GetIPSet")
GetInvitationsCount = Action("GetInvitationsCount")
GetMalwareProtectionPlan = Action("GetMalwareProtectionPlan")
GetMalwareScan = Action("GetMalwareScan")
GetMalwareScanSettings = Action("GetMalwareScanSettings")
GetMasterAccount = Action("GetMasterAccount")
GetMemberDetectors = Action("GetMemberDetectors")
GetMembers = Action("GetMembers")
GetOrganizationStatistics = Action("GetOrganizationStatistics")
GetRemainingFreeTrialDays = Action("GetRemainingFreeTrialDays")
GetThreatEntitySet = Action("GetThreatEntitySet")
GetThreatIntelSet = Action("GetThreatIntelSet")
GetTrustedEntitySet = Action("GetTrustedEntitySet")
GetUsageStatistics = Action("GetUsageStatistics")
InviteMembers = Action("InviteMembers")
ListCoverage = Action("ListCoverage")
ListDetectors = Action("ListDetectors")
ListFilters = Action("ListFilters")
ListFindings = Action("ListFindings")
ListIPSets = Action("ListIPSets")
ListInvitations = Action("ListInvitations")
ListMalwareProtectionPlans = Action("ListMalwareProtectionPlans")
ListMalwareScans = Action("ListMalwareScans")
ListMembers = Action("ListMembers")
ListOrganizationAdminAccounts = Action("ListOrganizationAdminAccounts")
ListPublishingDestinations = Action("ListPublishingDestinations")
ListTagsForResource = Action("ListTagsForResource")
ListThreatEntitySets = Action("ListThreatEntitySets")
ListThreatIntelSets = Action("ListThreatIntelSets")
ListTrustedEntitySets = Action("ListTrustedEntitySets")
SendObjectMalwareScan = Action("SendObjectMalwareScan")
SendSecurityTelemetry = Action("SendSecurityTelemetry")
StartMalwareScan = Action("StartMalwareScan")
StartMonitoringMembers = Action("StartMonitoringMembers")
StopMonitoringMembers = Action("StopMonitoringMembers")
TagResource = Action("TagResource")
UnarchiveFindings = Action("UnarchiveFindings")
UntagResource = Action("UntagResource")
UpdateDetector = Action("UpdateDetector")
UpdateFilter = Action("UpdateFilter")
UpdateFindingsFeedback = Action("UpdateFindingsFeedback")
UpdateIPSet = Action("UpdateIPSet")
UpdateMalwareProtectionPlan = Action("UpdateMalwareProtectionPlan")
UpdateMalwareScanSettings = Action("UpdateMalwareScanSettings")
UpdateMemberDetectors = Action("UpdateMemberDetectors")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
UpdatePublishingDestination = Action("UpdatePublishingDestination")
UpdateThreatEntitySet = Action("UpdateThreatEntitySet")
UpdateThreatIntelSet = Action("UpdateThreatIntelSet")
UpdateTrustedEntitySet = Action("UpdateTrustedEntitySet")
