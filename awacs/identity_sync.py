# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Identity Sync"
prefix = "identity-sync"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
CreateSyncFilter = Action("CreateSyncFilter")
CreateSyncProfile = Action("CreateSyncProfile")
CreateSyncTarget = Action("CreateSyncTarget")
DeleteSyncFilter = Action("DeleteSyncFilter")
DeleteSyncProfile = Action("DeleteSyncProfile")
DeleteSyncTarget = Action("DeleteSyncTarget")
GetSyncProfile = Action("GetSyncProfile")
GetSyncTarget = Action("GetSyncTarget")
ListSyncFilters = Action("ListSyncFilters")
StartSync = Action("StartSync")
StopSync = Action("StopSync")
UpdateSyncTarget = Action("UpdateSyncTarget")
