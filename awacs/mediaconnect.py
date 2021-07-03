# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaConnect"
prefix = "mediaconnect"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddFlowMediaStreams = Action("AddFlowMediaStreams")
AddFlowOutputs = Action("AddFlowOutputs")
AddFlowSources = Action("AddFlowSources")
AddFlowVpcInterfaces = Action("AddFlowVpcInterfaces")
CreateFlow = Action("CreateFlow")
DeleteFlow = Action("DeleteFlow")
DescribeFlow = Action("DescribeFlow")
DescribeOffering = Action("DescribeOffering")
DescribeReservation = Action("DescribeReservation")
GrantFlowEntitlements = Action("GrantFlowEntitlements")
ListEntitlements = Action("ListEntitlements")
ListFlows = Action("ListFlows")
ListOfferings = Action("ListOfferings")
ListReservations = Action("ListReservations")
ListTagsForResource = Action("ListTagsForResource")
PurchaseOffering = Action("PurchaseOffering")
RemoveFlowMediaStream = Action("RemoveFlowMediaStream")
RemoveFlowOutput = Action("RemoveFlowOutput")
RemoveFlowSource = Action("RemoveFlowSource")
RemoveFlowVpcInterface = Action("RemoveFlowVpcInterface")
RevokeFlowEntitlement = Action("RevokeFlowEntitlement")
StartFlow = Action("StartFlow")
StopFlow = Action("StopFlow")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFlow = Action("UpdateFlow")
UpdateFlowEntitlement = Action("UpdateFlowEntitlement")
UpdateFlowMediaStream = Action("UpdateFlowMediaStream")
UpdateFlowOutput = Action("UpdateFlowOutput")
UpdateFlowSource = Action("UpdateFlowSource")
