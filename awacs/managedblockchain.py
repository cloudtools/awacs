# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Blockchain"
prefix = "managedblockchain"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateMember = Action("CreateMember")
CreateNetwork = Action("CreateNetwork")
CreateNode = Action("CreateNode")
CreateProposal = Action("CreateProposal")
DeleteMember = Action("DeleteMember")
DeleteNode = Action("DeleteNode")
GetMember = Action("GetMember")
GetNetwork = Action("GetNetwork")
GetNode = Action("GetNode")
GetProposal = Action("GetProposal")
ListInvitations = Action("ListInvitations")
ListMembers = Action("ListMembers")
ListNetworks = Action("ListNetworks")
ListNodes = Action("ListNodes")
ListProposalVotes = Action("ListProposalVotes")
ListProposals = Action("ListProposals")
ListTagsForResource = Action("ListTagsForResource")
RejectInvitation = Action("RejectInvitation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMember = Action("UpdateMember")
UpdateNode = Action("UpdateNode")
VoteOnProposal = Action("VoteOnProposal")
