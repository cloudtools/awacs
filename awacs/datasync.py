# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DataSync"
prefix = "datasync"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddStorageSystem = Action("AddStorageSystem")
CancelTaskExecution = Action("CancelTaskExecution")
CreateAgent = Action("CreateAgent")
CreateLocationAzureBlob = Action("CreateLocationAzureBlob")
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
DescribeDiscoveryJob = Action("DescribeDiscoveryJob")
DescribeLocationAzureBlob = Action("DescribeLocationAzureBlob")
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
DescribeStorageSystem = Action("DescribeStorageSystem")
DescribeStorageSystemResourceMetrics = Action("DescribeStorageSystemResourceMetrics")
DescribeStorageSystemResources = Action("DescribeStorageSystemResources")
DescribeTask = Action("DescribeTask")
DescribeTaskExecution = Action("DescribeTaskExecution")
GenerateRecommendations = Action("GenerateRecommendations")
ListAgents = Action("ListAgents")
ListDiscoveryJobs = Action("ListDiscoveryJobs")
ListLocations = Action("ListLocations")
ListStorageSystems = Action("ListStorageSystems")
ListTagsForResource = Action("ListTagsForResource")
ListTaskExecutions = Action("ListTaskExecutions")
ListTasks = Action("ListTasks")
RemoveStorageSystem = Action("RemoveStorageSystem")
StartDiscoveryJob = Action("StartDiscoveryJob")
StartTaskExecution = Action("StartTaskExecution")
StopDiscoveryJob = Action("StopDiscoveryJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateDiscoveryJob = Action("UpdateDiscoveryJob")
UpdateLocationAzureBlob = Action("UpdateLocationAzureBlob")
UpdateLocationEfs = Action("UpdateLocationEfs")
UpdateLocationFsxLustre = Action("UpdateLocationFsxLustre")
UpdateLocationFsxOntap = Action("UpdateLocationFsxOntap")
UpdateLocationFsxOpenZfs = Action("UpdateLocationFsxOpenZfs")
UpdateLocationFsxWindows = Action("UpdateLocationFsxWindows")
UpdateLocationHdfs = Action("UpdateLocationHdfs")
UpdateLocationNfs = Action("UpdateLocationNfs")
UpdateLocationObjectStorage = Action("UpdateLocationObjectStorage")
UpdateLocationS3 = Action("UpdateLocationS3")
UpdateLocationSmb = Action("UpdateLocationSmb")
UpdateStorageSystem = Action("UpdateStorageSystem")
UpdateTask = Action("UpdateTask")
UpdateTaskExecution = Action("UpdateTaskExecution")
