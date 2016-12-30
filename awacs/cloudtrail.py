# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CloudTrail'
prefix = 'cloudtrail'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTags = Action('AddTags')
CreateTrail = Action('CreateTrail')
DeleteTrail = Action('DeleteTrail')
DescribeTrails = Action('DescribeTrails')
GetEventSelectors = Action('GetEventSelectors')
GetTrailStatus = Action('GetTrailStatus')
ListPublicKeys = Action('ListPublicKeys')
ListTags = Action('ListTags')
LookupEvents = Action('LookupEvents')
PutEventSelectors = Action('PutEventSelectors')
RemoveTags = Action('RemoveTags')
StartLogging = Action('StartLogging')
StopLogging = Action('StopLogging')
UpdateTrail = Action('UpdateTrail')
