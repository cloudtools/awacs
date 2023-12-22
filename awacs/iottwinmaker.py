# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT TwinMaker"
prefix = "iottwinmaker"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchPutPropertyValues = Action("BatchPutPropertyValues")
CancelMetadataTransferJob = Action("CancelMetadataTransferJob")
CreateComponentType = Action("CreateComponentType")
CreateEntity = Action("CreateEntity")
CreateMetadataTransferJob = Action("CreateMetadataTransferJob")
CreateScene = Action("CreateScene")
CreateSyncJob = Action("CreateSyncJob")
CreateWorkspace = Action("CreateWorkspace")
DeleteComponentType = Action("DeleteComponentType")
DeleteEntity = Action("DeleteEntity")
DeleteScene = Action("DeleteScene")
DeleteSyncJob = Action("DeleteSyncJob")
DeleteWorkspace = Action("DeleteWorkspace")
ExecuteQuery = Action("ExecuteQuery")
GetComponentType = Action("GetComponentType")
GetEntity = Action("GetEntity")
GetMetadataTransferJob = Action("GetMetadataTransferJob")
GetPricingPlan = Action("GetPricingPlan")
GetPropertyValue = Action("GetPropertyValue")
GetPropertyValueHistory = Action("GetPropertyValueHistory")
GetScene = Action("GetScene")
GetSyncJob = Action("GetSyncJob")
GetWorkspace = Action("GetWorkspace")
ListComponentTypes = Action("ListComponentTypes")
ListComponents = Action("ListComponents")
ListEntities = Action("ListEntities")
ListMetadataTransferJobs = Action("ListMetadataTransferJobs")
ListProperties = Action("ListProperties")
ListScenes = Action("ListScenes")
ListSyncJobs = Action("ListSyncJobs")
ListSyncResources = Action("ListSyncResources")
ListTagsForResource = Action("ListTagsForResource")
ListWorkspaces = Action("ListWorkspaces")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateComponentType = Action("UpdateComponentType")
UpdateEntity = Action("UpdateEntity")
UpdatePricingPlan = Action("UpdatePricingPlan")
UpdateScene = Action("UpdateScene")
UpdateWorkspace = Action("UpdateWorkspace")
