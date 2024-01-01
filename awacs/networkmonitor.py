# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Network Monitor"
prefix = "networkmonitor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateMonitor = Action("CreateMonitor")
CreateProbe = Action("CreateProbe")
DeleteMonitor = Action("DeleteMonitor")
DeleteProbe = Action("DeleteProbe")
GetMonitor = Action("GetMonitor")
GetProbe = Action("GetProbe")
ListMonitors = Action("ListMonitors")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMonitor = Action("UpdateMonitor")
UpdateProbe = Action("UpdateProbe")
