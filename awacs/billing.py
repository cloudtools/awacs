# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Billing and Cost Management"
prefix = "billing"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


GetBillingData = Action("GetBillingData")
GetBillingDetails = Action("GetBillingDetails")
GetBillingNotifications = Action("GetBillingNotifications")
GetBillingPreferences = Action("GetBillingPreferences")
GetContractInformation = Action("GetContractInformation")
GetCredits = Action("GetCredits")
GetIAMAccessPreference = Action("GetIAMAccessPreference")
GetSellerOfRecord = Action("GetSellerOfRecord")
ListBillingViews = Action("ListBillingViews")
PutContractInformation = Action("PutContractInformation")
RedeemCredits = Action("RedeemCredits")
UpdateBillingPreferences = Action("UpdateBillingPreferences")
UpdateIAMAccessPreference = Action("UpdateIAMAccessPreference")
