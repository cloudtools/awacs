# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Parallel Computing Service"
prefix = "pcs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
CreateCluster = Action("CreateCluster")
CreateComputeNodeGroup = Action("CreateComputeNodeGroup")
CreateQueue = Action("CreateQueue")
DeleteCluster = Action("DeleteCluster")
DeleteComputeNodeGroup = Action("DeleteComputeNodeGroup")
DeleteQueue = Action("DeleteQueue")
GetCluster = Action("GetCluster")
GetComputeNodeGroup = Action("GetComputeNodeGroup")
GetQueue = Action("GetQueue")
ListClusters = Action("ListClusters")
ListComputeNodeGroups = Action("ListComputeNodeGroups")
ListQueues = Action("ListQueues")
ListTagsForResource = Action("ListTagsForResource")
RegisterComputeNodeGroupInstance = Action("RegisterComputeNodeGroupInstance")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateComputeNodeGroup = Action("UpdateComputeNodeGroup")
UpdateQueue = Action("UpdateQueue")
