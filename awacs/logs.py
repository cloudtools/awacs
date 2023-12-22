# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Logs"
prefix = "logs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateKmsKey = Action("AssociateKmsKey")
CancelExportTask = Action("CancelExportTask")
CreateDelivery = Action("CreateDelivery")
CreateExportTask = Action("CreateExportTask")
CreateLogAnomalyDetector = Action("CreateLogAnomalyDetector")
CreateLogDelivery = Action("CreateLogDelivery")
CreateLogGroup = Action("CreateLogGroup")
CreateLogStream = Action("CreateLogStream")
DeleteAccountPolicy = Action("DeleteAccountPolicy")
DeleteDataProtectionPolicy = Action("DeleteDataProtectionPolicy")
DeleteDelivery = Action("DeleteDelivery")
DeleteDeliveryDestination = Action("DeleteDeliveryDestination")
DeleteDeliveryDestinationPolicy = Action("DeleteDeliveryDestinationPolicy")
DeleteDeliverySource = Action("DeleteDeliverySource")
DeleteDestination = Action("DeleteDestination")
DeleteLogAnomalyDetector = Action("DeleteLogAnomalyDetector")
DeleteLogDelivery = Action("DeleteLogDelivery")
DeleteLogGroup = Action("DeleteLogGroup")
DeleteLogStream = Action("DeleteLogStream")
DeleteMetricFilter = Action("DeleteMetricFilter")
DeleteQueryDefinition = Action("DeleteQueryDefinition")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRetentionPolicy = Action("DeleteRetentionPolicy")
DeleteSubscriptionFilter = Action("DeleteSubscriptionFilter")
DescribeAccountPolicies = Action("DescribeAccountPolicies")
DescribeDeliveries = Action("DescribeDeliveries")
DescribeDeliveryDestinations = Action("DescribeDeliveryDestinations")
DescribeDeliverySources = Action("DescribeDeliverySources")
DescribeDestinations = Action("DescribeDestinations")
DescribeExportTasks = Action("DescribeExportTasks")
DescribeLogGroups = Action("DescribeLogGroups")
DescribeLogStreams = Action("DescribeLogStreams")
DescribeMetricFilters = Action("DescribeMetricFilters")
DescribeQueries = Action("DescribeQueries")
DescribeQueryDefinitions = Action("DescribeQueryDefinitions")
DescribeResourcePolicies = Action("DescribeResourcePolicies")
DescribeSubscriptionFilters = Action("DescribeSubscriptionFilters")
DisassociateKmsKey = Action("DisassociateKmsKey")
FilterLogEvents = Action("FilterLogEvents")
GetDataProtectionPolicy = Action("GetDataProtectionPolicy")
GetDelivery = Action("GetDelivery")
GetDeliveryDestination = Action("GetDeliveryDestination")
GetDeliveryDestinationPolicy = Action("GetDeliveryDestinationPolicy")
GetDeliverySource = Action("GetDeliverySource")
GetLogAnomalyDetector = Action("GetLogAnomalyDetector")
GetLogDelivery = Action("GetLogDelivery")
GetLogEvents = Action("GetLogEvents")
GetLogGroupFields = Action("GetLogGroupFields")
GetLogRecord = Action("GetLogRecord")
GetQueryResults = Action("GetQueryResults")
Link = Action("Link")
ListAnomalies = Action("ListAnomalies")
ListLogAnomalyDetectors = Action("ListLogAnomalyDetectors")
ListLogDeliveries = Action("ListLogDeliveries")
ListTagsForResource = Action("ListTagsForResource")
ListTagsLogGroup = Action("ListTagsLogGroup")
PutAccountPolicy = Action("PutAccountPolicy")
PutDataProtectionPolicy = Action("PutDataProtectionPolicy")
PutDeliveryDestination = Action("PutDeliveryDestination")
PutDeliveryDestinationPolicy = Action("PutDeliveryDestinationPolicy")
PutDeliverySource = Action("PutDeliverySource")
PutDestination = Action("PutDestination")
PutDestinationPolicy = Action("PutDestinationPolicy")
PutLogEvents = Action("PutLogEvents")
PutMetricFilter = Action("PutMetricFilter")
PutQueryDefinition = Action("PutQueryDefinition")
PutResourcePolicy = Action("PutResourcePolicy")
PutRetentionPolicy = Action("PutRetentionPolicy")
PutSubscriptionFilter = Action("PutSubscriptionFilter")
StartLiveTail = Action("StartLiveTail")
StartQuery = Action("StartQuery")
StopLiveTail = Action("StopLiveTail")
StopQuery = Action("StopQuery")
TagLogGroup = Action("TagLogGroup")
TagResource = Action("TagResource")
TestMetricFilter = Action("TestMetricFilter")
Unmask = Action("Unmask")
UntagLogGroup = Action("UntagLogGroup")
UntagResource = Action("UntagResource")
UpdateAnomaly = Action("UpdateAnomaly")
UpdateLogAnomalyDetector = Action("UpdateLogAnomalyDetector")
UpdateLogDelivery = Action("UpdateLogDelivery")
