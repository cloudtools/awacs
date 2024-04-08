# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon RDS"
prefix = "rds"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddRoleToDBCluster = Action("AddRoleToDBCluster")
AddRoleToDBInstance = Action("AddRoleToDBInstance")
AddSourceIdentifierToSubscription = Action("AddSourceIdentifierToSubscription")
AddTagsToResource = Action("AddTagsToResource")
ApplyPendingMaintenanceAction = Action("ApplyPendingMaintenanceAction")
AuthorizeDBSecurityGroupIngress = Action("AuthorizeDBSecurityGroupIngress")
BacktrackDBCluster = Action("BacktrackDBCluster")
CancelExportTask = Action("CancelExportTask")
CopyDBClusterParameterGroup = Action("CopyDBClusterParameterGroup")
CopyDBClusterSnapshot = Action("CopyDBClusterSnapshot")
CopyDBParameterGroup = Action("CopyDBParameterGroup")
CopyDBSnapshot = Action("CopyDBSnapshot")
CopyOptionGroup = Action("CopyOptionGroup")
CreateBlueGreenDeployment = Action("CreateBlueGreenDeployment")
CreateCustomAvailabilityZone = Action("CreateCustomAvailabilityZone")
CreateCustomDBEngineVersion = Action("CreateCustomDBEngineVersion")
CreateDBCluster = Action("CreateDBCluster")
CreateDBClusterEndpoint = Action("CreateDBClusterEndpoint")
CreateDBClusterParameterGroup = Action("CreateDBClusterParameterGroup")
CreateDBClusterSnapshot = Action("CreateDBClusterSnapshot")
CreateDBInstance = Action("CreateDBInstance")
CreateDBInstanceReadReplica = Action("CreateDBInstanceReadReplica")
CreateDBParameterGroup = Action("CreateDBParameterGroup")
CreateDBProxy = Action("CreateDBProxy")
CreateDBProxyEndpoint = Action("CreateDBProxyEndpoint")
CreateDBSecurityGroup = Action("CreateDBSecurityGroup")
CreateDBShardGroup = Action("CreateDBShardGroup")
CreateDBSnapshot = Action("CreateDBSnapshot")
CreateDBSubnetGroup = Action("CreateDBSubnetGroup")
CreateEventSubscription = Action("CreateEventSubscription")
CreateGlobalCluster = Action("CreateGlobalCluster")
CreateIntegration = Action("CreateIntegration")
CreateOptionGroup = Action("CreateOptionGroup")
CreateTenantDatabase = Action("CreateTenantDatabase")
CrossRegionCommunication = Action("CrossRegionCommunication")
DeleteBlueGreenDeployment = Action("DeleteBlueGreenDeployment")
DeleteCustomAvailabilityZone = Action("DeleteCustomAvailabilityZone")
DeleteCustomDBEngineVersion = Action("DeleteCustomDBEngineVersion")
DeleteDBCluster = Action("DeleteDBCluster")
DeleteDBClusterAutomatedBackup = Action("DeleteDBClusterAutomatedBackup")
DeleteDBClusterEndpoint = Action("DeleteDBClusterEndpoint")
DeleteDBClusterParameterGroup = Action("DeleteDBClusterParameterGroup")
DeleteDBClusterSnapshot = Action("DeleteDBClusterSnapshot")
DeleteDBInstance = Action("DeleteDBInstance")
DeleteDBInstanceAutomatedBackup = Action("DeleteDBInstanceAutomatedBackup")
DeleteDBParameterGroup = Action("DeleteDBParameterGroup")
DeleteDBProxy = Action("DeleteDBProxy")
DeleteDBProxyEndpoint = Action("DeleteDBProxyEndpoint")
DeleteDBSecurityGroup = Action("DeleteDBSecurityGroup")
DeleteDBShardGroup = Action("DeleteDBShardGroup")
DeleteDBSnapshot = Action("DeleteDBSnapshot")
DeleteDBSubnetGroup = Action("DeleteDBSubnetGroup")
DeleteEventSubscription = Action("DeleteEventSubscription")
DeleteGlobalCluster = Action("DeleteGlobalCluster")
DeleteInstallationMedia = Action("DeleteInstallationMedia")
DeleteIntegration = Action("DeleteIntegration")
DeleteOptionGroup = Action("DeleteOptionGroup")
DeleteTenantDatabase = Action("DeleteTenantDatabase")
DeregisterDBProxyTargets = Action("DeregisterDBProxyTargets")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeBlueGreenDeployments = Action("DescribeBlueGreenDeployments")
DescribeCertificates = Action("DescribeCertificates")
DescribeCustomAvailabilityZones = Action("DescribeCustomAvailabilityZones")
DescribeDBClusterAutomatedBackups = Action("DescribeDBClusterAutomatedBackups")
DescribeDBClusterBacktracks = Action("DescribeDBClusterBacktracks")
DescribeDBClusterEndpoints = Action("DescribeDBClusterEndpoints")
DescribeDBClusterParameterGroups = Action("DescribeDBClusterParameterGroups")
DescribeDBClusterParameters = Action("DescribeDBClusterParameters")
DescribeDBClusterSnapshotAttributes = Action("DescribeDBClusterSnapshotAttributes")
DescribeDBClusterSnapshots = Action("DescribeDBClusterSnapshots")
DescribeDBClusters = Action("DescribeDBClusters")
DescribeDBEngineVersions = Action("DescribeDBEngineVersions")
DescribeDBInstanceAutomatedBackups = Action("DescribeDBInstanceAutomatedBackups")
DescribeDBInstances = Action("DescribeDBInstances")
DescribeDBLogFiles = Action("DescribeDBLogFiles")
DescribeDBParameterGroups = Action("DescribeDBParameterGroups")
DescribeDBParameters = Action("DescribeDBParameters")
DescribeDBProxies = Action("DescribeDBProxies")
DescribeDBProxyEndpoints = Action("DescribeDBProxyEndpoints")
DescribeDBProxyTargetGroups = Action("DescribeDBProxyTargetGroups")
DescribeDBProxyTargets = Action("DescribeDBProxyTargets")
DescribeDBRecommendations = Action("DescribeDBRecommendations")
DescribeDBSecurityGroups = Action("DescribeDBSecurityGroups")
DescribeDBShardGroups = Action("DescribeDBShardGroups")
DescribeDBSnapshotAttributes = Action("DescribeDBSnapshotAttributes")
DescribeDBSnapshots = Action("DescribeDBSnapshots")
DescribeDBSubnetGroups = Action("DescribeDBSubnetGroups")
DescribeDbSnapshotTenantDatabases = Action("DescribeDbSnapshotTenantDatabases")
DescribeEngineDefaultClusterParameters = Action(
    "DescribeEngineDefaultClusterParameters"
)
DescribeEngineDefaultParameters = Action("DescribeEngineDefaultParameters")
DescribeEventCategories = Action("DescribeEventCategories")
DescribeEventSubscriptions = Action("DescribeEventSubscriptions")
DescribeEvents = Action("DescribeEvents")
DescribeExportTasks = Action("DescribeExportTasks")
DescribeGlobalClusters = Action("DescribeGlobalClusters")
DescribeInstallationMedia = Action("DescribeInstallationMedia")
DescribeIntegrations = Action("DescribeIntegrations")
DescribeOptionGroupOptions = Action("DescribeOptionGroupOptions")
DescribeOptionGroups = Action("DescribeOptionGroups")
DescribeOrderableDBInstanceOptions = Action("DescribeOrderableDBInstanceOptions")
DescribePendingMaintenanceActions = Action("DescribePendingMaintenanceActions")
DescribeRecommendationGroups = Action("DescribeRecommendationGroups")
DescribeRecommendations = Action("DescribeRecommendations")
DescribeReservedDBInstances = Action("DescribeReservedDBInstances")
DescribeReservedDBInstancesOfferings = Action("DescribeReservedDBInstancesOfferings")
DescribeSourceRegions = Action("DescribeSourceRegions")
DescribeTenantDatabases = Action("DescribeTenantDatabases")
DescribeValidDBInstanceModifications = Action("DescribeValidDBInstanceModifications")
DisableHttpEndpoint = Action("DisableHttpEndpoint")
DownloadCompleteDBLogFile = Action("DownloadCompleteDBLogFile")
DownloadDBLogFilePortion = Action("DownloadDBLogFilePortion")
EnableHttpEndpoint = Action("EnableHttpEndpoint")
FailoverDBCluster = Action("FailoverDBCluster")
FailoverGlobalCluster = Action("FailoverGlobalCluster")
ImportInstallationMedia = Action("ImportInstallationMedia")
ListTagsForResource = Action("ListTagsForResource")
ModifyActivityStream = Action("ModifyActivityStream")
ModifyCertificates = Action("ModifyCertificates")
ModifyCurrentDBClusterCapacity = Action("ModifyCurrentDBClusterCapacity")
ModifyCustomDBEngineVersion = Action("ModifyCustomDBEngineVersion")
ModifyDBCluster = Action("ModifyDBCluster")
ModifyDBClusterEndpoint = Action("ModifyDBClusterEndpoint")
ModifyDBClusterParameterGroup = Action("ModifyDBClusterParameterGroup")
ModifyDBClusterSnapshotAttribute = Action("ModifyDBClusterSnapshotAttribute")
ModifyDBInstance = Action("ModifyDBInstance")
ModifyDBParameterGroup = Action("ModifyDBParameterGroup")
ModifyDBProxy = Action("ModifyDBProxy")
ModifyDBProxyEndpoint = Action("ModifyDBProxyEndpoint")
ModifyDBProxyTargetGroup = Action("ModifyDBProxyTargetGroup")
ModifyDBRecommendation = Action("ModifyDBRecommendation")
ModifyDBShardGroup = Action("ModifyDBShardGroup")
ModifyDBSnapshot = Action("ModifyDBSnapshot")
ModifyDBSnapshotAttribute = Action("ModifyDBSnapshotAttribute")
ModifyDBSubnetGroup = Action("ModifyDBSubnetGroup")
ModifyEventSubscription = Action("ModifyEventSubscription")
ModifyGlobalCluster = Action("ModifyGlobalCluster")
ModifyIntegration = Action("ModifyIntegration")
ModifyOptionGroup = Action("ModifyOptionGroup")
ModifyRecommendation = Action("ModifyRecommendation")
ModifyTenantDatabase = Action("ModifyTenantDatabase")
PromoteReadReplica = Action("PromoteReadReplica")
PromoteReadReplicaDBCluster = Action("PromoteReadReplicaDBCluster")
PurchaseReservedDBInstancesOffering = Action("PurchaseReservedDBInstancesOffering")
RebootDBCluster = Action("RebootDBCluster")
RebootDBInstance = Action("RebootDBInstance")
RebootDBShardGroup = Action("RebootDBShardGroup")
RegisterDBProxyTargets = Action("RegisterDBProxyTargets")
RemoveFromGlobalCluster = Action("RemoveFromGlobalCluster")
RemoveRoleFromDBCluster = Action("RemoveRoleFromDBCluster")
RemoveRoleFromDBInstance = Action("RemoveRoleFromDBInstance")
RemoveSourceIdentifierFromSubscription = Action(
    "RemoveSourceIdentifierFromSubscription"
)
RemoveTagsFromResource = Action("RemoveTagsFromResource")
ResetDBClusterParameterGroup = Action("ResetDBClusterParameterGroup")
ResetDBParameterGroup = Action("ResetDBParameterGroup")
RestoreDBClusterFromS3 = Action("RestoreDBClusterFromS3")
RestoreDBClusterFromSnapshot = Action("RestoreDBClusterFromSnapshot")
RestoreDBClusterToPointInTime = Action("RestoreDBClusterToPointInTime")
RestoreDBInstanceFromDBSnapshot = Action("RestoreDBInstanceFromDBSnapshot")
RestoreDBInstanceFromS3 = Action("RestoreDBInstanceFromS3")
RestoreDBInstanceToPointInTime = Action("RestoreDBInstanceToPointInTime")
RevokeDBSecurityGroupIngress = Action("RevokeDBSecurityGroupIngress")
StartActivityStream = Action("StartActivityStream")
StartDBCluster = Action("StartDBCluster")
StartDBInstance = Action("StartDBInstance")
StartDBInstanceAutomatedBackupsReplication = Action(
    "StartDBInstanceAutomatedBackupsReplication"
)
StartExportTask = Action("StartExportTask")
StopActivityStream = Action("StopActivityStream")
StopDBCluster = Action("StopDBCluster")
StopDBInstance = Action("StopDBInstance")
StopDBInstanceAutomatedBackupsReplication = Action(
    "StopDBInstanceAutomatedBackupsReplication"
)
SwitchoverBlueGreenDeployment = Action("SwitchoverBlueGreenDeployment")
SwitchoverGlobalCluster = Action("SwitchoverGlobalCluster")
SwitchoverReadReplica = Action("SwitchoverReadReplica")
