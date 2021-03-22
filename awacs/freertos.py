# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FreeRTOS"
prefix = "freertos"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateSoftwareConfiguration = Action("CreateSoftwareConfiguration")
DeleteSoftwareConfiguration = Action("DeleteSoftwareConfiguration")
DescribeHardwarePlatform = Action("DescribeHardwarePlatform")
DescribeSoftwareConfiguration = Action("DescribeSoftwareConfiguration")
GetSoftwareURL = Action("GetSoftwareURL")
GetSoftwareURLForConfiguration = Action("GetSoftwareURLForConfiguration")
ListFreeRTOSVersions = Action("ListFreeRTOSVersions")
ListHardwarePlatforms = Action("ListHardwarePlatforms")
ListHardwareVendors = Action("ListHardwareVendors")
ListSoftwareConfigurations = Action("ListSoftwareConfigurations")
UpdateSoftwareConfiguration = Action("UpdateSoftwareConfiguration")
