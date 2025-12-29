# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Network Firewall"
prefix = "network-firewall"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptNetworkFirewallTransitGatewayAttachment = Action(
    "AcceptNetworkFirewallTransitGatewayAttachment"
)
AssociateAvailabilityZones = Action("AssociateAvailabilityZones")
AssociateFirewallPolicy = Action("AssociateFirewallPolicy")
AssociateSubnets = Action("AssociateSubnets")
AttachRuleGroupsToProxyConfiguration = Action("AttachRuleGroupsToProxyConfiguration")
CreateFirewall = Action("CreateFirewall")
CreateFirewallPolicy = Action("CreateFirewallPolicy")
CreateProxy = Action("CreateProxy")
CreateProxyConfiguration = Action("CreateProxyConfiguration")
CreateProxyRuleGroup = Action("CreateProxyRuleGroup")
CreateProxyRules = Action("CreateProxyRules")
CreateRuleGroup = Action("CreateRuleGroup")
CreateTLSInspectionConfiguration = Action("CreateTLSInspectionConfiguration")
CreateVpcEndpointAssociation = Action("CreateVpcEndpointAssociation")
DeleteFirewall = Action("DeleteFirewall")
DeleteFirewallPolicy = Action("DeleteFirewallPolicy")
DeleteNetworkFirewallTransitGatewayAttachment = Action(
    "DeleteNetworkFirewallTransitGatewayAttachment"
)
DeleteProxy = Action("DeleteProxy")
DeleteProxyConfiguration = Action("DeleteProxyConfiguration")
DeleteProxyRuleGroup = Action("DeleteProxyRuleGroup")
DeleteProxyRules = Action("DeleteProxyRules")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRuleGroup = Action("DeleteRuleGroup")
DeleteTLSInspectionConfiguration = Action("DeleteTLSInspectionConfiguration")
DeleteVpcEndpointAssociation = Action("DeleteVpcEndpointAssociation")
DescribeFirewall = Action("DescribeFirewall")
DescribeFirewallMetadata = Action("DescribeFirewallMetadata")
DescribeFirewallPolicy = Action("DescribeFirewallPolicy")
DescribeFlowOperation = Action("DescribeFlowOperation")
DescribeLoggingConfiguration = Action("DescribeLoggingConfiguration")
DescribeProxy = Action("DescribeProxy")
DescribeProxyConfiguration = Action("DescribeProxyConfiguration")
DescribeProxyRule = Action("DescribeProxyRule")
DescribeProxyRuleGroup = Action("DescribeProxyRuleGroup")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeRuleGroup = Action("DescribeRuleGroup")
DescribeRuleGroupMetadata = Action("DescribeRuleGroupMetadata")
DescribeRuleGroupSummary = Action("DescribeRuleGroupSummary")
DescribeTLSInspectionConfiguration = Action("DescribeTLSInspectionConfiguration")
DescribeVpcEndpointAssociation = Action("DescribeVpcEndpointAssociation")
DetachRuleGroupsFromProxyConfiguration = Action(
    "DetachRuleGroupsFromProxyConfiguration"
)
DisassociateAvailabilityZones = Action("DisassociateAvailabilityZones")
DisassociateSubnets = Action("DisassociateSubnets")
GetAnalysisReportResults = Action("GetAnalysisReportResults")
ListAnalysisReports = Action("ListAnalysisReports")
ListFirewallPolicies = Action("ListFirewallPolicies")
ListFirewalls = Action("ListFirewalls")
ListFlowOperationResults = Action("ListFlowOperationResults")
ListFlowOperations = Action("ListFlowOperations")
ListProxies = Action("ListProxies")
ListProxyConfigurations = Action("ListProxyConfigurations")
ListProxyRuleGroups = Action("ListProxyRuleGroups")
ListRuleGroups = Action("ListRuleGroups")
ListTLSInspectionConfigurations = Action("ListTLSInspectionConfigurations")
ListTagsForResource = Action("ListTagsForResource")
ListVpcEndpointAssociations = Action("ListVpcEndpointAssociations")
PutResourcePolicy = Action("PutResourcePolicy")
RejectNetworkFirewallTransitGatewayAttachment = Action(
    "RejectNetworkFirewallTransitGatewayAttachment"
)
StartAnalysisReport = Action("StartAnalysisReport")
StartFlowCapture = Action("StartFlowCapture")
StartFlowFlush = Action("StartFlowFlush")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAvailabilityZoneChangeProtection = Action(
    "UpdateAvailabilityZoneChangeProtection"
)
UpdateFirewallAnalysisSettings = Action("UpdateFirewallAnalysisSettings")
UpdateFirewallDeleteProtection = Action("UpdateFirewallDeleteProtection")
UpdateFirewallDescription = Action("UpdateFirewallDescription")
UpdateFirewallEncryptionConfiguration = Action("UpdateFirewallEncryptionConfiguration")
UpdateFirewallPolicy = Action("UpdateFirewallPolicy")
UpdateFirewallPolicyChangeProtection = Action("UpdateFirewallPolicyChangeProtection")
UpdateLoggingConfiguration = Action("UpdateLoggingConfiguration")
UpdateProxy = Action("UpdateProxy")
UpdateProxyConfiguration = Action("UpdateProxyConfiguration")
UpdateProxyRule = Action("UpdateProxyRule")
UpdateProxyRuleGroupPriorities = Action("UpdateProxyRuleGroupPriorities")
UpdateProxyRulePriorities = Action("UpdateProxyRulePriorities")
UpdateRuleGroup = Action("UpdateRuleGroup")
UpdateSubnetChangeProtection = Action("UpdateSubnetChangeProtection")
UpdateTLSInspectionConfiguration = Action("UpdateTLSInspectionConfiguration")
