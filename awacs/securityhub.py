# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Security Hub"
prefix = "securityhub"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAdministratorInvitation = Action("AcceptAdministratorInvitation")
AcceptInvitation = Action("AcceptInvitation")
BatchDisableStandards = Action("BatchDisableStandards")
BatchEnableStandards = Action("BatchEnableStandards")
BatchImportFindings = Action("BatchImportFindings")
BatchUpdateFindings = Action("BatchUpdateFindings")
CreateActionTarget = Action("CreateActionTarget")
CreateInsight = Action("CreateInsight")
CreateMembers = Action("CreateMembers")
DeclineInvitations = Action("DeclineInvitations")
DeleteActionTarget = Action("DeleteActionTarget")
DeleteInsight = Action("DeleteInsight")
DeleteInvitations = Action("DeleteInvitations")
DeleteMembers = Action("DeleteMembers")
DescribeActionTargets = Action("DescribeActionTargets")
DescribeHub = Action("DescribeHub")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
DescribeProducts = Action("DescribeProducts")
DescribeStandards = Action("DescribeStandards")
DescribeStandardsControls = Action("DescribeStandardsControls")
DisableImportFindingsForProduct = Action("DisableImportFindingsForProduct")
DisableOrganizationAdminAccount = Action("DisableOrganizationAdminAccount")
DisableSecurityHub = Action("DisableSecurityHub")
DisassociateFromAdministratorAccount = Action("DisassociateFromAdministratorAccount")
DisassociateFromMasterAccount = Action("DisassociateFromMasterAccount")
DisassociateMembers = Action("DisassociateMembers")
EnableImportFindingsForProduct = Action("EnableImportFindingsForProduct")
EnableOrganizationAdminAccount = Action("EnableOrganizationAdminAccount")
EnableSecurityHub = Action("EnableSecurityHub")
GetAdhocInsightResults = Action("GetAdhocInsightResults")
GetAdministratorAccount = Action("GetAdministratorAccount")
GetControlFindingSummary = Action("GetControlFindingSummary")
GetEnabledStandards = Action("GetEnabledStandards")
GetFindings = Action("GetFindings")
GetFreeTrialEndDate = Action("GetFreeTrialEndDate")
GetFreeTrialUsage = Action("GetFreeTrialUsage")
GetInsightFindingTrend = Action("GetInsightFindingTrend")
GetInsightResults = Action("GetInsightResults")
GetInsights = Action("GetInsights")
GetInvitationsCount = Action("GetInvitationsCount")
GetMasterAccount = Action("GetMasterAccount")
GetMembers = Action("GetMembers")
GetUsage = Action("GetUsage")
InviteMembers = Action("InviteMembers")
ListControlEvaluationSummaries = Action("ListControlEvaluationSummaries")
ListEnabledProductsForImport = Action("ListEnabledProductsForImport")
ListInvitations = Action("ListInvitations")
ListMembers = Action("ListMembers")
ListOrganizationAdminAccounts = Action("ListOrganizationAdminAccounts")
ListProductSubscribers = Action("ListProductSubscribers")
ListTagsForResource = Action("ListTagsForResource")
SendFindingEvents = Action("SendFindingEvents")
SendInsightEvents = Action("SendInsightEvents")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateActionTarget = Action("UpdateActionTarget")
UpdateFindings = Action("UpdateFindings")
UpdateInsight = Action("UpdateInsight")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
UpdateSecurityHubConfiguration = Action("UpdateSecurityHubConfiguration")
UpdateStandardsControl = Action("UpdateStandardsControl")
