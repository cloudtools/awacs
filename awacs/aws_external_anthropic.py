# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Claude Platform on AWS"
prefix = "aws-external-anthropic"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ArchiveAgent = Action("ArchiveAgent")
ArchiveDeployment = Action("ArchiveDeployment")
ArchiveEnvironment = Action("ArchiveEnvironment")
ArchiveMemoryStore = Action("ArchiveMemoryStore")
ArchiveSession = Action("ArchiveSession")
ArchiveVault = Action("ArchiveVault")
ArchiveWorkspace = Action("ArchiveWorkspace")
AssumeConsole = Action("AssumeConsole")
CallWithBearerToken = Action("CallWithBearerToken")
CancelBatchInference = Action("CancelBatchInference")
CountTokens = Action("CountTokens")
CreateAgent = Action("CreateAgent")
CreateBatchInference = Action("CreateBatchInference")
CreateDeployment = Action("CreateDeployment")
CreateEnvironment = Action("CreateEnvironment")
CreateFile = Action("CreateFile")
CreateInference = Action("CreateInference")
CreateMemoryStore = Action("CreateMemoryStore")
CreateSession = Action("CreateSession")
CreateSkill = Action("CreateSkill")
CreateUserProfile = Action("CreateUserProfile")
CreateUserProfileEnrollmentUrl = Action("CreateUserProfileEnrollmentUrl")
CreateVault = Action("CreateVault")
CreateWebhook = Action("CreateWebhook")
CreateWorkspace = Action("CreateWorkspace")
DeleteBatchInference = Action("DeleteBatchInference")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteFile = Action("DeleteFile")
DeleteMemoryStore = Action("DeleteMemoryStore")
DeleteSession = Action("DeleteSession")
DeleteSkill = Action("DeleteSkill")
DeleteVault = Action("DeleteVault")
DeleteWebhook = Action("DeleteWebhook")
DisableKey = Action("DisableKey")
GetAccountStatus = Action("GetAccountStatus")
GetAgent = Action("GetAgent")
GetBatchInference = Action("GetBatchInference")
GetDeployment = Action("GetDeployment")
GetEnvironment = Action("GetEnvironment")
GetFile = Action("GetFile")
GetKey = Action("GetKey")
GetMemoryStore = Action("GetMemoryStore")
GetModel = Action("GetModel")
GetSession = Action("GetSession")
GetSkill = Action("GetSkill")
GetUserProfile = Action("GetUserProfile")
GetVault = Action("GetVault")
GetWebhook = Action("GetWebhook")
GetWorkspace = Action("GetWorkspace")
ListAgents = Action("ListAgents")
ListBatchInferences = Action("ListBatchInferences")
ListDeployments = Action("ListDeployments")
ListEnvironments = Action("ListEnvironments")
ListFiles = Action("ListFiles")
ListKeys = Action("ListKeys")
ListMemoryStores = Action("ListMemoryStores")
ListModels = Action("ListModels")
ListSessions = Action("ListSessions")
ListSkills = Action("ListSkills")
ListTagsForResource = Action("ListTagsForResource")
ListUserProfiles = Action("ListUserProfiles")
ListVaults = Action("ListVaults")
ListWebhooks = Action("ListWebhooks")
ListWorkspaces = Action("ListWorkspaces")
PauseDeployment = Action("PauseDeployment")
ProcessEnvironmentWork = Action("ProcessEnvironmentWork")
RegisterKey = Action("RegisterKey")
RotateWebhookSecret = Action("RotateWebhookSecret")
RunDeployment = Action("RunDeployment")
TagResource = Action("TagResource")
UnpauseDeployment = Action("UnpauseDeployment")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateDeployment = Action("UpdateDeployment")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateKey = Action("UpdateKey")
UpdateMemoryStore = Action("UpdateMemoryStore")
UpdateSession = Action("UpdateSession")
UpdateSkill = Action("UpdateSkill")
UpdateUserProfile = Action("UpdateUserProfile")
UpdateVault = Action("UpdateVault")
UpdateWebhook = Action("UpdateWebhook")
UpdateWorkspace = Action("UpdateWorkspace")
