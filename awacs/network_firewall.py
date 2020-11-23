# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Network Firewall'
prefix = 'network-firewall'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateFirewallPolicy = Action('AssociateFirewallPolicy')
AssociateSubnets = Action('AssociateSubnets')
CreateFirewall = Action('CreateFirewall')
CreateFirewallPolicy = Action('CreateFirewallPolicy')
CreateRuleGroup = Action('CreateRuleGroup')
DeleteFirewall = Action('DeleteFirewall')
DeleteFirewallPolicy = Action('DeleteFirewallPolicy')
DeleteResourcePolicy = Action('DeleteResourcePolicy')
DeleteRuleGroup = Action('DeleteRuleGroup')
DescribeFirewall = Action('DescribeFirewall')
DescribeFirewallPolicy = Action('DescribeFirewallPolicy')
DescribeLoggingConfiguration = Action('DescribeLoggingConfiguration')
DescribeResourcePolicy = Action('DescribeResourcePolicy')
DescribeRuleGroup = Action('DescribeRuleGroup')
DisassociateSubnets = Action('DisassociateSubnets')
ListFirewallPolicies = Action('ListFirewallPolicies')
ListFirewalls = Action('ListFirewalls')
ListRuleGroups = Action('ListRuleGroups')
ListTagsForResource = Action('ListTagsForResource')
PutResourcePolicy = Action('PutResourcePolicy')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateFirewallDeleteProtection = Action('UpdateFirewallDeleteProtection')
UpdateFirewallDescription = Action('UpdateFirewallDescription')
UpdateFirewallPolicy = Action('UpdateFirewallPolicy')
UpdateFirewallPolicyChangeProtection = \
    Action('UpdateFirewallPolicyChangeProtection')
UpdateLoggingConfiguration = Action('UpdateLoggingConfiguration')
UpdateRuleGroup = Action('UpdateRuleGroup')
UpdateSubnetChangeProtection = Action('UpdateSubnetChangeProtection')
