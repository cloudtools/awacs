# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Direct Connect'
prefix = 'directconnect'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AllocateConnectionOnInterconnect = \
    Action('AllocateConnectionOnInterconnect')
AllocatePrivateVirtualInterface = \
    Action('AllocatePrivateVirtualInterface')
AllocatePublicVirtualInterface = Action('AllocatePublicVirtualInterface')
ConfirmConnection = Action('ConfirmConnection')
ConfirmPrivateVirtualInterface = Action('ConfirmPrivateVirtualInterface')
ConfirmPublicVirtualInterface = Action('ConfirmPublicVirtualInterface')
CreateConnection = Action('CreateConnection')
CreateInterconnect = Action('CreateInterconnect')
CreatePrivateVirtualInterface = Action('CreatePrivateVirtualInterface')
CreatePublicVirtualInterface = Action('CreatePublicVirtualInterface')
DeleteConnection = Action('DeleteConnection')
DeleteInterconnect = Action('DeleteInterconnect')
DeleteVirtualInterface = Action('DeleteVirtualInterface')
DescribeConnections = Action('DescribeConnections')
DescribeConnectionsOnInterconnect = \
    Action('DescribeConnectionsOnInterconnect')
DescribeInterconnects = Action('DescribeInterconnects')
DescribeLocations = Action('DescribeLocations')
DescribeVirtualGateways = Action('DescribeVirtualGateways')
DescribeVirtualInterfaces = Action('DescribeVirtualInterfaces')
