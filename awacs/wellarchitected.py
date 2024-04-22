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
ConfigureIntegration = Action("ConfigureIntegration")
CreateLensShare = Action("CreateLensShare")
CreateLensVersion = Action("CreateLensVersion")
CreateMilestone = Action("CreateMilestone")
CreateProfile = Action("CreateProfile")
CreateProfileShare = Action("CreateProfileShare")
CreateReviewTemplate = Action("CreateReviewTemplate")
CreateTemplateShare = Action("CreateTemplateShare")
CreateWorkload = Action("CreateWorkload")
CreateWorkloadShare = Action("CreateWorkloadShare")
DeleteLens = Action("DeleteLens")
DeleteLensShare = Action("DeleteLensShare")
DeleteProfile = Action("DeleteProfile")
DeleteProfileShare = Action("DeleteProfileShare")
DeleteReviewTemplate = Action("DeleteReviewTemplate")
DeleteTemplateShare = Action("DeleteTemplateShare")
DeleteWorkload = Action("DeleteWorkload")
DeleteWorkloadShare = Action("DeleteWorkloadShare")
DisassociateLenses = Action("DisassociateLenses")
DisassociateProfiles = Action("DisassociateProfiles")
ExportLens = Action("ExportLens")
GetAnswer = Action("GetAnswer")
GetConsolidatedReport = Action("GetConsolidatedReport")
GetGlobalSettings = Action("GetGlobalSettings")
GetLens = Action("GetLens")
GetLensReview = Action("GetLensReview")
GetLensReviewReport = Action("GetLensReviewReport")
GetLensVersionDifference = Action("GetLensVersionDifference")
GetMilestone = Action("GetMilestone")
GetProfile = Action("GetProfile")
GetProfileTemplate = Action("GetProfileTemplate")
GetReviewTemplate = Action("GetReviewTemplate")
GetReviewTemplateAnswer = Action("GetReviewTemplateAnswer")
GetReviewTemplateLensReview = Action("GetReviewTemplateLensReview")
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
ListReviewTemplateAnswers = Action("ListReviewTemplateAnswers")
ListReviewTemplates = Action("ListReviewTemplates")
ListShareInvitations = Action("ListShareInvitations")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateShares = Action("ListTemplateShares")
ListWorkloadShares = Action("ListWorkloadShares")
ListWorkloads = Action("ListWorkloads")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAnswer = Action("UpdateAnswer")
UpdateGlobalSettings = Action("UpdateGlobalSettings")
UpdateIntegration = Action("UpdateIntegration")
UpdateLensReview = Action("UpdateLensReview")
UpdateProfile = Action("UpdateProfile")
UpdateReviewTemplate = Action("UpdateReviewTemplate")
UpdateReviewTemplateAnswer = Action("UpdateReviewTemplateAnswer")
UpdateReviewTemplateLensReview = Action("UpdateReviewTemplateLensReview")
UpdateShareInvitation = Action("UpdateShareInvitation")
UpdateWorkload = Action("UpdateWorkload")
UpdateWorkloadShare = Action("UpdateWorkloadShare")
UpgradeLensReview = Action("UpgradeLensReview")
UpgradeProfileVersion = Action("UpgradeProfileVersion")
UpgradeReviewTemplateLensReview = Action("UpgradeReviewTemplateLensReview")
