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


CancelTrainedModel = Action("CancelTrainedModel")
CancelTrainedModelInferenceJob = Action("CancelTrainedModelInferenceJob")
CreateAudienceModel = Action("CreateAudienceModel")
CreateConfiguredAudienceModel = Action("CreateConfiguredAudienceModel")
CreateConfiguredModelAlgorithm = Action("CreateConfiguredModelAlgorithm")
CreateConfiguredModelAlgorithmAssociation = Action(
    "CreateConfiguredModelAlgorithmAssociation"
)
CreateMLInputChannel = Action("CreateMLInputChannel")
CreateTrainedModel = Action("CreateTrainedModel")
CreateTrainingDataset = Action("CreateTrainingDataset")
DeleteAudienceGenerationJob = Action("DeleteAudienceGenerationJob")
DeleteAudienceModel = Action("DeleteAudienceModel")
DeleteConfiguredAudienceModel = Action("DeleteConfiguredAudienceModel")
DeleteConfiguredAudienceModelPolicy = Action("DeleteConfiguredAudienceModelPolicy")
DeleteConfiguredModelAlgorithm = Action("DeleteConfiguredModelAlgorithm")
DeleteConfiguredModelAlgorithmAssociation = Action(
    "DeleteConfiguredModelAlgorithmAssociation"
)
DeleteMLConfiguration = Action("DeleteMLConfiguration")
DeleteMLInputChannelData = Action("DeleteMLInputChannelData")
DeleteTrainedModelOutput = Action("DeleteTrainedModelOutput")
DeleteTrainingDataset = Action("DeleteTrainingDataset")
GetAudienceGenerationJob = Action("GetAudienceGenerationJob")
GetAudienceModel = Action("GetAudienceModel")
GetCollaborationConfiguredModelAlgorithmAssociation = Action(
    "GetCollaborationConfiguredModelAlgorithmAssociation"
)
GetCollaborationMLInputChannel = Action("GetCollaborationMLInputChannel")
GetCollaborationTrainedModel = Action("GetCollaborationTrainedModel")
GetConfiguredAudienceModel = Action("GetConfiguredAudienceModel")
GetConfiguredAudienceModelPolicy = Action("GetConfiguredAudienceModelPolicy")
GetConfiguredModelAlgorithm = Action("GetConfiguredModelAlgorithm")
GetConfiguredModelAlgorithmAssociation = Action(
    "GetConfiguredModelAlgorithmAssociation"
)
GetMLConfiguration = Action("GetMLConfiguration")
GetMLInputChannel = Action("GetMLInputChannel")
GetTrainedModel = Action("GetTrainedModel")
GetTrainedModelInferenceJob = Action("GetTrainedModelInferenceJob")
GetTrainingDataset = Action("GetTrainingDataset")
ListAudienceExportJobs = Action("ListAudienceExportJobs")
ListAudienceGenerationJobs = Action("ListAudienceGenerationJobs")
ListAudienceModels = Action("ListAudienceModels")
ListCollaborationConfiguredModelAlgorithmAssociations = Action(
    "ListCollaborationConfiguredModelAlgorithmAssociations"
)
ListCollaborationMLInputChannels = Action("ListCollaborationMLInputChannels")
ListCollaborationTrainedModelExportJobs = Action(
    "ListCollaborationTrainedModelExportJobs"
)
ListCollaborationTrainedModelInferenceJobs = Action(
    "ListCollaborationTrainedModelInferenceJobs"
)
ListCollaborationTrainedModels = Action("ListCollaborationTrainedModels")
ListConfiguredAudienceModels = Action("ListConfiguredAudienceModels")
ListConfiguredModelAlgorithmAssociations = Action(
    "ListConfiguredModelAlgorithmAssociations"
)
ListConfiguredModelAlgorithms = Action("ListConfiguredModelAlgorithms")
ListMLInputChannels = Action("ListMLInputChannels")
ListTagsForResource = Action("ListTagsForResource")
ListTrainedModelInferenceJobs = Action("ListTrainedModelInferenceJobs")
ListTrainedModels = Action("ListTrainedModels")
ListTrainingDatasets = Action("ListTrainingDatasets")
PutConfiguredAudienceModelPolicy = Action("PutConfiguredAudienceModelPolicy")
PutMLConfiguration = Action("PutMLConfiguration")
StartAudienceExportJob = Action("StartAudienceExportJob")
StartAudienceGenerationJob = Action("StartAudienceGenerationJob")
StartTrainedModelExportJob = Action("StartTrainedModelExportJob")
StartTrainedModelInferenceJob = Action("StartTrainedModelInferenceJob")
TagResource = Action("TagResource")
UnTagResource = Action("UnTagResource")
UpdateConfiguredAudienceModel = Action("UpdateConfiguredAudienceModel")
