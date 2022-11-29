# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Direct Connect"
prefix = "directconnect"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptDirectConnectGatewayAssociationProposal = Action(
    "AcceptDirectConnectGatewayAssociationProposal"
)
AllocateConnectionOnInterconnect = Action("AllocateConnectionOnInterconnect")
AllocateHostedConnection = Action("AllocateHostedConnection")
AllocatePrivateVirtualInterface = Action("AllocatePrivateVirtualInterface")
AllocatePublicVirtualInterface = Action("AllocatePublicVirtualInterface")
AllocateTransitVirtualInterface = Action("AllocateTransitVirtualInterface")
AssociateConnectionWithLag = Action("AssociateConnectionWithLag")
AssociateHostedConnection = Action("AssociateHostedConnection")
AssociateMacSecKey = Action("AssociateMacSecKey")
AssociateVirtualInterface = Action("AssociateVirtualInterface")
ConfirmConnection = Action("ConfirmConnection")
ConfirmCustomerAgreement = Action("ConfirmCustomerAgreement")
ConfirmPrivateVirtualInterface = Action("ConfirmPrivateVirtualInterface")
ConfirmPublicVirtualInterface = Action("ConfirmPublicVirtualInterface")
ConfirmTransitVirtualInterface = Action("ConfirmTransitVirtualInterface")
CreateBGPPeer = Action("CreateBGPPeer")
CreateConnection = Action("CreateConnection")
CreateDirectConnectGateway = Action("CreateDirectConnectGateway")
CreateDirectConnectGatewayAssociation = Action("CreateDirectConnectGatewayAssociation")
CreateDirectConnectGatewayAssociationProposal = Action(
    "CreateDirectConnectGatewayAssociationProposal"
)
CreateInterconnect = Action("CreateInterconnect")
CreateLag = Action("CreateLag")
CreatePrivateVirtualInterface = Action("CreatePrivateVirtualInterface")
CreatePublicVirtualInterface = Action("CreatePublicVirtualInterface")
CreateTransitVirtualInterface = Action("CreateTransitVirtualInterface")
DeleteBGPPeer = Action("DeleteBGPPeer")
DeleteConnection = Action("DeleteConnection")
DeleteDirectConnectGateway = Action("DeleteDirectConnectGateway")
DeleteDirectConnectGatewayAssociation = Action("DeleteDirectConnectGatewayAssociation")
DeleteDirectConnectGatewayAssociationProposal = Action(
    "DeleteDirectConnectGatewayAssociationProposal"
)
DeleteInterconnect = Action("DeleteInterconnect")
DeleteLag = Action("DeleteLag")
DeleteVirtualInterface = Action("DeleteVirtualInterface")
DescribeConnectionLoa = Action("DescribeConnectionLoa")
DescribeConnections = Action("DescribeConnections")
DescribeConnectionsOnInterconnect = Action("DescribeConnectionsOnInterconnect")
DescribeCustomerMetadata = Action("DescribeCustomerMetadata")
DescribeDirectConnectGatewayAssociationProposals = Action(
    "DescribeDirectConnectGatewayAssociationProposals"
)
DescribeDirectConnectGatewayAssociations = Action(
    "DescribeDirectConnectGatewayAssociations"
)
DescribeDirectConnectGatewayAttachments = Action(
    "DescribeDirectConnectGatewayAttachments"
)
DescribeDirectConnectGateways = Action("DescribeDirectConnectGateways")
DescribeHostedConnections = Action("DescribeHostedConnections")
DescribeInterconnectLoa = Action("DescribeInterconnectLoa")
DescribeInterconnects = Action("DescribeInterconnects")
DescribeLags = Action("DescribeLags")
DescribeLoa = Action("DescribeLoa")
DescribeLocations = Action("DescribeLocations")
DescribeRouterConfiguration = Action("DescribeRouterConfiguration")
DescribeTags = Action("DescribeTags")
DescribeVirtualGateways = Action("DescribeVirtualGateways")
DescribeVirtualInterfaces = Action("DescribeVirtualInterfaces")
DisassociateConnectionFromLag = Action("DisassociateConnectionFromLag")
DisassociateMacSecKey = Action("DisassociateMacSecKey")
ListVirtualInterfaceTestHistory = Action("ListVirtualInterfaceTestHistory")
StartBgpFailoverTest = Action("StartBgpFailoverTest")
StopBgpFailoverTest = Action("StopBgpFailoverTest")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnection = Action("UpdateConnection")
UpdateDirectConnectGateway = Action("UpdateDirectConnectGateway")
UpdateDirectConnectGatewayAssociation = Action("UpdateDirectConnectGatewayAssociation")
UpdateLag = Action("UpdateLag")
UpdateVirtualInterfaceAttributes = Action("UpdateVirtualInterfaceAttributes")
