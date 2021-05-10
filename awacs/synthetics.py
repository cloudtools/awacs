# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Synthetics"
prefix = "synthetics"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCanary = Action("CreateCanary")
DeleteCanary = Action("DeleteCanary")
DescribeCanaries = Action("DescribeCanaries")
DescribeCanariesLastRun = Action("DescribeCanariesLastRun")
DescribeRuntimeVersions = Action("DescribeRuntimeVersions")
GetCanary = Action("GetCanary")
GetCanaryRuns = Action("GetCanaryRuns")
ListTagsForResource = Action("ListTagsForResource")
StartCanary = Action("StartCanary")
StopCanary = Action("StopCanary")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCanary = Action("UpdateCanary")
