# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS WAF V2'
prefix = 'wafv2'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateWebACL = Action('AssociateWebACL')
CheckCapacity = Action('CheckCapacity')
CreateIPSet = Action('CreateIPSet')
CreateRegexPatternSet = Action('CreateRegexPatternSet')
CreateRuleGroup = Action('CreateRuleGroup')
CreateWebACL = Action('CreateWebACL')
DeleteFirewallManagerRuleGroups = \
    Action('DeleteFirewallManagerRuleGroups')
DeleteIPSet = Action('DeleteIPSet')
DeleteLoggingConfiguration = Action('DeleteLoggingConfiguration')
DeletePermissionPolicy = Action('DeletePermissionPolicy')
DeleteRegexPatternSet = Action('DeleteRegexPatternSet')
DeleteRuleGroup = Action('DeleteRuleGroup')
DeleteWebACL = Action('DeleteWebACL')
DescribeManagedRuleGroup = Action('DescribeManagedRuleGroup')
DisassociateFirewallManager = Action('DisassociateFirewallManager')
DisassociateWebACL = Action('DisassociateWebACL')
GetIPSet = Action('GetIPSet')
GetLoggingConfiguration = Action('GetLoggingConfiguration')
GetPermissionPolicy = Action('GetPermissionPolicy')
GetRateBasedStatementManagedKeys = \
    Action('GetRateBasedStatementManagedKeys')
GetRegexPatternSet = Action('GetRegexPatternSet')
GetRuleGroup = Action('GetRuleGroup')
GetSampledRequests = Action('GetSampledRequests')
GetWebACL = Action('GetWebACL')
GetWebACLForResource = Action('GetWebACLForResource')
ListAvailableManagedRuleGroups = Action('ListAvailableManagedRuleGroups')
ListIPSets = Action('ListIPSets')
ListLoggingConfigurations = Action('ListLoggingConfigurations')
ListRegexPatternSets = Action('ListRegexPatternSets')
ListResourcesForWebACL = Action('ListResourcesForWebACL')
ListRuleGroups = Action('ListRuleGroups')
ListTagsForResource = Action('ListTagsForResource')
ListWebACLs = Action('ListWebACLs')
PutFirewallManagerRuleGroups = Action('PutFirewallManagerRuleGroups')
PutLoggingConfiguration = Action('PutLoggingConfiguration')
PutPermissionPolicy = Action('PutPermissionPolicy')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateIPSet = Action('UpdateIPSet')
UpdateRegexPatternSet = Action('UpdateRegexPatternSet')
UpdateRuleGroup = Action('UpdateRuleGroup')
UpdateWebACL = Action('UpdateWebACL')
