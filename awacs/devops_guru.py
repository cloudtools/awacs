# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon DevOps Guru"
prefix = "devops-guru"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddNotificationChannel = Action("AddNotificationChannel")
DeleteInsight = Action("DeleteInsight")
DescribeAccountHealth = Action("DescribeAccountHealth")
DescribeAccountOverview = Action("DescribeAccountOverview")
DescribeAnomaly = Action("DescribeAnomaly")
DescribeEventSourcesConfig = Action("DescribeEventSourcesConfig")
DescribeFeedback = Action("DescribeFeedback")
DescribeInsight = Action("DescribeInsight")
DescribeOrganizationHealth = Action("DescribeOrganizationHealth")
DescribeOrganizationOverview = Action("DescribeOrganizationOverview")
DescribeOrganizationResourceCollectionHealth = Action(
    "DescribeOrganizationResourceCollectionHealth"
)
DescribeResourceCollectionHealth = Action("DescribeResourceCollectionHealth")
DescribeServiceIntegration = Action("DescribeServiceIntegration")
GetCostEstimation = Action("GetCostEstimation")
GetResourceCollection = Action("GetResourceCollection")
ListAnomaliesForInsight = Action("ListAnomaliesForInsight")
ListAnomalousLogGroups = Action("ListAnomalousLogGroups")
ListEvents = Action("ListEvents")
ListInsights = Action("ListInsights")
ListMonitoredResources = Action("ListMonitoredResources")
ListNotificationChannels = Action("ListNotificationChannels")
ListOrganizationInsights = Action("ListOrganizationInsights")
ListRecommendations = Action("ListRecommendations")
PutFeedback = Action("PutFeedback")
RemoveNotificationChannel = Action("RemoveNotificationChannel")
SearchInsights = Action("SearchInsights")
SearchOrganizationInsights = Action("SearchOrganizationInsights")
StartCostEstimation = Action("StartCostEstimation")
UpdateEventSourcesConfig = Action("UpdateEventSourcesConfig")
UpdateResourceCollection = Action("UpdateResourceCollection")
UpdateServiceIntegration = Action("UpdateServiceIntegration")
