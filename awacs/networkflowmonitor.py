# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Network Flow Monitor"
prefix = "networkflowmonitor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateMonitor = Action("CreateMonitor")
CreateScope = Action("CreateScope")
DeleteMonitor = Action("DeleteMonitor")
DeleteScope = Action("DeleteScope")
GetMonitor = Action("GetMonitor")
GetQueryResultsMonitorTopContributors = Action("GetQueryResultsMonitorTopContributors")
GetQueryResultsWorkloadInsightsTopContributors = Action(
    "GetQueryResultsWorkloadInsightsTopContributors"
)
GetQueryResultsWorkloadInsightsTopContributorsData = Action(
    "GetQueryResultsWorkloadInsightsTopContributorsData"
)
GetQueryStatusMonitorTopContributors = Action("GetQueryStatusMonitorTopContributors")
GetQueryStatusWorkloadInsightsTopContributors = Action(
    "GetQueryStatusWorkloadInsightsTopContributors"
)
GetQueryStatusWorkloadInsightsTopContributorsData = Action(
    "GetQueryStatusWorkloadInsightsTopContributorsData"
)
GetScope = Action("GetScope")
ListMonitors = Action("ListMonitors")
ListScopes = Action("ListScopes")
ListTagsForResource = Action("ListTagsForResource")
Publish = Action("Publish")
StartQueryMonitorTopContributors = Action("StartQueryMonitorTopContributors")
StartQueryWorkloadInsightsTopContributors = Action(
    "StartQueryWorkloadInsightsTopContributors"
)
StartQueryWorkloadInsightsTopContributorsData = Action(
    "StartQueryWorkloadInsightsTopContributorsData"
)
StopQueryMonitorTopContributors = Action("StopQueryMonitorTopContributors")
StopQueryWorkloadInsightsTopContributors = Action(
    "StopQueryWorkloadInsightsTopContributors"
)
StopQueryWorkloadInsightsTopContributorsData = Action(
    "StopQueryWorkloadInsightsTopContributorsData"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMonitor = Action("UpdateMonitor")
UpdateScope = Action("UpdateScope")
