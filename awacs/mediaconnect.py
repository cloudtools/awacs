# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaConnect"
prefix = "mediaconnect"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddBridgeOutputs = Action("AddBridgeOutputs")
AddBridgeSources = Action("AddBridgeSources")
AddFlowMediaStreams = Action("AddFlowMediaStreams")
AddFlowOutputs = Action("AddFlowOutputs")
AddFlowSources = Action("AddFlowSources")
AddFlowVpcInterfaces = Action("AddFlowVpcInterfaces")
AssociateRouterNetworkInterface = Action("AssociateRouterNetworkInterface")
CreateBridge = Action("CreateBridge")
CreateFlow = Action("CreateFlow")
CreateGateway = Action("CreateGateway")
CreateRouterInput = Action("CreateRouterInput")
CreateRouterNetworkInterface = Action("CreateRouterNetworkInterface")
CreateRouterOutput = Action("CreateRouterOutput")
DeleteBridge = Action("DeleteBridge")
DeleteFlow = Action("DeleteFlow")
DeleteGateway = Action("DeleteGateway")
DeleteRouterInput = Action("DeleteRouterInput")
DeleteRouterNetworkInterface = Action("DeleteRouterNetworkInterface")
DeleteRouterOutput = Action("DeleteRouterOutput")
DeregisterGatewayInstance = Action("DeregisterGatewayInstance")
DescribeBridge = Action("DescribeBridge")
DescribeFlow = Action("DescribeFlow")
DescribeFlowSourceMetadata = Action("DescribeFlowSourceMetadata")
DescribeFlowSourceThumbnail = Action("DescribeFlowSourceThumbnail")
DescribeGateway = Action("DescribeGateway")
DescribeGatewayInstance = Action("DescribeGatewayInstance")
DescribeOffering = Action("DescribeOffering")
DescribeReservation = Action("DescribeReservation")
DiscoverGatewayPollEndpoint = Action("DiscoverGatewayPollEndpoint")
GetRouterInput = Action("GetRouterInput")
GetRouterInputSourceMetadata = Action("GetRouterInputSourceMetadata")
GetRouterInputThumbnail = Action("GetRouterInputThumbnail")
GetRouterNetworkInterface = Action("GetRouterNetworkInterface")
GetRouterOutput = Action("GetRouterOutput")
GrantFlowEntitlements = Action("GrantFlowEntitlements")
ListBridges = Action("ListBridges")
ListEntitlements = Action("ListEntitlements")
ListFlows = Action("ListFlows")
ListGatewayInstances = Action("ListGatewayInstances")
ListGateways = Action("ListGateways")
ListOfferings = Action("ListOfferings")
ListReservations = Action("ListReservations")
ListRouterInputs = Action("ListRouterInputs")
ListRouterNetworkInterfaces = Action("ListRouterNetworkInterfaces")
ListRouterOutputs = Action("ListRouterOutputs")
ListTagsForResource = Action("ListTagsForResource")
PollGateway = Action("PollGateway")
PurchaseOffering = Action("PurchaseOffering")
RemoveBridgeOutput = Action("RemoveBridgeOutput")
RemoveBridgeSource = Action("RemoveBridgeSource")
RemoveFlowMediaStream = Action("RemoveFlowMediaStream")
RemoveFlowOutput = Action("RemoveFlowOutput")
RemoveFlowSource = Action("RemoveFlowSource")
RemoveFlowVpcInterface = Action("RemoveFlowVpcInterface")
RestartRouterInput = Action("RestartRouterInput")
RestartRouterOutput = Action("RestartRouterOutput")
RevokeFlowEntitlement = Action("RevokeFlowEntitlement")
StartFlow = Action("StartFlow")
StartRouterInput = Action("StartRouterInput")
StartRouterOutput = Action("StartRouterOutput")
StopFlow = Action("StopFlow")
StopRouterInput = Action("StopRouterInput")
StopRouterOutput = Action("StopRouterOutput")
SubmitGatewayStateChange = Action("SubmitGatewayStateChange")
TagResource = Action("TagResource")
TakeRouterInput = Action("TakeRouterInput")
UntagResource = Action("UntagResource")
UpdateBridge = Action("UpdateBridge")
UpdateBridgeOutput = Action("UpdateBridgeOutput")
UpdateBridgeSource = Action("UpdateBridgeSource")
UpdateBridgeState = Action("UpdateBridgeState")
UpdateFlow = Action("UpdateFlow")
UpdateFlowEntitlement = Action("UpdateFlowEntitlement")
UpdateFlowMediaStream = Action("UpdateFlowMediaStream")
UpdateFlowOutput = Action("UpdateFlowOutput")
UpdateFlowSource = Action("UpdateFlowSource")
UpdateGatewayInstance = Action("UpdateGatewayInstance")
UpdateRouterInput = Action("UpdateRouterInput")
UpdateRouterNetworkInterface = Action("UpdateRouterNetworkInterface")
UpdateRouterOutput = Action("UpdateRouterOutput")
