# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Detective'
prefix = 'detective'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptInvitation = Action('AcceptInvitation')
CreateGraph = Action('CreateGraph')
CreateMembers = Action('CreateMembers')
DeleteGraph = Action('DeleteGraph')
DeleteMembers = Action('DeleteMembers')
DisassociateMembership = Action('DisassociateMembership')
GetFreeTrialEligibility = Action('GetFreeTrialEligibility')
GetGraphIngestState = Action('GetGraphIngestState')
GetMembers = Action('GetMembers')
GetPricingInformation = Action('GetPricingInformation')
GetUsageInformation = Action('GetUsageInformation')
ListGraphs = Action('ListGraphs')
ListInvitations = Action('ListInvitations')
ListMembers = Action('ListMembers')
RejectInvitation = Action('RejectInvitation')
SearchGraph = Action('SearchGraph')
StartMonitoringMember = Action('StartMonitoringMember')
