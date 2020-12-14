# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Global Accelerator'
prefix = 'globalaccelerator'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddCustomRoutingEndpoints = Action('AddCustomRoutingEndpoints')
AdvertiseByoipCidr = Action('AdvertiseByoipCidr')
AllowCustomRoutingTraffic = Action('AllowCustomRoutingTraffic')
CreateAccelerator = Action('CreateAccelerator')
CreateCustomRoutingAccelerator = Action('CreateCustomRoutingAccelerator')
CreateCustomRoutingEndpointGroup = \
    Action('CreateCustomRoutingEndpointGroup')
CreateCustomRoutingListener = Action('CreateCustomRoutingListener')
CreateEndpointGroup = Action('CreateEndpointGroup')
CreateListener = Action('CreateListener')
DeleteAccelerator = Action('DeleteAccelerator')
DeleteCustomRoutingAccelerator = Action('DeleteCustomRoutingAccelerator')
DeleteCustomRoutingEndpointGroup = \
    Action('DeleteCustomRoutingEndpointGroup')
DeleteCustomRoutingListener = Action('DeleteCustomRoutingListener')
DeleteEndpointGroup = Action('DeleteEndpointGroup')
DeleteListener = Action('DeleteListener')
DenyCustomRoutingTraffic = Action('DenyCustomRoutingTraffic')
DeprovisionByoipCidr = Action('DeprovisionByoipCidr')
DescribeAccelerator = Action('DescribeAccelerator')
DescribeAcceleratorAttributes = Action('DescribeAcceleratorAttributes')
DescribeCustomRoutingAccelerator = \
    Action('DescribeCustomRoutingAccelerator')
DescribeCustomRoutingAcceleratorAttributes = \
    Action('DescribeCustomRoutingAcceleratorAttributes')
DescribeCustomRoutingEndpointGroup = \
    Action('DescribeCustomRoutingEndpointGroup')
DescribeCustomRoutingListener = Action('DescribeCustomRoutingListener')
DescribeEndpointGroup = Action('DescribeEndpointGroup')
DescribeListener = Action('DescribeListener')
ListAccelerators = Action('ListAccelerators')
ListByoipCidrs = Action('ListByoipCidrs')
ListCustomRoutingAccelerators = Action('ListCustomRoutingAccelerators')
ListCustomRoutingEndpointGroups = \
    Action('ListCustomRoutingEndpointGroups')
ListCustomRoutingListeners = Action('ListCustomRoutingListeners')
ListCustomRoutingPortMappings = Action('ListCustomRoutingPortMappings')
ListCustomRoutingPortMappingsByDestination = \
    Action('ListCustomRoutingPortMappingsByDestination')
ListEndpointGroups = Action('ListEndpointGroups')
ListListeners = Action('ListListeners')
ListTagsForResource = Action('ListTagsForResource')
ProvisionByoipCidr = Action('ProvisionByoipCidr')
RemoveCustomRoutingEndpoints = Action('RemoveCustomRoutingEndpoints')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAccelerator = Action('UpdateAccelerator')
UpdateAcceleratorAttributes = Action('UpdateAcceleratorAttributes')
UpdateCustomRoutingAccelerator = Action('UpdateCustomRoutingAccelerator')
UpdateCustomRoutingAcceleratorAttributes = \
    Action('UpdateCustomRoutingAcceleratorAttributes')
UpdateCustomRoutingListener = Action('UpdateCustomRoutingListener')
UpdateEndpointGroup = Action('UpdateEndpointGroup')
UpdateListener = Action('UpdateListener')
WithdrawByoipCidr = Action('WithdrawByoipCidr')
