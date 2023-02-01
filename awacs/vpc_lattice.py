# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon VPC Lattice"
prefix = "vpc-lattice"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAccessLogSubscription = Action("CreateAccessLogSubscription")
CreateListener = Action("CreateListener")
CreateRule = Action("CreateRule")
CreateService = Action("CreateService")
CreateServiceNetwork = Action("CreateServiceNetwork")
CreateServiceNetworkServiceAssociation = Action(
    "CreateServiceNetworkServiceAssociation"
)
CreateServiceNetworkVpcAssociation = Action("CreateServiceNetworkVpcAssociation")
CreateTargetGroup = Action("CreateTargetGroup")
DeleteAccessLogSubscription = Action("DeleteAccessLogSubscription")
DeleteAuthPolicy = Action("DeleteAuthPolicy")
DeleteListener = Action("DeleteListener")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRule = Action("DeleteRule")
DeleteService = Action("DeleteService")
DeleteServiceNetwork = Action("DeleteServiceNetwork")
DeleteServiceNetworkServiceAssociation = Action(
    "DeleteServiceNetworkServiceAssociation"
)
DeleteServiceNetworkVpcAssociation = Action("DeleteServiceNetworkVpcAssociation")
DeleteTargetGroup = Action("DeleteTargetGroup")
DeregisterTargets = Action("DeregisterTargets")
GetAccessLogSubscription = Action("GetAccessLogSubscription")
GetAuthPolicy = Action("GetAuthPolicy")
GetListener = Action("GetListener")
GetResourcePolicy = Action("GetResourcePolicy")
GetRule = Action("GetRule")
GetService = Action("GetService")
GetServiceNetwork = Action("GetServiceNetwork")
GetServiceNetworkServiceAssociation = Action("GetServiceNetworkServiceAssociation")
GetServiceNetworkVpcAssociation = Action("GetServiceNetworkVpcAssociation")
GetTargetGroup = Action("GetTargetGroup")
ListAccessLogSubscriptions = Action("ListAccessLogSubscriptions")
ListListeners = Action("ListListeners")
ListRules = Action("ListRules")
ListServiceNetworkServiceAssociations = Action("ListServiceNetworkServiceAssociations")
ListServiceNetworkVpcAssociations = Action("ListServiceNetworkVpcAssociations")
ListServiceNetworks = Action("ListServiceNetworks")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
ListTargetGroups = Action("ListTargetGroups")
ListTargets = Action("ListTargets")
PutAuthPolicy = Action("PutAuthPolicy")
PutResourcePolicy = Action("PutResourcePolicy")
RegisterTargets = Action("RegisterTargets")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccessLogSubscription = Action("UpdateAccessLogSubscription")
UpdateListener = Action("UpdateListener")
UpdateRule = Action("UpdateRule")
UpdateService = Action("UpdateService")
UpdateServiceNetwork = Action("UpdateServiceNetwork")
UpdateServiceNetworkVpcAssociation = Action("UpdateServiceNetworkVpcAssociation")
UpdateTargetGroup = Action("UpdateTargetGroup")
