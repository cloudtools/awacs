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
ApplyPendingMaintenanceAction = Action('ApplyPendingMaintenanceAction')
CreateEndpoint = Action('CreateEndpoint')
CreateEventSubscription = Action('CreateEventSubscription')
CreateReplicationInstance = Action('CreateReplicationInstance')
CreateReplicationSubnetGroup = Action('CreateReplicationSubnetGroup')
CreateReplicationTask = Action('CreateReplicationTask')
DeleteCertificate = Action('DeleteCertificate')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteEventSubscription = Action('DeleteEventSubscription')
DeleteReplicationInstance = Action('DeleteReplicationInstance')
DeleteReplicationSubnetGroup = Action('DeleteReplicationSubnetGroup')
DeleteReplicationTask = Action('DeleteReplicationTask')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeCertificates = Action('DescribeCertificates')
DescribeConnections = Action('DescribeConnections')
DescribeEndpointTypes = Action('DescribeEndpointTypes')
DescribeEndpoints = Action('DescribeEndpoints')
DescribeEventCategories = Action('DescribeEventCategories')
DescribeEventSubscriptions = Action('DescribeEventSubscriptions')
DescribeEvents = Action('DescribeEvents')
DescribeOrderableReplicationInstances = \
    Action('DescribeOrderableReplicationInstances')
DescribeRefreshSchemasStatus = Action('DescribeRefreshSchemasStatus')
DescribeReplicationInstanceTaskLogs = \
    Action('DescribeReplicationInstanceTaskLogs')
DescribeReplicationInstances = Action('DescribeReplicationInstances')
DescribeReplicationSubnetGroups = \
    Action('DescribeReplicationSubnetGroups')
DescribeReplicationTaskAssessmentResults = \
    Action('DescribeReplicationTaskAssessmentResults')
DescribeReplicationTasks = Action('DescribeReplicationTasks')
DescribeSchemas = Action('DescribeSchemas')
DescribeTableStatistics = Action('DescribeTableStatistics')
ImportCertificate = Action('ImportCertificate')
ListTagsForResource = Action('ListTagsForResource')
ModifyEndpoint = Action('ModifyEndpoint')
ModifyEventSubscription = Action('ModifyEventSubscription')
ModifyReplicationInstance = Action('ModifyReplicationInstance')
ModifyReplicationSubnetGroup = Action('ModifyReplicationSubnetGroup')
ModifyReplicationTask = Action('ModifyReplicationTask')
RebootReplicationInstance = Action('RebootReplicationInstance')
RefreshSchemas = Action('RefreshSchemas')
ReloadTables = Action('ReloadTables')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
StartReplicationTask = Action('StartReplicationTask')
StartReplicationTaskAssessment = Action('StartReplicationTaskAssessment')
StopReplicationTask = Action('StopReplicationTask')
TestConnection = Action('TestConnection')
