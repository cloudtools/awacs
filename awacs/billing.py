# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Billing"
prefix = "billing"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBillingView = Action("CreateBillingView")
DeleteBillingView = Action("DeleteBillingView")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
GetBillingData = Action("GetBillingData")
GetBillingDetails = Action("GetBillingDetails")
GetBillingNotifications = Action("GetBillingNotifications")
GetBillingPreferences = Action("GetBillingPreferences")
GetBillingView = Action("GetBillingView")
GetContractInformation = Action("GetContractInformation")
GetCredits = Action("GetCredits")
GetIAMAccessPreference = Action("GetIAMAccessPreference")
GetResourcePolicy = Action("GetResourcePolicy")
GetSellerOfRecord = Action("GetSellerOfRecord")
ListBillingViews = Action("ListBillingViews")
ListSourceViewsForBillingView = Action("ListSourceViewsForBillingView")
ListTagsForResource = Action("ListTagsForResource")
PutContractInformation = Action("PutContractInformation")
PutResourcePolicy = Action("PutResourcePolicy")
RedeemCredits = Action("RedeemCredits")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBillingPreferences = Action("UpdateBillingPreferences")
UpdateBillingView = Action("UpdateBillingView")
UpdateIAMAccessPreference = Action("UpdateIAMAccessPreference")
