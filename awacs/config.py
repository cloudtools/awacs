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
DeleteConformancePack = Action('DeleteConformancePack')
DeleteDeliveryChannel = Action('DeleteDeliveryChannel')
DeleteEvaluationResults = Action('DeleteEvaluationResults')
DeleteOrganizationConfigRule = Action('DeleteOrganizationConfigRule')
DeleteOrganizationConformancePack = \
    Action('DeleteOrganizationConformancePack')
DeletePendingAggregationRequest = \
    Action('DeletePendingAggregationRequest')
DeleteRemediationConfiguration = Action('DeleteRemediationConfiguration')
DeleteRemediationExceptions = Action('DeleteRemediationExceptions')
DeleteResourceConfig = Action('DeleteResourceConfig')
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
DescribeConformancePackCompliance = \
    Action('DescribeConformancePackCompliance')
DescribeConformancePackStatus = Action('DescribeConformancePackStatus')
DescribeConformancePacks = Action('DescribeConformancePacks')
DescribeDeliveryChannelStatus = Action('DescribeDeliveryChannelStatus')
DescribeDeliveryChannels = Action('DescribeDeliveryChannels')
DescribeOrganizationConfigRuleStatuses = \
    Action('DescribeOrganizationConfigRuleStatuses')
DescribeOrganizationConfigRules = \
    Action('DescribeOrganizationConfigRules')
DescribeOrganizationConformancePackStatuses = \
    Action('DescribeOrganizationConformancePackStatuses')
DescribeOrganizationConformancePacks = \
    Action('DescribeOrganizationConformancePacks')
DescribePendingAggregationRequests = \
    Action('DescribePendingAggregationRequests')
DescribeRemediationConfigurations = \
    Action('DescribeRemediationConfigurations')
DescribeRemediationExceptions = Action('DescribeRemediationExceptions')
DescribeRemediationExecutionStatus = \
    Action('DescribeRemediationExecutionStatus')
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
GetConformancePackComplianceDetails = \
    Action('GetConformancePackComplianceDetails')
GetConformancePackComplianceSummary = \
    Action('GetConformancePackComplianceSummary')
GetDiscoveredResourceCounts = Action('GetDiscoveredResourceCounts')
GetOrganizationConfigRuleDetailedStatus = \
    Action('GetOrganizationConfigRuleDetailedStatus')
GetOrganizationConformancePackDetailedStatus = \
    Action('GetOrganizationConformancePackDetailedStatus')
GetResourceConfigHistory = Action('GetResourceConfigHistory')
GetResources = Action('GetResources')
GetTagKeys = Action('GetTagKeys')
ListAggregateDiscoveredResources = \
    Action('ListAggregateDiscoveredResources')
ListDiscoveredResources = Action('ListDiscoveredResources')
ListTagsForResource = Action('ListTagsForResource')
PutAggregationAuthorization = Action('PutAggregationAuthorization')
PutConfigRule = Action('PutConfigRule')
PutConfigurationAggregator = Action('PutConfigurationAggregator')
PutConfigurationRecorder = Action('PutConfigurationRecorder')
PutConformancePack = Action('PutConformancePack')
PutDeliveryChannel = Action('PutDeliveryChannel')
PutEvaluations = Action('PutEvaluations')
PutOrganizationConfigRule = Action('PutOrganizationConfigRule')
PutOrganizationConformancePack = Action('PutOrganizationConformancePack')
PutRemediationConfigurations = Action('PutRemediationConfigurations')
PutRemediationExceptions = Action('PutRemediationExceptions')
PutResourceConfig = Action('PutResourceConfig')
PutRetentionConfiguration = Action('PutRetentionConfiguration')
SelectAggregateResourceConfig = Action('SelectAggregateResourceConfig')
SelectResourceConfig = Action('SelectResourceConfig')
StartConfigRulesEvaluation = Action('StartConfigRulesEvaluation')
StartConfigurationRecorder = Action('StartConfigurationRecorder')
StartRemediationExecution = Action('StartRemediationExecution')
StopConfigurationRecorder = Action('StopConfigurationRecorder')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
