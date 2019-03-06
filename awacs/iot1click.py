# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT 1-Click'
prefix = 'iot1click'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateDeviceWithPlacement = Action('AssociateDeviceWithPlacement')
ClaimDevicesByClaimCode = Action('ClaimDevicesByClaimCode')
CreatePlacement = Action('CreatePlacement')
CreateProject = Action('CreateProject')
DeletePlacement = Action('DeletePlacement')
DeleteProject = Action('DeleteProject')
DescribeDevice = Action('DescribeDevice')
DescribePlacement = Action('DescribePlacement')
DescribeProject = Action('DescribeProject')
DisassociateDeviceFromPlacement = \
    Action('DisassociateDeviceFromPlacement')
FinalizeDeviceClaim = Action('FinalizeDeviceClaim')
GetDeviceMethods = Action('GetDeviceMethods')
GetDevicesInPlacement = Action('GetDevicesInPlacement')
InitializeDeviceClaim = Action('InitializeDeviceClaim')
InvokeDeviceMethod = Action('InvokeDeviceMethod')
ListDeviceEvents = Action('ListDeviceEvents')
ListDevices = Action('ListDevices')
ListPlacements = Action('ListPlacements')
ListProjects = Action('ListProjects')
UnclaimDevice = Action('UnclaimDevice')
UpdateDeviceState = Action('UpdateDeviceState')
UpdatePlacement = Action('UpdatePlacement')
UpdateProject = Action('UpdateProject')
