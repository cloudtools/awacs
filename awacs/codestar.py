# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CodeStar"
prefix = "codestar"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateTeamMember = Action("AssociateTeamMember")
CreateProject = Action("CreateProject")
CreateUserProfile = Action("CreateUserProfile")
DeleteExtendedAccess = Action("DeleteExtendedAccess")
DeleteProject = Action("DeleteProject")
DeleteUserProfile = Action("DeleteUserProfile")
DescribeProject = Action("DescribeProject")
DescribeUserProfile = Action("DescribeUserProfile")
DisassociateTeamMember = Action("DisassociateTeamMember")
GetExtendedAccess = Action("GetExtendedAccess")
ListProjects = Action("ListProjects")
ListResources = Action("ListResources")
ListTagsForProject = Action("ListTagsForProject")
ListTeamMembers = Action("ListTeamMembers")
ListUserProfiles = Action("ListUserProfiles")
PutExtendedAccess = Action("PutExtendedAccess")
TagProject = Action("TagProject")
UntagProject = Action("UntagProject")
UpdateProject = Action("UpdateProject")
UpdateTeamMember = Action("UpdateTeamMember")
UpdateUserProfile = Action("UpdateUserProfile")
VerifyServiceRole = Action("VerifyServiceRole")
