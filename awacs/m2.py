# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Mainframe Modernization Service"
prefix = "m2"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelBatchJobExecution = Action("CancelBatchJobExecution")
CreateApplication = Action("CreateApplication")
CreateDataSetImportTask = Action("CreateDataSetImportTask")
CreateDeployment = Action("CreateDeployment")
CreateEnvironment = Action("CreateEnvironment")
DeleteApplication = Action("DeleteApplication")
DeleteApplicationFromEnvironment = Action("DeleteApplicationFromEnvironment")
DeleteEnvironment = Action("DeleteEnvironment")
GetApplication = Action("GetApplication")
GetApplicationVersion = Action("GetApplicationVersion")
GetBatchJobExecution = Action("GetBatchJobExecution")
GetDataSetDetails = Action("GetDataSetDetails")
GetDataSetImportTask = Action("GetDataSetImportTask")
GetDeployment = Action("GetDeployment")
GetEnvironment = Action("GetEnvironment")
GetSignedBluinsightsUrl = Action("GetSignedBluinsightsUrl")
ListApplicationVersions = Action("ListApplicationVersions")
ListApplications = Action("ListApplications")
ListBatchJobDefinitions = Action("ListBatchJobDefinitions")
ListBatchJobExecutions = Action("ListBatchJobExecutions")
ListBatchJobRestartPoints = Action("ListBatchJobRestartPoints")
ListDataSetImportHistory = Action("ListDataSetImportHistory")
ListDataSets = Action("ListDataSets")
ListDeployments = Action("ListDeployments")
ListEngineVersions = Action("ListEngineVersions")
ListEnvironments = Action("ListEnvironments")
ListTagsForResource = Action("ListTagsForResource")
StartApplication = Action("StartApplication")
StartBatchJob = Action("StartBatchJob")
StopApplication = Action("StopApplication")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateEnvironment = Action("UpdateEnvironment")
