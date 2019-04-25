# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Security Hub'
prefix = 'securityhub'


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
BatchDisableStandards = Action('BatchDisableStandards')
BatchEnableStandards = Action('BatchEnableStandards')
BatchImportFindings = Action('BatchImportFindings')
CreateInsight = Action('CreateInsight')
CreateMembers = Action('CreateMembers')
DeclineInvitations = Action('DeclineInvitations')
DeleteInsight = Action('DeleteInsight')
DeleteInvitations = Action('DeleteInvitations')
DeleteMembers = Action('DeleteMembers')
DisableImportFindingsForProduct = \
    Action('DisableImportFindingsForProduct')
DisableSecurityHub = Action('DisableSecurityHub')
DisassociateFromMasterAccount = Action('DisassociateFromMasterAccount')
DisassociateMembers = Action('DisassociateMembers')
EnableImportFindingsForProduct = Action('EnableImportFindingsForProduct')
EnableSecurityHub = Action('EnableSecurityHub')
GetEnabledStandards = Action('GetEnabledStandards')
GetFindings = Action('GetFindings')
GetInsightResults = Action('GetInsightResults')
GetInsights = Action('GetInsights')
GetInvitationsCount = Action('GetInvitationsCount')
GetMasterAccount = Action('GetMasterAccount')
GetMembers = Action('GetMembers')
InviteMembers = Action('InviteMembers')
ListEnabledProductsForImport = Action('ListEnabledProductsForImport')
ListInvitations = Action('ListInvitations')
ListMembers = Action('ListMembers')
UpdateFindings = Action('UpdateFindings')
UpdateInsight = Action('UpdateInsight')
