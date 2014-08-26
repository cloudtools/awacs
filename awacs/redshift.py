# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Redshift'
prefix = 'redshift'

AuthorizeClusterSecurityGroupIngress = \
    Action(prefix, 'AuthorizeClusterSecurityGroupIngress')
AuthorizeSnapshotAccess = Action(prefix, 'AuthorizeSnapshotAccess')
CopyClusterSnapshot = Action(prefix, 'CopyClusterSnapshot')
CreateCluster = Action(prefix, 'CreateCluster')
CreateClusterParameterGroup = \
    Action(prefix, 'CreateClusterParameterGroup')
CreateClusterSecurityGroup = \
    Action(prefix, 'CreateClusterSecurityGroup')
CreateClusterSnapshot = Action(prefix, 'CreateClusterSnapshot')
CreateClusterSubnetGroup = Action(prefix, 'CreateClusterSubnetGroup')
CreateEventSubscription = Action(prefix, 'CreateEventSubscription')
CreateHsmClientCertificate = \
    Action(prefix, 'CreateHsmClientCertificate')
CreateHsmConfiguration = Action(prefix, 'CreateHsmConfiguration')
DeleteCluster = Action(prefix, 'DeleteCluster')
DeleteClusterParameterGroup = \
    Action(prefix, 'DeleteClusterParameterGroup')
DeleteClusterSecurityGroup = \
    Action(prefix, 'DeleteClusterSecurityGroup')
DeleteClusterSnapshot = Action(prefix, 'DeleteClusterSnapshot')
DeleteClusterSubnetGroup = Action(prefix, 'DeleteClusterSubnetGroup')
DeleteEventSubscription = Action(prefix, 'DeleteEventSubscription')
DeleteHsmClientCertificate = \
    Action(prefix, 'DeleteHsmClientCertificate')
DeleteHsmConfiguration = Action(prefix, 'DeleteHsmConfiguration')
DescribeClusterParameterGroups = \
    Action(prefix, 'DescribeClusterParameterGroups')
DescribeClusterParameters = Action(prefix, 'DescribeClusterParameters')
DescribeClusterSecurityGroups = \
    Action(prefix, 'DescribeClusterSecurityGroups')
DescribeClusterSnapshots = Action(prefix, 'DescribeClusterSnapshots')
DescribeClusterSubnetGroups = \
    Action(prefix, 'DescribeClusterSubnetGroups')
DescribeClusterVersions = Action(prefix, 'DescribeClusterVersions')
DescribeClusters = Action(prefix, 'DescribeClusters')
DescribeDefaultClusterParameters = \
    Action(prefix, 'DescribeDefaultClusterParameters')
DescribeEventCategories = Action(prefix, 'DescribeEventCategories')
DescribeEventSubscriptions = \
    Action(prefix, 'DescribeEventSubscriptions')
DescribeEvents = Action(prefix, 'DescribeEvents')
DescribeHsmClientCertificates = \
    Action(prefix, 'DescribeHsmClientCertificates')
DescribeHsmConfigurations = Action(prefix, 'DescribeHsmConfigurations')
DescribeLoggingStatus = Action(prefix, 'DescribeLoggingStatus')
DescribeOrderableClusterOptions = \
    Action(prefix, 'DescribeOrderableClusterOptions')
DescribeReservedNodeOfferings = \
    Action(prefix, 'DescribeReservedNodeOfferings')
DescribeReservedNodes = Action(prefix, 'DescribeReservedNodes')
DescribeResize = Action(prefix, 'DescribeResize')
DisableLogging = Action(prefix, 'DisableLogging')
DisableSnapshotCopy = Action(prefix, 'DisableSnapshotCopy')
EnableLogging = Action(prefix, 'EnableLogging')
EnableSnapshotCopy = Action(prefix, 'EnableSnapshotCopy')
ModifyCluster = Action(prefix, 'ModifyCluster')
ModifyClusterParameterGroup = \
    Action(prefix, 'ModifyClusterParameterGroup')
ModifyClusterSubnetGroup = Action(prefix, 'ModifyClusterSubnetGroup')
ModifyEventSubscription = Action(prefix, 'ModifyEventSubscription')
ModifySnapshotCopyRetentionPeriod = \
    Action(prefix, 'ModifySnapshotCopyRetentionPeriod')
PurchaseReservedNodeOffering = \
    Action(prefix, 'PurchaseReservedNodeOffering')
RebootCluster = Action(prefix, 'RebootCluster')
ResetClusterParameterGroup = \
    Action(prefix, 'ResetClusterParameterGroup')
RestoreFromClusterSnapshot = \
    Action(prefix, 'RestoreFromClusterSnapshot')
RevokeClusterSecurityGroupIngress = \
    Action(prefix, 'RevokeClusterSecurityGroupIngress')
RevokeSnapshotAccess = Action(prefix, 'RevokeSnapshotAccess')
RotateEncryptionKey = Action(prefix, 'RotateEncryptionKey')
ViewQueriesInConsole = Action(prefix, 'ViewQueriesInConsole')
