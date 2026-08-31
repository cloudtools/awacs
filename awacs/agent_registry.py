# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Agent Registry"
prefix = "agent-registry"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateRegistry = Action("CreateRegistry")
CreateRegistryRecord = Action("CreateRegistryRecord")
DeleteRegistry = Action("DeleteRegistry")
DeleteRegistryRecord = Action("DeleteRegistryRecord")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
GetDiscoverableRegistryRecord = Action("GetDiscoverableRegistryRecord")
GetRegistry = Action("GetRegistry")
GetRegistryRecord = Action("GetRegistryRecord")
GetResourcePolicy = Action("GetResourcePolicy")
InvokeRegistryMcp = Action("InvokeRegistryMcp")
ListDiscoverableRegistryRecords = Action("ListDiscoverableRegistryRecords")
ListRegistries = Action("ListRegistries")
ListRegistryRecords = Action("ListRegistryRecords")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
SearchDiscoverableRegistryRecords = Action("SearchDiscoverableRegistryRecords")
SubmitRegistryRecordForApproval = Action("SubmitRegistryRecordForApproval")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateRegistry = Action("UpdateRegistry")
UpdateRegistryRecord = Action("UpdateRegistryRecord")
UpdateRegistryRecordStatus = Action("UpdateRegistryRecordStatus")
