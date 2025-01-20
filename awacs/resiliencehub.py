# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Resilience Hub"
prefix = "resiliencehub"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptResourceGroupingRecommendations = Action("AcceptResourceGroupingRecommendations")
AddDraftAppVersionResourceMappings = Action("AddDraftAppVersionResourceMappings")
BatchUpdateRecommendationStatus = Action("BatchUpdateRecommendationStatus")
CreateApp = Action("CreateApp")
CreateAppVersionAppComponent = Action("CreateAppVersionAppComponent")
CreateAppVersionResource = Action("CreateAppVersionResource")
CreateRecommendationTemplate = Action("CreateRecommendationTemplate")
CreateResiliencyPolicy = Action("CreateResiliencyPolicy")
DeleteApp = Action("DeleteApp")
DeleteAppAssessment = Action("DeleteAppAssessment")
DeleteAppInputSource = Action("DeleteAppInputSource")
DeleteAppVersionAppComponent = Action("DeleteAppVersionAppComponent")
DeleteAppVersionResource = Action("DeleteAppVersionResource")
DeleteRecommendationTemplate = Action("DeleteRecommendationTemplate")
DeleteResiliencyPolicy = Action("DeleteResiliencyPolicy")
DescribeApp = Action("DescribeApp")
DescribeAppAssessment = Action("DescribeAppAssessment")
DescribeAppVersion = Action("DescribeAppVersion")
DescribeAppVersionAppComponent = Action("DescribeAppVersionAppComponent")
DescribeAppVersionResource = Action("DescribeAppVersionResource")
DescribeAppVersionResourcesResolutionStatus = Action(
    "DescribeAppVersionResourcesResolutionStatus"
)
DescribeAppVersionTemplate = Action("DescribeAppVersionTemplate")
DescribeDraftAppVersionResourcesImportStatus = Action(
    "DescribeDraftAppVersionResourcesImportStatus"
)
DescribeMetricsExport = Action("DescribeMetricsExport")
DescribeResiliencyPolicy = Action("DescribeResiliencyPolicy")
DescribeResourceGroupingRecommendationTask = Action(
    "DescribeResourceGroupingRecommendationTask"
)
ImportResourcesToDraftAppVersion = Action("ImportResourcesToDraftAppVersion")
ListAlarmRecommendations = Action("ListAlarmRecommendations")
ListAppAssessmentComplianceDrifts = Action("ListAppAssessmentComplianceDrifts")
ListAppAssessmentResourceDrifts = Action("ListAppAssessmentResourceDrifts")
ListAppAssessments = Action("ListAppAssessments")
ListAppComponentCompliances = Action("ListAppComponentCompliances")
ListAppComponentRecommendations = Action("ListAppComponentRecommendations")
ListAppInputSources = Action("ListAppInputSources")
ListAppVersionAppComponents = Action("ListAppVersionAppComponents")
ListAppVersionResourceMappings = Action("ListAppVersionResourceMappings")
ListAppVersionResources = Action("ListAppVersionResources")
ListAppVersions = Action("ListAppVersions")
ListApps = Action("ListApps")
ListMetrics = Action("ListMetrics")
ListRecommendationTemplates = Action("ListRecommendationTemplates")
ListResiliencyPolicies = Action("ListResiliencyPolicies")
ListResourceGroupingRecommendations = Action("ListResourceGroupingRecommendations")
ListSopRecommendations = Action("ListSopRecommendations")
ListSuggestedResiliencyPolicies = Action("ListSuggestedResiliencyPolicies")
ListTagsForResource = Action("ListTagsForResource")
ListTestRecommendations = Action("ListTestRecommendations")
ListUnsupportedAppVersionResources = Action("ListUnsupportedAppVersionResources")
PublishAppVersion = Action("PublishAppVersion")
PutDraftAppVersionTemplate = Action("PutDraftAppVersionTemplate")
RejectResourceGroupingRecommendations = Action("RejectResourceGroupingRecommendations")
RemoveDraftAppVersionResourceMappings = Action("RemoveDraftAppVersionResourceMappings")
ResolveAppVersionResources = Action("ResolveAppVersionResources")
StartAppAssessment = Action("StartAppAssessment")
StartMetricsExport = Action("StartMetricsExport")
StartResourceGroupingRecommendationTask = Action(
    "StartResourceGroupingRecommendationTask"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApp = Action("UpdateApp")
UpdateAppVersion = Action("UpdateAppVersion")
UpdateAppVersionAppComponent = Action("UpdateAppVersionAppComponent")
UpdateAppVersionResource = Action("UpdateAppVersionResource")
UpdateResiliencyPolicy = Action("UpdateResiliencyPolicy")
