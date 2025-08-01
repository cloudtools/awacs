# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SageMaker with MLflow"
prefix = "sagemaker-mlflow"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AccessUI = Action("AccessUI")
CreateExperiment = Action("CreateExperiment")
CreateModelVersion = Action("CreateModelVersion")
CreateRegisteredModel = Action("CreateRegisteredModel")
CreateRun = Action("CreateRun")
DeleteExperiment = Action("DeleteExperiment")
DeleteLoggedModel = Action("DeleteLoggedModel")
DeleteLoggedModelTag = Action("DeleteLoggedModelTag")
DeleteModelVersion = Action("DeleteModelVersion")
DeleteModelVersionTag = Action("DeleteModelVersionTag")
DeleteRegisteredModel = Action("DeleteRegisteredModel")
DeleteRegisteredModelAlias = Action("DeleteRegisteredModelAlias")
DeleteRegisteredModelTag = Action("DeleteRegisteredModelTag")
DeleteRun = Action("DeleteRun")
DeleteTag = Action("DeleteTag")
DeleteTraceTag = Action("DeleteTraceTag")
DeleteTraces = Action("DeleteTraces")
EndTrace = Action("EndTrace")
FinalizeLoggedModel = Action("FinalizeLoggedModel")
GetDownloadURIForModelVersionArtifacts = Action(
    "GetDownloadURIForModelVersionArtifacts"
)
GetExperiment = Action("GetExperiment")
GetExperimentByName = Action("GetExperimentByName")
GetLatestModelVersions = Action("GetLatestModelVersions")
GetLoggedModel = Action("GetLoggedModel")
GetMetricHistory = Action("GetMetricHistory")
GetModelVersion = Action("GetModelVersion")
GetModelVersionByAlias = Action("GetModelVersionByAlias")
GetRegisteredModel = Action("GetRegisteredModel")
GetRun = Action("GetRun")
GetTraceInfo = Action("GetTraceInfo")
ListArtifacts = Action("ListArtifacts")
ListLoggedModelArtifacts = Action("ListLoggedModelArtifacts")
LogBatch = Action("LogBatch")
LogInputs = Action("LogInputs")
LogLoggedModelParams = Action("LogLoggedModelParams")
LogMetric = Action("LogMetric")
LogModel = Action("LogModel")
LogOutputs = Action("LogOutputs")
LogParam = Action("LogParam")
RenameRegisteredModel = Action("RenameRegisteredModel")
RestoreExperiment = Action("RestoreExperiment")
RestoreRun = Action("RestoreRun")
SearchExperiments = Action("SearchExperiments")
SearchLoggedModels = Action("SearchLoggedModels")
SearchModelVersions = Action("SearchModelVersions")
SearchRegisteredModels = Action("SearchRegisteredModels")
SearchRuns = Action("SearchRuns")
SearchTraces = Action("SearchTraces")
SetExperimentTag = Action("SetExperimentTag")
SetLoggedModelTags = Action("SetLoggedModelTags")
SetModelVersionTag = Action("SetModelVersionTag")
SetRegisteredModelAlias = Action("SetRegisteredModelAlias")
SetRegisteredModelTag = Action("SetRegisteredModelTag")
SetTag = Action("SetTag")
SetTraceTag = Action("SetTraceTag")
StartTrace = Action("StartTrace")
TransitionModelVersionStage = Action("TransitionModelVersionStage")
UpdateExperiment = Action("UpdateExperiment")
UpdateModelVersion = Action("UpdateModelVersion")
UpdateRegisteredModel = Action("UpdateRegisteredModel")
UpdateRun = Action("UpdateRun")
