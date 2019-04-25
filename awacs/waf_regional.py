# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS WAF Regional'
prefix = 'waf-regional'


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
CreateByteMatchSet = Action('CreateByteMatchSet')
CreateGeoMatchSet = Action('CreateGeoMatchSet')
CreateIPSet = Action('CreateIPSet')
CreateRateBasedRule = Action('CreateRateBasedRule')
CreateRegexMatchSet = Action('CreateRegexMatchSet')
CreateRegexPatternSet = Action('CreateRegexPatternSet')
CreateRule = Action('CreateRule')
CreateRuleGroup = Action('CreateRuleGroup')
CreateSizeConstraintSet = Action('CreateSizeConstraintSet')
CreateSqlInjectionMatchSet = Action('CreateSqlInjectionMatchSet')
CreateWebACL = Action('CreateWebACL')
CreateXssMatchSet = Action('CreateXssMatchSet')
DeleteByteMatchSet = Action('DeleteByteMatchSet')
DeleteGeoMatchSet = Action('DeleteGeoMatchSet')
DeleteIPSet = Action('DeleteIPSet')
DeletePermissionPolicy = Action('DeletePermissionPolicy')
DeleteRateBasedRule = Action('DeleteRateBasedRule')
DeleteRegexMatchSet = Action('DeleteRegexMatchSet')
DeleteRegexPatternSet = Action('DeleteRegexPatternSet')
DeleteRule = Action('DeleteRule')
DeleteRuleGroup = Action('DeleteRuleGroup')
DeleteSizeConstraintSet = Action('DeleteSizeConstraintSet')
DeleteSqlInjectionMatchSet = Action('DeleteSqlInjectionMatchSet')
DeleteWebACL = Action('DeleteWebACL')
DeleteXssMatchSet = Action('DeleteXssMatchSet')
DisassociateWebACL = Action('DisassociateWebACL')
GetByteMatchSet = Action('GetByteMatchSet')
GetChangeToken = Action('GetChangeToken')
GetChangeTokenStatus = Action('GetChangeTokenStatus')
GetGeoMatchSet = Action('GetGeoMatchSet')
GetIPSet = Action('GetIPSet')
GetPermissionPolicy = Action('GetPermissionPolicy')
GetRateBasedRule = Action('GetRateBasedRule')
GetRateBasedRuleManagedKeys = Action('GetRateBasedRuleManagedKeys')
GetRegexMatchSet = Action('GetRegexMatchSet')
GetRegexPatternSet = Action('GetRegexPatternSet')
GetRule = Action('GetRule')
GetRuleGroup = Action('GetRuleGroup')
GetSampledRequests = Action('GetSampledRequests')
GetSizeConstraintSet = Action('GetSizeConstraintSet')
GetSqlInjectionMatchSet = Action('GetSqlInjectionMatchSet')
GetWebACL = Action('GetWebACL')
GetWebACLForResource = Action('GetWebACLForResource')
GetXssMatchSet = Action('GetXssMatchSet')
ListActivatedRulesInRuleGroup = Action('ListActivatedRulesInRuleGroup')
ListByteMatchSets = Action('ListByteMatchSets')
ListGeoMatchSets = Action('ListGeoMatchSets')
ListIPSets = Action('ListIPSets')
ListRateBasedRules = Action('ListRateBasedRules')
ListRegexMatchSets = Action('ListRegexMatchSets')
ListRegexPatternSets = Action('ListRegexPatternSets')
ListResourcesForWebACL = Action('ListResourcesForWebACL')
ListRuleGroups = Action('ListRuleGroups')
ListRules = Action('ListRules')
ListSizeConstraintSets = Action('ListSizeConstraintSets')
ListSqlInjectionMatchSets = Action('ListSqlInjectionMatchSets')
ListSubscribedRuleGroups = Action('ListSubscribedRuleGroups')
ListWebACLs = Action('ListWebACLs')
ListXssMatchSets = Action('ListXssMatchSets')
PutPermissionPolicy = Action('PutPermissionPolicy')
UpdateByteMatchSet = Action('UpdateByteMatchSet')
UpdateGeoMatchSet = Action('UpdateGeoMatchSet')
UpdateIPSet = Action('UpdateIPSet')
UpdateRateBasedRule = Action('UpdateRateBasedRule')
UpdateRegexMatchSet = Action('UpdateRegexMatchSet')
UpdateRegexPatternSet = Action('UpdateRegexPatternSet')
UpdateRule = Action('UpdateRule')
UpdateRuleGroup = Action('UpdateRuleGroup')
UpdateSizeConstraintSet = Action('UpdateSizeConstraintSet')
UpdateSqlInjectionMatchSet = Action('UpdateSqlInjectionMatchSet')
UpdateWebACL = Action('UpdateWebACL')
UpdateXssMatchSet = Action('UpdateXssMatchSet')
