# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Timestream InfluxDB"
prefix = "timestream-influxdb"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateDbCluster = Action("CreateDbCluster")
CreateDbInstance = Action("CreateDbInstance")
CreateDbParameterGroup = Action("CreateDbParameterGroup")
DeleteDbCluster = Action("DeleteDbCluster")
DeleteDbInstance = Action("DeleteDbInstance")
GetDbCluster = Action("GetDbCluster")
GetDbInstance = Action("GetDbInstance")
GetDbParameterGroup = Action("GetDbParameterGroup")
ListDbClusters = Action("ListDbClusters")
ListDbInstances = Action("ListDbInstances")
ListDbInstancesForCluster = Action("ListDbInstancesForCluster")
ListDbParameterGroups = Action("ListDbParameterGroups")
ListTagsForResource = Action("ListTagsForResource")
RebootDbCluster = Action("RebootDbCluster")
RebootDbInstance = Action("RebootDbInstance")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDbCluster = Action("UpdateDbCluster")
UpdateDbInstance = Action("UpdateDbInstance")
