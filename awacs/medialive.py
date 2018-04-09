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


CreateChannel = Action('CreateChannel')
CreateInput = Action('CreateInput')
CreateInputSecurityGroup = Action('CreateInputSecurityGroup')
DeleteChannel = Action('DeleteChannel')
DeleteInput = Action('DeleteInput')
DeleteInputSecurityGroup = Action('DeleteInputSecurityGroup')
DescribeChannel = Action('DescribeChannel')
DescribeInput = Action('DescribeInput')
DescribeInputSecurityGroup = Action('DescribeInputSecurityGroup')
ListChannels = Action('ListChannels')
ListInputSecurityGroups = Action('ListInputSecurityGroups')
ListInputs = Action('ListInputs')
StartChannel = Action('StartChannel')
StopChannel = Action('StopChannel')
