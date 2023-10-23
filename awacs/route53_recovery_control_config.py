# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53 Recovery Controls"
prefix = "route53-recovery-control-config"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCluster = Action("CreateCluster")
CreateControlPanel = Action("CreateControlPanel")
CreateRoutingControl = Action("CreateRoutingControl")
CreateSafetyRule = Action("CreateSafetyRule")
DeleteCluster = Action("DeleteCluster")
DeleteControlPanel = Action("DeleteControlPanel")
DeleteRoutingControl = Action("DeleteRoutingControl")
DeleteSafetyRule = Action("DeleteSafetyRule")
DescribeCluster = Action("DescribeCluster")
DescribeControlPanel = Action("DescribeControlPanel")
DescribeRoutingControl = Action("DescribeRoutingControl")
DescribeRoutingControlByName = Action("DescribeRoutingControlByName")
DescribeSafetyRule = Action("DescribeSafetyRule")
GetResourcePolicy = Action("GetResourcePolicy")
ListAssociatedRoute53HealthChecks = Action("ListAssociatedRoute53HealthChecks")
ListClusters = Action("ListClusters")
ListControlPanels = Action("ListControlPanels")
ListRoutingControls = Action("ListRoutingControls")
ListSafetyRules = Action("ListSafetyRules")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateControlPanel = Action("UpdateControlPanel")
UpdateRoutingControl = Action("UpdateRoutingControl")
UpdateSafetyRule = Action("UpdateSafetyRule")
