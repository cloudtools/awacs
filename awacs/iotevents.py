# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT Events'
prefix = 'iotevents'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchAcknowledgeAlarm = Action('BatchAcknowledgeAlarm')
BatchDisableAlarm = Action('BatchDisableAlarm')
BatchEnableAlarm = Action('BatchEnableAlarm')
BatchPutMessage = Action('BatchPutMessage')
BatchResetAlarm = Action('BatchResetAlarm')
BatchSnoozeAlarm = Action('BatchSnoozeAlarm')
BatchUpdateDetector = Action('BatchUpdateDetector')
CreateAlarmModel = Action('CreateAlarmModel')
CreateDetectorModel = Action('CreateDetectorModel')
CreateInput = Action('CreateInput')
DeleteAlarmModel = Action('DeleteAlarmModel')
DeleteDetectorModel = Action('DeleteDetectorModel')
DeleteInput = Action('DeleteInput')
DescribeAlarm = Action('DescribeAlarm')
DescribeAlarmModel = Action('DescribeAlarmModel')
DescribeDetector = Action('DescribeDetector')
DescribeDetectorModel = Action('DescribeDetectorModel')
DescribeInput = Action('DescribeInput')
DescribeLoggingOptions = Action('DescribeLoggingOptions')
ListAlarmModelVersions = Action('ListAlarmModelVersions')
ListAlarmModels = Action('ListAlarmModels')
ListAlarms = Action('ListAlarms')
ListDetectorModelVersions = Action('ListDetectorModelVersions')
ListDetectorModels = Action('ListDetectorModels')
ListDetectors = Action('ListDetectors')
ListInputs = Action('ListInputs')
ListTagsForResource = Action('ListTagsForResource')
PutLoggingOptions = Action('PutLoggingOptions')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAlarmModel = Action('UpdateAlarmModel')
UpdateDetectorModel = Action('UpdateDetectorModel')
UpdateInput = Action('UpdateInput')
UpdateInputRouting = Action('UpdateInputRouting')
