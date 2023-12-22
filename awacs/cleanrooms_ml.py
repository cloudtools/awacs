# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Clean Rooms ML"
prefix = "cleanrooms-ml"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAudienceModel = Action("CreateAudienceModel")
CreateConfiguredAudienceModel = Action("CreateConfiguredAudienceModel")
CreateTrainingDataset = Action("CreateTrainingDataset")
DeleteAudienceGenerationJob = Action("DeleteAudienceGenerationJob")
DeleteAudienceModel = Action("DeleteAudienceModel")
DeleteConfiguredAudienceModel = Action("DeleteConfiguredAudienceModel")
DeleteConfiguredAudienceModelPolicy = Action("DeleteConfiguredAudienceModelPolicy")
DeleteTrainingDataset = Action("DeleteTrainingDataset")
GetAudienceGenerationJob = Action("GetAudienceGenerationJob")
GetAudienceModel = Action("GetAudienceModel")
GetConfiguredAudienceModel = Action("GetConfiguredAudienceModel")
GetConfiguredAudienceModelPolicy = Action("GetConfiguredAudienceModelPolicy")
GetTrainingDataset = Action("GetTrainingDataset")
ListAudienceExportJobs = Action("ListAudienceExportJobs")
ListAudienceGenerationJobs = Action("ListAudienceGenerationJobs")
ListAudienceModels = Action("ListAudienceModels")
ListConfiguredAudienceModels = Action("ListConfiguredAudienceModels")
ListTagsForResource = Action("ListTagsForResource")
ListTrainingDatasets = Action("ListTrainingDatasets")
PutConfiguredAudienceModelPolicy = Action("PutConfiguredAudienceModelPolicy")
StartAudienceExportJob = Action("StartAudienceExportJob")
StartAudienceGenerationJob = Action("StartAudienceGenerationJob")
TagResource = Action("TagResource")
UnTagResource = Action("UnTagResource")
UpdateConfiguredAudienceModel = Action("UpdateConfiguredAudienceModel")
