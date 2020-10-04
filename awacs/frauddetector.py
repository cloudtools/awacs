# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Fraud Detector'
prefix = 'frauddetector'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchCreateVariable = Action('BatchCreateVariable')
BatchGetVariable = Action('BatchGetVariable')
CreateDetectorVersion = Action('CreateDetectorVersion')
CreateModel = Action('CreateModel')
CreateModelVersion = Action('CreateModelVersion')
CreateRule = Action('CreateRule')
CreateVariable = Action('CreateVariable')
DeleteDetector = Action('DeleteDetector')
DeleteDetectorVersion = Action('DeleteDetectorVersion')
DeleteEvent = Action('DeleteEvent')
DeleteRule = Action('DeleteRule')
DescribeDetector = Action('DescribeDetector')
DescribeModelVersions = Action('DescribeModelVersions')
GetDetectorVersion = Action('GetDetectorVersion')
GetDetectors = Action('GetDetectors')
GetEntityTypes = Action('GetEntityTypes')
GetEventPrediction = Action('GetEventPrediction')
GetEventTypes = Action('GetEventTypes')
GetExternalModels = Action('GetExternalModels')
GetKMSEncryptionKey = Action('GetKMSEncryptionKey')
GetLabels = Action('GetLabels')
GetModelVersion = Action('GetModelVersion')
GetModels = Action('GetModels')
GetOutcomes = Action('GetOutcomes')
GetRules = Action('GetRules')
GetVariables = Action('GetVariables')
ListTagsForResource = Action('ListTagsForResource')
PutDetector = Action('PutDetector')
PutEntityType = Action('PutEntityType')
PutEventType = Action('PutEventType')
PutExternalModel = Action('PutExternalModel')
PutKMSEncryptionKey = Action('PutKMSEncryptionKey')
PutLabel = Action('PutLabel')
PutOutcome = Action('PutOutcome')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDetectorVersion = Action('UpdateDetectorVersion')
UpdateDetectorVersionMetadata = Action('UpdateDetectorVersionMetadata')
UpdateDetectorVersionStatus = Action('UpdateDetectorVersionStatus')
UpdateModel = Action('UpdateModel')
UpdateModelVersion = Action('UpdateModelVersion')
UpdateModelVersionStatus = Action('UpdateModelVersionStatus')
UpdateRuleMetadata = Action('UpdateRuleMetadata')
UpdateRuleVersion = Action('UpdateRuleVersion')
UpdateVariable = Action('UpdateVariable')
