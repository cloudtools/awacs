# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Direct Connect'
prefix = 'directconnect'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AllocateConnectionOnInterconnect = \
    Action('AllocateConnectionOnInterconnect')
AllocateHostedConnection = Action('AllocateHostedConnection')
AllocatePrivateVirtualInterface = \
    Action('AllocatePrivateVirtualInterface')
AllocatePublicVirtualInterface = Action('AllocatePublicVirtualInterface')
AssociateConnectionWithLag = Action('AssociateConnectionWithLag')
AssociateHostedConnection = Action('AssociateHostedConnection')
AssociateVirtualInterface = Action('AssociateVirtualInterface')
ConfirmConnection = Action('ConfirmConnection')
ConfirmPrivateVirtualInterface = Action('ConfirmPrivateVirtualInterface')
ConfirmPublicVirtualInterface = Action('ConfirmPublicVirtualInterface')
CreateBGPPeer = Action('CreateBGPPeer')
CreateConnection = Action('CreateConnection')
CreateDirectConnectGateway = Action('CreateDirectConnectGateway')
CreateDirectConnectGatewayAssociation = \
    Action('CreateDirectConnectGatewayAssociation')
CreateInterconnect = Action('CreateInterconnect')
CreateLag = Action('CreateLag')
CreatePrivateVirtualInterface = Action('CreatePrivateVirtualInterface')
CreatePublicVirtualInterface = Action('CreatePublicVirtualInterface')
DeleteBGPPeer = Action('DeleteBGPPeer')
DeleteConnection = Action('DeleteConnection')
DeleteDirectConnectGateway = Action('DeleteDirectConnectGateway')
DeleteDirectConnectGatewayAssociation = \
    Action('DeleteDirectConnectGatewayAssociation')
DeleteInterconnect = Action('DeleteInterconnect')
DeleteLag = Action('DeleteLag')
DeleteVirtualInterface = Action('DeleteVirtualInterface')
DescribeConnectionLoa = Action('DescribeConnectionLoa')
DescribeConnections = Action('DescribeConnections')
DescribeConnectionsOnInterconnect = \
    Action('DescribeConnectionsOnInterconnect')
DescribeDirectConnectGatewayAssociations = \
    Action('DescribeDirectConnectGatewayAssociations')
DescribeDirectConnectGatewayAttachments = \
    Action('DescribeDirectConnectGatewayAttachments')
DescribeDirectConnectGateways = Action('DescribeDirectConnectGateways')
DescribeHostedConnections = Action('DescribeHostedConnections')
DescribeInterconnectLoa = Action('DescribeInterconnectLoa')
DescribeInterconnects = Action('DescribeInterconnects')
DescribeLags = Action('DescribeLags')
DescribeLoa = Action('DescribeLoa')
DescribeLocations = Action('DescribeLocations')
DescribeTags = Action('DescribeTags')
DescribeVirtualGateways = Action('DescribeVirtualGateways')
DescribeVirtualInterfaces = Action('DescribeVirtualInterfaces')
DisassociateConnectionFromLag = Action('DisassociateConnectionFromLag')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateLag = Action('UpdateLag')
UpdateVirtualInterfaceAttributes = \
    Action('UpdateVirtualInterfaceAttributes')
