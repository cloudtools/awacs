# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Bedrock Powered by AWS Mantle"
prefix = "bedrock-mantle"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ArchiveProject = Action("ArchiveProject")
CallWithBearerToken = Action("CallWithBearerToken")
CancelFineTuningJob = Action("CancelFineTuningJob")
CancelInference = Action("CancelInference")
CreateFile = Action("CreateFile")
CreateFineTuningJob = Action("CreateFineTuningJob")
CreateInference = Action("CreateInference")
CreateProject = Action("CreateProject")
DeleteFile = Action("DeleteFile")
DeleteInference = Action("DeleteInference")
GetFile = Action("GetFile")
GetFineTuningJob = Action("GetFineTuningJob")
GetInference = Action("GetInference")
GetModel = Action("GetModel")
GetProject = Action("GetProject")
ListFiles = Action("ListFiles")
ListFineTuningJobs = Action("ListFineTuningJobs")
ListModels = Action("ListModels")
ListProjects = Action("ListProjects")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateProject = Action("UpdateProject")
