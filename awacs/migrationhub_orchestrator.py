# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Migration Hub Orchestrator"
prefix = "migrationhub-orchestrator"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateTemplate = Action("CreateTemplate")
CreateWorkflow = Action("CreateWorkflow")
CreateWorkflowStep = Action("CreateWorkflowStep")
CreateWorkflowStepGroup = Action("CreateWorkflowStepGroup")
DeleteTemplate = Action("DeleteTemplate")
DeleteWorkflow = Action("DeleteWorkflow")
DeleteWorkflowStep = Action("DeleteWorkflowStep")
DeleteWorkflowStepGroup = Action("DeleteWorkflowStepGroup")
GetMessage = Action("GetMessage")
GetTemplate = Action("GetTemplate")
GetTemplateStep = Action("GetTemplateStep")
GetTemplateStepGroup = Action("GetTemplateStepGroup")
GetWorkflow = Action("GetWorkflow")
GetWorkflowStep = Action("GetWorkflowStep")
GetWorkflowStepGroup = Action("GetWorkflowStepGroup")
ListPlugins = Action("ListPlugins")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateStepGroups = Action("ListTemplateStepGroups")
ListTemplateSteps = Action("ListTemplateSteps")
ListTemplates = Action("ListTemplates")
ListWorkflowStepGroups = Action("ListWorkflowStepGroups")
ListWorkflowSteps = Action("ListWorkflowSteps")
ListWorkflows = Action("ListWorkflows")
RegisterPlugin = Action("RegisterPlugin")
RetryWorkflowStep = Action("RetryWorkflowStep")
SendMessage = Action("SendMessage")
StartWorkflow = Action("StartWorkflow")
StopWorkflow = Action("StopWorkflow")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTemplate = Action("UpdateTemplate")
UpdateWorkflow = Action("UpdateWorkflow")
UpdateWorkflowStep = Action("UpdateWorkflowStep")
UpdateWorkflowStepGroup = Action("UpdateWorkflowStepGroup")
