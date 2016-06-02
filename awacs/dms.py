# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Database Migration Service'
prefix = 'dms'


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
CreateEndpoint = Action('CreateEndpoint')
CreateReplicationInstance = Action('CreateReplicationInstance')
CreateReplicationSubnetGroup = Action('CreateReplicationSubnetGroup')
CreateReplicationTask = Action('CreateReplicationTask')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteReplicationInstance = Action('DeleteReplicationInstance')
DeleteReplicationSubnetGroup = Action('DeleteReplicationSubnetGroup')
DeleteReplicationTask = Action('DeleteReplicationTask')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeConnections = Action('DescribeConnections')
DescribeEndpointTypes = Action('DescribeEndpointTypes')
DescribeEndpoints = Action('DescribeEndpoints')
DescribeOrderableReplicationInstances = \
    Action('DescribeOrderableReplicationInstances')
DescribeRefreshSchemasStatus = Action('DescribeRefreshSchemasStatus')
DescribeReplicationInstances = Action('DescribeReplicationInstances')
DescribeReplicationSubnetGroups = \
    Action('DescribeReplicationSubnetGroups')
DescribeReplicationTasks = Action('DescribeReplicationTasks')
DescribeSchemas = Action('DescribeSchemas')
DescribeTableStatistics = Action('DescribeTableStatistics')
ListTagsForResource = Action('ListTagsForResource')
ModifyEndpoint = Action('ModifyEndpoint')
ModifyReplicationInstance = Action('ModifyReplicationInstance')
ModifyReplicationSubnetGroup = Action('ModifyReplicationSubnetGroup')
RefreshSchemas = Action('RefreshSchemas')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
StartReplicationTask = Action('StartReplicationTask')
StopReplicationTask = Action('StopReplicationTask')
TestConnection = Action('TestConnection')
