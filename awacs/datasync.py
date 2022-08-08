# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DataSync"
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
CreateLocationFsxLustre = Action("CreateLocationFsxLustre")
CreateLocationFsxOntap = Action("CreateLocationFsxOntap")
CreateLocationFsxOpenZfs = Action("CreateLocationFsxOpenZfs")
CreateLocationFsxWindows = Action("CreateLocationFsxWindows")
CreateLocationHdfs = Action("CreateLocationHdfs")
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
DescribeLocationFsxLustre = Action("DescribeLocationFsxLustre")
DescribeLocationFsxOntap = Action("DescribeLocationFsxOntap")
DescribeLocationFsxOpenZfs = Action("DescribeLocationFsxOpenZfs")
DescribeLocationFsxWindows = Action("DescribeLocationFsxWindows")
DescribeLocationHdfs = Action("DescribeLocationHdfs")
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
UpdateLocationHdfs = Action("UpdateLocationHdfs")
UpdateLocationNfs = Action("UpdateLocationNfs")
UpdateLocationObjectStorage = Action("UpdateLocationObjectStorage")
UpdateLocationSmb = Action("UpdateLocationSmb")
UpdateTask = Action("UpdateTask")
UpdateTaskExecution = Action("UpdateTaskExecution")
