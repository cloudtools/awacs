# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Step Functions"
prefix = "states"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateActivity = Action("CreateActivity")
CreateStateMachine = Action("CreateStateMachine")
DeleteActivity = Action("DeleteActivity")
DeleteStateMachine = Action("DeleteStateMachine")
DescribeActivity = Action("DescribeActivity")
DescribeExecution = Action("DescribeExecution")
DescribeStateMachine = Action("DescribeStateMachine")
DescribeStateMachineForExecution = Action("DescribeStateMachineForExecution")
GetActivityTask = Action("GetActivityTask")
GetExecutionHistory = Action("GetExecutionHistory")
ListActivities = Action("ListActivities")
ListExecutions = Action("ListExecutions")
ListStateMachines = Action("ListStateMachines")
ListTagsForResource = Action("ListTagsForResource")
SendTaskFailure = Action("SendTaskFailure")
SendTaskHeartbeat = Action("SendTaskHeartbeat")
SendTaskSuccess = Action("SendTaskSuccess")
StartExecution = Action("StartExecution")
StartSyncExecution = Action("StartSyncExecution")
StopExecution = Action("StopExecution")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateStateMachine = Action("UpdateStateMachine")
