# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Cost Explorer Service"
prefix = "ce"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAnomalyMonitor = Action("CreateAnomalyMonitor")
CreateAnomalySubscription = Action("CreateAnomalySubscription")
CreateCostCategoryDefinition = Action("CreateCostCategoryDefinition")
CreateNotificationSubscription = Action("CreateNotificationSubscription")
CreateReport = Action("CreateReport")
DeleteAnomalyMonitor = Action("DeleteAnomalyMonitor")
DeleteAnomalySubscription = Action("DeleteAnomalySubscription")
DeleteCostCategoryDefinition = Action("DeleteCostCategoryDefinition")
DeleteNotificationSubscription = Action("DeleteNotificationSubscription")
DeleteReport = Action("DeleteReport")
DescribeCostCategoryDefinition = Action("DescribeCostCategoryDefinition")
DescribeNotificationSubscription = Action("DescribeNotificationSubscription")
DescribeReport = Action("DescribeReport")
GetAnomalies = Action("GetAnomalies")
GetAnomalyMonitors = Action("GetAnomalyMonitors")
GetAnomalySubscriptions = Action("GetAnomalySubscriptions")
GetApproximateUsageRecords = Action("GetApproximateUsageRecords")
GetCommitmentPurchaseAnalysis = Action("GetCommitmentPurchaseAnalysis")
GetConsoleActionSetEnforced = Action("GetConsoleActionSetEnforced")
GetCostAndUsage = Action("GetCostAndUsage")
GetCostAndUsageWithResources = Action("GetCostAndUsageWithResources")
GetCostCategories = Action("GetCostCategories")
GetCostForecast = Action("GetCostForecast")
GetDimensionValues = Action("GetDimensionValues")
GetPreferences = Action("GetPreferences")
GetReservationCoverage = Action("GetReservationCoverage")
GetReservationPurchaseRecommendation = Action("GetReservationPurchaseRecommendation")
GetReservationUtilization = Action("GetReservationUtilization")
GetRightsizingRecommendation = Action("GetRightsizingRecommendation")
GetSavingsPlanPurchaseRecommendationDetails = Action(
    "GetSavingsPlanPurchaseRecommendationDetails"
)
GetSavingsPlansCoverage = Action("GetSavingsPlansCoverage")
GetSavingsPlansPurchaseRecommendation = Action("GetSavingsPlansPurchaseRecommendation")
GetSavingsPlansUtilization = Action("GetSavingsPlansUtilization")
GetSavingsPlansUtilizationDetails = Action("GetSavingsPlansUtilizationDetails")
GetTags = Action("GetTags")
GetUsageForecast = Action("GetUsageForecast")
ListCommitmentPurchaseAnalyses = Action("ListCommitmentPurchaseAnalyses")
ListCostAllocationTagBackfillHistory = Action("ListCostAllocationTagBackfillHistory")
ListCostAllocationTags = Action("ListCostAllocationTags")
ListCostCategoryDefinitions = Action("ListCostCategoryDefinitions")
ListSavingsPlansPurchaseRecommendationGeneration = Action(
    "ListSavingsPlansPurchaseRecommendationGeneration"
)
ListTagsForResource = Action("ListTagsForResource")
ProvideAnomalyFeedback = Action("ProvideAnomalyFeedback")
StartCommitmentPurchaseAnalysis = Action("StartCommitmentPurchaseAnalysis")
StartCostAllocationTagBackfill = Action("StartCostAllocationTagBackfill")
StartSavingsPlansPurchaseRecommendationGeneration = Action(
    "StartSavingsPlansPurchaseRecommendationGeneration"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAnomalyMonitor = Action("UpdateAnomalyMonitor")
UpdateAnomalySubscription = Action("UpdateAnomalySubscription")
UpdateConsoleActionSetEnforced = Action("UpdateConsoleActionSetEnforced")
UpdateCostAllocationTagsStatus = Action("UpdateCostAllocationTagsStatus")
UpdateCostCategoryDefinition = Action("UpdateCostCategoryDefinition")
UpdateNotificationSubscription = Action("UpdateNotificationSubscription")
UpdatePreferences = Action("UpdatePreferences")
UpdateReport = Action("UpdateReport")
