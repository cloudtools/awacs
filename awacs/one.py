# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon One Enterprise"
prefix = "one"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateDeviceActivationQrCode = Action("CreateDeviceActivationQrCode")
CreateDeviceConfigurationTemplate = Action("CreateDeviceConfigurationTemplate")
CreateDeviceInstance = Action("CreateDeviceInstance")
CreateDeviceInstanceConfiguration = Action("CreateDeviceInstanceConfiguration")
CreateSite = Action("CreateSite")
DeleteAssociatedDevice = Action("DeleteAssociatedDevice")
DeleteDeviceConfigurationTemplate = Action("DeleteDeviceConfigurationTemplate")
DeleteDeviceInstance = Action("DeleteDeviceInstance")
DeleteSite = Action("DeleteSite")
DeleteUser = Action("DeleteUser")
GetDeviceConfigurationTemplate = Action("GetDeviceConfigurationTemplate")
GetDeviceInstance = Action("GetDeviceInstance")
GetDeviceInstanceConfiguration = Action("GetDeviceInstanceConfiguration")
GetSite = Action("GetSite")
GetSiteAddress = Action("GetSiteAddress")
ListDeviceConfigurationTemplates = Action("ListDeviceConfigurationTemplates")
ListDeviceInstances = Action("ListDeviceInstances")
ListSites = Action("ListSites")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
RebootDevice = Action("RebootDevice")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDeviceConfigurationTemplate = Action("UpdateDeviceConfigurationTemplate")
UpdateDeviceInstance = Action("UpdateDeviceInstance")
UpdateSite = Action("UpdateSite")
UpdateSiteAddress = Action("UpdateSiteAddress")
