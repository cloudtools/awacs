# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CodeGuru Profiler"
prefix = "codeguru-profiler"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddNotificationChannels = Action("AddNotificationChannels")
BatchGetFrameMetricData = Action("BatchGetFrameMetricData")
ConfigureAgent = Action("ConfigureAgent")
CreateProfilingGroup = Action("CreateProfilingGroup")
DeleteProfilingGroup = Action("DeleteProfilingGroup")
DescribeProfilingGroup = Action("DescribeProfilingGroup")
GetFindingsReportAccountSummary = Action("GetFindingsReportAccountSummary")
GetNotificationConfiguration = Action("GetNotificationConfiguration")
GetPolicy = Action("GetPolicy")
GetProfile = Action("GetProfile")
GetRecommendations = Action("GetRecommendations")
ListFindingsReports = Action("ListFindingsReports")
ListProfileTimes = Action("ListProfileTimes")
ListProfilingGroups = Action("ListProfilingGroups")
ListTagsForResource = Action("ListTagsForResource")
PostAgentProfile = Action("PostAgentProfile")
PutPermission = Action("PutPermission")
RemoveNotificationChannel = Action("RemoveNotificationChannel")
RemovePermission = Action("RemovePermission")
SubmitFeedback = Action("SubmitFeedback")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateProfilingGroup = Action("UpdateProfilingGroup")
