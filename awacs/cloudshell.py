# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudShell"
prefix = "cloudshell"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateEnvironment = Action("CreateEnvironment")
CreateSession = Action("CreateSession")
DeleteEnvironment = Action("DeleteEnvironment")
DescribeEnvironments = Action("DescribeEnvironments")
GetEnvironmentStatus = Action("GetEnvironmentStatus")
GetFileDownloadUrls = Action("GetFileDownloadUrls")
GetFileUploadUrls = Action("GetFileUploadUrls")
PutCredentials = Action("PutCredentials")
StartEnvironment = Action("StartEnvironment")
StopEnvironment = Action("StopEnvironment")
