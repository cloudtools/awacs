# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Resilience Hub Service"
prefix = "resiliencehub"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddDraftAppVersionResourceMappings = Action("AddDraftAppVersionResourceMappings")
CreateApp = Action("CreateApp")
CreateRecommendationTemplate = Action("CreateRecommendationTemplate")
CreateResiliencyPolicy = Action("CreateResiliencyPolicy")
DeleteApp = Action("DeleteApp")
DeleteAppAssessment = Action("DeleteAppAssessment")
DeleteRecommendationTemplate = Action("DeleteRecommendationTemplate")
DeleteResiliencyPolicy = Action("DeleteResiliencyPolicy")
DescribeApp = Action("DescribeApp")
DescribeAppAssessment = Action("DescribeAppAssessment")
DescribeAppVersionResourcesResolutionStatus = Action(
    "DescribeAppVersionResourcesResolutionStatus"
)
DescribeAppVersionTemplate = Action("DescribeAppVersionTemplate")
DescribeDraftAppVersionResourcesImportStatus = Action(
    "DescribeDraftAppVersionResourcesImportStatus"
)
DescribeResiliencyPolicy = Action("DescribeResiliencyPolicy")
ImportResourcesToDraftAppVersion = Action("ImportResourcesToDraftAppVersion")
ListAlarmRecommendations = Action("ListAlarmRecommendations")
ListAppAssessments = Action("ListAppAssessments")
ListAppComponentCompliances = Action("ListAppComponentCompliances")
ListAppComponentRecommendations = Action("ListAppComponentRecommendations")
ListAppVersionResourceMappings = Action("ListAppVersionResourceMappings")
ListAppVersionResources = Action("ListAppVersionResources")
ListAppVersions = Action("ListAppVersions")
ListApps = Action("ListApps")
ListRecommendationTemplates = Action("ListRecommendationTemplates")
ListResiliencyPolicies = Action("ListResiliencyPolicies")
ListSopRecommendations = Action("ListSopRecommendations")
ListSuggestedResiliencyPolicies = Action("ListSuggestedResiliencyPolicies")
ListTagsForResource = Action("ListTagsForResource")
ListTestRecommendations = Action("ListTestRecommendations")
ListUnsupportedAppVersionResources = Action("ListUnsupportedAppVersionResources")
PublishAppVersion = Action("PublishAppVersion")
PutDraftAppVersionTemplate = Action("PutDraftAppVersionTemplate")
RemoveDraftAppVersionResourceMappings = Action("RemoveDraftAppVersionResourceMappings")
ResolveAppVersionResources = Action("ResolveAppVersionResources")
StartAppAssessment = Action("StartAppAssessment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApp = Action("UpdateApp")
UpdateResiliencyPolicy = Action("UpdateResiliencyPolicy")
