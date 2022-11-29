# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FinSpace"
prefix = "finspace"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateEnvironment = Action("CreateEnvironment")
CreateUser = Action("CreateUser")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteUser = Action("DeleteUser")
GetEnvironment = Action("GetEnvironment")
GetLoadSampleDataSetGroupIntoEnvironmentStatus = Action(
    "GetLoadSampleDataSetGroupIntoEnvironmentStatus"
)
GetUser = Action("GetUser")
ListEnvironments = Action("ListEnvironments")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
LoadSampleDataSetGroupIntoEnvironment = Action("LoadSampleDataSetGroupIntoEnvironment")
ResetUserPassword = Action("ResetUserPassword")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateUser = Action("UpdateUser")
