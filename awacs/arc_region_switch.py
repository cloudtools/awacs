# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon ARC Region switch"
prefix = "arc-region-switch"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ApprovePlanExecutionStep = Action("ApprovePlanExecutionStep")
CancelPlanExecution = Action("CancelPlanExecution")
CreatePlan = Action("CreatePlan")
DeletePlan = Action("DeletePlan")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
GetPlan = Action("GetPlan")
GetPlanEvaluationStatus = Action("GetPlanEvaluationStatus")
GetPlanExecution = Action("GetPlanExecution")
GetPlanInRegion = Action("GetPlanInRegion")
GetResourcePolicy = Action("GetResourcePolicy")
ListPlanExecutionEvents = Action("ListPlanExecutionEvents")
ListPlanExecutions = Action("ListPlanExecutions")
ListPlans = Action("ListPlans")
ListPlansInRegion = Action("ListPlansInRegion")
ListRoute53HealthChecks = Action("ListRoute53HealthChecks")
ListRoute53HealthChecksInRegion = Action("ListRoute53HealthChecksInRegion")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
StartPlanExecution = Action("StartPlanExecution")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdatePlan = Action("UpdatePlan")
UpdatePlanExecution = Action("UpdatePlanExecution")
UpdatePlanExecutionStep = Action("UpdatePlanExecutionStep")
