# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EMR Serverless"
prefix = "emr-serverless"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AccessInteractiveEndpoints = Action("AccessInteractiveEndpoints")
AccessLivyEndpoints = Action("AccessLivyEndpoints")
CancelJobRun = Action("CancelJobRun")
CreateApplication = Action("CreateApplication")
DeleteApplication = Action("DeleteApplication")
GetApplication = Action("GetApplication")
GetDashboardForJobRun = Action("GetDashboardForJobRun")
GetJobRun = Action("GetJobRun")
ListApplications = Action("ListApplications")
ListJobRunAttempts = Action("ListJobRunAttempts")
ListJobRuns = Action("ListJobRuns")
ListTagsForResource = Action("ListTagsForResource")
StartApplication = Action("StartApplication")
StartJobRun = Action("StartJobRun")
StopApplication = Action("StopApplication")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
