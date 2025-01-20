# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Directory Service Data"
prefix = "ds-data"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddGroupMember = Action("AddGroupMember")
CreateGroup = Action("CreateGroup")
CreateUser = Action("CreateUser")
DeleteGroup = Action("DeleteGroup")
DeleteUser = Action("DeleteUser")
DescribeGroup = Action("DescribeGroup")
DescribeUser = Action("DescribeUser")
DisableUser = Action("DisableUser")
ListGroupMembers = Action("ListGroupMembers")
ListGroups = Action("ListGroups")
ListGroupsForMember = Action("ListGroupsForMember")
ListUsers = Action("ListUsers")
RemoveGroupMember = Action("RemoveGroupMember")
SearchGroups = Action("SearchGroups")
SearchUsers = Action("SearchUsers")
UpdateGroup = Action("UpdateGroup")
UpdateUser = Action("UpdateUser")
