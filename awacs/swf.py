# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Simple Workflow Service"
prefix = "swf"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelTimer = Action("CancelTimer")
CancelWorkflowExecution = Action("CancelWorkflowExecution")
CompleteWorkflowExecution = Action("CompleteWorkflowExecution")
ContinueAsNewWorkflowExecution = Action("ContinueAsNewWorkflowExecution")
CountClosedWorkflowExecutions = Action("CountClosedWorkflowExecutions")
CountOpenWorkflowExecutions = Action("CountOpenWorkflowExecutions")
CountPendingActivityTasks = Action("CountPendingActivityTasks")
CountPendingDecisionTasks = Action("CountPendingDecisionTasks")
DeleteActivityType = Action("DeleteActivityType")
DeleteWorkflowType = Action("DeleteWorkflowType")
DeprecateActivityType = Action("DeprecateActivityType")
DeprecateDomain = Action("DeprecateDomain")
DeprecateWorkflowType = Action("DeprecateWorkflowType")
DescribeActivityType = Action("DescribeActivityType")
DescribeDomain = Action("DescribeDomain")
DescribeWorkflowExecution = Action("DescribeWorkflowExecution")
DescribeWorkflowType = Action("DescribeWorkflowType")
FailWorkflowExecution = Action("FailWorkflowExecution")
GetWorkflowExecutionHistory = Action("GetWorkflowExecutionHistory")
ListActivityTypes = Action("ListActivityTypes")
ListClosedWorkflowExecutions = Action("ListClosedWorkflowExecutions")
ListDomains = Action("ListDomains")
ListOpenWorkflowExecutions = Action("ListOpenWorkflowExecutions")
ListTagsForResource = Action("ListTagsForResource")
ListWorkflowTypes = Action("ListWorkflowTypes")
PollForActivityTask = Action("PollForActivityTask")
PollForDecisionTask = Action("PollForDecisionTask")
RecordActivityTaskHeartbeat = Action("RecordActivityTaskHeartbeat")
RecordMarker = Action("RecordMarker")
RegisterActivityType = Action("RegisterActivityType")
RegisterDomain = Action("RegisterDomain")
RegisterWorkflowType = Action("RegisterWorkflowType")
RequestCancelActivityTask = Action("RequestCancelActivityTask")
RequestCancelExternalWorkflowExecution = Action(
    "RequestCancelExternalWorkflowExecution"
)
RequestCancelWorkflowExecution = Action("RequestCancelWorkflowExecution")
RespondActivityTaskCanceled = Action("RespondActivityTaskCanceled")
RespondActivityTaskCompleted = Action("RespondActivityTaskCompleted")
RespondActivityTaskFailed = Action("RespondActivityTaskFailed")
RespondDecisionTaskCompleted = Action("RespondDecisionTaskCompleted")
ScheduleActivityTask = Action("ScheduleActivityTask")
SignalExternalWorkflowExecution = Action("SignalExternalWorkflowExecution")
SignalWorkflowExecution = Action("SignalWorkflowExecution")
StartChildWorkflowExecution = Action("StartChildWorkflowExecution")
StartTimer = Action("StartTimer")
StartWorkflowExecution = Action("StartWorkflowExecution")
TagResource = Action("TagResource")
TerminateWorkflowExecution = Action("TerminateWorkflowExecution")
UndeprecateActivityType = Action("UndeprecateActivityType")
UndeprecateDomain = Action("UndeprecateDomain")
UndeprecateWorkflowType = Action("UndeprecateWorkflowType")
UntagResource = Action("UntagResource")
