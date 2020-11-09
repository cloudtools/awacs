# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EventBridge'
prefix = 'events'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ActivateEventSource = Action('ActivateEventSource')
CancelReplay = Action('CancelReplay')
CreateArchive = Action('CreateArchive')
CreateEventBus = Action('CreateEventBus')
CreatePartnerEventSource = Action('CreatePartnerEventSource')
DeactivateEventSource = Action('DeactivateEventSource')
DeleteArchive = Action('DeleteArchive')
DeleteEventBus = Action('DeleteEventBus')
DeletePartnerEventSource = Action('DeletePartnerEventSource')
DeleteRule = Action('DeleteRule')
DescribeArchive = Action('DescribeArchive')
DescribeEventBus = Action('DescribeEventBus')
DescribeEventSource = Action('DescribeEventSource')
DescribePartnerEventSource = Action('DescribePartnerEventSource')
DescribeReplay = Action('DescribeReplay')
DescribeRule = Action('DescribeRule')
DisableRule = Action('DisableRule')
EnableRule = Action('EnableRule')
ListArchives = Action('ListArchives')
ListEventBuses = Action('ListEventBuses')
ListEventSources = Action('ListEventSources')
ListPartnerEventSourceAccounts = Action('ListPartnerEventSourceAccounts')
ListPartnerEventSources = Action('ListPartnerEventSources')
ListReplays = Action('ListReplays')
ListRuleNamesByTarget = Action('ListRuleNamesByTarget')
ListRules = Action('ListRules')
ListTagsForResource = Action('ListTagsForResource')
ListTargetsByRule = Action('ListTargetsByRule')
PutEvents = Action('PutEvents')
PutPartnerEvents = Action('PutPartnerEvents')
PutPermission = Action('PutPermission')
PutRule = Action('PutRule')
PutTargets = Action('PutTargets')
RemovePermission = Action('RemovePermission')
RemoveTargets = Action('RemoveTargets')
StartReplay = Action('StartReplay')
TagResource = Action('TagResource')
TestEventPattern = Action('TestEventPattern')
UntagResource = Action('UntagResource')
UpdateArchive = Action('UpdateArchive')
