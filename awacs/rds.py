# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon RDS'
prefix = 'rds'


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
AddSourceIdentifierToSubscription = \
    Action('AddSourceIdentifierToSubscription')
ApplyPendingMaintenanceAction = Action('ApplyPendingMaintenanceAction')
AuthorizeDBSecurityGroupIngress = \
    Action('AuthorizeDBSecurityGroupIngress')
CopyDBClusterSnapshot = Action('CopyDBClusterSnapshot')
CopyDBParameterGroup = Action('CopyDBParameterGroup')
CopyDBSnapshot = Action('CopyDBSnapshot')
CopyOptionGroup = Action('CopyOptionGroup')
CreateDBClusterParameterGroup = Action('CreateDBClusterParameterGroup')
CreateDBClusterSnapshot = Action('CreateDBClusterSnapshot')
CreateDBCluster = Action('CreateDBCluster')
CreateDBInstance = Action('CreateDBInstance')
CreateDBInstanceReadReplica = Action('CreateDBInstanceReadReplica')
CreateDBParameterGroup = Action('CreateDBParameterGroup')
CreateDBSecurityGroup = Action('CreateDBSecurityGroup')
CreateDBSnapshot = Action('CreateDBSnapshot')
CreateDBSubnetGroup = Action('CreateDBSubnetGroup')
CreateEventSubscription = Action('CreateEventSubscription')
CreateOptionGroup = Action('CreateOptionGroup')
DeleteDBClusterParameterGroup = Action('DeleteDBClusterParameterGroup')
DeleteDBClusterSnapshot = Action('DeleteDBClusterSnapshot')
DeleteDBCluster = Action('DeleteDBCluster')
DeleteDBInstance = Action('DeleteDBInstance')
DeleteDBParameterGroup = Action('DeleteDBParameterGroup')
DeleteDBSecurityGroup = Action('DeleteDBSecurityGroup')
DeleteDBSnapshot = Action('DeleteDBSnapshot')
DeleteDBSubnetGroup = Action('DeleteDBSubnetGroup')
DeleteEventSubscription = Action('DeleteEventSubscription')
DeleteOptionGroup = Action('DeleteOptionGroup')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeCertificates = Action('DescribeCertificates')
DescribeEngineDefaultClusterParameters = \
    Action('DescribeEngineDefaultClusterParameters')
DescribeEngineDefaultParameters = \
    Action('DescribeEngineDefaultParameters')
DescribeDBClusterParameterGroups = \
    Action('DescribeDBClusterParameterGroups')
DescribeDBClusterParameters = Action('DescribeDBClusterParameters')
DescribeDBClusterSnapshots = Action('DescribeDBClusterSnapshots')
DescribeDBClusters = Action('DescribeDBClusters')
DescribeDBInstances = Action('DescribeDBInstances')
DescribeDBLogFiles = Action('DescribeDBLogFiles')
DescribeDBParameterGroups = Action('DescribeDBParameterGroups')
DescribeDBParameters = Action('DescribeDBParameters')
DescribeDBSecurityGroups = Action('DescribeDBSecurityGroups')
DescribeDBSnapshotAttributes = Action('DescribeDBSnapshotAttributes')
DescribeDBSnapshots = Action('DescribeDBSnapshots')
DescribeDBEngineVersions = Action('DescribeDBEngineVersions')
DescribeDBSubnetGroups = Action('DescribeDBSubnetGroups')
DescribeEventCategories = Action('DescribeEventCategories')
DescribeEvents = Action('DescribeEvents')
DescribeEventSubscriptions = Action('DescribeEventSubscriptions')
DescribeOptionGroups = Action('DescribeOptionGroups')
DescribeOptionGroupOptions = Action('DescribeOptionGroupOptions')
DescribeOrderableDBInstanceOptions = \
    Action('DescribeOrderableDBInstanceOptions')
DescribePendingMaintenanceActions = \
    Action('DescribePendingMaintenanceActions')
DescribeReservedDBInstances = Action('DescribeReservedDBInstances')
DescribeReservedDBInstancesOfferings = \
    Action('DescribeReservedDBInstancesOfferings')
DownloadCompleteDBLogFile = Action('DownloadCompleteDBLogFile')
DownloadDBLogFilePortion = Action('DownloadDBLogFilePortion')
FailoverDBCluster = Action('FailoverDBCluster')
ListTagsForResource = Action('ListTagsForResource')
ModifyDBClusterParameterGroup = Action('ModifyDBClusterParameterGroup')
ModifyDBCluster = Action('ModifyDBCluster')
ModifyDBInstance = Action('ModifyDBInstance')
ModifyDBParameterGroup = Action('ModifyDBParameterGroup')
ModifyDBSnapshotAttribute = Action('ModifyDBSnapshotAttribute')
ModifyDBSubnetGroup = Action('ModifyDBSubnetGroup')
ModifyEventSubscription = Action('ModifyEventSubscription')
ModifyOptionGroup = Action('ModifyOptionGroup')
PromoteReadReplica = Action('PromoteReadReplica')
PurchaseReservedDBInstancesOffering = \
    Action('PurchaseReservedDBInstancesOffering')
RebootDBInstance = Action('RebootDBInstance')
RemoveSourceIdentifierFromSubscription = \
    Action('RemoveSourceIdentifierFromSubscription')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
RestoreDBClusterFromSnapshot = Action('RestoreDBClusterFromSnapshot')
RestoreDBClusterToPointInTime = Action('RestoreDBClusterToPointInTime')
RestoreDBInstanceFromDBSnapshot = \
    Action('RestoreDBInstanceFromDBSnapshot')
RestoreDBInstanceToPointInTime = Action('RestoreDBInstanceToPointInTime')
ResetDBClusterParameterGroup = Action('ResetDBClusterParameterGroup')
ResetDBParameterGroup = Action('ResetDBParameterGroup')
RevokeDBSecurityGroupIngress = Action('RevokeDBSecurityGroupIngress')
