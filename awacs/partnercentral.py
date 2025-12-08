# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Partner Central"
prefix = "partnercentral"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptChannelHandshake = Action("AcceptChannelHandshake")
AcceptConnectionInvitation = Action("AcceptConnectionInvitation")
AcceptEngagementInvitation = Action("AcceptEngagementInvitation")
AmendBenefitApplication = Action("AmendBenefitApplication")
AssignOpportunity = Action("AssignOpportunity")
AssociateAwsTrainingCertificationEmailDomain = Action(
    "AssociateAwsTrainingCertificationEmailDomain"
)
AssociateBenefitApplicationResource = Action("AssociateBenefitApplicationResource")
AssociateOpportunity = Action("AssociateOpportunity")
CancelBenefitApplication = Action("CancelBenefitApplication")
CancelChannelHandshake = Action("CancelChannelHandshake")
CancelConnection = Action("CancelConnection")
CancelConnectionInvitation = Action("CancelConnectionInvitation")
CancelProfileUpdateTask = Action("CancelProfileUpdateTask")
CreateBenefitApplication = Action("CreateBenefitApplication")
CreateBusinessPlan = Action("CreateBusinessPlan")
CreateChannelHandshake = Action("CreateChannelHandshake")
CreateCollaborationChannelMembers = Action("CreateCollaborationChannelMembers")
CreateCollaborationChannelRequest = Action("CreateCollaborationChannelRequest")
CreateConnectionInvitation = Action("CreateConnectionInvitation")
CreateEngagement = Action("CreateEngagement")
CreateEngagementContext = Action("CreateEngagementContext")
CreateEngagementInvitation = Action("CreateEngagementInvitation")
CreateOpportunity = Action("CreateOpportunity")
CreatePartner = Action("CreatePartner")
CreateProgramManagementAccount = Action("CreateProgramManagementAccount")
CreateRelationship = Action("CreateRelationship")
CreateResourceSnapshot = Action("CreateResourceSnapshot")
CreateResourceSnapshotJob = Action("CreateResourceSnapshotJob")
DeleteProgramManagementAccount = Action("DeleteProgramManagementAccount")
DeleteRelationship = Action("DeleteRelationship")
DeleteResourceSnapshotJob = Action("DeleteResourceSnapshotJob")
DisassociateAwsTrainingCertificationEmailDomain = Action(
    "DisassociateAwsTrainingCertificationEmailDomain"
)
DisassociateBenefitApplicationResource = Action(
    "DisassociateBenefitApplicationResource"
)
DisassociateOpportunity = Action("DisassociateOpportunity")
EnrollInPartnerPath = Action("EnrollInPartnerPath")
GetAllianceLeadContact = Action("GetAllianceLeadContact")
GetAwsOpportunitySummary = Action("GetAwsOpportunitySummary")
GetBenefit = Action("GetBenefit")
GetBenefitAllocation = Action("GetBenefitAllocation")
GetBenefitApplication = Action("GetBenefitApplication")
GetBusinessPlan = Action("GetBusinessPlan")
GetCollaborationChannel = Action("GetCollaborationChannel")
GetConnection = Action("GetConnection")
GetConnectionInvitation = Action("GetConnectionInvitation")
GetConnectionPreferences = Action("GetConnectionPreferences")
GetEngagement = Action("GetEngagement")
GetEngagementInvitation = Action("GetEngagementInvitation")
GetOpportunity = Action("GetOpportunity")
GetPartner = Action("GetPartner")
GetPartnerDashboard = Action("GetPartnerDashboard")
GetPartnerProfile = Action("GetPartnerProfile")
GetProfileUpdateTask = Action("GetProfileUpdateTask")
GetProfileVisibility = Action("GetProfileVisibility")
GetProgramManagementAccount = Action("GetProgramManagementAccount")
GetRelationship = Action("GetRelationship")
GetResourceSnapshot = Action("GetResourceSnapshot")
GetResourceSnapshotJob = Action("GetResourceSnapshotJob")
GetSellingSystemSettings = Action("GetSellingSystemSettings")
GetVerification = Action("GetVerification")
ListBenefitAllocations = Action("ListBenefitAllocations")
ListBenefitApplications = Action("ListBenefitApplications")
ListBenefits = Action("ListBenefits")
ListBusinessPlans = Action("ListBusinessPlans")
ListChannelHandshakes = Action("ListChannelHandshakes")
ListCollaborationChannels = Action("ListCollaborationChannels")
ListConnectionInvitations = Action("ListConnectionInvitations")
ListConnections = Action("ListConnections")
ListEngagementByAcceptingInvitationTasks = Action(
    "ListEngagementByAcceptingInvitationTasks"
)
ListEngagementFromOpportunityTasks = Action("ListEngagementFromOpportunityTasks")
ListEngagementInvitations = Action("ListEngagementInvitations")
ListEngagementMembers = Action("ListEngagementMembers")
ListEngagementResourceAssociations = Action("ListEngagementResourceAssociations")
ListEngagements = Action("ListEngagements")
ListOpportunities = Action("ListOpportunities")
ListOpportunityFromEngagementTasks = Action("ListOpportunityFromEngagementTasks")
ListPartnerPaths = Action("ListPartnerPaths")
ListPartners = Action("ListPartners")
ListProgramManagementAccounts = Action("ListProgramManagementAccounts")
ListRelationships = Action("ListRelationships")
ListResourceSnapshotJobs = Action("ListResourceSnapshotJobs")
ListResourceSnapshots = Action("ListResourceSnapshots")
ListSolutions = Action("ListSolutions")
ListTagsForResource = Action("ListTagsForResource")
PutAllianceLeadContact = Action("PutAllianceLeadContact")
PutBusinessPlan = Action("PutBusinessPlan")
PutProfileVisibility = Action("PutProfileVisibility")
PutSellingSystemSettings = Action("PutSellingSystemSettings")
RecallBenefitApplication = Action("RecallBenefitApplication")
RejectChannelHandshake = Action("RejectChannelHandshake")
RejectConnectionInvitation = Action("RejectConnectionInvitation")
RejectEngagementInvitation = Action("RejectEngagementInvitation")
SearchPartnerProfiles = Action("SearchPartnerProfiles")
SendEmailVerificationCode = Action("SendEmailVerificationCode")
StartEngagementByAcceptingInvitationTask = Action(
    "StartEngagementByAcceptingInvitationTask"
)
StartEngagementFromOpportunityTask = Action("StartEngagementFromOpportunityTask")
StartOpportunityFromEngagementTask = Action("StartOpportunityFromEngagementTask")
StartProfileUpdateTask = Action("StartProfileUpdateTask")
StartResourceSnapshotJob = Action("StartResourceSnapshotJob")
StartVerification = Action("StartVerification")
StopResourceSnapshotJob = Action("StopResourceSnapshotJob")
SubmitBenefitApplication = Action("SubmitBenefitApplication")
SubmitOpportunity = Action("SubmitOpportunity")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBenefitApplication = Action("UpdateBenefitApplication")
UpdateConnectionPreferences = Action("UpdateConnectionPreferences")
UpdateEngagementContext = Action("UpdateEngagementContext")
UpdateOpportunity = Action("UpdateOpportunity")
UpdateProgramManagementAccount = Action("UpdateProgramManagementAccount")
UpdateRelationship = Action("UpdateRelationship")
