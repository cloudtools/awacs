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
ConnectorRegistrationsV2 = Action("ConnectorRegistrationsV2")
CreateActionTarget = Action("CreateActionTarget")
CreateAggregatorV2 = Action("CreateAggregatorV2")
CreateAutomationRule = Action("CreateAutomationRule")
CreateAutomationRuleV2 = Action("CreateAutomationRuleV2")
CreateConfigurationPolicy = Action("CreateConfigurationPolicy")
CreateConnectorV2 = Action("CreateConnectorV2")
CreateFindingAggregator = Action("CreateFindingAggregator")
CreateInsight = Action("CreateInsight")
CreateMembers = Action("CreateMembers")
CreateTicketV2 = Action("CreateTicketV2")
DeclineInvitations = Action("DeclineInvitations")
DeleteActionTarget = Action("DeleteActionTarget")
DeleteAggregatorV2 = Action("DeleteAggregatorV2")
DeleteAutomationRuleV2 = Action("DeleteAutomationRuleV2")
DeleteConfigurationPolicy = Action("DeleteConfigurationPolicy")
DeleteConnectorV2 = Action("DeleteConnectorV2")
DeleteFindingAggregator = Action("DeleteFindingAggregator")
DeleteInsight = Action("DeleteInsight")
DeleteInvitations = Action("DeleteInvitations")
DeleteMembers = Action("DeleteMembers")
DescribeActionTargets = Action("DescribeActionTargets")
DescribeHub = Action("DescribeHub")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
DescribeProducts = Action("DescribeProducts")
DescribeProductsV2 = Action("DescribeProductsV2")
DescribeSecurityHubV2 = Action("DescribeSecurityHubV2")
DescribeStandards = Action("DescribeStandards")
DescribeStandardsControls = Action("DescribeStandardsControls")
DisableImportFindingsForProduct = Action("DisableImportFindingsForProduct")
DisableOrganizationAdminAccount = Action("DisableOrganizationAdminAccount")
DisableSecurityHub = Action("DisableSecurityHub")
DisableSecurityHubV2 = Action("DisableSecurityHubV2")
DisassociateFromAdministratorAccount = Action("DisassociateFromAdministratorAccount")
DisassociateFromMasterAccount = Action("DisassociateFromMasterAccount")
DisassociateMembers = Action("DisassociateMembers")
EnableImportFindingsForProduct = Action("EnableImportFindingsForProduct")
EnableOrganizationAdminAccount = Action("EnableOrganizationAdminAccount")
EnableSecurityHub = Action("EnableSecurityHub")
EnableSecurityHubV2 = Action("EnableSecurityHubV2")
GetAdhocInsightResults = Action("GetAdhocInsightResults")
GetAdministratorAccount = Action("GetAdministratorAccount")
GetAggregatorV2 = Action("GetAggregatorV2")
GetAutomationRuleV2 = Action("GetAutomationRuleV2")
GetConfigurationPolicy = Action("GetConfigurationPolicy")
GetConfigurationPolicyAssociation = Action("GetConfigurationPolicyAssociation")
GetConnectorV2 = Action("GetConnectorV2")
GetControlFindingSummary = Action("GetControlFindingSummary")
GetEnabledStandards = Action("GetEnabledStandards")
GetFindingAggregator = Action("GetFindingAggregator")
GetFindingHistory = Action("GetFindingHistory")
GetFindings = Action("GetFindings")
GetFindingsTrendsV2 = Action("GetFindingsTrendsV2")
GetFreeTrialEndDate = Action("GetFreeTrialEndDate")
GetFreeTrialUsage = Action("GetFreeTrialUsage")
GetInsightFindingTrend = Action("GetInsightFindingTrend")
GetInsightResults = Action("GetInsightResults")
GetInsights = Action("GetInsights")
GetInvitationsCount = Action("GetInvitationsCount")
GetMasterAccount = Action("GetMasterAccount")
GetMembers = Action("GetMembers")
GetResourceStatisticsV2 = Action("GetResourceStatisticsV2")
GetResourcesStatisticsV2 = Action("GetResourcesStatisticsV2")
GetResourcesTrendsV2 = Action("GetResourcesTrendsV2")
GetResourcesV2 = Action("GetResourcesV2")
GetSecurityControlDefinition = Action("GetSecurityControlDefinition")
GetUsage = Action("GetUsage")
InviteMembers = Action("InviteMembers")
ListAggregatorV2s = Action("ListAggregatorV2s")
ListAggregatorsV2 = Action("ListAggregatorsV2")
ListAutomationRules = Action("ListAutomationRules")
ListAutomationRulesV2 = Action("ListAutomationRulesV2")
ListConfigurationPolicies = Action("ListConfigurationPolicies")
ListConfigurationPolicyAssociations = Action("ListConfigurationPolicyAssociations")
ListConnectorsV2 = Action("ListConnectorsV2")
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
UpdateAggregatorV2 = Action("UpdateAggregatorV2")
UpdateAutomationRuleV2 = Action("UpdateAutomationRuleV2")
UpdateConfigurationPolicy = Action("UpdateConfigurationPolicy")
UpdateConnectorV2 = Action("UpdateConnectorV2")
UpdateFindingAggregator = Action("UpdateFindingAggregator")
UpdateFindings = Action("UpdateFindings")
UpdateInsight = Action("UpdateInsight")
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
UpdateSecurityControl = Action("UpdateSecurityControl")
UpdateSecurityHubConfiguration = Action("UpdateSecurityHubConfiguration")
UpdateStandardsControl = Action("UpdateStandardsControl")
