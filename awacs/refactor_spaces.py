# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Migration Hub Refactor Spaces"
prefix = "refactor-spaces"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApplication = Action("CreateApplication")
CreateEnvironment = Action("CreateEnvironment")
CreateRoute = Action("CreateRoute")
CreateService = Action("CreateService")
DeleteApplication = Action("DeleteApplication")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRoute = Action("DeleteRoute")
DeleteService = Action("DeleteService")
GetApplication = Action("GetApplication")
GetEnvironment = Action("GetEnvironment")
GetResourcePolicy = Action("GetResourcePolicy")
GetRoute = Action("GetRoute")
GetService = Action("GetService")
ListApplications = Action("ListApplications")
ListEnvironmentVpcs = Action("ListEnvironmentVpcs")
ListEnvironments = Action("ListEnvironments")
ListRoutes = Action("ListRoutes")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateRoute = Action("UpdateRoute")
