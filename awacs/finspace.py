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
CreateKxEnvironment = Action("CreateKxEnvironment")
CreateKxUser = Action("CreateKxUser")
CreateUser = Action("CreateUser")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteKxCluster = Action("DeleteKxCluster")
DeleteKxDatabase = Action("DeleteKxDatabase")
DeleteKxEnvironment = Action("DeleteKxEnvironment")
DeleteKxUser = Action("DeleteKxUser")
DeleteUser = Action("DeleteUser")
GetEnvironment = Action("GetEnvironment")
GetKxChangeset = Action("GetKxChangeset")
GetKxCluster = Action("GetKxCluster")
GetKxConnectionString = Action("GetKxConnectionString")
GetKxDatabase = Action("GetKxDatabase")
GetKxEnvironment = Action("GetKxEnvironment")
GetKxUser = Action("GetKxUser")
GetLoadSampleDataSetGroupIntoEnvironmentStatus = Action(
    "GetLoadSampleDataSetGroupIntoEnvironmentStatus"
)
GetUser = Action("GetUser")
ListEnvironments = Action("ListEnvironments")
ListKxChangesets = Action("ListKxChangesets")
ListKxClusterNodes = Action("ListKxClusterNodes")
ListKxClusters = Action("ListKxClusters")
ListKxDatabases = Action("ListKxDatabases")
ListKxEnvironments = Action("ListKxEnvironments")
ListKxUsers = Action("ListKxUsers")
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
UpdateKxEnvironment = Action("UpdateKxEnvironment")
UpdateKxEnvironmentNetwork = Action("UpdateKxEnvironmentNetwork")
UpdateKxUser = Action("UpdateKxUser")
UpdateUser = Action("UpdateUser")
