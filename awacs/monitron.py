# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Monitron"
prefix = "monitron"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateProjectAdminUser = Action("AssociateProjectAdminUser")
CreateProject = Action("CreateProject")
CreateProjectUserAssociation = Action("CreateProjectUserAssociation")
CreateUserAccessRoleAssociation = Action("CreateUserAccessRoleAssociation")
DeleteProject = Action("DeleteProject")
DeleteProjectUserAssociation = Action("DeleteProjectUserAssociation")
DeleteUserAccessRoleAssociation = Action("DeleteUserAccessRoleAssociation")
DisassociateProjectAdminUser = Action("DisassociateProjectAdminUser")
GetProject = Action("GetProject")
GetProjectAdminUser = Action("GetProjectAdminUser")
ListProjectAdminUsers = Action("ListProjectAdminUsers")
ListProjectUserAssociations = Action("ListProjectUserAssociations")
ListProjects = Action("ListProjects")
ListTagsForResource = Action("ListTagsForResource")
ListUserAccessRoleAssociations = Action("ListUserAccessRoleAssociations")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateProject = Action("UpdateProject")
