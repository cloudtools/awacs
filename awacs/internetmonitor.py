# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Internet Monitor"
prefix = "internetmonitor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateMonitor = Action("CreateMonitor")
DeleteMonitor = Action("DeleteMonitor")
GetHealthEvent = Action("GetHealthEvent")
GetInternetEvent = Action("GetInternetEvent")
GetMonitor = Action("GetMonitor")
GetQueryResults = Action("GetQueryResults")
GetQueryStatus = Action("GetQueryStatus")
Link = Action("Link")
ListHealthEvents = Action("ListHealthEvents")
ListInternetEvents = Action("ListInternetEvents")
ListMonitors = Action("ListMonitors")
ListTagsForResource = Action("ListTagsForResource")
StartQuery = Action("StartQuery")
StopQuery = Action("StopQuery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMonitor = Action("UpdateMonitor")
