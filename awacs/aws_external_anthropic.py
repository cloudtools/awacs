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


ArchiveWorkspace = Action("ArchiveWorkspace")
AssumeConsole = Action("AssumeConsole")
CallWithBearerToken = Action("CallWithBearerToken")
CancelBatchInference = Action("CancelBatchInference")
CountTokens = Action("CountTokens")
CreateBatchInference = Action("CreateBatchInference")
CreateFile = Action("CreateFile")
CreateInference = Action("CreateInference")
CreateSkill = Action("CreateSkill")
CreateUserProfile = Action("CreateUserProfile")
CreateWorkspace = Action("CreateWorkspace")
DeleteBatchInference = Action("DeleteBatchInference")
DeleteFile = Action("DeleteFile")
DeleteSkill = Action("DeleteSkill")
GetAccountStatus = Action("GetAccountStatus")
GetBatchInference = Action("GetBatchInference")
GetFile = Action("GetFile")
GetModel = Action("GetModel")
GetSkill = Action("GetSkill")
GetUserProfile = Action("GetUserProfile")
GetWorkspace = Action("GetWorkspace")
ListBatchInferences = Action("ListBatchInferences")
ListFiles = Action("ListFiles")
ListModels = Action("ListModels")
ListSkills = Action("ListSkills")
ListUserProfiles = Action("ListUserProfiles")
ListWorkspaces = Action("ListWorkspaces")
UpdateSkill = Action("UpdateSkill")
UpdateUserProfile = Action("UpdateUserProfile")
UpdateWorkspace = Action("UpdateWorkspace")
