# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS service to manage AI agents for UI workflows"
prefix = "nova-act"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAct = Action("CreateAct")
CreateSession = Action("CreateSession")
CreateWorkflowDefinition = Action("CreateWorkflowDefinition")
CreateWorkflowRun = Action("CreateWorkflowRun")
DeleteWorkflowDefinition = Action("DeleteWorkflowDefinition")
DeleteWorkflowRun = Action("DeleteWorkflowRun")
GetWorkflowDefinition = Action("GetWorkflowDefinition")
GetWorkflowRun = Action("GetWorkflowRun")
InvokeActStep = Action("InvokeActStep")
ListActs = Action("ListActs")
ListModels = Action("ListModels")
ListSessions = Action("ListSessions")
ListWorkflowDefinitions = Action("ListWorkflowDefinitions")
ListWorkflowRuns = Action("ListWorkflowRuns")
UpdateAct = Action("UpdateAct")
UpdateWorkflowRun = Action("UpdateWorkflowRun")
