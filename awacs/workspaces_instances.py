# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS WorkSpaces Managed Instances"
prefix = "workspaces-instances"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateVolume = Action("AssociateVolume")
CreateVolume = Action("CreateVolume")
CreateWorkspaceInstance = Action("CreateWorkspaceInstance")
DeleteVolume = Action("DeleteVolume")
DeleteWorkspaceInstance = Action("DeleteWorkspaceInstance")
DisassociateVolume = Action("DisassociateVolume")
GetWorkspaceInstance = Action("GetWorkspaceInstance")
ListInstanceTypes = Action("ListInstanceTypes")
ListRegions = Action("ListRegions")
ListTagsForResource = Action("ListTagsForResource")
ListWorkspaceInstances = Action("ListWorkspaceInstances")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
