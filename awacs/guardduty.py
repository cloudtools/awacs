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
CreateFilter = Action('CreateFilter')
CreateIPSet = Action('CreateIPSet')
CreateMembers = Action('CreateMembers')
CreatePublishingDestination = Action('CreatePublishingDestination')
CreateSampleFindings = Action('CreateSampleFindings')
CreateThreatIntelSet = Action('CreateThreatIntelSet')
DeclineInvitations = Action('DeclineInvitations')
DeleteDetector = Action('DeleteDetector')
DeleteFilter = Action('DeleteFilter')
DeleteIPSet = Action('DeleteIPSet')
DeleteInvitations = Action('DeleteInvitations')
DeleteMembers = Action('DeleteMembers')
DeletePublishingDestination = Action('DeletePublishingDestination')
DeleteThreatIntelSet = Action('DeleteThreatIntelSet')
DescribeOrganizationConfiguration = \
    Action('DescribeOrganizationConfiguration')
DescribePublishingDestination = Action('DescribePublishingDestination')
DisableOrganizationAdminAccount = \
    Action('DisableOrganizationAdminAccount')
DisassociateFromMasterAccount = Action('DisassociateFromMasterAccount')
DisassociateMembers = Action('DisassociateMembers')
EnableOrganizationAdminAccount = Action('EnableOrganizationAdminAccount')
GetDetector = Action('GetDetector')
GetFilter = Action('GetFilter')
GetFindings = Action('GetFindings')
GetFindingsStatistics = Action('GetFindingsStatistics')
GetIPSet = Action('GetIPSet')
GetInvitationsCount = Action('GetInvitationsCount')
GetMasterAccount = Action('GetMasterAccount')
GetMembers = Action('GetMembers')
GetThreatIntelSet = Action('GetThreatIntelSet')
InviteMembers = Action('InviteMembers')
ListDetectors = Action('ListDetectors')
ListFilters = Action('ListFilters')
ListFindings = Action('ListFindings')
ListIPSets = Action('ListIPSets')
ListInvitations = Action('ListInvitations')
ListMembers = Action('ListMembers')
ListOrganizationAdminAccounts = Action('ListOrganizationAdminAccounts')
ListPublishingDestinations = Action('ListPublishingDestinations')
ListTagsForResource = Action('ListTagsForResource')
ListThreatIntelSets = Action('ListThreatIntelSets')
StartMonitoringMembers = Action('StartMonitoringMembers')
StopMonitoringMembers = Action('StopMonitoringMembers')
TagResource = Action('TagResource')
UnarchiveFindings = Action('UnarchiveFindings')
UntagResource = Action('UntagResource')
UpdateDetector = Action('UpdateDetector')
UpdateFilter = Action('UpdateFilter')
UpdateFindingsFeedback = Action('UpdateFindingsFeedback')
UpdateIPSet = Action('UpdateIPSet')
UpdateOrganizationConfiguration = \
    Action('UpdateOrganizationConfiguration')
UpdatePublishingDestination = Action('UpdatePublishingDestination')
UpdateThreatIntelSet = Action('UpdateThreatIntelSet')
