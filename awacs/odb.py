# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Service - Oracle Database@AWS"
prefix = "odb"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptMarketplaceRegistration = Action("AcceptMarketplaceRegistration")
CreateCloudAutonomousVmCluster = Action("CreateCloudAutonomousVmCluster")
CreateCloudExadataInfrastructure = Action("CreateCloudExadataInfrastructure")
CreateCloudVmCluster = Action("CreateCloudVmCluster")
CreateDbNode = Action("CreateDbNode")
CreateOdbNetwork = Action("CreateOdbNetwork")
CreateOdbPeeringConnection = Action("CreateOdbPeeringConnection")
CreateOutboundIntegration = Action("CreateOutboundIntegration")
DeleteCloudAutonomousVmCluster = Action("DeleteCloudAutonomousVmCluster")
DeleteCloudExadataInfrastructure = Action("DeleteCloudExadataInfrastructure")
DeleteCloudVmCluster = Action("DeleteCloudVmCluster")
DeleteDbNode = Action("DeleteDbNode")
DeleteOdbNetwork = Action("DeleteOdbNetwork")
DeleteOdbPeeringConnection = Action("DeleteOdbPeeringConnection")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
GetCloudAutonomousVmCluster = Action("GetCloudAutonomousVmCluster")
GetCloudExadataInfrastructure = Action("GetCloudExadataInfrastructure")
GetCloudExadataInfrastructureUnallocatedResources = Action(
    "GetCloudExadataInfrastructureUnallocatedResources"
)
GetCloudVmCluster = Action("GetCloudVmCluster")
GetDbNode = Action("GetDbNode")
GetDbServer = Action("GetDbServer")
GetOciOnboardingStatus = Action("GetOciOnboardingStatus")
GetOdbNetwork = Action("GetOdbNetwork")
GetOdbPeeringConnection = Action("GetOdbPeeringConnection")
GetResourcePolicy = Action("GetResourcePolicy")
InitializeService = Action("InitializeService")
ListAutonomousVirtualMachines = Action("ListAutonomousVirtualMachines")
ListCloudAutonomousVmClusters = Action("ListCloudAutonomousVmClusters")
ListCloudExadataInfrastructures = Action("ListCloudExadataInfrastructures")
ListCloudVmClusters = Action("ListCloudVmClusters")
ListDbNodes = Action("ListDbNodes")
ListDbServers = Action("ListDbServers")
ListDbSystemShapes = Action("ListDbSystemShapes")
ListGiVersions = Action("ListGiVersions")
ListOdbNetworks = Action("ListOdbNetworks")
ListOdbPeeringConnections = Action("ListOdbPeeringConnections")
ListSystemVersions = Action("ListSystemVersions")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
RebootDbNode = Action("RebootDbNode")
StartDbNode = Action("StartDbNode")
StopDbNode = Action("StopDbNode")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCloudExadataInfrastructure = Action("UpdateCloudExadataInfrastructure")
UpdateOdbNetwork = Action("UpdateOdbNetwork")
UpdateOdbPeeringConnection = Action("UpdateOdbPeeringConnection")
UpdateOutboundIntegration = Action("UpdateOutboundIntegration")
