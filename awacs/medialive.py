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
DeleteChannel = Action('DeleteChannel')
DeleteInput = Action('DeleteInput')
DeleteInputSecurityGroup = Action('DeleteInputSecurityGroup')
DeleteReservation = Action('DeleteReservation')
DescribeChannel = Action('DescribeChannel')
DescribeInput = Action('DescribeInput')
DescribeInputSecurityGroup = Action('DescribeInputSecurityGroup')
DescribeOffering = Action('DescribeOffering')
DescribeReservation = Action('DescribeReservation')
DescribeSchedule = Action('DescribeSchedule')
ListChannels = Action('ListChannels')
ListInputSecurityGroups = Action('ListInputSecurityGroups')
ListInputs = Action('ListInputs')
ListOfferings = Action('ListOfferings')
ListReservations = Action('ListReservations')
PurchaseOffering = Action('PurchaseOffering')
StartChannel = Action('StartChannel')
StopChannel = Action('StopChannel')
UpdateChannel = Action('UpdateChannel')
UpdateInput = Action('UpdateInput')
UpdateInputSecurityGroup = Action('UpdateInputSecurityGroup')
