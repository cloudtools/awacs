# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon ElastiCache"
prefix = "elasticache"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CopySnapshot = Action("CopySnapshot")
CreateCacheCluster = Action("CreateCacheCluster")
CreateCacheParameterGroup = Action("CreateCacheParameterGroup")
CreateCacheSecurityGroup = Action("CreateCacheSecurityGroup")
CreateCacheSubnetGroup = Action("CreateCacheSubnetGroup")
CreateGlobalReplicationGroup = Action("CreateGlobalReplicationGroup")
CreateReplicationGroup = Action("CreateReplicationGroup")
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
DescribeServiceUpdates = Action("DescribeServiceUpdates")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeUpdateActions = Action("DescribeUpdateActions")
DescribeUserGroups = Action("DescribeUserGroups")
DescribeUsers = Action("DescribeUsers")
DisassociateGlobalReplicationGroup = Action("DisassociateGlobalReplicationGroup")
FailoverGlobalReplicationGroup = Action("FailoverGlobalReplicationGroup")
IncreaseNodeGroupsInGlobalReplicationGroup = Action(
    "IncreaseNodeGroupsInGlobalReplicationGroup"
)
IncreaseReplicaCount = Action("IncreaseReplicaCount")
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
