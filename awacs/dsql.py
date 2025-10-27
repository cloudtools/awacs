# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Aurora DSQL"
prefix = "dsql"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddPeerCluster = Action("AddPeerCluster")
CreateCluster = Action("CreateCluster")
CreateMultiRegionClusters = Action("CreateMultiRegionClusters")
DbConnect = Action("DbConnect")
DbConnectAdmin = Action("DbConnectAdmin")
DeleteCluster = Action("DeleteCluster")
DeleteClusterPolicy = Action("DeleteClusterPolicy")
DeleteMultiRegionClusters = Action("DeleteMultiRegionClusters")
GetBackupJob = Action("GetBackupJob")
GetCluster = Action("GetCluster")
GetClusterPolicy = Action("GetClusterPolicy")
GetRestoreJob = Action("GetRestoreJob")
GetVpcEndpointServiceName = Action("GetVpcEndpointServiceName")
InjectError = Action("InjectError")
ListClusters = Action("ListClusters")
ListTagsForResource = Action("ListTagsForResource")
PutClusterPolicy = Action("PutClusterPolicy")
PutMultiRegionProperties = Action("PutMultiRegionProperties")
PutWitnessRegion = Action("PutWitnessRegion")
RemovePeerCluster = Action("RemovePeerCluster")
StartBackupJob = Action("StartBackupJob")
StartRestoreJob = Action("StartRestoreJob")
StopBackupJob = Action("StopBackupJob")
StopRestoreJob = Action("StopRestoreJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCluster = Action("UpdateCluster")
