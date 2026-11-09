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
AssociateBusinessPlan = Action("AssociateBusinessPlan")
AssociateOpportunity = Action("AssociateOpportunity")
CancelBenefitApplication = Action("CancelBenefitApplication")
CancelBusinessPlan = Action("CancelBusinessPlan")
CancelBusinessPlanSubmissionTask = Action("CancelBusinessPlanSubmissionTask")
CancelChannelHandshake = Action("CancelChannelHandshake")
CancelConnection = Action("CancelConnection")
CancelConnectionInvitation = Action("CancelConnectionInvitation")
CancelProfileUpdateTask = Action("CancelProfileUpdateTask")
CreateBenefitApplication = Action("CreateBenefitApplication")
CreateBusinessPlan = Action("CreateBusinessPlan")
CreateBusinessPlanItem = Action("CreateBusinessPlanItem")
CreateChannelHandshake = Action("CreateChannelHandshake")
CreateCollaborationChannelMembers = Action("CreateCollaborationChannelMembers")
CreateCollaborationChannelRequest = Action("CreateCollaborationChannelRequest")
CreateConnectionInvitation = Action("CreateConnectionInvitation")
CreateEngagement = Action("CreateEngagement")
CreateEngagementContext = Action("CreateEngagementContext")
CreateEngagementInvitation = Action("CreateEngagementInvitation")
CreateMarketplaceRevenueShare = Action("CreateMarketplaceRevenueShare")
CreateMarketplaceRevenueShareAllocation = Action(
    "CreateMarketplaceRevenueShareAllocation"
)
CreateOpportunity = Action("CreateOpportunity")
CreatePartner = Action("CreatePartner")
CreateProgramManagementAccount = Action("CreateProgramManagementAccount")
CreateRelationship = Action("CreateRelationship")
CreateResourceSnapshot = Action("CreateResourceSnapshot")
CreateResourceSnapshotJob = Action("CreateResourceSnapshotJob")
CreateRevenueAttribution = Action("CreateRevenueAttribution")
DeleteBusinessPlanAttachment = Action("DeleteBusinessPlanAttachment")
DeleteBusinessPlanItem = Action("DeleteBusinessPlanItem")
DeleteProgramManagementAccount = Action("DeleteProgramManagementAccount")
DeleteRelationship = Action("DeleteRelationship")
DeleteResourceSnapshotJob = Action("DeleteResourceSnapshotJob")
DisassociateAwsTrainingCertificationEmailDomain = Action(
    "DisassociateAwsTrainingCertificationEmailDomain"
)
DisassociateBenefitApplicationResource = Action(
    "DisassociateBenefitApplicationResource"
)
DisassociateBusinessPlan = Action("DisassociateBusinessPlan")
DisassociateOpportunity = Action("DisassociateOpportunity")
EnrollInPartnerPath = Action("EnrollInPartnerPath")
GetAllianceLeadContact = Action("GetAllianceLeadContact")
GetAwsOpportunitySummary = Action("GetAwsOpportunitySummary")
GetBenefit = Action("GetBenefit")
GetBenefitAllocation = Action("GetBenefitAllocation")
GetBenefitApplication = Action("GetBenefitApplication")
GetBusinessPlan = Action("GetBusinessPlan")
GetBusinessPlanAttachment = Action("GetBusinessPlanAttachment")
GetBusinessPlanAttachmentImportTask = Action("GetBusinessPlanAttachmentImportTask")
GetBusinessPlanItem = Action("GetBusinessPlanItem")
GetBusinessPlanItemSchema = Action("GetBusinessPlanItemSchema")
GetBusinessPlanSettings = Action("GetBusinessPlanSettings")
GetBusinessPlanSubmissionTask = Action("GetBusinessPlanSubmissionTask")
GetCollaborationChannel = Action("GetCollaborationChannel")
GetConnection = Action("GetConnection")
GetConnectionInvitation = Action("GetConnectionInvitation")
GetConnectionPreferences = Action("GetConnectionPreferences")
GetEngagement = Action("GetEngagement")
GetEngagementInvitation = Action("GetEngagementInvitation")
GetMarketplaceRevenueShare = Action("GetMarketplaceRevenueShare")
GetMarketplaceRevenueShareAllocation = Action("GetMarketplaceRevenueShareAllocation")
GetOpportunity = Action("GetOpportunity")
GetPartner = Action("GetPartner")
GetPartnerCentralContentDocument = Action("GetPartnerCentralContentDocument")
GetPartnerCentralContentMetadata = Action("GetPartnerCentralContentMetadata")
GetPartnerDashboard = Action("GetPartnerDashboard")
GetPartnerProfile = Action("GetPartnerProfile")
GetPartnerReportingData = Action("GetPartnerReportingData")
GetProfileUpdateTask = Action("GetProfileUpdateTask")
GetProfileVisibility = Action("GetProfileVisibility")
GetProgramManagementAccount = Action("GetProgramManagementAccount")
GetProspectingFromEngagementTask = Action("GetProspectingFromEngagementTask")
GetQualificationsAssociationDetails = Action("GetQualificationsAssociationDetails")
GetQualificationsAssociationTask = Action("GetQualificationsAssociationTask")
GetQualificationsDisassociationTask = Action("GetQualificationsDisassociationTask")
GetRelationship = Action("GetRelationship")
GetResourceSnapshot = Action("GetResourceSnapshot")
GetResourceSnapshotJob = Action("GetResourceSnapshotJob")
GetRevenueAttribution = Action("GetRevenueAttribution")
GetRevenueAttributionAllocation = Action("GetRevenueAttributionAllocation")
GetRevenueAttributionAllocationsTask = Action("GetRevenueAttributionAllocationsTask")
GetSellingSystemSettings = Action("GetSellingSystemSettings")
GetVerification = Action("GetVerification")
ListBenefitAllocations = Action("ListBenefitAllocations")
ListBenefitApplications = Action("ListBenefitApplications")
ListBenefits = Action("ListBenefits")
ListBusinessPlanAssociations = Action("ListBusinessPlanAssociations")
ListBusinessPlanAttachmentImportTasks = Action("ListBusinessPlanAttachmentImportTasks")
ListBusinessPlanAttachments = Action("ListBusinessPlanAttachments")
ListBusinessPlanHistory = Action("ListBusinessPlanHistory")
ListBusinessPlanItems = Action("ListBusinessPlanItems")
ListBusinessPlanSubmissionTasks = Action("ListBusinessPlanSubmissionTasks")
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
ListMarketplaceRevenueShareAllocations = Action(
    "ListMarketplaceRevenueShareAllocations"
)
ListMarketplaceRevenueShares = Action("ListMarketplaceRevenueShares")
ListOpportunities = Action("ListOpportunities")
ListOpportunityFromEngagementTasks = Action("ListOpportunityFromEngagementTasks")
ListPartnerCentralContent = Action("ListPartnerCentralContent")
ListPartnerPaths = Action("ListPartnerPaths")
ListPartners = Action("ListPartners")
ListProgramManagementAccounts = Action("ListProgramManagementAccounts")
ListProspectingFromEngagementTasks = Action("ListProspectingFromEngagementTasks")
ListRelationships = Action("ListRelationships")
ListResourceSnapshotJobs = Action("ListResourceSnapshotJobs")
ListResourceSnapshots = Action("ListResourceSnapshots")
ListRevenueAttributionAllocations = Action("ListRevenueAttributionAllocations")
ListRevenueAttributions = Action("ListRevenueAttributions")
ListSolutions = Action("ListSolutions")
ListTagsForResource = Action("ListTagsForResource")
PutAllianceLeadContact = Action("PutAllianceLeadContact")
PutBusinessPlan = Action("PutBusinessPlan")
PutBusinessPlanSettings = Action("PutBusinessPlanSettings")
PutProfileVisibility = Action("PutProfileVisibility")
PutSellingSystemSettings = Action("PutSellingSystemSettings")
RecallBenefitApplication = Action("RecallBenefitApplication")
RejectChannelHandshake = Action("RejectChannelHandshake")
RejectConnectionInvitation = Action("RejectConnectionInvitation")
RejectEngagementInvitation = Action("RejectEngagementInvitation")
SearchOpportunities = Action("SearchOpportunities")
SearchPartnerCentralContent = Action("SearchPartnerCentralContent")
SearchPartnerProfiles = Action("SearchPartnerProfiles")
SendEmailVerificationCode = Action("SendEmailVerificationCode")
StartBusinessPlanAttachmentImportTask = Action("StartBusinessPlanAttachmentImportTask")
StartBusinessPlanSubmissionTask = Action("StartBusinessPlanSubmissionTask")
StartEngagementByAcceptingInvitationTask = Action(
    "StartEngagementByAcceptingInvitationTask"
)
StartEngagementFromOpportunityTask = Action("StartEngagementFromOpportunityTask")
StartOpportunityFromEngagementTask = Action("StartOpportunityFromEngagementTask")
StartProfileUpdateTask = Action("StartProfileUpdateTask")
StartProspectingFromEngagementTask = Action("StartProspectingFromEngagementTask")
StartQualificationsAssociationTask = Action("StartQualificationsAssociationTask")
StartQualificationsDisassociationTask = Action("StartQualificationsDisassociationTask")
StartResourceSnapshotJob = Action("StartResourceSnapshotJob")
StartRevenueAttributionAllocationsTask = Action(
    "StartRevenueAttributionAllocationsTask"
)
StartVerification = Action("StartVerification")
StopResourceSnapshotJob = Action("StopResourceSnapshotJob")
SubmitBenefitApplication = Action("SubmitBenefitApplication")
SubmitOpportunity = Action("SubmitOpportunity")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBenefitApplication = Action("UpdateBenefitApplication")
UpdateBusinessPlan = Action("UpdateBusinessPlan")
UpdateBusinessPlanItem = Action("UpdateBusinessPlanItem")
UpdateConnectionPreferences = Action("UpdateConnectionPreferences")
UpdateEngagementContext = Action("UpdateEngagementContext")
UpdateMarketplaceRevenueShareAllocation = Action(
    "UpdateMarketplaceRevenueShareAllocation"
)
UpdateOpportunity = Action("UpdateOpportunity")
UpdateProgramManagementAccount = Action("UpdateProgramManagementAccount")
UpdateRelationship = Action("UpdateRelationship")
UpdateRevenueAttribution = Action("UpdateRevenueAttribution")
UseSession = Action("UseSession")
