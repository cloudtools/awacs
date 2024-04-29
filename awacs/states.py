# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Step Functions"
prefix = "states"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateActivity = Action("CreateActivity")
CreateStateMachine = Action("CreateStateMachine")
CreateStateMachineAlias = Action("CreateStateMachineAlias")
DeleteActivity = Action("DeleteActivity")
DeleteStateMachine = Action("DeleteStateMachine")
DeleteStateMachineAlias = Action("DeleteStateMachineAlias")
DeleteStateMachineVersion = Action("DeleteStateMachineVersion")
DescribeActivity = Action("DescribeActivity")
DescribeExecution = Action("DescribeExecution")
DescribeMapRun = Action("DescribeMapRun")
DescribeStateMachine = Action("DescribeStateMachine")
DescribeStateMachineAlias = Action("DescribeStateMachineAlias")
DescribeStateMachineForExecution = Action("DescribeStateMachineForExecution")
GetActivityTask = Action("GetActivityTask")
GetExecutionHistory = Action("GetExecutionHistory")
InvokeHTTPEndpoint = Action("InvokeHTTPEndpoint")
ListActivities = Action("ListActivities")
ListExecutions = Action("ListExecutions")
ListMapRuns = Action("ListMapRuns")
ListStateMachineAliases = Action("ListStateMachineAliases")
ListStateMachineVersions = Action("ListStateMachineVersions")
ListStateMachines = Action("ListStateMachines")
ListTagsForResource = Action("ListTagsForResource")
PublishStateMachineVersion = Action("PublishStateMachineVersion")
RedriveExecution = Action("RedriveExecution")
RevealSecrets = Action("RevealSecrets")
SendTaskFailure = Action("SendTaskFailure")
SendTaskHeartbeat = Action("SendTaskHeartbeat")
SendTaskSuccess = Action("SendTaskSuccess")
StartExecution = Action("StartExecution")
StartSyncExecution = Action("StartSyncExecution")
StopExecution = Action("StopExecution")
TagResource = Action("TagResource")
TestState = Action("TestState")
UntagResource = Action("UntagResource")
UpdateMapRun = Action("UpdateMapRun")
UpdateStateMachine = Action("UpdateStateMachine")
UpdateStateMachineAlias = Action("UpdateStateMachineAlias")
ValidateStateMachineDefinition = Action("ValidateStateMachineDefinition")
