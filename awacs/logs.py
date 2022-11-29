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
CreateExportTask = Action("CreateExportTask")
CreateLogDelivery = Action("CreateLogDelivery")
CreateLogGroup = Action("CreateLogGroup")
CreateLogStream = Action("CreateLogStream")
DeleteDataProtectionPolicy = Action("DeleteDataProtectionPolicy")
DeleteDestination = Action("DeleteDestination")
DeleteLogDelivery = Action("DeleteLogDelivery")
DeleteLogGroup = Action("DeleteLogGroup")
DeleteLogStream = Action("DeleteLogStream")
DeleteMetricFilter = Action("DeleteMetricFilter")
DeleteQueryDefinition = Action("DeleteQueryDefinition")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRetentionPolicy = Action("DeleteRetentionPolicy")
DeleteSubscriptionFilter = Action("DeleteSubscriptionFilter")
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
GetLogDelivery = Action("GetLogDelivery")
GetLogEvents = Action("GetLogEvents")
GetLogGroupFields = Action("GetLogGroupFields")
GetLogRecord = Action("GetLogRecord")
GetQueryResults = Action("GetQueryResults")
Link = Action("Link")
ListLogDeliveries = Action("ListLogDeliveries")
ListTagsForResource = Action("ListTagsForResource")
ListTagsLogGroup = Action("ListTagsLogGroup")
PutDataProtectionPolicy = Action("PutDataProtectionPolicy")
PutDestination = Action("PutDestination")
PutDestinationPolicy = Action("PutDestinationPolicy")
PutLogEvents = Action("PutLogEvents")
PutMetricFilter = Action("PutMetricFilter")
PutQueryDefinition = Action("PutQueryDefinition")
PutResourcePolicy = Action("PutResourcePolicy")
PutRetentionPolicy = Action("PutRetentionPolicy")
PutSubscriptionFilter = Action("PutSubscriptionFilter")
StartQuery = Action("StartQuery")
StopQuery = Action("StopQuery")
TagLogGroup = Action("TagLogGroup")
TagResource = Action("TagResource")
TestMetricFilter = Action("TestMetricFilter")
Unmask = Action("Unmask")
UntagLogGroup = Action("UntagLogGroup")
UntagResource = Action("UntagResource")
UpdateLogDelivery = Action("UpdateLogDelivery")
