# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Synthetics"
prefix = "synthetics"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateResource = Action("AssociateResource")
CreateCanary = Action("CreateCanary")
CreateGroup = Action("CreateGroup")
DeleteCanary = Action("DeleteCanary")
DeleteGroup = Action("DeleteGroup")
DescribeCanaries = Action("DescribeCanaries")
DescribeCanariesLastRun = Action("DescribeCanariesLastRun")
DescribeRuntimeVersions = Action("DescribeRuntimeVersions")
DisassociateResource = Action("DisassociateResource")
GetCanary = Action("GetCanary")
GetCanaryRuns = Action("GetCanaryRuns")
GetGroup = Action("GetGroup")
ListAssociatedGroups = Action("ListAssociatedGroups")
ListGroupResources = Action("ListGroupResources")
ListGroups = Action("ListGroups")
ListTagsForResource = Action("ListTagsForResource")
StartCanary = Action("StartCanary")
StopCanary = Action("StopCanary")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCanary = Action("UpdateCanary")
