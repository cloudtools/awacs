# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS ElastiCache'
prefix = 'elasticache'

AddTagsToResource = Action(prefix, 'AddTagsToResource')
AuthorizeCacheSecurityGroupIngress = \
    Action(prefix, 'AuthorizeCacheSecurityGroupIngress')
CopySnapshot = Action(prefix, 'CopySnapshot')
CreateCacheCluster = Action(prefix, 'CreateCacheCluster')
CreateCacheParameterGroup = Action(prefix, 'CreateCacheParameterGroup')
CreateCacheSecurityGroup = Action(prefix, 'CreateCacheSecurityGroup')
CreateCacheSubnetGroup = Action(prefix, 'CreateCacheSubnetGroup')
CreateReplicationGroup = Action(prefix, 'CreateReplicationGroup')
CreateSnapshot = Action(prefix, 'CreateSnapshot')
DeleteCacheCluster = Action(prefix, 'DeleteCacheCluster')
DeleteCacheParameterGroup = Action(prefix, 'DeleteCacheParameterGroup')
DeleteCacheSecurityGroup = Action(prefix, 'DeleteCacheSecurityGroup')
DeleteCacheSubnetGroup = Action(prefix, 'DeleteCacheSubnetGroup')
DeleteReplicationGroup = Action(prefix, 'DeleteReplicationGroup')
DeleteSnapshot = Action(prefix, 'DeleteSnapshot')
DescribeCacheClusters = Action(prefix, 'DescribeCacheClusters')
DescribeCacheEngineVersions = \
    Action(prefix, 'DescribeCacheEngineVersions')
DescribeCacheParameterGroups = \
    Action(prefix, 'DescribeCacheParameterGroups')
DescribeCacheParameters = Action(prefix, 'DescribeCacheParameters')
DescribeCacheSecurityGroups = \
    Action(prefix, 'DescribeCacheSecurityGroups')
DescribeCacheSubnetGroups = \
    Action(prefix, 'DescribeCacheSubnetGroups')
DescribeEngineDefaultParameters = \
    Action(prefix, 'DescribeEngineDefaultParameters')
DescribeEvents = Action(prefix, 'DescribeEvents')
DescribeReplicationGroups = Action(prefix, 'DescribeReplicationGroups')
DescribeReservedCacheNodes = \
    Action(prefix, 'DescribeReservedCacheNodes')
DescribeReservedCacheNodesOfferings = \
    Action(prefix, 'DescribeReservedCacheNodesOfferings')
DescribeSnapshots = Action(prefix, 'DescribeSnapshots')
ListTagsForResource = Action(prefix, 'ListTagsForResource')
ModifyCacheCluster = Action(prefix, 'ModifyCacheCluster')
ModifyCacheParameterGroup = Action(prefix, 'ModifyCacheParameterGroup')
ModifyCacheSubnetGroup = Action(prefix, 'ModifyCacheSubnetGroup')
ModifyReplicationGroup = Action(prefix, 'ModifyReplicationGroup')
PurchaseReservedCacheNodesOffering = \
    Action(prefix, 'PurchaseReservedCacheNodesOffering')
RebootCacheCluster = Action(prefix, 'RebootCacheCluster')
RemoveTagsFromResource = Action(prefix, 'RemoveTagsFromResource')
ResetCacheParameterGroup = Action(prefix, 'ResetCacheParameterGroup')
RevokeCacheSecurityGroupIngress = \
    Action(prefix, 'RevokeCacheSecurityGroupIngress')
