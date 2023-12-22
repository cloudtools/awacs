# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Security Hub"
prefix = "securityhub"


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
BatchDeleteAutomationRules = Action("BatchDeleteAutomationRules")
BatchDisableStandards = Action("BatchDisableStandards")
BatchEnableStandards = Action("BatchEnableStandards")
BatchGetAutomationRules = Action("BatchGetAutomationRules")
BatchGetConfigurationPolicyAssociations = Action(
    "BatchGetConfigurationPolicyAssociations"
)
BatchGetControlEvaluations = Action("BatchGetControlEvaluations")
BatchGetSecurityControls = Action("BatchGetSecurityControls")
BatchGetStandardsControlAssociations = Action("BatchGetStandardsControlAssociations")
BatchImportFindings = Action("BatchImportFindings")
BatchUpdateAutomationRules = Action("BatchUpdateAutomationRules")
BatchUpdateFindings = Action("BatchUpdateFindings")
BatchUpdateStandardsControlAssociations = Action(
    "BatchUpdateStandardsControlAssociations"
)
CreateActionTarget = Action("CreateActionTarget")
CreateAutomationRule = Action("CreateAutomationRule")
CreateConfigurationPolicy = Action("CreateConfigurationPolicy")
CreateFindingAggregator = Action("CreateFindingAggregator")
CreateInsight = Action("CreateInsight")
CreateMembers = Action("CreateMembers")
DeclineInvitations = Action("DeclineInvitations")
DeleteActionTarget = Action("DeleteActionTarget")
DeleteConfigurationPolicy = Action("DeleteConfigurationPolicy")
DeleteFindingAggregator = Action("DeleteFindingAggregator")
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
GetConfigurationPolicy = Action("GetConfigurationPolicy")
GetConfigurationPolicyAssociation = Action("GetConfigurationPolicyAssociation")
GetControlFindingSummary = Action("GetControlFindingSummary")
GetEnabledStandards = Action("GetEnabledStandards")
GetFindingAggregator = Action("GetFindingAggregator")
GetFindingHistory = Action("GetFindingHistory")
GetFindings = Action("GetFindings")
GetFreeTrialEndDate = Action("GetFreeTrialEndDate")
GetFreeTrialUsage = Action("GetFreeTrialUsage")
GetInsightFindingTrend = Action("GetInsightFindingTrend")
GetInsightResults = Action("GetInsightResults")
GetInsights = Action("GetInsights")
GetInvitationsCount = Action("GetInvitationsCount")
GetMasterAccount = Action("GetMasterAccount")
GetMembers = Action("GetMembers")
GetSecurityControlDefinition = Action("GetSecurityControlDefinition")
GetUsage = Action("GetUsage")
InviteMembers = Action("InviteMembers")
ListAutomationRules = Action("ListAutomationRules")
ListConfigurationPolicies = Action("ListConfigurationPolicies")
ListConfigurationPolicyAssociations = Action("ListConfigurationPolicyAssociations")
ListControlEvaluationSummaries = Action("ListControlEvaluationSummaries")
ListEnabledProductsForImport = Action("ListEnabledProductsForImport")
ListFindingAggregators = Action("ListFindingAggregators")
ListInvitations = Action("ListInvitations")
ListMembers = Action("ListMembers")
ListOrganizationAdminAccounts = Action("ListOrganizationAdminAccounts")
ListProductSubscribers = Action("ListProductSubscribers")
ListSecurityControlDefinitions = Action("ListSecurityControlDefinitions")
ListStandardsControlAssociations = Action("ListStandardsControlAssociations")
ListTagsForResource = Action("ListTagsForResource")
SendFindingEvents = Action("SendFindingEvents")
SendInsightEvents = Action("SendInsightEvents")
StartConfigurationPolicyAssociation = Action("StartConfigurationPolicyAssociation")
StartConfigurationPolicyDisassociation = Action(
    "StartConfigurationPolicyDisassociation"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateActionTarget = Action("UpdateActionTarget")
UpdateConfigurationPolicy = Action("UpdateConfigurationPolicy")
UpdateFindingAggregator = Action("UpdateFindingAggregator")
UpdateFindings = Action("UpdateFindings")
UpdateInsight = Action("UpdateInsight")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
UpdateSecurityControl = Action("UpdateSecurityControl")
UpdateSecurityHubConfiguration = Action("UpdateSecurityHubConfiguration")
UpdateStandardsControl = Action("UpdateStandardsControl")
