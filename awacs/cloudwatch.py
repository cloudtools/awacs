# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch"
prefix = "cloudwatch"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetServiceLevelIndicatorReport = Action("BatchGetServiceLevelIndicatorReport")
BatchGetServiceLevelObjectiveBudgetReport = Action(
    "BatchGetServiceLevelObjectiveBudgetReport"
)
CreateServiceLevelObjective = Action("CreateServiceLevelObjective")
DeleteAlarms = Action("DeleteAlarms")
DeleteAnomalyDetector = Action("DeleteAnomalyDetector")
DeleteDashboards = Action("DeleteDashboards")
DeleteInsightRules = Action("DeleteInsightRules")
DeleteMetricStream = Action("DeleteMetricStream")
DeleteServiceLevelObjective = Action("DeleteServiceLevelObjective")
DescribeAlarmHistory = Action("DescribeAlarmHistory")
DescribeAlarms = Action("DescribeAlarms")
DescribeAlarmsForMetric = Action("DescribeAlarmsForMetric")
DescribeAnomalyDetectors = Action("DescribeAnomalyDetectors")
DescribeInsightRules = Action("DescribeInsightRules")
DisableAlarmActions = Action("DisableAlarmActions")
DisableInsightRules = Action("DisableInsightRules")
EnableAlarmActions = Action("EnableAlarmActions")
EnableInsightRules = Action("EnableInsightRules")
EnableTopologyDiscovery = Action("EnableTopologyDiscovery")
GenerateQuery = Action("GenerateQuery")
GetDashboard = Action("GetDashboard")
GetInsightRuleReport = Action("GetInsightRuleReport")
GetMetricData = Action("GetMetricData")
GetMetricStatistics = Action("GetMetricStatistics")
GetMetricStream = Action("GetMetricStream")
GetMetricWidgetImage = Action("GetMetricWidgetImage")
GetService = Action("GetService")
GetServiceData = Action("GetServiceData")
GetServiceLevelObjective = Action("GetServiceLevelObjective")
GetTopologyDiscoveryStatus = Action("GetTopologyDiscoveryStatus")
GetTopologyMap = Action("GetTopologyMap")
Link = Action("Link")
ListDashboards = Action("ListDashboards")
ListEntitiesForMetric = Action("ListEntitiesForMetric")
ListManagedInsightRules = Action("ListManagedInsightRules")
ListMetricStreams = Action("ListMetricStreams")
ListMetrics = Action("ListMetrics")
ListServiceLevelObjectives = Action("ListServiceLevelObjectives")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
PutAnomalyDetector = Action("PutAnomalyDetector")
PutCompositeAlarm = Action("PutCompositeAlarm")
PutDashboard = Action("PutDashboard")
PutInsightRule = Action("PutInsightRule")
PutManagedInsightRules = Action("PutManagedInsightRules")
PutMetricAlarm = Action("PutMetricAlarm")
PutMetricData = Action("PutMetricData")
PutMetricStream = Action("PutMetricStream")
SetAlarmState = Action("SetAlarmState")
StartMetricStreams = Action("StartMetricStreams")
StopMetricStreams = Action("StopMetricStreams")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateServiceLevelObjective = Action("UpdateServiceLevelObjective")
