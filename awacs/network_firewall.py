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
DeleteFirewall = Action("DeleteFirewall")
DeleteFirewallPolicy = Action("DeleteFirewallPolicy")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRuleGroup = Action("DeleteRuleGroup")
DeleteTLSInspectionConfiguration = Action("DeleteTLSInspectionConfiguration")
DescribeFirewall = Action("DescribeFirewall")
DescribeFirewallPolicy = Action("DescribeFirewallPolicy")
DescribeLoggingConfiguration = Action("DescribeLoggingConfiguration")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeRuleGroup = Action("DescribeRuleGroup")
DescribeRuleGroupMetadata = Action("DescribeRuleGroupMetadata")
DescribeTLSInspectionConfiguration = Action("DescribeTLSInspectionConfiguration")
DisassociateSubnets = Action("DisassociateSubnets")
ListFirewallPolicies = Action("ListFirewallPolicies")
ListFirewalls = Action("ListFirewalls")
ListRuleGroups = Action("ListRuleGroups")
ListTLSInspectionConfigurations = Action("ListTLSInspectionConfigurations")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFirewallDeleteProtection = Action("UpdateFirewallDeleteProtection")
UpdateFirewallDescription = Action("UpdateFirewallDescription")
UpdateFirewallEncryptionConfiguration = Action("UpdateFirewallEncryptionConfiguration")
UpdateFirewallPolicy = Action("UpdateFirewallPolicy")
UpdateFirewallPolicyChangeProtection = Action("UpdateFirewallPolicyChangeProtection")
UpdateLoggingConfiguration = Action("UpdateLoggingConfiguration")
UpdateRuleGroup = Action("UpdateRuleGroup")
UpdateSubnetChangeProtection = Action("UpdateSubnetChangeProtection")
UpdateTLSInspectionConfiguration = Action("UpdateTLSInspectionConfiguration")
