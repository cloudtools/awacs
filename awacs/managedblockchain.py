# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Blockchain"
prefix = "managedblockchain"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAccessor = Action("CreateAccessor")
CreateMember = Action("CreateMember")
CreateNetwork = Action("CreateNetwork")
CreateNode = Action("CreateNode")
CreateProposal = Action("CreateProposal")
DeleteAccessor = Action("DeleteAccessor")
DeleteMember = Action("DeleteMember")
DeleteNode = Action("DeleteNode")
GET = Action("GET")
GetAccessor = Action("GetAccessor")
GetMember = Action("GetMember")
GetNetwork = Action("GetNetwork")
GetNode = Action("GetNode")
GetProposal = Action("GetProposal")
Invoke = Action("Invoke")
InvokeRpcBitcoinMainnet = Action("InvokeRpcBitcoinMainnet")
InvokeRpcBitcoinTestnet = Action("InvokeRpcBitcoinTestnet")
InvokeRpcPolygonMainnet = Action("InvokeRpcPolygonMainnet")
InvokeRpcPolygonMumbaiTestnet = Action("InvokeRpcPolygonMumbaiTestnet")
ListAccessors = Action("ListAccessors")
ListInvitations = Action("ListInvitations")
ListMembers = Action("ListMembers")
ListNetworks = Action("ListNetworks")
ListNodes = Action("ListNodes")
ListProposalVotes = Action("ListProposalVotes")
ListProposals = Action("ListProposals")
ListTagsForResource = Action("ListTagsForResource")
POST = Action("POST")
RejectInvitation = Action("RejectInvitation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMember = Action("UpdateMember")
UpdateNode = Action("UpdateNode")
VoteOnProposal = Action("VoteOnProposal")
