# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Application Insights"
prefix = "applicationinsights"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddWorkload = Action("AddWorkload")
CreateApplication = Action("CreateApplication")
CreateComponent = Action("CreateComponent")
CreateLogPattern = Action("CreateLogPattern")
DeleteApplication = Action("DeleteApplication")
DeleteComponent = Action("DeleteComponent")
DeleteLogPattern = Action("DeleteLogPattern")
DescribeApplication = Action("DescribeApplication")
DescribeComponent = Action("DescribeComponent")
DescribeComponentConfiguration = Action("DescribeComponentConfiguration")
DescribeComponentConfigurationRecommendation = Action(
    "DescribeComponentConfigurationRecommendation"
)
DescribeLogPattern = Action("DescribeLogPattern")
DescribeObservation = Action("DescribeObservation")
DescribeProblem = Action("DescribeProblem")
DescribeProblemObservations = Action("DescribeProblemObservations")
DescribeWorkload = Action("DescribeWorkload")
Link = Action("Link")
ListApplications = Action("ListApplications")
ListComponents = Action("ListComponents")
ListConfigurationHistory = Action("ListConfigurationHistory")
ListLogPatternSets = Action("ListLogPatternSets")
ListLogPatterns = Action("ListLogPatterns")
ListProblems = Action("ListProblems")
ListTagsForResource = Action("ListTagsForResource")
ListWorkloads = Action("ListWorkloads")
RemoveWorkload = Action("RemoveWorkload")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateComponent = Action("UpdateComponent")
UpdateComponentConfiguration = Action("UpdateComponentConfiguration")
UpdateLogPattern = Action("UpdateLogPattern")
UpdateProblem = Action("UpdateProblem")
UpdateWorkload = Action("UpdateWorkload")
