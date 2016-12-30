# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Config'
prefix = 'config'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


DeleteConfigRule = Action('DeleteConfigRule')
DeleteConfigurationRecorder = Action('DeleteConfigurationRecorder')
DeleteDeliveryChannel = Action('DeleteDeliveryChannel')
DeleteEvaluationResults = Action('DeleteEvaluationResults')
DeliverConfigSnapshot = Action('DeliverConfigSnapshot')
DescribeComplianceByConfigRule = Action('DescribeComplianceByConfigRule')
DescribeComplianceByResource = Action('DescribeComplianceByResource')
DescribeConfigRuleEvaluationStatus = \
    Action('DescribeConfigRuleEvaluationStatus')
DescribeConfigRules = Action('DescribeConfigRules')
DescribeConfigurationRecorderStatus = \
    Action('DescribeConfigurationRecorderStatus')
DescribeConfigurationRecorders = Action('DescribeConfigurationRecorders')
DescribeDeliveryChannelStatus = Action('DescribeDeliveryChannelStatus')
DescribeDeliveryChannels = Action('DescribeDeliveryChannels')
GetComplianceDetailsByConfigRule = \
    Action('GetComplianceDetailsByConfigRule')
GetComplianceDetailsByResource = Action('GetComplianceDetailsByResource')
GetComplianceSummaryByConfigRule = \
    Action('GetComplianceSummaryByConfigRule')
GetComplianceSummaryByResourceType = \
    Action('GetComplianceSummaryByResourceType')
GetResourceConfigHistory = Action('GetResourceConfigHistory')
GetResources = Action('GetResources')
GetTagKeys = Action('GetTagKeys')
ListDiscoveredResources = Action('ListDiscoveredResources')
PutConfigRule = Action('PutConfigRule')
PutConfigurationRecorder = Action('PutConfigurationRecorder')
PutDeliveryChannel = Action('PutDeliveryChannel')
PutEvaluations = Action('PutEvaluations')
StartConfigRulesEvaluation = Action('StartConfigRulesEvaluation')
StartConfigurationRecorder = Action('StartConfigurationRecorder')
StopConfigurationRecorder = Action('StopConfigurationRecorder')
