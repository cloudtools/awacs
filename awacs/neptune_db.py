# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Neptune"
prefix = "neptune-db"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelLoaderJob = Action("CancelLoaderJob")
CancelMLDataProcessingJob = Action("CancelMLDataProcessingJob")
CancelMLModelTrainingJob = Action("CancelMLModelTrainingJob")
CancelMLModelTransformJob = Action("CancelMLModelTransformJob")
CancelQuery = Action("CancelQuery")
CreateMLEndpoint = Action("CreateMLEndpoint")
DeleteDataViaQuery = Action("DeleteDataViaQuery")
DeleteMLEndpoint = Action("DeleteMLEndpoint")
DeleteStatistics = Action("DeleteStatistics")
GetEngineStatus = Action("GetEngineStatus")
GetGraphSummary = Action("GetGraphSummary")
GetLoaderJobStatus = Action("GetLoaderJobStatus")
GetMLDataProcessingJobStatus = Action("GetMLDataProcessingJobStatus")
GetMLEndpointStatus = Action("GetMLEndpointStatus")
GetMLModelTrainingJobStatus = Action("GetMLModelTrainingJobStatus")
GetMLModelTransformJobStatus = Action("GetMLModelTransformJobStatus")
GetQueryStatus = Action("GetQueryStatus")
GetStatisticsStatus = Action("GetStatisticsStatus")
GetStreamRecords = Action("GetStreamRecords")
ListLoaderJobs = Action("ListLoaderJobs")
ListMLDataProcessingJobs = Action("ListMLDataProcessingJobs")
ListMLEndpoints = Action("ListMLEndpoints")
ListMLModelTrainingJobs = Action("ListMLModelTrainingJobs")
ListMLModelTransformJobs = Action("ListMLModelTransformJobs")
ManageStatistics = Action("ManageStatistics")
ReadDataViaQuery = Action("ReadDataViaQuery")
ResetDatabase = Action("ResetDatabase")
StartLoaderJob = Action("StartLoaderJob")
StartMLDataProcessingJob = Action("StartMLDataProcessingJob")
StartMLModelTrainingJob = Action("StartMLModelTrainingJob")
StartMLModelTransformJob = Action("StartMLModelTransformJob")
WriteDataViaQuery = Action("WriteDataViaQuery")
connect = Action("connect")
