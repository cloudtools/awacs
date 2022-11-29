# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Identity Store"
prefix = "identitystore"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateGroup = Action("CreateGroup")
CreateGroupMembership = Action("CreateGroupMembership")
CreateUser = Action("CreateUser")
DeleteGroup = Action("DeleteGroup")
DeleteGroupMembership = Action("DeleteGroupMembership")
DeleteUser = Action("DeleteUser")
DescribeGroup = Action("DescribeGroup")
DescribeGroupMembership = Action("DescribeGroupMembership")
DescribeUser = Action("DescribeUser")
GetGroupId = Action("GetGroupId")
GetGroupMembershipId = Action("GetGroupMembershipId")
GetUserId = Action("GetUserId")
IsMemberInGroups = Action("IsMemberInGroups")
ListGroupMemberships = Action("ListGroupMemberships")
ListGroupMembershipsForMember = Action("ListGroupMembershipsForMember")
ListGroups = Action("ListGroups")
ListUsers = Action("ListUsers")
UpdateGroup = Action("UpdateGroup")
UpdateUser = Action("UpdateUser")
