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


CreateCluster = Action("CreateCluster")
CreateMultiRegionClusters = Action("CreateMultiRegionClusters")
DbConnect = Action("DbConnect")
DbConnectAdmin = Action("DbConnectAdmin")
DeleteCluster = Action("DeleteCluster")
DeleteMultiRegionClusters = Action("DeleteMultiRegionClusters")
GetCluster = Action("GetCluster")
ListClusters = Action("ListClusters")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCluster = Action("UpdateCluster")
