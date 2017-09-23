# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS WAF'
prefix = 'waf'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateByteMatchSet = Action('CreateByteMatchSet')
CreateIPSet = Action('CreateIPSet')
CreateRateBasedRule = Action('CreateRateBasedRule')
CreateRule = Action('CreateRule')
CreateSizeConstraintSet = Action('CreateSizeConstraintSet')
CreateSqlInjectionMatchSet = Action('CreateSqlInjectionMatchSet')
CreateWebACL = Action('CreateWebACL')
CreateXssMatchSet = Action('CreateXssMatchSet')
DeleteByteMatchSet = Action('DeleteByteMatchSet')
DeleteIPSet = Action('DeleteIPSet')
DeleteRateBasedRule = Action('DeleteRateBasedRule')
DeleteRule = Action('DeleteRule')
DeleteSizeConstraintSet = Action('DeleteSizeConstraintSet')
DeleteSqlInjectionMatchSet = Action('DeleteSqlInjectionMatchSet')
DeleteWebACL = Action('DeleteWebACL')
DeleteXssMatchSet = Action('DeleteXssMatchSet')
GetByteMatchSet = Action('GetByteMatchSet')
GetChangeToken = Action('GetChangeToken')
GetChangeTokenStatus = Action('GetChangeTokenStatus')
GetIPSet = Action('GetIPSet')
GetRateBasedRule = Action('GetRateBasedRule')
GetRateBasedRuleManagedKeys = Action('GetRateBasedRuleManagedKeys')
GetRule = Action('GetRule')
GetSampledRequests = Action('GetSampledRequests')
GetSizeConstraintSet = Action('GetSizeConstraintSet')
GetSqlInjectionMatchSet = Action('GetSqlInjectionMatchSet')
GetWebACL = Action('GetWebACL')
GetXssMatchSet = Action('GetXssMatchSet')
ListByteMatchSets = Action('ListByteMatchSets')
ListIPSets = Action('ListIPSets')
ListRateBasedules = Action('ListRateBasedules')
ListRules = Action('ListRules')
ListSizeConstraintSets = Action('ListSizeConstraintSets')
ListSqlInjectionMatchSets = Action('ListSqlInjectionMatchSets')
ListWebACLs = Action('ListWebACLs')
ListXssMatchSets = Action('ListXssMatchSets')
UpdateByteMatchSet = Action('UpdateByteMatchSet')
UpdateIPSet = Action('UpdateIPSet')
UpdateRateBasedRule = Action('UpdateRateBasedRule')
UpdateRule = Action('UpdateRule')
UpdateSizeConstraintSet = Action('UpdateSizeConstraintSet')
UpdateSqlInjectionMatchSet = Action('UpdateSqlInjectionMatchSet')
UpdateWebACL = Action('UpdateWebACL')
UpdateXssMatchSet = Action('UpdateXssMatchSet')
