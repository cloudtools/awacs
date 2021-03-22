# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch"
prefix = "cloudwatch"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DeleteAlarms = Action("DeleteAlarms")
DeleteAnomalyDetector = Action("DeleteAnomalyDetector")
DeleteDashboards = Action("DeleteDashboards")
DeleteInsightRules = Action("DeleteInsightRules")
DescribeAlarmHistory = Action("DescribeAlarmHistory")
DescribeAlarms = Action("DescribeAlarms")
DescribeAlarmsForMetric = Action("DescribeAlarmsForMetric")
DescribeAnomalyDetectors = Action("DescribeAnomalyDetectors")
DescribeInsightRules = Action("DescribeInsightRules")
DisableAlarmActions = Action("DisableAlarmActions")
DisableInsightRules = Action("DisableInsightRules")
EnableAlarmActions = Action("EnableAlarmActions")
EnableInsightRules = Action("EnableInsightRules")
GetDashboard = Action("GetDashboard")
GetInsightRuleReport = Action("GetInsightRuleReport")
GetMetricData = Action("GetMetricData")
GetMetricStatistics = Action("GetMetricStatistics")
GetMetricWidgetImage = Action("GetMetricWidgetImage")
ListDashboards = Action("ListDashboards")
ListMetrics = Action("ListMetrics")
ListTagsForResource = Action("ListTagsForResource")
PutAnomalyDetector = Action("PutAnomalyDetector")
PutCompositeAlarm = Action("PutCompositeAlarm")
PutDashboard = Action("PutDashboard")
PutInsightRule = Action("PutInsightRule")
PutMetricAlarm = Action("PutMetricAlarm")
PutMetricData = Action("PutMetricData")
SetAlarmState = Action("SetAlarmState")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
