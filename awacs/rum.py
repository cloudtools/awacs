# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudWatch RUM"
prefix = "rum"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreateRumMetricDefinitions = Action("BatchCreateRumMetricDefinitions")
BatchDeleteRumMetricDefinitions = Action("BatchDeleteRumMetricDefinitions")
BatchGetRumMetricDefinitions = Action("BatchGetRumMetricDefinitions")
CreateAppMonitor = Action("CreateAppMonitor")
DeleteAppMonitor = Action("DeleteAppMonitor")
DeleteRumMetricsDestination = Action("DeleteRumMetricsDestination")
GetAppMonitor = Action("GetAppMonitor")
GetAppMonitorData = Action("GetAppMonitorData")
ListAppMonitors = Action("ListAppMonitors")
ListRumMetricsDestinations = Action("ListRumMetricsDestinations")
ListTagsForResource = Action("ListTagsForResource")
PutRumEvents = Action("PutRumEvents")
PutRumMetricsDestination = Action("PutRumMetricsDestination")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAppMonitor = Action("UpdateAppMonitor")
UpdateRumMetricDefinition = Action("UpdateRumMetricDefinition")
