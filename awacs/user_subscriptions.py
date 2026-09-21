# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS User Subscriptions"
prefix = "user-subscriptions"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelPurchaseSession = Action("CancelPurchaseSession")
ConfirmPurchaseSession = Action("ConfirmPurchaseSession")
CreateClaim = Action("CreateClaim")
CreateClaimAddOn = Action("CreateClaimAddOn")
CreatePurchaseSession = Action("CreatePurchaseSession")
CreateUpdatePlanPreview = Action("CreateUpdatePlanPreview")
DeleteAutoTopUpRule = Action("DeleteAutoTopUpRule")
DeleteClaim = Action("DeleteClaim")
GetAutoTopUpRule = Action("GetAutoTopUpRule")
GetCurrentPlanDetails = Action("GetCurrentPlanDetails")
GetEffectiveUsageLimit = Action("GetEffectiveUsageLimit")
GetPurchaseSession = Action("GetPurchaseSession")
GetUsageLimitHistory = Action("GetUsageLimitHistory")
ListApplicationClaims = Action("ListApplicationClaims")
ListClaimAddOns = Action("ListClaimAddOns")
ListClaims = Action("ListClaims")
ListEntitlements = Action("ListEntitlements")
ListUsageLimits = Action("ListUsageLimits")
ListUserSubscriptions = Action("ListUserSubscriptions")
SetAutoTopUpRule = Action("SetAutoTopUpRule")
SetOverageConfig = Action("SetOverageConfig")
SetUsageLimit = Action("SetUsageLimit")
UpdateClaim = Action("UpdateClaim")
