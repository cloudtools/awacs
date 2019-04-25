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


BatchGetAggregateResourceConfig = \
    Action('BatchGetAggregateResourceConfig')
BatchGetResourceConfig = Action('BatchGetResourceConfig')
DeleteAggregationAuthorization = Action('DeleteAggregationAuthorization')
DeleteConfigRule = Action('DeleteConfigRule')
DeleteConfigurationAggregator = Action('DeleteConfigurationAggregator')
DeleteConfigurationRecorder = Action('DeleteConfigurationRecorder')
DeleteDeliveryChannel = Action('DeleteDeliveryChannel')
DeleteEvaluationResults = Action('DeleteEvaluationResults')
DeletePendingAggregationRequest = \
    Action('DeletePendingAggregationRequest')
DeleteRetentionConfiguration = Action('DeleteRetentionConfiguration')
DeliverConfigSnapshot = Action('DeliverConfigSnapshot')
DescribeAggregateComplianceByConfigRules = \
    Action('DescribeAggregateComplianceByConfigRules')
DescribeAggregationAuthorizations = \
    Action('DescribeAggregationAuthorizations')
DescribeComplianceByConfigRule = Action('DescribeComplianceByConfigRule')
DescribeComplianceByResource = Action('DescribeComplianceByResource')
DescribeConfigRuleEvaluationStatus = \
    Action('DescribeConfigRuleEvaluationStatus')
DescribeConfigRules = Action('DescribeConfigRules')
DescribeConfigurationAggregatorSourcesStatus = \
    Action('DescribeConfigurationAggregatorSourcesStatus')
DescribeConfigurationAggregators = \
    Action('DescribeConfigurationAggregators')
DescribeConfigurationRecorderStatus = \
    Action('DescribeConfigurationRecorderStatus')
DescribeConfigurationRecorders = Action('DescribeConfigurationRecorders')
DescribeDeliveryChannelStatus = Action('DescribeDeliveryChannelStatus')
DescribeDeliveryChannels = Action('DescribeDeliveryChannels')
DescribePendingAggregationRequests = \
    Action('DescribePendingAggregationRequests')
DescribeRetentionConfigurations = \
    Action('DescribeRetentionConfigurations')
GetAggregateComplianceDetailsByConfigRule = \
    Action('GetAggregateComplianceDetailsByConfigRule')
GetAggregateConfigRuleComplianceSummary = \
    Action('GetAggregateConfigRuleComplianceSummary')
GetAggregateDiscoveredResourceCounts = \
    Action('GetAggregateDiscoveredResourceCounts')
GetAggregateResourceConfig = Action('GetAggregateResourceConfig')
GetComplianceDetailsByConfigRule = \
    Action('GetComplianceDetailsByConfigRule')
GetComplianceDetailsByResource = Action('GetComplianceDetailsByResource')
GetComplianceSummaryByConfigRule = \
    Action('GetComplianceSummaryByConfigRule')
GetComplianceSummaryByResourceType = \
    Action('GetComplianceSummaryByResourceType')
GetDiscoveredResourceCounts = Action('GetDiscoveredResourceCounts')
GetResourceConfigHistory = Action('GetResourceConfigHistory')
GetResources = Action('GetResources')
GetTagKeys = Action('GetTagKeys')
ListAggregateDiscoveredResources = \
    Action('ListAggregateDiscoveredResources')
ListDiscoveredResources = Action('ListDiscoveredResources')
PutAggregationAuthorization = Action('PutAggregationAuthorization')
PutConfigRule = Action('PutConfigRule')
PutConfigurationAggregator = Action('PutConfigurationAggregator')
PutConfigurationRecorder = Action('PutConfigurationRecorder')
PutDeliveryChannel = Action('PutDeliveryChannel')
PutEvaluations = Action('PutEvaluations')
PutRetentionConfiguration = Action('PutRetentionConfiguration')
StartConfigRulesEvaluation = Action('StartConfigRulesEvaluation')
StartConfigurationRecorder = Action('StartConfigurationRecorder')
StopConfigurationRecorder = Action('StopConfigurationRecorder')
