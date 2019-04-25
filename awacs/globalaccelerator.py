# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Global Accelerator'
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


CreateAccelerator = Action('CreateAccelerator')
CreateEndpointGroup = Action('CreateEndpointGroup')
CreateListener = Action('CreateListener')
DeleteAccelerator = Action('DeleteAccelerator')
DeleteEndpointGroup = Action('DeleteEndpointGroup')
DeleteListener = Action('DeleteListener')
DescribeAccelerator = Action('DescribeAccelerator')
DescribeAcceleratorAttributes = Action('DescribeAcceleratorAttributes')
DescribeEndpointGroup = Action('DescribeEndpointGroup')
DescribeListener = Action('DescribeListener')
ListAccelerators = Action('ListAccelerators')
ListEndpointGroups = Action('ListEndpointGroups')
ListListeners = Action('ListListeners')
UpdateAccelerator = Action('UpdateAccelerator')
UpdateAcceleratorAttributes = Action('UpdateAcceleratorAttributes')
UpdateEndpointGroup = Action('UpdateEndpointGroup')
UpdateListener = Action('UpdateListener')
