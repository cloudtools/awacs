# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Direct Connect'
prefix = 'directconnect:'

CreateConnection = Action(prefix, 'CreateConnection')
CreatePrivateVirtualInterface = \
    Action(prefix, 'CreatePrivateVirtualInterface')
CreatePublicVirtualInterface = \
    Action(prefix, 'CreatePublicVirtualInterface')
DeleteConnection = Action(prefix, 'DeleteConnection')
DeleteVirtualInterface = Action(prefix, 'DeleteVirtualInterface')
DescribeConnectionDetail = Action(prefix, 'DescribeConnectionDetail')
DescribeConnections = Action(prefix, 'DescribeConnections')
DescribeOfferingDetail = Action(prefix, 'DescribeOfferingDetail')
DescribeOfferings = Action(prefix, 'DescribeOfferings')
DescribeVirtualGateways = Action(prefix, 'DescribeVirtualGateways')
DescribeVirtualInterfaces = Action(prefix, 'DescribeVirtualInterfaces')
