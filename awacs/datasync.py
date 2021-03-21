# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWSDataSync"
prefix = "datasync"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelTaskExecution = Action("CancelTaskExecution")
CreateAgent = Action("CreateAgent")
CreateLocationEfs = Action("CreateLocationEfs")
CreateLocationFsxWindows = Action("CreateLocationFsxWindows")
CreateLocationNfs = Action("CreateLocationNfs")
CreateLocationObjectStorage = Action("CreateLocationObjectStorage")
CreateLocationS3 = Action("CreateLocationS3")
CreateLocationSmb = Action("CreateLocationSmb")
CreateTask = Action("CreateTask")
DeleteAgent = Action("DeleteAgent")
DeleteLocation = Action("DeleteLocation")
DeleteTask = Action("DeleteTask")
DescribeAgent = Action("DescribeAgent")
DescribeLocationEfs = Action("DescribeLocationEfs")
DescribeLocationFsxWindows = Action("DescribeLocationFsxWindows")
DescribeLocationNfs = Action("DescribeLocationNfs")
DescribeLocationObjectStorage = Action("DescribeLocationObjectStorage")
DescribeLocationS3 = Action("DescribeLocationS3")
DescribeLocationSmb = Action("DescribeLocationSmb")
DescribeTask = Action("DescribeTask")
DescribeTaskExecution = Action("DescribeTaskExecution")
ListAgents = Action("ListAgents")
ListLocations = Action("ListLocations")
ListTagsForResource = Action("ListTagsForResource")
ListTaskExecutions = Action("ListTaskExecutions")
ListTasks = Action("ListTasks")
StartTaskExecution = Action("StartTaskExecution")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateTask = Action("UpdateTask")
UpdateTaskExecution = Action("UpdateTaskExecution")
