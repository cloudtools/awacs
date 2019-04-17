# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon ElastiCache'
prefix = 'elasticache'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToResource = Action('AddTagsToResource')
AuthorizeCacheSecurityGroupIngress = \
    Action('AuthorizeCacheSecurityGroupIngress')
CopySnapshot = Action('CopySnapshot')
CreateCacheCluster = Action('CreateCacheCluster')
CreateCacheParameterGroup = Action('CreateCacheParameterGroup')
CreateCacheSecurityGroup = Action('CreateCacheSecurityGroup')
CreateCacheSubnetGroup = Action('CreateCacheSubnetGroup')
CreateReplicationGroup = Action('CreateReplicationGroup')
CreateSnapshot = Action('CreateSnapshot')
DecreaseReplicaCount = Action('DecreaseReplicaCount')
DeleteCacheCluster = Action('DeleteCacheCluster')
DeleteCacheParameterGroup = Action('DeleteCacheParameterGroup')
DeleteCacheSecurityGroup = Action('DeleteCacheSecurityGroup')
DeleteCacheSubnetGroup = Action('DeleteCacheSubnetGroup')
DeleteReplicationGroup = Action('DeleteReplicationGroup')
DeleteSnapshot = Action('DeleteSnapshot')
DescribeCacheClusters = Action('DescribeCacheClusters')
DescribeCacheEngineVersions = Action('DescribeCacheEngineVersions')
DescribeCacheParameterGroups = Action('DescribeCacheParameterGroups')
DescribeCacheParameters = Action('DescribeCacheParameters')
DescribeCacheSecurityGroups = Action('DescribeCacheSecurityGroups')
DescribeCacheSubnetGroups = Action('DescribeCacheSubnetGroups')
DescribeEngineDefaultParameters = \
    Action('DescribeEngineDefaultParameters')
DescribeEvents = Action('DescribeEvents')
DescribeReplicationGroups = Action('DescribeReplicationGroups')
DescribeReservedCacheNodes = Action('DescribeReservedCacheNodes')
DescribeReservedCacheNodesOfferings = \
    Action('DescribeReservedCacheNodesOfferings')
DescribeSnapshots = Action('DescribeSnapshots')
IncreaseReplicaCount = Action('IncreaseReplicaCount')
ListAllowedNodeTypeModifications = \
    Action('ListAllowedNodeTypeModifications')
ListTagsForResource = Action('ListTagsForResource')
ModifyCacheCluster = Action('ModifyCacheCluster')
ModifyCacheParameterGroup = Action('ModifyCacheParameterGroup')
ModifyCacheSubnetGroup = Action('ModifyCacheSubnetGroup')
ModifyReplicationGroup = Action('ModifyReplicationGroup')
ModifyReplicationGroupShardConfiguration = \
    Action('ModifyReplicationGroupShardConfiguration')
PurchaseReservedCacheNodesOffering = \
    Action('PurchaseReservedCacheNodesOffering')
RebootCacheCluster = Action('RebootCacheCluster')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
ResetCacheParameterGroup = Action('ResetCacheParameterGroup')
RevokeCacheSecurityGroupIngress = \
    Action('RevokeCacheSecurityGroupIngress')
TestFailover = Action('TestFailover')
