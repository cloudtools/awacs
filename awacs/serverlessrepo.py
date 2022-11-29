# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Serverless Application Repository"
prefix = "serverlessrepo"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApplication = Action("CreateApplication")
CreateApplicationVersion = Action("CreateApplicationVersion")
CreateCloudFormationChangeSet = Action("CreateCloudFormationChangeSet")
CreateCloudFormationTemplate = Action("CreateCloudFormationTemplate")
DeleteApplication = Action("DeleteApplication")
GetApplication = Action("GetApplication")
GetApplicationPolicy = Action("GetApplicationPolicy")
GetCloudFormationTemplate = Action("GetCloudFormationTemplate")
ListApplicationDependencies = Action("ListApplicationDependencies")
ListApplicationVersions = Action("ListApplicationVersions")
ListApplications = Action("ListApplications")
PutApplicationPolicy = Action("PutApplicationPolicy")
SearchApplications = Action("SearchApplications")
UnshareApplication = Action("UnshareApplication")
UpdateApplication = Action("UpdateApplication")
