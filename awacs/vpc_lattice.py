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


AssociateViaAWSServiceEventsAndStates = Action("AssociateViaAWSService-EventsAndStates")
CreateAccessLogSubscription = Action("CreateAccessLogSubscription")
CreateListener = Action("CreateListener")
CreateResourceConfiguration = Action("CreateResourceConfiguration")
CreateResourceGateway = Action("CreateResourceGateway")
CreateRule = Action("CreateRule")
CreateService = Action("CreateService")
CreateServiceNetwork = Action("CreateServiceNetwork")
CreateServiceNetworkResourceAssociation = Action(
    "CreateServiceNetworkResourceAssociation"
)
CreateServiceNetworkServiceAssociation = Action(
    "CreateServiceNetworkServiceAssociation"
)
CreateServiceNetworkVpcAssociation = Action("CreateServiceNetworkVpcAssociation")
CreateServiceNetworkVpcEndpointAssociation = Action(
    "CreateServiceNetworkVpcEndpointAssociation"
)
CreateTargetGroup = Action("CreateTargetGroup")
DeleteAccessLogSubscription = Action("DeleteAccessLogSubscription")
DeleteAuthPolicy = Action("DeleteAuthPolicy")
DeleteListener = Action("DeleteListener")
DeleteResourceConfiguration = Action("DeleteResourceConfiguration")
DeleteResourceEndpointAssociation = Action("DeleteResourceEndpointAssociation")
DeleteResourceGateway = Action("DeleteResourceGateway")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRule = Action("DeleteRule")
DeleteService = Action("DeleteService")
DeleteServiceNetwork = Action("DeleteServiceNetwork")
DeleteServiceNetworkResourceAssociation = Action(
    "DeleteServiceNetworkResourceAssociation"
)
DeleteServiceNetworkServiceAssociation = Action(
    "DeleteServiceNetworkServiceAssociation"
)
DeleteServiceNetworkVpcAssociation = Action("DeleteServiceNetworkVpcAssociation")
DeleteTargetGroup = Action("DeleteTargetGroup")
DeregisterTargets = Action("DeregisterTargets")
GetAccessLogSubscription = Action("GetAccessLogSubscription")
GetAuthPolicy = Action("GetAuthPolicy")
GetListener = Action("GetListener")
GetResourceConfiguration = Action("GetResourceConfiguration")
GetResourceGateway = Action("GetResourceGateway")
GetResourcePolicy = Action("GetResourcePolicy")
GetRule = Action("GetRule")
GetService = Action("GetService")
GetServiceNetwork = Action("GetServiceNetwork")
GetServiceNetworkResourceAssociation = Action("GetServiceNetworkResourceAssociation")
GetServiceNetworkServiceAssociation = Action("GetServiceNetworkServiceAssociation")
GetServiceNetworkVpcAssociation = Action("GetServiceNetworkVpcAssociation")
GetTargetGroup = Action("GetTargetGroup")
ListAccessLogSubscriptions = Action("ListAccessLogSubscriptions")
ListListeners = Action("ListListeners")
ListResourceConfigurations = Action("ListResourceConfigurations")
ListResourceEndpointAssociations = Action("ListResourceEndpointAssociations")
ListResourceGateways = Action("ListResourceGateways")
ListRules = Action("ListRules")
ListServiceNetworkResourceAssociations = Action(
    "ListServiceNetworkResourceAssociations"
)
ListServiceNetworkServiceAssociations = Action("ListServiceNetworkServiceAssociations")
ListServiceNetworkVpcAssociations = Action("ListServiceNetworkVpcAssociations")
ListServiceNetworkVpcEndpointAssociations = Action(
    "ListServiceNetworkVpcEndpointAssociations"
)
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
UpdateResourceConfiguration = Action("UpdateResourceConfiguration")
UpdateResourceGateway = Action("UpdateResourceGateway")
UpdateRule = Action("UpdateRule")
UpdateService = Action("UpdateService")
UpdateServiceNetwork = Action("UpdateServiceNetwork")
UpdateServiceNetworkVpcAssociation = Action("UpdateServiceNetworkVpcAssociation")
UpdateTargetGroup = Action("UpdateTargetGroup")
