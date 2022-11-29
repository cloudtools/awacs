# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Lookout for Metrics"
prefix = "lookoutmetrics"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateAnomalyDetector = Action("ActivateAnomalyDetector")
BackTestAnomalyDetector = Action("BackTestAnomalyDetector")
CreateAlert = Action("CreateAlert")
CreateAnomalyDetector = Action("CreateAnomalyDetector")
CreateMetricSet = Action("CreateMetricSet")
DeactivateAnomalyDetector = Action("DeactivateAnomalyDetector")
DeleteAlert = Action("DeleteAlert")
DeleteAnomalyDetector = Action("DeleteAnomalyDetector")
DescribeAlert = Action("DescribeAlert")
DescribeAnomalyDetectionExecutions = Action("DescribeAnomalyDetectionExecutions")
DescribeAnomalyDetector = Action("DescribeAnomalyDetector")
DescribeMetricSet = Action("DescribeMetricSet")
DetectMetricSetConfig = Action("DetectMetricSetConfig")
GetAnomalyGroup = Action("GetAnomalyGroup")
GetDataQualityMetrics = Action("GetDataQualityMetrics")
GetFeedback = Action("GetFeedback")
GetSampleData = Action("GetSampleData")
ListAlerts = Action("ListAlerts")
ListAnomalyDetectors = Action("ListAnomalyDetectors")
ListAnomalyGroupRelatedMetrics = Action("ListAnomalyGroupRelatedMetrics")
ListAnomalyGroupSummaries = Action("ListAnomalyGroupSummaries")
ListAnomalyGroupTimeSeries = Action("ListAnomalyGroupTimeSeries")
ListMetricSets = Action("ListMetricSets")
ListTagsForResource = Action("ListTagsForResource")
PutFeedback = Action("PutFeedback")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAlert = Action("UpdateAlert")
UpdateAnomalyDetector = Action("UpdateAnomalyDetector")
UpdateMetricSet = Action("UpdateMetricSet")
