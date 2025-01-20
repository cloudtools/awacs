# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon DocumentDB Elastic Clusters"
prefix = "docdb-elastic"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ApplyPendingMaintenanceAction = Action("ApplyPendingMaintenanceAction")
CopyClusterSnapshot = Action("CopyClusterSnapshot")
CreateCluster = Action("CreateCluster")
CreateClusterSnapshot = Action("CreateClusterSnapshot")
DeleteCluster = Action("DeleteCluster")
DeleteClusterSnapshot = Action("DeleteClusterSnapshot")
GetCluster = Action("GetCluster")
GetClusterSnapshot = Action("GetClusterSnapshot")
GetPendingMaintenanceAction = Action("GetPendingMaintenanceAction")
ListClusterSnapshots = Action("ListClusterSnapshots")
ListClusters = Action("ListClusters")
ListPendingMaintenanceActions = Action("ListPendingMaintenanceActions")
ListTagsForResource = Action("ListTagsForResource")
RestoreClusterFromSnapshot = Action("RestoreClusterFromSnapshot")
StartCluster = Action("StartCluster")
StopCluster = Action("StopCluster")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCluster = Action("UpdateCluster")
