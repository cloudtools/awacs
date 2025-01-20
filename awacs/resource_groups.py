# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Resource Groups"
prefix = "resource-groups"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateResource = Action("AssociateResource")
CancelTagSyncTask = Action("CancelTagSyncTask")
CreateGroup = Action("CreateGroup")
DeleteGroup = Action("DeleteGroup")
DeleteGroupPolicy = Action("DeleteGroupPolicy")
DisassociateResource = Action("DisassociateResource")
GetAccountSettings = Action("GetAccountSettings")
GetGroup = Action("GetGroup")
GetGroupConfiguration = Action("GetGroupConfiguration")
GetGroupPolicy = Action("GetGroupPolicy")
GetGroupQuery = Action("GetGroupQuery")
GetTagSyncTask = Action("GetTagSyncTask")
GetTags = Action("GetTags")
GroupResources = Action("GroupResources")
ListGroupResources = Action("ListGroupResources")
ListGroupingStatuses = Action("ListGroupingStatuses")
ListGroups = Action("ListGroups")
ListResourceTypes = Action("ListResourceTypes")
ListTagSyncTasks = Action("ListTagSyncTasks")
PutGroupConfiguration = Action("PutGroupConfiguration")
PutGroupPolicy = Action("PutGroupPolicy")
SearchResources = Action("SearchResources")
StartTagSyncTask = Action("StartTagSyncTask")
Tag = Action("Tag")
UngroupResources = Action("UngroupResources")
Untag = Action("Untag")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateGroup = Action("UpdateGroup")
UpdateGroupQuery = Action("UpdateGroupQuery")
