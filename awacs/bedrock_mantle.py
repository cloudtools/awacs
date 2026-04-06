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
AssociateCustomizedModel = Action("AssociateCustomizedModel")
CallWithBearerToken = Action("CallWithBearerToken")
CancelFineTuningJob = Action("CancelFineTuningJob")
CancelInference = Action("CancelInference")
CreateCustomizedModel = Action("CreateCustomizedModel")
CreateFile = Action("CreateFile")
CreateFineTuningJob = Action("CreateFineTuningJob")
CreateInference = Action("CreateInference")
CreateProject = Action("CreateProject")
CreateReservation = Action("CreateReservation")
DeleteCustomizedModel = Action("DeleteCustomizedModel")
DeleteFile = Action("DeleteFile")
DeleteInference = Action("DeleteInference")
DeleteReservation = Action("DeleteReservation")
DisassociateCustomizedModel = Action("DisassociateCustomizedModel")
GetCustomizedModel = Action("GetCustomizedModel")
GetFile = Action("GetFile")
GetFineTuningJob = Action("GetFineTuningJob")
GetInference = Action("GetInference")
GetModel = Action("GetModel")
GetProject = Action("GetProject")
GetReservation = Action("GetReservation")
ListCustomizedModelAssociations = Action("ListCustomizedModelAssociations")
ListCustomizedModels = Action("ListCustomizedModels")
ListFiles = Action("ListFiles")
ListFineTuningJobs = Action("ListFineTuningJobs")
ListModels = Action("ListModels")
ListProjects = Action("ListProjects")
ListReservations = Action("ListReservations")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateProject = Action("UpdateProject")
UpdateReservation = Action("UpdateReservation")
