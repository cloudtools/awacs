# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon MemoryDB"
prefix = "memorydb"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchUpdateCluster = Action("BatchUpdateCluster")
BatchUpdateClusters = Action("BatchUpdateClusters")
Connect = Action("Connect")
CopySnapshot = Action("CopySnapshot")
CreateAcl = Action("CreateAcl")
CreateCluster = Action("CreateCluster")
CreateMultiRegionCluster = Action("CreateMultiRegionCluster")
CreateParameterGroup = Action("CreateParameterGroup")
CreateSnapshot = Action("CreateSnapshot")
CreateSubnetGroup = Action("CreateSubnetGroup")
CreateUser = Action("CreateUser")
DeleteAcl = Action("DeleteAcl")
DeleteCluster = Action("DeleteCluster")
DeleteMultiRegionCluster = Action("DeleteMultiRegionCluster")
DeleteParameterGroup = Action("DeleteParameterGroup")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteSubnetGroup = Action("DeleteSubnetGroup")
DeleteUser = Action("DeleteUser")
DescribeAcls = Action("DescribeAcls")
DescribeClusters = Action("DescribeClusters")
DescribeEngineVersions = Action("DescribeEngineVersions")
DescribeEvents = Action("DescribeEvents")
DescribeMultiRegionClusters = Action("DescribeMultiRegionClusters")
DescribeMultiRegionParameterGroups = Action("DescribeMultiRegionParameterGroups")
DescribeMultiRegionParameters = Action("DescribeMultiRegionParameters")
DescribeParameterGroups = Action("DescribeParameterGroups")
DescribeParameters = Action("DescribeParameters")
DescribeReservedNodes = Action("DescribeReservedNodes")
DescribeReservedNodesOfferings = Action("DescribeReservedNodesOfferings")
DescribeServiceUpdates = Action("DescribeServiceUpdates")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeSubnetGroups = Action("DescribeSubnetGroups")
DescribeUsers = Action("DescribeUsers")
FailoverShard = Action("FailoverShard")
ListAllowedMultiRegionClusterUpdates = Action("ListAllowedMultiRegionClusterUpdates")
ListAllowedNodeTypeUpdates = Action("ListAllowedNodeTypeUpdates")
ListNodeTypeUpdates = Action("ListNodeTypeUpdates")
ListTags = Action("ListTags")
PurchaseReservedNodesOffering = Action("PurchaseReservedNodesOffering")
ResetParameterGroup = Action("ResetParameterGroup")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAcl = Action("UpdateAcl")
UpdateCluster = Action("UpdateCluster")
UpdateMultiRegionCluster = Action("UpdateMultiRegionCluster")
UpdateParameterGroup = Action("UpdateParameterGroup")
UpdateSubnetGroup = Action("UpdateSubnetGroup")
UpdateUser = Action("UpdateUser")
