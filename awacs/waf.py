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
CreateRule = Action('CreateRule')
CreateSqlInjectionMatchSet = Action('CreateSqlInjectionMatchSet')
CreateWebACL = Action('CreateWebACL')
DeleteByteMatchSet = Action('DeleteByteMatchSet')
DeleteIPSet = Action('DeleteIPSet')
DeleteRule = Action('DeleteRule')
DeleteSqlInjectionMatchSet = Action('DeleteSqlInjectionMatchSet')
DeleteWebACL = Action('DeleteWebACL')
GetByteMatchSet = Action('GetByteMatchSet')
GetChangeToken = Action('GetChangeToken')
GetChangeTokenStatus = Action('GetChangeTokenStatus')
GetIPSet = Action('GetIPSet')
GetRule = Action('GetRule')
GetSampledRequests = Action('GetSampledRequests')
GetSqlInjectionMatchSet = Action('GetSqlInjectionMatchSet')
GetWebACL = Action('GetWebACL')
ListByteMatchSets = Action('ListByteMatchSets')
ListIPSets = Action('ListIPSets')
ListRules = Action('ListRules')
ListSqlInjectionMatchSets = Action('ListSqlInjectionMatchSets')
ListWebACLs = Action('ListWebACLs')
UpdateByteMatchSet = Action('UpdateByteMatchSet')
UpdateIPSet = Action('UpdateIPSet')
UpdateRule = Action('UpdateRule')
UpdateSqlInjectionMatchSet = Action('UpdateSqlInjectionMatchSet')
UpdateWebACL = Action('UpdateWebACL')
