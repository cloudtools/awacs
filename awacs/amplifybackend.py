# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Amplify Admin"
prefix = "amplifybackend"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CreateToken = Action("CreateToken")
DeleteBackend = Action("DeleteBackend")
DeleteBackendAPI = Action("DeleteBackendAPI")
DeleteBackendAuth = Action("DeleteBackendAuth")
DeleteToken = Action("DeleteToken")
GenerateBackendAPIModels = Action("GenerateBackendAPIModels")
GetBackend = Action("GetBackend")
GetBackendAPI = Action("GetBackendAPI")
GetBackendAPIModels = Action("GetBackendAPIModels")
GetBackendAuth = Action("GetBackendAuth")
GetBackendJob = Action("GetBackendJob")
GetToken = Action("GetToken")
ImportBackendAuth = Action("ImportBackendAuth")
ListBackendJobs = Action("ListBackendJobs")
RemoveAllBackends = Action("RemoveAllBackends")
RemoveBackendConfig = Action("RemoveBackendConfig")
UpdateBackendAPI = Action("UpdateBackendAPI")
UpdateBackendAuth = Action("UpdateBackendAuth")
UpdateBackendConfig = Action("UpdateBackendConfig")
UpdateBackendJob = Action("UpdateBackendJob")
