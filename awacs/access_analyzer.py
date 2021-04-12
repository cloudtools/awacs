# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IAM Access Analyzer"
prefix = "access-analyzer"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ApplyArchiveRule = Action("ApplyArchiveRule")
CancelPolicyGeneration = Action("CancelPolicyGeneration")
CreateAccessPreview = Action("CreateAccessPreview")
CreateAnalyzer = Action("CreateAnalyzer")
CreateArchiveRule = Action("CreateArchiveRule")
DeleteAnalyzer = Action("DeleteAnalyzer")
DeleteArchiveRule = Action("DeleteArchiveRule")
GetAccessPreview = Action("GetAccessPreview")
GetAnalyzedResource = Action("GetAnalyzedResource")
GetAnalyzer = Action("GetAnalyzer")
GetArchiveRule = Action("GetArchiveRule")
GetFinding = Action("GetFinding")
GetGeneratedPolicy = Action("GetGeneratedPolicy")
ListAccessPreviewFindings = Action("ListAccessPreviewFindings")
ListAccessPreviews = Action("ListAccessPreviews")
ListAnalyzedResources = Action("ListAnalyzedResources")
ListAnalyzers = Action("ListAnalyzers")
ListArchiveRules = Action("ListArchiveRules")
ListFindings = Action("ListFindings")
ListPolicyGenerations = Action("ListPolicyGenerations")
ListTagsForResource = Action("ListTagsForResource")
StartPolicyGeneration = Action("StartPolicyGeneration")
StartResourceScan = Action("StartResourceScan")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateArchiveRule = Action("UpdateArchiveRule")
UpdateFindings = Action("UpdateFindings")
ValidatePolicy = Action("ValidatePolicy")
