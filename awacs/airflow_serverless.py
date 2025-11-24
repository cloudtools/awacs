# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS MWAA Serverless"
prefix = "airflow-serverless"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateWorkflow = Action("CreateWorkflow")
DeleteWorkflow = Action("DeleteWorkflow")
GetTaskInstance = Action("GetTaskInstance")
GetWorkflow = Action("GetWorkflow")
GetWorkflowRun = Action("GetWorkflowRun")
ListTagsForResource = Action("ListTagsForResource")
ListTaskInstances = Action("ListTaskInstances")
ListWorkflowRuns = Action("ListWorkflowRuns")
ListWorkflowVersions = Action("ListWorkflowVersions")
ListWorkflows = Action("ListWorkflows")
StartWorkflowRun = Action("StartWorkflowRun")
StopWorkflowRun = Action("StopWorkflowRun")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateWorkflow = Action("UpdateWorkflow")
