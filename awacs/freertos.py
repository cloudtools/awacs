# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FreeRTOS"
prefix = "freertos"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateSoftwareConfiguration = Action("CreateSoftwareConfiguration")
CreateSubscription = Action("CreateSubscription")
DeleteSoftwareConfiguration = Action("DeleteSoftwareConfiguration")
DescribeHardwarePlatform = Action("DescribeHardwarePlatform")
DescribeSoftwareConfiguration = Action("DescribeSoftwareConfiguration")
DescribeSubscription = Action("DescribeSubscription")
GetEmpPatchUrl = Action("GetEmpPatchUrl")
GetSoftwareURL = Action("GetSoftwareURL")
GetSoftwareURLForConfiguration = Action("GetSoftwareURLForConfiguration")
GetSubscriptionBillingAmount = Action("GetSubscriptionBillingAmount")
ListFreeRTOSVersions = Action("ListFreeRTOSVersions")
ListHardwarePlatforms = Action("ListHardwarePlatforms")
ListHardwareVendors = Action("ListHardwareVendors")
ListSoftwareConfigurations = Action("ListSoftwareConfigurations")
ListSoftwarePatches = Action("ListSoftwarePatches")
ListSubscriptionEmails = Action("ListSubscriptionEmails")
ListSubscriptions = Action("ListSubscriptions")
UpdateEmailRecipients = Action("UpdateEmailRecipients")
UpdateSoftwareConfiguration = Action("UpdateSoftwareConfiguration")
VerifyEmail = Action("VerifyEmail")
