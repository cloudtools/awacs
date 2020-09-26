# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Cost Explorer Service'
prefix = 'ce'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAnomalyMonitor = Action('CreateAnomalyMonitor')
CreateAnomalySubscription = Action('CreateAnomalySubscription')
CreateCostCategoryDefinition = Action('CreateCostCategoryDefinition')
DeleteAnomalyMonitor = Action('DeleteAnomalyMonitor')
DeleteAnomalySubscription = Action('DeleteAnomalySubscription')
DeleteCostCategoryDefinition = Action('DeleteCostCategoryDefinition')
DescribeCostCategoryDefinition = Action('DescribeCostCategoryDefinition')
GetAnomalies = Action('GetAnomalies')
GetAnomalyMonitors = Action('GetAnomalyMonitors')
GetAnomalySubscriptions = Action('GetAnomalySubscriptions')
GetCostAndUsage = Action('GetCostAndUsage')
GetCostAndUsageWithResources = Action('GetCostAndUsageWithResources')
GetCostForecast = Action('GetCostForecast')
GetDimensionValues = Action('GetDimensionValues')
GetReservationCoverage = Action('GetReservationCoverage')
GetReservationPurchaseRecommendation = \
    Action('GetReservationPurchaseRecommendation')
GetReservationUtilization = Action('GetReservationUtilization')
GetRightsizingRecommendation = Action('GetRightsizingRecommendation')
GetSavingsPlansCoverage = Action('GetSavingsPlansCoverage')
GetSavingsPlansPurchaseRecommendation = \
    Action('GetSavingsPlansPurchaseRecommendation')
GetSavingsPlansUtilization = Action('GetSavingsPlansUtilization')
GetSavingsPlansUtilizationDetails = \
    Action('GetSavingsPlansUtilizationDetails')
GetTags = Action('GetTags')
GetUsageForecast = Action('GetUsageForecast')
ListCostCategoryDefinitions = Action('ListCostCategoryDefinitions')
ProvideAnomalyFeedback = Action('ProvideAnomalyFeedback')
UpdateAnomalyMonitor = Action('UpdateAnomalyMonitor')
UpdateAnomalySubscription = Action('UpdateAnomalySubscription')
UpdateCostCategoryDefinition = Action('UpdateCostCategoryDefinition')
