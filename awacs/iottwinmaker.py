# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT TwinMaker"
prefix = "iottwinmaker"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchPutPropertyValues = Action("BatchPutPropertyValues")
CreateComponentType = Action("CreateComponentType")
CreateEntity = Action("CreateEntity")
CreateScene = Action("CreateScene")
CreateWorkspace = Action("CreateWorkspace")
DeleteComponentType = Action("DeleteComponentType")
DeleteEntity = Action("DeleteEntity")
DeleteScene = Action("DeleteScene")
DeleteWorkspace = Action("DeleteWorkspace")
GetComponentType = Action("GetComponentType")
GetEntity = Action("GetEntity")
GetPropertyValue = Action("GetPropertyValue")
GetPropertyValueHistory = Action("GetPropertyValueHistory")
GetScene = Action("GetScene")
GetWorkspace = Action("GetWorkspace")
ListComponentTypes = Action("ListComponentTypes")
ListEntities = Action("ListEntities")
ListScenes = Action("ListScenes")
ListTagsForResource = Action("ListTagsForResource")
ListWorkspaces = Action("ListWorkspaces")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateComponentType = Action("UpdateComponentType")
UpdateEntity = Action("UpdateEntity")
UpdateScene = Action("UpdateScene")
UpdateWorkspace = Action("UpdateWorkspace")
