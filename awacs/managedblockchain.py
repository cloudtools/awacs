# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Managed Blockchain'
prefix = 'managedblockchain'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateMember = Action('CreateMember')
CreateNetwork = Action('CreateNetwork')
CreateNode = Action('CreateNode')
CreateProposal = Action('CreateProposal')
DeleteMember = Action('DeleteMember')
DeleteNode = Action('DeleteNode')
GetMember = Action('GetMember')
GetNetwork = Action('GetNetwork')
GetNode = Action('GetNode')
GetProposal = Action('GetProposal')
ListInvitations = Action('ListInvitations')
ListMembers = Action('ListMembers')
ListNetworks = Action('ListNetworks')
ListNodes = Action('ListNodes')
ListProposalVotes = Action('ListProposalVotes')
ListProposals = Action('ListProposals')
RejectInvitation = Action('RejectInvitation')
UpdateMember = Action('UpdateMember')
UpdateNode = Action('UpdateNode')
VoteOnProposal = Action('VoteOnProposal')
