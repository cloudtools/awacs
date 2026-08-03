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
AssociateIamRoleToResource = Action("AssociateIamRoleToResource")
CreateAutonomousDatabase = Action("CreateAutonomousDatabase")
CreateAutonomousDatabaseBackup = Action("CreateAutonomousDatabaseBackup")
CreateAutonomousDatabaseWallet = Action("CreateAutonomousDatabaseWallet")
CreateCloudAutonomousVmCluster = Action("CreateCloudAutonomousVmCluster")
CreateCloudExadataInfrastructure = Action("CreateCloudExadataInfrastructure")
CreateCloudVmCluster = Action("CreateCloudVmCluster")
CreateDbNode = Action("CreateDbNode")
CreateGrantShare = Action("CreateGrantShare")
CreateOdbNetwork = Action("CreateOdbNetwork")
CreateOdbPeeringConnection = Action("CreateOdbPeeringConnection")
CreateOutboundIntegration = Action("CreateOutboundIntegration")
DeleteAutonomousDatabase = Action("DeleteAutonomousDatabase")
DeleteAutonomousDatabaseBackup = Action("DeleteAutonomousDatabaseBackup")
DeleteCloudAutonomousVmCluster = Action("DeleteCloudAutonomousVmCluster")
DeleteCloudExadataInfrastructure = Action("DeleteCloudExadataInfrastructure")
DeleteCloudVmCluster = Action("DeleteCloudVmCluster")
DeleteDbNode = Action("DeleteDbNode")
DeleteGrantShare = Action("DeleteGrantShare")
DeleteOdbNetwork = Action("DeleteOdbNetwork")
DeleteOdbPeeringConnection = Action("DeleteOdbPeeringConnection")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DisassociateIamRoleFromResource = Action("DisassociateIamRoleFromResource")
FailoverAutonomousDatabase = Action("FailoverAutonomousDatabase")
GetAutonomousDatabase = Action("GetAutonomousDatabase")
GetAutonomousDatabaseBackup = Action("GetAutonomousDatabaseBackup")
GetAutonomousDatabaseWalletDetails = Action("GetAutonomousDatabaseWalletDetails")
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
ListAutonomousDatabaseBackups = Action("ListAutonomousDatabaseBackups")
ListAutonomousDatabaseCharacterSets = Action("ListAutonomousDatabaseCharacterSets")
ListAutonomousDatabaseClones = Action("ListAutonomousDatabaseClones")
ListAutonomousDatabasePeers = Action("ListAutonomousDatabasePeers")
ListAutonomousDatabaseVersions = Action("ListAutonomousDatabaseVersions")
ListAutonomousDatabases = Action("ListAutonomousDatabases")
ListAutonomousVirtualMachines = Action("ListAutonomousVirtualMachines")
ListCloudAutonomousVmClusters = Action("ListCloudAutonomousVmClusters")
ListCloudExadataInfrastructures = Action("ListCloudExadataInfrastructures")
ListCloudVmClusters = Action("ListCloudVmClusters")
ListDbNodes = Action("ListDbNodes")
ListDbServers = Action("ListDbServers")
ListDbSystemShapes = Action("ListDbSystemShapes")
ListFlexComponents = Action("ListFlexComponents")
ListGiVersions = Action("ListGiVersions")
ListOdbNetworks = Action("ListOdbNetworks")
ListOdbPeeringConnections = Action("ListOdbPeeringConnections")
ListSystemVersions = Action("ListSystemVersions")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
RebootAutonomousDatabase = Action("RebootAutonomousDatabase")
RebootDbNode = Action("RebootDbNode")
RestoreAutonomousDatabase = Action("RestoreAutonomousDatabase")
ShrinkAutonomousDatabase = Action("ShrinkAutonomousDatabase")
StartAutonomousDatabase = Action("StartAutonomousDatabase")
StartDbNode = Action("StartDbNode")
StopAutonomousDatabase = Action("StopAutonomousDatabase")
StopDbNode = Action("StopDbNode")
SwitchoverAutonomousDatabase = Action("SwitchoverAutonomousDatabase")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAutonomousDatabase = Action("UpdateAutonomousDatabase")
UpdateAutonomousDatabaseBackup = Action("UpdateAutonomousDatabaseBackup")
UpdateCloudExadataInfrastructure = Action("UpdateCloudExadataInfrastructure")
UpdateGrantShare = Action("UpdateGrantShare")
UpdateOdbNetwork = Action("UpdateOdbNetwork")
UpdateOdbPeeringConnection = Action("UpdateOdbPeeringConnection")
UpdateOutboundIntegration = Action("UpdateOutboundIntegration")
