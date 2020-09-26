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


BatchUpdateSchedule = Action('BatchUpdateSchedule')
CreateChannel = Action('CreateChannel')
CreateInput = Action('CreateInput')
CreateInputSecurityGroup = Action('CreateInputSecurityGroup')
CreateMultiplex = Action('CreateMultiplex')
CreateTags = Action('CreateTags')
DeleteChannel = Action('DeleteChannel')
DeleteInput = Action('DeleteInput')
DeleteInputSecurityGroup = Action('DeleteInputSecurityGroup')
DeleteMultiplex = Action('DeleteMultiplex')
DeleteReservation = Action('DeleteReservation')
DeleteTags = Action('DeleteTags')
DescribeChannel = Action('DescribeChannel')
DescribeInput = Action('DescribeInput')
DescribeInputDevice = Action('DescribeInputDevice')
DescribeInputDeviceThumbnail = Action('DescribeInputDeviceThumbnail')
DescribeInputSecurityGroup = Action('DescribeInputSecurityGroup')
DescribeMultiplex = Action('DescribeMultiplex')
DescribeOffering = Action('DescribeOffering')
DescribeReservation = Action('DescribeReservation')
DescribeSchedule = Action('DescribeSchedule')
ListChannels = Action('ListChannels')
ListInputDevices = Action('ListInputDevices')
ListInputSecurityGroups = Action('ListInputSecurityGroups')
ListInputs = Action('ListInputs')
ListMultiplexes = Action('ListMultiplexes')
ListOfferings = Action('ListOfferings')
ListReservations = Action('ListReservations')
ListTagsForResource = Action('ListTagsForResource')
PurchaseOffering = Action('PurchaseOffering')
StartChannel = Action('StartChannel')
StartMultiplex = Action('StartMultiplex')
StopChannel = Action('StopChannel')
StopMultiplex = Action('StopMultiplex')
UpdateChannel = Action('UpdateChannel')
UpdateChannelClass = Action('UpdateChannelClass')
UpdateInput = Action('UpdateInput')
UpdateInputDevice = Action('UpdateInputDevice')
UpdateInputSecurityGroup = Action('UpdateInputSecurityGroup')
UpdateMultiplex = Action('UpdateMultiplex')
UpdateReservation = Action('UpdateReservation')
