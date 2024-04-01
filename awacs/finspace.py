# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FinSpace"
prefix = "finspace"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ConnectKxCluster = Action("ConnectKxCluster")
CreateEnvironment = Action("CreateEnvironment")
CreateKxChangeset = Action("CreateKxChangeset")
CreateKxCluster = Action("CreateKxCluster")
CreateKxDatabase = Action("CreateKxDatabase")
CreateKxDataview = Action("CreateKxDataview")
CreateKxEnvironment = Action("CreateKxEnvironment")
CreateKxScalingGroup = Action("CreateKxScalingGroup")
CreateKxUser = Action("CreateKxUser")
CreateKxVolume = Action("CreateKxVolume")
CreateUser = Action("CreateUser")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteKxCluster = Action("DeleteKxCluster")
DeleteKxClusterNode = Action("DeleteKxClusterNode")
DeleteKxDatabase = Action("DeleteKxDatabase")
DeleteKxDataview = Action("DeleteKxDataview")
DeleteKxEnvironment = Action("DeleteKxEnvironment")
DeleteKxScalingGroup = Action("DeleteKxScalingGroup")
DeleteKxUser = Action("DeleteKxUser")
DeleteKxVolume = Action("DeleteKxVolume")
DeleteUser = Action("DeleteUser")
GetEnvironment = Action("GetEnvironment")
GetKxChangeset = Action("GetKxChangeset")
GetKxCluster = Action("GetKxCluster")
GetKxConnectionString = Action("GetKxConnectionString")
GetKxDatabase = Action("GetKxDatabase")
GetKxDataview = Action("GetKxDataview")
GetKxEnvironment = Action("GetKxEnvironment")
GetKxScalingGroup = Action("GetKxScalingGroup")
GetKxUser = Action("GetKxUser")
GetKxVolume = Action("GetKxVolume")
GetLoadSampleDataSetGroupIntoEnvironmentStatus = Action(
    "GetLoadSampleDataSetGroupIntoEnvironmentStatus"
)
GetUser = Action("GetUser")
ListEnvironments = Action("ListEnvironments")
ListKxChangesets = Action("ListKxChangesets")
ListKxClusterNodes = Action("ListKxClusterNodes")
ListKxClusters = Action("ListKxClusters")
ListKxDatabases = Action("ListKxDatabases")
ListKxDataviews = Action("ListKxDataviews")
ListKxEnvironments = Action("ListKxEnvironments")
ListKxScalingGroups = Action("ListKxScalingGroups")
ListKxUsers = Action("ListKxUsers")
ListKxVolumes = Action("ListKxVolumes")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
LoadSampleDataSetGroupIntoEnvironment = Action("LoadSampleDataSetGroupIntoEnvironment")
MountKxDatabase = Action("MountKxDatabase")
ResetUserPassword = Action("ResetUserPassword")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateKxClusterCodeConfiguration = Action("UpdateKxClusterCodeConfiguration")
UpdateKxClusterDatabases = Action("UpdateKxClusterDatabases")
UpdateKxDatabase = Action("UpdateKxDatabase")
UpdateKxDataview = Action("UpdateKxDataview")
UpdateKxEnvironment = Action("UpdateKxEnvironment")
UpdateKxEnvironmentNetwork = Action("UpdateKxEnvironmentNetwork")
UpdateKxUser = Action("UpdateKxUser")
UpdateKxVolume = Action("UpdateKxVolume")
UpdateUser = Action("UpdateUser")
