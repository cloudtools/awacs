# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon GuardDuty'
prefix = 'guardduty'


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
ArchiveFindings = Action('ArchiveFindings')
CreateDetector = Action('CreateDetector')
CreateIPSet = Action('CreateIPSet')
CreateMembers = Action('CreateMembers')
CreateSampleFindings = Action('CreateSampleFindings')
CreateThreatIntelSet = Action('CreateThreatIntelSet')
DeclineInvitations = Action('DeclineInvitations')
DeleteDetector = Action('DeleteDetector')
DeleteIPSet = Action('DeleteIPSet')
DeleteInvitations = Action('DeleteInvitations')
DeleteMembers = Action('DeleteMembers')
DeleteThreatIntelSet = Action('DeleteThreatIntelSet')
DisassociateFromMasterAccount = Action('DisassociateFromMasterAccount')
DisassociateMembers = Action('DisassociateMembers')
GetDetector = Action('GetDetector')
GetFindings = Action('GetFindings')
GetFindingsStatistics = Action('GetFindingsStatistics')
GetIPSet = Action('GetIPSet')
GetInvitationsCount = Action('GetInvitationsCount')
GetMasterAccount = Action('GetMasterAccount')
GetMembers = Action('GetMembers')
GetThreatIntelSet = Action('GetThreatIntelSet')
InviteMembers = Action('InviteMembers')
ListDetectors = Action('ListDetectors')
ListFindings = Action('ListFindings')
ListIPSets = Action('ListIPSets')
ListInvitations = Action('ListInvitations')
ListMembers = Action('ListMembers')
ListThreatIntelSets = Action('ListThreatIntelSets')
StartMonitoringMembers = Action('StartMonitoringMembers')
StopMonitoringMembers = Action('StopMonitoringMembers')
UnarchiveFindings = Action('UnarchiveFindings')
UpdateDetector = Action('UpdateDetector')
UpdateFindingsFeedback = Action('UpdateFindingsFeedback')
UpdateIPSet = Action('UpdateIPSet')
UpdateThreatIntelSet = Action('UpdateThreatIntelSet')
