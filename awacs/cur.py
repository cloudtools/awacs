# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Cost and Usage Report"
prefix = "cur"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DeleteReportDefinition = Action("DeleteReportDefinition")
DescribeReportDefinitions = Action("DescribeReportDefinitions")
GetClassicReport = Action("GetClassicReport")
GetClassicReportPreferences = Action("GetClassicReportPreferences")
GetUsageReport = Action("GetUsageReport")
ListTagsForResource = Action("ListTagsForResource")
ModifyReportDefinition = Action("ModifyReportDefinition")
PutClassicReportPreferences = Action("PutClassicReportPreferences")
PutReportDefinition = Action("PutReportDefinition")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
ValidateReportDestination = Action("ValidateReportDestination")
