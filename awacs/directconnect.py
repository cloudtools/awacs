# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action


CreateConnection = Action("directconnect:CreateConnection")
CreatePrivateVirtualInterface = \
    Action("directconnect:CreatePrivateVirtualInterface")
CreatePublicVirtualInterface = \
    Action("directconnect:CreatePublicVirtualInterface")
DeleteConnection = Action("directconnect:DeleteConnection")
DeleteVirtualInterface = Action("directconnect:DeleteVirtualInterface")
DescribeConnectionDetail = Action("directconnect:DescribeConnectionDetail")
DescribeConnections = Action("directconnect:DescribeConnections")
DescribeOfferingDetail = Action("directconnect:DescribeOfferingDetail")
DescribeOfferings = Action("directconnect:DescribeOfferings")
DescribeVirtualGateways = Action("directconnect:DescribeVirtualGateways")
DescribeVirtualInterfaces = Action("directconnect:DescribeVirtualInterfaces")
