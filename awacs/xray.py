# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS XRay'
prefix = 'xray'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetTraces = Action('BatchGetTraces')
CreateGroup = Action('CreateGroup')
CreateSamplingRule = Action('CreateSamplingRule')
DeleteGroup = Action('DeleteGroup')
DeleteSamplingRule = Action('DeleteSamplingRule')
GetEncryptionConfig = Action('GetEncryptionConfig')
GetGroup = Action('GetGroup')
GetGroups = Action('GetGroups')
GetSamplingRules = Action('GetSamplingRules')
GetSamplingStatisticSummaries = Action('GetSamplingStatisticSummaries')
GetSamplingTargets = Action('GetSamplingTargets')
GetServiceGraph = Action('GetServiceGraph')
GetTraceGraph = Action('GetTraceGraph')
GetTraceSummaries = Action('GetTraceSummaries')
PutEncryptionConfig = Action('PutEncryptionConfig')
PutTelemetryRecords = Action('PutTelemetryRecords')
PutTraceSegments = Action('PutTraceSegments')
UpdateGroup = Action('UpdateGroup')
UpdateSamplingRule = Action('UpdateSamplingRule')
