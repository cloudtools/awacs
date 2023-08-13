# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Well-Architected Tool"
prefix = "wellarchitected"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateLenses = Action("AssociateLenses")
AssociateProfiles = Action("AssociateProfiles")
CreateLensShare = Action("CreateLensShare")
CreateLensVersion = Action("CreateLensVersion")
CreateMilestone = Action("CreateMilestone")
CreateProfile = Action("CreateProfile")
CreateProfileShare = Action("CreateProfileShare")
CreateWorkload = Action("CreateWorkload")
CreateWorkloadShare = Action("CreateWorkloadShare")
DeleteLens = Action("DeleteLens")
DeleteLensShare = Action("DeleteLensShare")
DeleteProfile = Action("DeleteProfile")
DeleteProfileShare = Action("DeleteProfileShare")
DeleteWorkload = Action("DeleteWorkload")
DeleteWorkloadShare = Action("DeleteWorkloadShare")
DisassociateLenses = Action("DisassociateLenses")
DisassociateProfiles = Action("DisassociateProfiles")
ExportLens = Action("ExportLens")
GetAnswer = Action("GetAnswer")
GetConsolidatedReport = Action("GetConsolidatedReport")
GetLens = Action("GetLens")
GetLensReview = Action("GetLensReview")
GetLensReviewReport = Action("GetLensReviewReport")
GetLensVersionDifference = Action("GetLensVersionDifference")
GetMilestone = Action("GetMilestone")
GetProfile = Action("GetProfile")
GetProfileTemplate = Action("GetProfileTemplate")
GetWorkload = Action("GetWorkload")
ImportLens = Action("ImportLens")
ListAnswers = Action("ListAnswers")
ListCheckDetails = Action("ListCheckDetails")
ListCheckSummaries = Action("ListCheckSummaries")
ListLensReviewImprovements = Action("ListLensReviewImprovements")
ListLensReviews = Action("ListLensReviews")
ListLensShares = Action("ListLensShares")
ListLenses = Action("ListLenses")
ListMilestones = Action("ListMilestones")
ListNotifications = Action("ListNotifications")
ListProfileNotifications = Action("ListProfileNotifications")
ListProfileShares = Action("ListProfileShares")
ListProfiles = Action("ListProfiles")
ListShareInvitations = Action("ListShareInvitations")
ListTagsForResource = Action("ListTagsForResource")
ListWorkloadShares = Action("ListWorkloadShares")
ListWorkloads = Action("ListWorkloads")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAnswer = Action("UpdateAnswer")
UpdateGlobalSettings = Action("UpdateGlobalSettings")
UpdateLensReview = Action("UpdateLensReview")
UpdateProfile = Action("UpdateProfile")
UpdateShareInvitation = Action("UpdateShareInvitation")
UpdateWorkload = Action("UpdateWorkload")
UpdateWorkloadShare = Action("UpdateWorkloadShare")
UpgradeLensReview = Action("UpgradeLensReview")
UpgradeProfileVersion = Action("UpgradeProfileVersion")
