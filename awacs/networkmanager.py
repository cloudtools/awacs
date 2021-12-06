# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Network Manager"
prefix = "networkmanager"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAttachment = Action("AcceptAttachment")
AssociateConnectPeer = Action("AssociateConnectPeer")
AssociateCustomerGateway = Action("AssociateCustomerGateway")
AssociateLink = Action("AssociateLink")
AssociateTransitGatewayConnectPeer = Action("AssociateTransitGatewayConnectPeer")
CreateConnectAttachment = Action("CreateConnectAttachment")
CreateConnectPeer = Action("CreateConnectPeer")
CreateConnection = Action("CreateConnection")
CreateCoreNetwork = Action("CreateCoreNetwork")
CreateDevice = Action("CreateDevice")
CreateGlobalNetwork = Action("CreateGlobalNetwork")
CreateLink = Action("CreateLink")
CreateSite = Action("CreateSite")
CreateSiteToSiteVpnAttachment = Action("CreateSiteToSiteVpnAttachment")
CreateVpcAttachment = Action("CreateVpcAttachment")
DeleteAttachment = Action("DeleteAttachment")
DeleteConnectPeer = Action("DeleteConnectPeer")
DeleteConnection = Action("DeleteConnection")
DeleteCoreNetwork = Action("DeleteCoreNetwork")
DeleteCoreNetworkPolicyVersion = Action("DeleteCoreNetworkPolicyVersion")
DeleteDevice = Action("DeleteDevice")
DeleteGlobalNetwork = Action("DeleteGlobalNetwork")
DeleteLink = Action("DeleteLink")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSite = Action("DeleteSite")
DeregisterTransitGateway = Action("DeregisterTransitGateway")
DescribeGlobalNetworks = Action("DescribeGlobalNetworks")
DisassociateConnectPeer = Action("DisassociateConnectPeer")
DisassociateCustomerGateway = Action("DisassociateCustomerGateway")
DisassociateLink = Action("DisassociateLink")
DisassociateTransitGatewayConnectPeer = Action("DisassociateTransitGatewayConnectPeer")
ExecuteCoreNetworkChangeSet = Action("ExecuteCoreNetworkChangeSet")
GetConnectAttachment = Action("GetConnectAttachment")
GetConnectPeer = Action("GetConnectPeer")
GetConnectPeerAssociations = Action("GetConnectPeerAssociations")
GetConnections = Action("GetConnections")
GetCoreNetwork = Action("GetCoreNetwork")
GetCoreNetworkChangeSet = Action("GetCoreNetworkChangeSet")
GetCoreNetworkPolicy = Action("GetCoreNetworkPolicy")
GetCustomerGatewayAssociations = Action("GetCustomerGatewayAssociations")
GetDevices = Action("GetDevices")
GetLinkAssociations = Action("GetLinkAssociations")
GetLinks = Action("GetLinks")
GetNetworkResourceCounts = Action("GetNetworkResourceCounts")
GetNetworkResourceRelationships = Action("GetNetworkResourceRelationships")
GetNetworkResources = Action("GetNetworkResources")
GetNetworkRoutes = Action("GetNetworkRoutes")
GetNetworkTelemetry = Action("GetNetworkTelemetry")
GetResourcePolicy = Action("GetResourcePolicy")
GetRouteAnalysis = Action("GetRouteAnalysis")
GetSiteToSiteVpnAttachment = Action("GetSiteToSiteVpnAttachment")
GetSites = Action("GetSites")
GetTransitGatewayConnectPeerAssociations = Action(
    "GetTransitGatewayConnectPeerAssociations"
)
GetTransitGatewayRegistrations = Action("GetTransitGatewayRegistrations")
GetVpcAttachment = Action("GetVpcAttachment")
ListAttachments = Action("ListAttachments")
ListConnectPeers = Action("ListConnectPeers")
ListCoreNetworkPolicyVersions = Action("ListCoreNetworkPolicyVersions")
ListCoreNetworks = Action("ListCoreNetworks")
ListTagsForResource = Action("ListTagsForResource")
PutCoreNetworkPolicy = Action("PutCoreNetworkPolicy")
PutResourcePolicy = Action("PutResourcePolicy")
RegisterTransitGateway = Action("RegisterTransitGateway")
RejectAttachment = Action("RejectAttachment")
RestoreCoreNetworkPolicyVersion = Action("RestoreCoreNetworkPolicyVersion")
StartRouteAnalysis = Action("StartRouteAnalysis")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnection = Action("UpdateConnection")
UpdateCoreNetwork = Action("UpdateCoreNetwork")
UpdateDevice = Action("UpdateDevice")
UpdateGlobalNetwork = Action("UpdateGlobalNetwork")
UpdateLink = Action("UpdateLink")
UpdateNetworkResourceMetadata = Action("UpdateNetworkResourceMetadata")
UpdateSite = Action("UpdateSite")
UpdateVpcAttachment = Action("UpdateVpcAttachment")
