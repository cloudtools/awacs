# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkSpaces Thin Client"
prefix = "thinclient"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateEnvironment = Action("CreateEnvironment")
DeleteDevice = Action("DeleteDevice")
DeleteEnvironment = Action("DeleteEnvironment")
DeregisterDevice = Action("DeregisterDevice")
GetDevice = Action("GetDevice")
GetDeviceDetails = Action("GetDeviceDetails")
GetEnvironment = Action("GetEnvironment")
GetSoftwareSet = Action("GetSoftwareSet")
ListDeviceSessions = Action("ListDeviceSessions")
ListDevices = Action("ListDevices")
ListEnvironments = Action("ListEnvironments")
ListSoftwareSets = Action("ListSoftwareSets")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDevice = Action("UpdateDevice")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateSoftwareSet = Action("UpdateSoftwareSet")
