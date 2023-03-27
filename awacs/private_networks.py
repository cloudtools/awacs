# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS service providing managed private networks"
prefix = "private-networks"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcknowledgeOrderReceipt = Action("AcknowledgeOrderReceipt")
ActivateDeviceIdentifier = Action("ActivateDeviceIdentifier")
ActivateNetworkSite = Action("ActivateNetworkSite")
ConfigureAccessPoint = Action("ConfigureAccessPoint")
CreateNetwork = Action("CreateNetwork")
CreateNetworkSite = Action("CreateNetworkSite")
DeactivateDeviceIdentifier = Action("DeactivateDeviceIdentifier")
DeleteNetwork = Action("DeleteNetwork")
DeleteNetworkSite = Action("DeleteNetworkSite")
GetDeviceIdentifier = Action("GetDeviceIdentifier")
GetNetwork = Action("GetNetwork")
GetNetworkResource = Action("GetNetworkResource")
GetNetworkSite = Action("GetNetworkSite")
GetOrder = Action("GetOrder")
ListDeviceIdentifiers = Action("ListDeviceIdentifiers")
ListNetworkResources = Action("ListNetworkResources")
ListNetworkSites = Action("ListNetworkSites")
ListNetworks = Action("ListNetworks")
ListOrders = Action("ListOrders")
ListTagsForResource = Action("ListTagsForResource")
Ping = Action("Ping")
StartNetworkResourceUpdate = Action("StartNetworkResourceUpdate")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateNetworkSite = Action("UpdateNetworkSite")
UpdateNetworkSitePlan = Action("UpdateNetworkSitePlan")
