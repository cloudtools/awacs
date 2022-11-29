# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Resource Group Tagging API"
prefix = "tag"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddResourceTags = Action("AddResourceTags")
DescribeReportCreation = Action("DescribeReportCreation")
GetComplianceSummary = Action("GetComplianceSummary")
GetResources = Action("GetResources")
GetTagKeys = Action("GetTagKeys")
GetTagValues = Action("GetTagValues")
RemoveResourceTags = Action("RemoveResourceTags")
StartReportCreation = Action("StartReportCreation")
TagResources = Action("TagResources")
UntagResources = Action("UntagResources")
