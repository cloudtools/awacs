# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Inspector"
prefix = "inspector"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddAttributesToFindings = Action("AddAttributesToFindings")
CreateAssessmentTarget = Action("CreateAssessmentTarget")
CreateAssessmentTemplate = Action("CreateAssessmentTemplate")
CreateExclusionsPreview = Action("CreateExclusionsPreview")
CreateResourceGroup = Action("CreateResourceGroup")
DeleteAssessmentRun = Action("DeleteAssessmentRun")
DeleteAssessmentTarget = Action("DeleteAssessmentTarget")
DeleteAssessmentTemplate = Action("DeleteAssessmentTemplate")
DescribeAssessmentRuns = Action("DescribeAssessmentRuns")
DescribeAssessmentTargets = Action("DescribeAssessmentTargets")
DescribeAssessmentTemplates = Action("DescribeAssessmentTemplates")
DescribeCrossAccountAccessRole = Action("DescribeCrossAccountAccessRole")
DescribeExclusions = Action("DescribeExclusions")
DescribeFindings = Action("DescribeFindings")
DescribeResourceGroups = Action("DescribeResourceGroups")
DescribeRulesPackages = Action("DescribeRulesPackages")
GetAssessmentReport = Action("GetAssessmentReport")
GetExclusionsPreview = Action("GetExclusionsPreview")
GetTelemetryMetadata = Action("GetTelemetryMetadata")
ListAssessmentRunAgents = Action("ListAssessmentRunAgents")
ListAssessmentRuns = Action("ListAssessmentRuns")
ListAssessmentTargets = Action("ListAssessmentTargets")
ListAssessmentTemplates = Action("ListAssessmentTemplates")
ListEventSubscriptions = Action("ListEventSubscriptions")
ListExclusions = Action("ListExclusions")
ListFindings = Action("ListFindings")
ListRulesPackages = Action("ListRulesPackages")
ListTagsForResource = Action("ListTagsForResource")
PreviewAgents = Action("PreviewAgents")
RegisterCrossAccountAccessRole = Action("RegisterCrossAccountAccessRole")
RemoveAttributesFromFindings = Action("RemoveAttributesFromFindings")
SetTagsForResource = Action("SetTagsForResource")
StartAssessmentRun = Action("StartAssessmentRun")
StopAssessmentRun = Action("StopAssessmentRun")
SubscribeToEvent = Action("SubscribeToEvent")
UnsubscribeFromEvent = Action("UnsubscribeFromEvent")
UpdateAssessmentTarget = Action("UpdateAssessmentTarget")
