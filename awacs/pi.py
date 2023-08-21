# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Performance Insights"
prefix = "pi"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreatePerformanceAnalysisReport = Action("CreatePerformanceAnalysisReport")
DeletePerformanceAnalysisReport = Action("DeletePerformanceAnalysisReport")
DescribeDimensionKeys = Action("DescribeDimensionKeys")
GetDimensionKeyDetails = Action("GetDimensionKeyDetails")
GetPerformanceAnalysisReport = Action("GetPerformanceAnalysisReport")
GetResourceMetadata = Action("GetResourceMetadata")
GetResourceMetrics = Action("GetResourceMetrics")
ListAvailableResourceDimensions = Action("ListAvailableResourceDimensions")
ListAvailableResourceMetrics = Action("ListAvailableResourceMetrics")
ListPerformanceAnalysisReports = Action("ListPerformanceAnalysisReports")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
