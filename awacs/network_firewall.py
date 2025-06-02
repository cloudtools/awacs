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


AssociateFirewallPolicy = Action("AssociateFirewallPolicy")
AssociateSubnets = Action("AssociateSubnets")
CreateFirewall = Action("CreateFirewall")
CreateFirewallPolicy = Action("CreateFirewallPolicy")
CreateRuleGroup = Action("CreateRuleGroup")
CreateTLSInspectionConfiguration = Action("CreateTLSInspectionConfiguration")
CreateVpcEndpointAssociation = Action("CreateVpcEndpointAssociation")
DeleteFirewall = Action("DeleteFirewall")
DeleteFirewallPolicy = Action("DeleteFirewallPolicy")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRuleGroup = Action("DeleteRuleGroup")
DeleteTLSInspectionConfiguration = Action("DeleteTLSInspectionConfiguration")
DeleteVpcEndpointAssociation = Action("DeleteVpcEndpointAssociation")
DescribeFirewall = Action("DescribeFirewall")
DescribeFirewallMetadata = Action("DescribeFirewallMetadata")
DescribeFirewallPolicy = Action("DescribeFirewallPolicy")
DescribeFlowOperation = Action("DescribeFlowOperation")
DescribeLoggingConfiguration = Action("DescribeLoggingConfiguration")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeRuleGroup = Action("DescribeRuleGroup")
DescribeRuleGroupMetadata = Action("DescribeRuleGroupMetadata")
DescribeTLSInspectionConfiguration = Action("DescribeTLSInspectionConfiguration")
DescribeVpcEndpointAssociation = Action("DescribeVpcEndpointAssociation")
DisassociateSubnets = Action("DisassociateSubnets")
GetAnalysisReportResults = Action("GetAnalysisReportResults")
ListAnalysisReports = Action("ListAnalysisReports")
ListFirewallPolicies = Action("ListFirewallPolicies")
ListFirewalls = Action("ListFirewalls")
ListFlowOperationResults = Action("ListFlowOperationResults")
ListFlowOperations = Action("ListFlowOperations")
ListRuleGroups = Action("ListRuleGroups")
ListTLSInspectionConfigurations = Action("ListTLSInspectionConfigurations")
ListTagsForResource = Action("ListTagsForResource")
ListVpcEndpointAssociations = Action("ListVpcEndpointAssociations")
PutResourcePolicy = Action("PutResourcePolicy")
StartAnalysisReport = Action("StartAnalysisReport")
StartFlowCapture = Action("StartFlowCapture")
StartFlowFlush = Action("StartFlowFlush")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFirewallAnalysisSettings = Action("UpdateFirewallAnalysisSettings")
UpdateFirewallDeleteProtection = Action("UpdateFirewallDeleteProtection")
UpdateFirewallDescription = Action("UpdateFirewallDescription")
UpdateFirewallEncryptionConfiguration = Action("UpdateFirewallEncryptionConfiguration")
UpdateFirewallPolicy = Action("UpdateFirewallPolicy")
UpdateFirewallPolicyChangeProtection = Action("UpdateFirewallPolicyChangeProtection")
UpdateLoggingConfiguration = Action("UpdateLoggingConfiguration")
UpdateRuleGroup = Action("UpdateRuleGroup")
UpdateSubnetChangeProtection = Action("UpdateSubnetChangeProtection")
UpdateTLSInspectionConfiguration = Action("UpdateTLSInspectionConfiguration")
