# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon DevOps Guru"
prefix = "devops-guru"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddNotificationChannel = Action("AddNotificationChannel")
DescribeAccountHealth = Action("DescribeAccountHealth")
DescribeAccountOverview = Action("DescribeAccountOverview")
DescribeAnomaly = Action("DescribeAnomaly")
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
ListEvents = Action("ListEvents")
ListInsights = Action("ListInsights")
ListNotificationChannels = Action("ListNotificationChannels")
ListOrganizationInsights = Action("ListOrganizationInsights")
ListRecommendations = Action("ListRecommendations")
PutFeedback = Action("PutFeedback")
RemoveNotificationChannel = Action("RemoveNotificationChannel")
SearchInsights = Action("SearchInsights")
SearchOrganizationInsights = Action("SearchOrganizationInsights")
StartCostEstimation = Action("StartCostEstimation")
UpdateResourceCollection = Action("UpdateResourceCollection")
UpdateServiceIntegration = Action("UpdateServiceIntegration")
