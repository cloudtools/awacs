# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Redshift'
prefix = 'redshift'

AuthorizeClusterSecurityGroupIngress = \
    Action(prefix, 'AuthorizeClusterSecurityGroupIngress')
CopyClusterSnapshot = Action(prefix, 'CopyClusterSnapshot')
CreateCluster = Action(prefix, 'CreateCluster')
CreateClusterParameterGroup = \
    Action(prefix, 'CreateClusterParameterGroup')
CreateClusterSecurityGroup = \
    Action(prefix, 'CreateClusterSecurityGroup')
CreateClusterSnapshot = Action(prefix, 'CreateClusterSnapshot')
CreateClusterSubnetGroup = Action(prefix, 'CreateClusterSubnetGroup')
DeleteCluster = Action(prefix, 'DeleteCluster')
DeleteClusterParameterGroup = \
    Action(prefix, 'DeleteClusterParameterGroup')
DeleteClusterSecurityGroup = \
    Action(prefix, 'DeleteClusterSecurityGroup')
DeleteClusterSnapshot = Action(prefix, 'DeleteClusterSnapshot')
DeleteClusterSubnetGroup = Action(prefix, 'DeleteClusterSubnetGroup')
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
DescribeEvents = Action(prefix, 'DescribeEvents')
DescribeOrderableClusterOptions = \
    Action(prefix, 'DescribeOrderableClusterOptions')
DescribeReservedNodeOfferings = \
    Action(prefix, 'DescribeReservedNodeOfferings')
DescribeReservedNodes = Action(prefix, 'DescribeReservedNodes')
DescribeResize = Action(prefix, 'DescribeResize')
ModifyCluster = Action(prefix, 'ModifyCluster')
ModifyClusterParameterGroup = \
    Action(prefix, 'ModifyClusterParameterGroup')
ModifyClusterSubnetGroup = Action(prefix, 'ModifyClusterSubnetGroup')
PurchaseReservedNodeOffering = \
    Action(prefix, 'PurchaseReservedNodeOffering')
RebootCluster = Action(prefix, 'RebootCluster')
ResetClusterParameterGroup = \
    Action(prefix, 'ResetClusterParameterGroup')
RestoreFromClusterSnapshot = \
    Action(prefix, 'RestoreFromClusterSnapshot')
RevokeClusterSecurityGroupIngress = \
    Action(prefix, 'RevokeClusterSecurityGroupIngress')
