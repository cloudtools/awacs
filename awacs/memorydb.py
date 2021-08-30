# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon MemoryDB"
prefix = "memorydb"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchUpdateClusters = Action("BatchUpdateClusters")
CopySnapshot = Action("CopySnapshot")
CreateAcl = Action("CreateAcl")
CreateCluster = Action("CreateCluster")
CreateParameterGroup = Action("CreateParameterGroup")
CreateSnapshot = Action("CreateSnapshot")
CreateSubnetGroup = Action("CreateSubnetGroup")
CreateUser = Action("CreateUser")
DeleteAcl = Action("DeleteAcl")
DeleteCluster = Action("DeleteCluster")
DeleteParameterGroup = Action("DeleteParameterGroup")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteSubnetGroup = Action("DeleteSubnetGroup")
DeleteUser = Action("DeleteUser")
DescribeAcls = Action("DescribeAcls")
DescribeClusters = Action("DescribeClusters")
DescribeEngineVersions = Action("DescribeEngineVersions")
DescribeEvents = Action("DescribeEvents")
DescribeParameterGroups = Action("DescribeParameterGroups")
DescribeParameters = Action("DescribeParameters")
DescribeServiceUpdates = Action("DescribeServiceUpdates")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeSubnetGroups = Action("DescribeSubnetGroups")
DescribeUsers = Action("DescribeUsers")
FailoverShard = Action("FailoverShard")
ListNodeTypeUpdates = Action("ListNodeTypeUpdates")
ListTags = Action("ListTags")
ResetParameterGroup = Action("ResetParameterGroup")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAcl = Action("UpdateAcl")
UpdateCluster = Action("UpdateCluster")
UpdateParameterGroup = Action("UpdateParameterGroup")
UpdateSubnetGroup = Action("UpdateSubnetGroup")
UpdateUser = Action("UpdateUser")
