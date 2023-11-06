# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Global Accelerator"
prefix = "globalaccelerator"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddCustomRoutingEndpoints = Action("AddCustomRoutingEndpoints")
AddEndpoints = Action("AddEndpoints")
AdvertiseByoipCidr = Action("AdvertiseByoipCidr")
AllowCustomRoutingTraffic = Action("AllowCustomRoutingTraffic")
CreateAccelerator = Action("CreateAccelerator")
CreateCrossAccountAttachment = Action("CreateCrossAccountAttachment")
CreateCustomRoutingAccelerator = Action("CreateCustomRoutingAccelerator")
CreateCustomRoutingEndpointGroup = Action("CreateCustomRoutingEndpointGroup")
CreateCustomRoutingListener = Action("CreateCustomRoutingListener")
CreateEndpointGroup = Action("CreateEndpointGroup")
CreateListener = Action("CreateListener")
DeleteAccelerator = Action("DeleteAccelerator")
DeleteCrossAccountAttachment = Action("DeleteCrossAccountAttachment")
DeleteCustomRoutingAccelerator = Action("DeleteCustomRoutingAccelerator")
DeleteCustomRoutingEndpointGroup = Action("DeleteCustomRoutingEndpointGroup")
DeleteCustomRoutingListener = Action("DeleteCustomRoutingListener")
DeleteEndpointGroup = Action("DeleteEndpointGroup")
DeleteListener = Action("DeleteListener")
DenyCustomRoutingTraffic = Action("DenyCustomRoutingTraffic")
DeprovisionByoipCidr = Action("DeprovisionByoipCidr")
DescribeAccelerator = Action("DescribeAccelerator")
DescribeAcceleratorAttributes = Action("DescribeAcceleratorAttributes")
DescribeCrossAccountAttachment = Action("DescribeCrossAccountAttachment")
DescribeCustomRoutingAccelerator = Action("DescribeCustomRoutingAccelerator")
DescribeCustomRoutingAcceleratorAttributes = Action(
    "DescribeCustomRoutingAcceleratorAttributes"
)
DescribeCustomRoutingEndpointGroup = Action("DescribeCustomRoutingEndpointGroup")
DescribeCustomRoutingListener = Action("DescribeCustomRoutingListener")
DescribeEndpointGroup = Action("DescribeEndpointGroup")
DescribeListener = Action("DescribeListener")
ListAccelerators = Action("ListAccelerators")
ListByoipCidrs = Action("ListByoipCidrs")
ListCrossAccountAttachments = Action("ListCrossAccountAttachments")
ListCrossAccountResourceAccounts = Action("ListCrossAccountResourceAccounts")
ListCrossAccountResources = Action("ListCrossAccountResources")
ListCustomRoutingAccelerators = Action("ListCustomRoutingAccelerators")
ListCustomRoutingEndpointGroups = Action("ListCustomRoutingEndpointGroups")
ListCustomRoutingListeners = Action("ListCustomRoutingListeners")
ListCustomRoutingPortMappings = Action("ListCustomRoutingPortMappings")
ListCustomRoutingPortMappingsByDestination = Action(
    "ListCustomRoutingPortMappingsByDestination"
)
ListEndpointGroups = Action("ListEndpointGroups")
ListListeners = Action("ListListeners")
ListTagsForResource = Action("ListTagsForResource")
ProvisionByoipCidr = Action("ProvisionByoipCidr")
RemoveCustomRoutingEndpoints = Action("RemoveCustomRoutingEndpoints")
RemoveEndpoints = Action("RemoveEndpoints")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccelerator = Action("UpdateAccelerator")
UpdateAcceleratorAttributes = Action("UpdateAcceleratorAttributes")
UpdateCrossAccountAttachment = Action("UpdateCrossAccountAttachment")
UpdateCustomRoutingAccelerator = Action("UpdateCustomRoutingAccelerator")
UpdateCustomRoutingAcceleratorAttributes = Action(
    "UpdateCustomRoutingAcceleratorAttributes"
)
UpdateCustomRoutingListener = Action("UpdateCustomRoutingListener")
UpdateEndpointGroup = Action("UpdateEndpointGroup")
UpdateListener = Action("UpdateListener")
WithdrawByoipCidr = Action("WithdrawByoipCidr")
