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


AuthorizeClusterSecurityGroupIngress = \
    Action('AuthorizeClusterSecurityGroupIngress')
AuthorizeSnapshotAccess = Action('AuthorizeSnapshotAccess')
CancelQuerySession = Action('CancelQuerySession')
CopyClusterSnapshot = Action('CopyClusterSnapshot')
CreateCluster = Action('CreateCluster')
CreateClusterParameterGroup = Action('CreateClusterParameterGroup')
CreateClusterSecurityGroup = Action('CreateClusterSecurityGroup')
CreateClusterSnapshot = Action('CreateClusterSnapshot')
CreateClusterSubnetGroup = Action('CreateClusterSubnetGroup')
CreateEventSubscription = Action('CreateEventSubscription')
CreateHsmClientCertificate = Action('CreateHsmClientCertificate')
CreateHsmConfiguration = Action('CreateHsmConfiguration')
CreateTags = Action('CreateTags')
DeleteCluster = Action('DeleteCluster')
DeleteClusterParameterGroup = Action('DeleteClusterParameterGroup')
DeleteClusterSecurityGroup = Action('DeleteClusterSecurityGroup')
DeleteClusterSnapshot = Action('DeleteClusterSnapshot')
DeleteClusterSubnetGroup = Action('DeleteClusterSubnetGroup')
DeleteEventSubscription = Action('DeleteEventSubscription')
DeleteHsmClientCertificate = Action('DeleteHsmClientCertificate')
DeleteHsmConfiguration = Action('DeleteHsmConfiguration')
DeleteTags = Action('DeleteTags')
DescribeClusterParameterGroups = Action('DescribeClusterParameterGroups')
DescribeClusterParameters = Action('DescribeClusterParameters')
DescribeClusterSecurityGroups = Action('DescribeClusterSecurityGroups')
DescribeClusterSnapshots = Action('DescribeClusterSnapshots')
DescribeClusterSubnetGroups = Action('DescribeClusterSubnetGroups')
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
DescribeReservedNodeOfferings = Action('DescribeReservedNodeOfferings')
DescribeReservedNodes = Action('DescribeReservedNodes')
DescribeResize = Action('DescribeResize')
DescribeTags = Action('DescribeTags')
DisableLogging = Action('DisableLogging')
DisableSnapshotCopy = Action('DisableSnapshotCopy')
EnableLogging = Action('EnableLogging')
EnableSnapshotCopy = Action('EnableSnapshotCopy')
ModifyCluster = Action('ModifyCluster')
ModifyClusterParameterGroup = Action('ModifyClusterParameterGroup')
ModifyClusterSubnetGroup = Action('ModifyClusterSubnetGroup')
ModifyEventSubscription = Action('ModifyEventSubscription')
ModifySnapshotCopyRetentionPeriod = \
    Action('ModifySnapshotCopyRetentionPeriod')
PurchaseReservedNodeOffering = Action('PurchaseReservedNodeOffering')
RebootCluster = Action('RebootCluster')
ResetClusterParameterGroup = Action('ResetClusterParameterGroup')
RestoreFromClusterSnapshot = Action('RestoreFromClusterSnapshot')
RevokeClusterSecurityGroupIngress = \
    Action('RevokeClusterSecurityGroupIngress')
RevokeSnapshotAccess = Action('RevokeSnapshotAccess')
RotateEncryptionKey = Action('RotateEncryptionKey')
ViewQueriesInConsole = Action('ViewQueriesInConsole')
