# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS X-Ray"
prefix = "xray"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetTraces = Action("BatchGetTraces")
CreateGroup = Action("CreateGroup")
CreateSamplingRule = Action("CreateSamplingRule")
DeleteGroup = Action("DeleteGroup")
DeleteSamplingRule = Action("DeleteSamplingRule")
GetEncryptionConfig = Action("GetEncryptionConfig")
GetGroup = Action("GetGroup")
GetGroups = Action("GetGroups")
GetInsight = Action("GetInsight")
GetInsightEvents = Action("GetInsightEvents")
GetInsightImpactGraph = Action("GetInsightImpactGraph")
GetInsightSummaries = Action("GetInsightSummaries")
GetSamplingRules = Action("GetSamplingRules")
GetSamplingStatisticSummaries = Action("GetSamplingStatisticSummaries")
GetSamplingTargets = Action("GetSamplingTargets")
GetServiceGraph = Action("GetServiceGraph")
GetTimeSeriesServiceStatistics = Action("GetTimeSeriesServiceStatistics")
GetTraceGraph = Action("GetTraceGraph")
GetTraceSummaries = Action("GetTraceSummaries")
ListTagsForResource = Action("ListTagsForResource")
PutEncryptionConfig = Action("PutEncryptionConfig")
PutTelemetryRecords = Action("PutTelemetryRecords")
PutTraceSegments = Action("PutTraceSegments")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGroup = Action("UpdateGroup")
UpdateSamplingRule = Action("UpdateSamplingRule")
