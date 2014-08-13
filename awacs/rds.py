# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon RDS'
prefix = 'rds'

AuthorizeDBSecurityGroupIngress = \
    Action(prefix, 'AuthorizeDBSecurityGroupIngress')
AddTagsToResource = Action(prefix, 'AddTagsToResource')
AddSourceIdentifierToSubscription = \
    Action(prefix, 'AddSourceIdentifierToSubscription')
CopyDBSnapshot = Action(prefix, 'CopyDBSnapshot')
CreateDBInstance = Action(prefix, 'CreateDBInstance')
CreateDBInstanceReadReplica = \
    Action(prefix, 'CreateDBInstanceReadReplica')
CreateDBParameterGroup = Action(prefix, 'CreateDBParameterGroup')
CreateDBSecurityGroup = Action(prefix, 'CreateDBSecurityGroup')
CreateDBSnapshot = Action(prefix, 'CreateDBSnapshot')
CreateDBSubnetGroup = Action(prefix, 'CreateDBSubnetGroup')
CreateEventSubscription = Action(prefix, 'CreateEventSubscription')
CreateOptionGroup = Action(prefix, 'CreateOptionGroup')
DeleteDBInstance = Action(prefix, 'DeleteDBInstance')
DeleteDBParameterGroup = Action(prefix, 'DeleteDBParameterGroup')
DeleteDBSecurityGroup = Action(prefix, 'DeleteDBSecurityGroup')
DeleteDBSnapshot = Action(prefix, 'DeleteDBSnapshot')
DeleteDBSubnetGroup = Action(prefix, 'DeleteDBSubnetGroup')
DeleteEventSubscription = Action(prefix, 'DeleteEventSubscription')
DeleteOptionGroup = Action(prefix, 'DeleteOptionGroup')
DescribeEngineDefaultParameters = \
    Action(prefix, 'DescribeEngineDefaultParameters')
DescribeDBInstances = Action(prefix, 'DescribeDBInstances')
DescribeDBLogFiles = Action(prefix, 'DescribeDBLogFiles')
DescribeDBParameterGroups = Action(prefix, 'DescribeDBParameterGroups')
DescribeDBParameters = Action(prefix, 'DescribeDBParameters')
DescribeDBSecurityGroups = Action(prefix, 'DescribeDBSecurityGroups')
DescribeDBSnapshots = Action(prefix, 'DescribeDBSnapshots')
DescribeDBEngineVersions = Action(prefix, 'DescribeDBEngineVersions')
DescribeDBSubnetGroups = Action(prefix, 'DescribeDBSubnetGroups')
DescribeEventCategories = Action(prefix, 'DescribeEventCategories')
DescribeEvents = Action(prefix, 'DescribeEvents')
DescribeEventSubscriptions = \
    Action(prefix, 'DescribeEventSubscriptions')
DescribeOptionGroups = Action(prefix, 'DescribeOptionGroups')
DescribeOptionGroupOptions = \
    Action(prefix, 'DescribeOptionGroupOptions')
DescribeOrderableDBInstanceOptions = \
    Action(prefix, 'DescribeOrderableDBInstanceOptions')
DescribeReservedDBInstances = \
    Action(prefix, 'DescribeReservedDBInstances')
DescribeReservedDBInstancesOfferings = \
    Action(prefix, 'DescribeReservedDBInstancesOfferings')
DownloadDBLogFilePortion = Action(prefix, 'DownloadDBLogFilePortion')
ListTagsForResource = Action(prefix, 'ListTagsForResource')
ModifyDBInstance = Action(prefix, 'ModifyDBInstance')
ModifyDBParameterGroup = Action(prefix, 'ModifyDBParameterGroup')
ModifyDBSubnetGroup = Action(prefix, 'ModifyDBSubnetGroup')
ModifyEventSubscription = Action(prefix, 'ModifyEventSubscription')
ModifyOptionGroup = Action(prefix, 'ModifyOptionGroup')
PromoteReadReplica = Action(prefix, 'PromoteReadReplica')
PurchaseReservedDBInstancesOffering = \
    Action(prefix, 'PurchaseReservedDBInstancesOffering')
RebootDBInstance = Action(prefix, 'RebootDBInstance')
RemoveSourceIdentifierFromSubscription = \
    Action(prefix, 'RemoveSourceIdentifierFromSubscription')
RemoveTagsFromResource = Action(prefix, 'RemoveTagsFromResource')
RestoreDBInstanceFromDBSnapshot = \
    Action(prefix, 'RestoreDBInstanceFromDBSnapshot')
RestoreDBInstanceToPointInTime = \
    Action(prefix, 'RestoreDBInstanceToPointInTime')
ResetDBParameterGroup = Action(prefix, 'ResetDBParameterGroup')
RevokeDBSecurityGroupIngress = \
    Action(prefix, 'RevokeDBSecurityGroupIngress')
