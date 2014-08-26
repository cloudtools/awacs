# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Direct Connect'
prefix = 'directconnect'

AllocateConnectionOnInterconnect = \
    Action(prefix, 'AllocateConnectionOnInterconnect')
AllocatePrivateVirtualInterface = \
    Action(prefix, 'AllocatePrivateVirtualInterface')
AllocatePublicVirtualInterface = \
    Action(prefix, 'AllocatePublicVirtualInterface')
ConfirmConnection = Action(prefix, 'ConfirmConnection')
ConfirmPrivateVirtualInterface = \
    Action(prefix, 'ConfirmPrivateVirtualInterface')
ConfirmPublicVirtualInterface = \
    Action(prefix, 'ConfirmPublicVirtualInterface')
CreateConnection = Action(prefix, 'CreateConnection')
CreateInterconnect = Action(prefix, 'CreateInterconnect')
CreatePrivateVirtualInterface = \
    Action(prefix, 'CreatePrivateVirtualInterface')
CreatePublicVirtualInterface = \
    Action(prefix, 'CreatePublicVirtualInterface')
DeleteConnection = Action(prefix, 'DeleteConnection')
DeleteInterconnect = Action(prefix, 'DeleteInterconnect')
DeleteVirtualInterface = Action(prefix, 'DeleteVirtualInterface')
DescribeConnectionDetail = Action(prefix, 'DescribeConnectionDetail')
DescribeConnections = Action(prefix, 'DescribeConnections')
DescribeOfferingDetail = Action(prefix, 'DescribeOfferingDetail')
DescribeOfferings = Action(prefix, 'DescribeOfferings')
DescribeConnectionsOnInterconnect = \
    Action(prefix, 'DescribeConnectionsOnInterconnect')
DescribeInterconnects = Action(prefix, 'DescribeInterconnects')
DescribeLocations = Action(prefix, 'DescribeLocations')
DescribeVirtualGateways = Action(prefix, 'DescribeVirtualGateways')
DescribeVirtualInterfaces = Action(prefix, 'DescribeVirtualInterfaces')
