# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CodeGuru Security"
prefix = "codeguru-security"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetFindings = Action("BatchGetFindings")
CreateScan = Action("CreateScan")
CreateUploadUrl = Action("CreateUploadUrl")
DeleteScansByCategory = Action("DeleteScansByCategory")
GetAccountConfiguration = Action("GetAccountConfiguration")
GetFindings = Action("GetFindings")
GetMetricsSummary = Action("GetMetricsSummary")
GetScan = Action("GetScan")
ListFindings = Action("ListFindings")
ListFindingsMetrics = Action("ListFindingsMetrics")
ListScans = Action("ListScans")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountConfiguration = Action("UpdateAccountConfiguration")
