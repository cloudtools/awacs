# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elemental MediaLive'
prefix = 'medialive'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptInputDeviceTransfer = Action('AcceptInputDeviceTransfer')
BatchDelete = Action('BatchDelete')
BatchStart = Action('BatchStart')
BatchStop = Action('BatchStop')
BatchUpdateSchedule = Action('BatchUpdateSchedule')
CancelInputDeviceTransfer = Action('CancelInputDeviceTransfer')
CreateChannel = Action('CreateChannel')
CreateInput = Action('CreateInput')
CreateInputSecurityGroup = Action('CreateInputSecurityGroup')
CreateMultiplex = Action('CreateMultiplex')
CreateMultiplexProgram = Action('CreateMultiplexProgram')
CreateTags = Action('CreateTags')
DeleteChannel = Action('DeleteChannel')
DeleteInput = Action('DeleteInput')
DeleteInputSecurityGroup = Action('DeleteInputSecurityGroup')
DeleteMultiplex = Action('DeleteMultiplex')
DeleteMultiplexProgram = Action('DeleteMultiplexProgram')
DeleteReservation = Action('DeleteReservation')
DeleteSchedule = Action('DeleteSchedule')
DeleteTags = Action('DeleteTags')
DescribeChannel = Action('DescribeChannel')
DescribeInput = Action('DescribeInput')
DescribeInputDevice = Action('DescribeInputDevice')
DescribeInputDeviceThumbnail = Action('DescribeInputDeviceThumbnail')
DescribeInputSecurityGroup = Action('DescribeInputSecurityGroup')
DescribeMultiplex = Action('DescribeMultiplex')
DescribeMultiplexProgram = Action('DescribeMultiplexProgram')
DescribeOffering = Action('DescribeOffering')
DescribeReservation = Action('DescribeReservation')
DescribeSchedule = Action('DescribeSchedule')
ListChannels = Action('ListChannels')
ListInputDeviceTransfers = Action('ListInputDeviceTransfers')
ListInputDevices = Action('ListInputDevices')
ListInputSecurityGroups = Action('ListInputSecurityGroups')
ListInputs = Action('ListInputs')
ListMultiplexPrograms = Action('ListMultiplexPrograms')
ListMultiplexes = Action('ListMultiplexes')
ListOfferings = Action('ListOfferings')
ListReservations = Action('ListReservations')
ListTagsForResource = Action('ListTagsForResource')
PurchaseOffering = Action('PurchaseOffering')
RejectInputDeviceTransfer = Action('RejectInputDeviceTransfer')
StartChannel = Action('StartChannel')
StartMultiplex = Action('StartMultiplex')
StopChannel = Action('StopChannel')
StopMultiplex = Action('StopMultiplex')
TransferInputDevice = Action('TransferInputDevice')
UpdateChannel = Action('UpdateChannel')
UpdateChannelClass = Action('UpdateChannelClass')
UpdateInput = Action('UpdateInput')
UpdateInputDevice = Action('UpdateInputDevice')
UpdateInputSecurityGroup = Action('UpdateInputSecurityGroup')
UpdateMultiplex = Action('UpdateMultiplex')
UpdateMultiplexProgram = Action('UpdateMultiplexProgram')
UpdateReservation = Action('UpdateReservation')
