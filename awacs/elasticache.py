# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon ElastiCache"
prefix = "elasticache"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTagsToResource = Action("AddTagsToResource")
AuthorizeCacheSecurityGroupIngress = Action("AuthorizeCacheSecurityGroupIngress")
BatchApplyUpdateAction = Action("BatchApplyUpdateAction")
BatchStopUpdateAction = Action("BatchStopUpdateAction")
CompleteMigration = Action("CompleteMigration")
Connect = Action("Connect")
CopyServerlessCacheSnapshot = Action("CopyServerlessCacheSnapshot")
CopySnapshot = Action("CopySnapshot")
CreateCacheCluster = Action("CreateCacheCluster")
CreateCacheParameterGroup = Action("CreateCacheParameterGroup")
CreateCacheSecurityGroup = Action("CreateCacheSecurityGroup")
CreateCacheSubnetGroup = Action("CreateCacheSubnetGroup")
CreateGlobalReplicationGroup = Action("CreateGlobalReplicationGroup")
CreateReplicationGroup = Action("CreateReplicationGroup")
CreateServerlessCache = Action("CreateServerlessCache")
CreateServerlessCacheSnapshot = Action("CreateServerlessCacheSnapshot")
CreateSnapshot = Action("CreateSnapshot")
CreateUser = Action("CreateUser")
CreateUserGroup = Action("CreateUserGroup")
DecreaseNodeGroupsInGlobalReplicationGroup = Action(
    "DecreaseNodeGroupsInGlobalReplicationGroup"
)
DecreaseReplicaCount = Action("DecreaseReplicaCount")
DeleteCacheCluster = Action("DeleteCacheCluster")
DeleteCacheParameterGroup = Action("DeleteCacheParameterGroup")
DeleteCacheSecurityGroup = Action("DeleteCacheSecurityGroup")
DeleteCacheSubnetGroup = Action("DeleteCacheSubnetGroup")
DeleteGlobalReplicationGroup = Action("DeleteGlobalReplicationGroup")
DeleteReplicationGroup = Action("DeleteReplicationGroup")
DeleteServerlessCache = Action("DeleteServerlessCache")
DeleteServerlessCacheSnapshot = Action("DeleteServerlessCacheSnapshot")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteUser = Action("DeleteUser")
DeleteUserGroup = Action("DeleteUserGroup")
DescribeCacheClusters = Action("DescribeCacheClusters")
DescribeCacheEngineVersions = Action("DescribeCacheEngineVersions")
DescribeCacheParameterGroups = Action("DescribeCacheParameterGroups")
DescribeCacheParameters = Action("DescribeCacheParameters")
DescribeCacheSecurityGroups = Action("DescribeCacheSecurityGroups")
DescribeCacheSubnetGroups = Action("DescribeCacheSubnetGroups")
DescribeEngineDefaultParameters = Action("DescribeEngineDefaultParameters")
DescribeEvents = Action("DescribeEvents")
DescribeGlobalReplicationGroups = Action("DescribeGlobalReplicationGroups")
DescribeReplicationGroups = Action("DescribeReplicationGroups")
DescribeReservedCacheNodes = Action("DescribeReservedCacheNodes")
DescribeReservedCacheNodesOfferings = Action("DescribeReservedCacheNodesOfferings")
DescribeServerlessCacheSnapshots = Action("DescribeServerlessCacheSnapshots")
DescribeServerlessCaches = Action("DescribeServerlessCaches")
DescribeServiceUpdates = Action("DescribeServiceUpdates")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeUpdateActions = Action("DescribeUpdateActions")
DescribeUserGroups = Action("DescribeUserGroups")
DescribeUsers = Action("DescribeUsers")
DisassociateGlobalReplicationGroup = Action("DisassociateGlobalReplicationGroup")
ExportServerlessCacheSnapshot = Action("ExportServerlessCacheSnapshot")
FailoverGlobalReplicationGroup = Action("FailoverGlobalReplicationGroup")
IncreaseNodeGroupsInGlobalReplicationGroup = Action(
    "IncreaseNodeGroupsInGlobalReplicationGroup"
)
IncreaseReplicaCount = Action("IncreaseReplicaCount")
InterruptClusterAzPower = Action("InterruptClusterAzPower")
ListAllowedNodeTypeModifications = Action("ListAllowedNodeTypeModifications")
ListTagsForResource = Action("ListTagsForResource")
ModifyCacheCluster = Action("ModifyCacheCluster")
ModifyCacheParameterGroup = Action("ModifyCacheParameterGroup")
ModifyCacheSubnetGroup = Action("ModifyCacheSubnetGroup")
ModifyGlobalReplicationGroup = Action("ModifyGlobalReplicationGroup")
ModifyReplicationGroup = Action("ModifyReplicationGroup")
ModifyReplicationGroupShardConfiguration = Action(
    "ModifyReplicationGroupShardConfiguration"
)
ModifyServerlessCache = Action("ModifyServerlessCache")
ModifyUser = Action("ModifyUser")
ModifyUserGroup = Action("ModifyUserGroup")
PurchaseReservedCacheNodesOffering = Action("PurchaseReservedCacheNodesOffering")
RebalanceSlotsInGlobalReplicationGroup = Action(
    "RebalanceSlotsInGlobalReplicationGroup"
)
RebootCacheCluster = Action("RebootCacheCluster")
RemoveTagsFromResource = Action("RemoveTagsFromResource")
ResetCacheParameterGroup = Action("ResetCacheParameterGroup")
RevokeCacheSecurityGroupIngress = Action("RevokeCacheSecurityGroupIngress")
StartMigration = Action("StartMigration")
TestFailover = Action("TestFailover")
TestMigration = Action("TestMigration")
