# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon RDS'
prefix = 'rds'

AuthorizeDBSecurityGroupIngress = \
    Action(prefix, 'AuthorizeDBSecurityGroupIngress')
CreateDBInstance = Action(prefix, 'CreateDBInstance')
CreateDBInstanceReadReplica = \
    Action(prefix, 'CreateDBInstanceReadReplica')
CreateDBParameterGroup = Action(prefix, 'CreateDBParameterGroup')
CreateDBSecurityGroup = Action(prefix, 'CreateDBSecurityGroup')
CreateDBSnapshot = Action(prefix, 'CreateDBSnapshot')
DeleteDBInstance = Action(prefix, 'DeleteDBInstance')
DeleteDBParameterGroup = Action(prefix, 'DeleteDBParameterGroup')
DeleteDBSecurityGroup = Action(prefix, 'DeleteDBSecurityGroup')
DeleteDBSnapshot = Action(prefix, 'DeleteDBSnapshot')
DescribeDBEngineVersions = Action(prefix, 'DescribeDBEngineVersions')
DescribeDBInstances = Action(prefix, 'DescribeDBInstances')
DescribeDBParameterGroups = Action(prefix, 'DescribeDBParameterGroups')
DescribeDBParameters = Action(prefix, 'DescribeDBParameters')
DescribeDBSecurityGroups = Action(prefix, 'DescribeDBSecurityGroups')
DescribeDBSnapshots = Action(prefix, 'DescribeDBSnapshots')
DescribeEngineDefaultParameters = \
    Action(prefix, 'DescribeEngineDefaultParameters')
DescribeEvents = Action(prefix, 'DescribeEvents')
DescribeReservedDBInstances = \
    Action(prefix, 'DescribeReservedDBInstances')
DescribeReservedDBInstancesOfferings = \
    Action(prefix, 'DescribeReservedDBInstancesOfferings')
ListTagsForResource = Action(prefix, 'ListTagsForResource')
ModifyDBInstance = Action(prefix, 'ModifyDBInstance')
ModifyDBParameterGroup = Action(prefix, 'ModifyDBParameterGroup')
PurchaseReservedDBInstancesOffering = \
    Action(prefix, 'PurchaseReservedDBInstancesOffering')
RebootDBInstance = Action(prefix, 'RebootDBInstance')
ResetDBParameterGroup = Action(prefix, 'ResetDBParameterGroup')
RestoreDBInstanceFromDBSnapshot = \
    Action(prefix, 'RestoreDBInstanceFromDBSnapshot')
RestoreDBInstanceToPointInTime = \
    Action(prefix, 'RestoreDBInstanceToPointInTime')
RevokeDBSecurityGroupIngress = \
    Action(prefix, 'RevokeDBSecurityGroupIngress')
