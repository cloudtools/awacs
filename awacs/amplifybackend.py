# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Amplify Admin"
prefix = "amplifybackend"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CloneBackend = Action("CloneBackend")
CreateBackend = Action("CreateBackend")
CreateBackendAPI = Action("CreateBackendAPI")
CreateBackendAuth = Action("CreateBackendAuth")
CreateBackendConfig = Action("CreateBackendConfig")
CreateBackendStorage = Action("CreateBackendStorage")
CreateToken = Action("CreateToken")
DeleteBackend = Action("DeleteBackend")
DeleteBackendAPI = Action("DeleteBackendAPI")
DeleteBackendAuth = Action("DeleteBackendAuth")
DeleteBackendStorage = Action("DeleteBackendStorage")
DeleteToken = Action("DeleteToken")
GenerateBackendAPIModels = Action("GenerateBackendAPIModels")
GetBackend = Action("GetBackend")
GetBackendAPI = Action("GetBackendAPI")
GetBackendAPIModels = Action("GetBackendAPIModels")
GetBackendAuth = Action("GetBackendAuth")
GetBackendJob = Action("GetBackendJob")
GetBackendStorage = Action("GetBackendStorage")
GetToken = Action("GetToken")
ImportBackendAuth = Action("ImportBackendAuth")
ImportBackendStorage = Action("ImportBackendStorage")
ListBackendJobs = Action("ListBackendJobs")
ListS3Buckets = Action("ListS3Buckets")
RemoveAllBackends = Action("RemoveAllBackends")
RemoveBackendConfig = Action("RemoveBackendConfig")
UpdateBackendAPI = Action("UpdateBackendAPI")
UpdateBackendAuth = Action("UpdateBackendAuth")
UpdateBackendConfig = Action("UpdateBackendConfig")
UpdateBackendJob = Action("UpdateBackendJob")
UpdateBackendStorage = Action("UpdateBackendStorage")
