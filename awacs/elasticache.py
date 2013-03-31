# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS ElastiCache'
prefix = 'elasticache'

AuthorizeCacheSecurityGroupIngress = \
    Action(prefix, 'AuthorizeCacheSecurityGroupIngress')
CreateCacheCluster = Action(prefix, 'CreateCacheCluster')
CreateCacheParameterGroup = Action(prefix, 'CreateCacheParameterGroup')
CreateCacheSecurityGroup = Action(prefix, 'CreateCacheSecurityGroup')
DeleteCacheCluster = Action(prefix, 'DeleteCacheCluster')
DeleteCacheParameterGroup = Action(prefix, 'DeleteCacheParameterGroup')
DeleteCacheSecurityGroup = Action(prefix, 'DeleteCacheSecurityGroup')
DescribeCacheClusters = Action(prefix, 'DescribeCacheClusters')
DescribeCacheParameterGroups = \
    Action(prefix, 'DescribeCacheParameterGroups')
DescribeCacheParameters = Action(prefix, 'DescribeCacheParameters')
DescribeCacheSecurityGroups = \
    Action(prefix, 'DescribeCacheSecurityGroups')
DescribeEngineDefaultParameters = \
    Action(prefix, 'DescribeEngineDefaultParameters')
DescribeEvents = Action(prefix, 'DescribeEvents')
ModifyCacheCluster = Action(prefix, 'ModifyCacheCluster')
ModifyCacheParameterGroup = Action(prefix, 'ModifyCacheParameterGroup')
RebootCacheCluster = Action(prefix, 'RebootCacheCluster')
ResetCacheParameterGroup = Action(prefix, 'ResetCacheParameterGroup')
RevokeCacheSecurityGroupIngress = \
    Action(prefix, 'RevokeCacheSecurityGroupIngress')
