# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Redshift'
prefix = 'redshift'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptReservedNodeExchange = Action('AcceptReservedNodeExchange')
AuthorizeClusterSecurityGroupIngress = \
    Action('AuthorizeClusterSecurityGroupIngress')
AuthorizeSnapshotAccess = Action('AuthorizeSnapshotAccess')
BatchDeleteClusterSnapshots = Action('BatchDeleteClusterSnapshots')
BatchModifyClusterSnapshots = Action('BatchModifyClusterSnapshots')
CancelQuery = Action('CancelQuery')
CancelQuerySession = Action('CancelQuerySession')
CancelResize = Action('CancelResize')
CopyClusterSnapshot = Action('CopyClusterSnapshot')
CreateCluster = Action('CreateCluster')
CreateClusterParameterGroup = Action('CreateClusterParameterGroup')
CreateClusterSecurityGroup = Action('CreateClusterSecurityGroup')
CreateClusterSnapshot = Action('CreateClusterSnapshot')
CreateClusterSubnetGroup = Action('CreateClusterSubnetGroup')
CreateClusterUser = Action('CreateClusterUser')
CreateEventSubscription = Action('CreateEventSubscription')
CreateHsmClientCertificate = Action('CreateHsmClientCertificate')
CreateHsmConfiguration = Action('CreateHsmConfiguration')
CreateSavedQuery = Action('CreateSavedQuery')
CreateSnapshotCopyGrant = Action('CreateSnapshotCopyGrant')
CreateSnapshotSchedule = Action('CreateSnapshotSchedule')
CreateTags = Action('CreateTags')
DeleteCluster = Action('DeleteCluster')
DeleteClusterParameterGroup = Action('DeleteClusterParameterGroup')
DeleteClusterSecurityGroup = Action('DeleteClusterSecurityGroup')
DeleteClusterSnapshot = Action('DeleteClusterSnapshot')
DeleteClusterSubnetGroup = Action('DeleteClusterSubnetGroup')
DeleteEventSubscription = Action('DeleteEventSubscription')
DeleteHsmClientCertificate = Action('DeleteHsmClientCertificate')
DeleteHsmConfiguration = Action('DeleteHsmConfiguration')
DeleteSavedQueries = Action('DeleteSavedQueries')
DeleteSnapshotCopyGrant = Action('DeleteSnapshotCopyGrant')
DeleteSnapshotSchedule = Action('DeleteSnapshotSchedule')
DeleteTags = Action('DeleteTags')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeClusterDbRevisions = Action('DescribeClusterDbRevisions')
DescribeClusterParameterGroups = Action('DescribeClusterParameterGroups')
DescribeClusterParameters = Action('DescribeClusterParameters')
DescribeClusterSecurityGroups = Action('DescribeClusterSecurityGroups')
DescribeClusterSnapshots = Action('DescribeClusterSnapshots')
DescribeClusterSubnetGroups = Action('DescribeClusterSubnetGroups')
DescribeClusterTracks = Action('DescribeClusterTracks')
DescribeClusterVersions = Action('DescribeClusterVersions')
DescribeClusters = Action('DescribeClusters')
DescribeDefaultClusterParameters = \
    Action('DescribeDefaultClusterParameters')
DescribeEventCategories = Action('DescribeEventCategories')
DescribeEventSubscriptions = Action('DescribeEventSubscriptions')
DescribeEvents = Action('DescribeEvents')
DescribeHsmClientCertificates = Action('DescribeHsmClientCertificates')
DescribeHsmConfigurations = Action('DescribeHsmConfigurations')
DescribeLoggingStatus = Action('DescribeLoggingStatus')
DescribeOrderableClusterOptions = \
    Action('DescribeOrderableClusterOptions')
DescribeQuery = Action('DescribeQuery')
DescribeReservedNodeOfferings = Action('DescribeReservedNodeOfferings')
DescribeReservedNodes = Action('DescribeReservedNodes')
DescribeResize = Action('DescribeResize')
DescribeSnapshotCopyGrants = Action('DescribeSnapshotCopyGrants')
DescribeSnapshotSchedules = Action('DescribeSnapshotSchedules')
DescribeStorage = Action('DescribeStorage')
DescribeTable = Action('DescribeTable')
DescribeTableRestoreStatus = Action('DescribeTableRestoreStatus')
DescribeTags = Action('DescribeTags')
DisableLogging = Action('DisableLogging')
DisableSnapshotCopy = Action('DisableSnapshotCopy')
EnableLogging = Action('EnableLogging')
EnableSnapshotCopy = Action('EnableSnapshotCopy')
ExecuteQuery = Action('ExecuteQuery')
FetchResults = Action('FetchResults')
GetClusterCredentials = Action('GetClusterCredentials')
GetReservedNodeExchangeOfferings = \
    Action('GetReservedNodeExchangeOfferings')
JoinGroup = Action('JoinGroup')
ListDatabases = Action('ListDatabases')
ListSavedQueries = Action('ListSavedQueries')
ListSchemas = Action('ListSchemas')
ListTables = Action('ListTables')
ModifyCluster = Action('ModifyCluster')
ModifyClusterDbRevision = Action('ModifyClusterDbRevision')
ModifyClusterIamRoles = Action('ModifyClusterIamRoles')
ModifyClusterMaintenance = Action('ModifyClusterMaintenance')
ModifyClusterParameterGroup = Action('ModifyClusterParameterGroup')
ModifyClusterSnapshot = Action('ModifyClusterSnapshot')
ModifyClusterSnapshotSchedule = Action('ModifyClusterSnapshotSchedule')
ModifyClusterSubnetGroup = Action('ModifyClusterSubnetGroup')
ModifyEventSubscription = Action('ModifyEventSubscription')
ModifySavedQuery = Action('ModifySavedQuery')
ModifySnapshotCopyRetentionPeriod = \
    Action('ModifySnapshotCopyRetentionPeriod')
ModifySnapshotSchedule = Action('ModifySnapshotSchedule')
PurchaseReservedNodeOffering = Action('PurchaseReservedNodeOffering')
RebootCluster = Action('RebootCluster')
ResetClusterParameterGroup = Action('ResetClusterParameterGroup')
ResizeCluster = Action('ResizeCluster')
RestoreFromClusterSnapshot = Action('RestoreFromClusterSnapshot')
RestoreTableFromClusterSnapshot = \
    Action('RestoreTableFromClusterSnapshot')
RevokeClusterSecurityGroupIngress = \
    Action('RevokeClusterSecurityGroupIngress')
RevokeSnapshotAccess = Action('RevokeSnapshotAccess')
RotateEncryptionKey = Action('RotateEncryptionKey')
ViewQueriesFromConsole = Action('ViewQueriesFromConsole')
ViewQueriesInConsole = Action('ViewQueriesInConsole')
