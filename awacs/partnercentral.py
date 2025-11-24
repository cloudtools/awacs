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
AcceptEngagementInvitation = Action("AcceptEngagementInvitation")
AssignOpportunity = Action("AssignOpportunity")
AssociateOpportunity = Action("AssociateOpportunity")
CancelChannelHandshake = Action("CancelChannelHandshake")
CreateChannelHandshake = Action("CreateChannelHandshake")
CreateEngagement = Action("CreateEngagement")
CreateEngagementInvitation = Action("CreateEngagementInvitation")
CreateOpportunity = Action("CreateOpportunity")
CreateProgramManagementAccount = Action("CreateProgramManagementAccount")
CreateRelationship = Action("CreateRelationship")
CreateResourceSnapshot = Action("CreateResourceSnapshot")
CreateResourceSnapshotJob = Action("CreateResourceSnapshotJob")
DeleteProgramManagementAccount = Action("DeleteProgramManagementAccount")
DeleteRelationship = Action("DeleteRelationship")
DeleteResourceSnapshotJob = Action("DeleteResourceSnapshotJob")
DisassociateOpportunity = Action("DisassociateOpportunity")
GetAwsOpportunitySummary = Action("GetAwsOpportunitySummary")
GetEngagement = Action("GetEngagement")
GetEngagementInvitation = Action("GetEngagementInvitation")
GetOpportunity = Action("GetOpportunity")
GetProgramManagementAccount = Action("GetProgramManagementAccount")
GetRelationship = Action("GetRelationship")
GetResourceSnapshot = Action("GetResourceSnapshot")
GetResourceSnapshotJob = Action("GetResourceSnapshotJob")
GetSellingSystemSettings = Action("GetSellingSystemSettings")
ListChannelHandshakes = Action("ListChannelHandshakes")
ListEngagementByAcceptingInvitationTasks = Action(
    "ListEngagementByAcceptingInvitationTasks"
)
ListEngagementFromOpportunityTasks = Action("ListEngagementFromOpportunityTasks")
ListEngagementInvitations = Action("ListEngagementInvitations")
ListEngagementMembers = Action("ListEngagementMembers")
ListEngagementResourceAssociations = Action("ListEngagementResourceAssociations")
ListEngagements = Action("ListEngagements")
ListOpportunities = Action("ListOpportunities")
ListProgramManagementAccounts = Action("ListProgramManagementAccounts")
ListRelationships = Action("ListRelationships")
ListResourceSnapshotJobs = Action("ListResourceSnapshotJobs")
ListResourceSnapshots = Action("ListResourceSnapshots")
ListSolutions = Action("ListSolutions")
ListTagsForResource = Action("ListTagsForResource")
PutSellingSystemSettings = Action("PutSellingSystemSettings")
RejectChannelHandshake = Action("RejectChannelHandshake")
RejectEngagementInvitation = Action("RejectEngagementInvitation")
StartEngagementByAcceptingInvitationTask = Action(
    "StartEngagementByAcceptingInvitationTask"
)
StartEngagementFromOpportunityTask = Action("StartEngagementFromOpportunityTask")
StartResourceSnapshotJob = Action("StartResourceSnapshotJob")
StopResourceSnapshotJob = Action("StopResourceSnapshotJob")
SubmitOpportunity = Action("SubmitOpportunity")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateOpportunity = Action("UpdateOpportunity")
UpdateProgramManagementAccount = Action("UpdateProgramManagementAccount")
UpdateRelationship = Action("UpdateRelationship")
