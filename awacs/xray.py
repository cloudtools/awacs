# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS X-Ray"
prefix = "xray"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetTraceSummaryById = Action("BatchGetTraceSummaryById")
BatchGetTraces = Action("BatchGetTraces")
CancelTraceRetrieval = Action("CancelTraceRetrieval")
CreateGroup = Action("CreateGroup")
CreateSamplingRule = Action("CreateSamplingRule")
DeleteGroup = Action("DeleteGroup")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSamplingRule = Action("DeleteSamplingRule")
GetDistinctTraceGraphs = Action("GetDistinctTraceGraphs")
GetEncryptionConfig = Action("GetEncryptionConfig")
GetGroup = Action("GetGroup")
GetGroups = Action("GetGroups")
GetIndexingRules = Action("GetIndexingRules")
GetInsight = Action("GetInsight")
GetInsightEvents = Action("GetInsightEvents")
GetInsightImpactGraph = Action("GetInsightImpactGraph")
GetInsightSummaries = Action("GetInsightSummaries")
GetRetrievedTracesGraph = Action("GetRetrievedTracesGraph")
GetSamplingRules = Action("GetSamplingRules")
GetSamplingStatisticSummaries = Action("GetSamplingStatisticSummaries")
GetSamplingTargets = Action("GetSamplingTargets")
GetServiceGraph = Action("GetServiceGraph")
GetTimeSeriesServiceStatistics = Action("GetTimeSeriesServiceStatistics")
GetTraceGraph = Action("GetTraceGraph")
GetTraceSegmentDestination = Action("GetTraceSegmentDestination")
GetTraceSummaries = Action("GetTraceSummaries")
Link = Action("Link")
ListResourcePolicies = Action("ListResourcePolicies")
ListRetrievedTraces = Action("ListRetrievedTraces")
ListTagsForResource = Action("ListTagsForResource")
PutEncryptionConfig = Action("PutEncryptionConfig")
PutResourcePolicy = Action("PutResourcePolicy")
PutSpans = Action("PutSpans")
PutSpansForIndexing = Action("PutSpansForIndexing")
PutTelemetryRecords = Action("PutTelemetryRecords")
PutTraceSegments = Action("PutTraceSegments")
StartTraceRetrieval = Action("StartTraceRetrieval")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGroup = Action("UpdateGroup")
UpdateIndexingRule = Action("UpdateIndexingRule")
UpdateSamplingRule = Action("UpdateSamplingRule")
UpdateTraceSegmentDestination = Action("UpdateTraceSegmentDestination")
