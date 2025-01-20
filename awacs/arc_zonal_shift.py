# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Application Recovery Controller - Zonal Shift"
prefix = "arc-zonal-shift"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelZonalShift = Action("CancelZonalShift")
CreatePracticeRunConfiguration = Action("CreatePracticeRunConfiguration")
DeletePracticeRunConfiguration = Action("DeletePracticeRunConfiguration")
GetAutoshiftObserverNotificationStatus = Action(
    "GetAutoshiftObserverNotificationStatus"
)
GetManagedResource = Action("GetManagedResource")
ListAutoshifts = Action("ListAutoshifts")
ListManagedResources = Action("ListManagedResources")
ListZonalShifts = Action("ListZonalShifts")
StartZonalShift = Action("StartZonalShift")
UpdateAutoshiftObserverNotificationStatus = Action(
    "UpdateAutoshiftObserverNotificationStatus"
)
UpdatePracticeRunConfiguration = Action("UpdatePracticeRunConfiguration")
UpdateZonalAutoshiftConfiguration = Action("UpdateZonalAutoshiftConfiguration")
UpdateZonalShift = Action("UpdateZonalShift")
