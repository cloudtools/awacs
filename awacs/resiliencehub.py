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
CreateAssertion = Action("CreateAssertion")
CreateInputSource = Action("CreateInputSource")
CreatePolicy = Action("CreatePolicy")
CreateRecommendationTemplate = Action("CreateRecommendationTemplate")
CreateReport = Action("CreateReport")
CreateResiliencyPolicy = Action("CreateResiliencyPolicy")
CreateService = Action("CreateService")
CreateServiceFunction = Action("CreateServiceFunction")
CreateServiceFunctionResources = Action("CreateServiceFunctionResources")
CreateSystem = Action("CreateSystem")
CreateUserJourney = Action("CreateUserJourney")
DeleteApp = Action("DeleteApp")
DeleteAppAssessment = Action("DeleteAppAssessment")
DeleteAppInputSource = Action("DeleteAppInputSource")
DeleteAppVersionAppComponent = Action("DeleteAppVersionAppComponent")
DeleteAppVersionResource = Action("DeleteAppVersionResource")
DeleteAssertion = Action("DeleteAssertion")
DeleteInputSource = Action("DeleteInputSource")
DeletePolicy = Action("DeletePolicy")
DeleteRecommendationTemplate = Action("DeleteRecommendationTemplate")
DeleteResiliencyPolicy = Action("DeleteResiliencyPolicy")
DeleteService = Action("DeleteService")
DeleteServiceFunction = Action("DeleteServiceFunction")
DeleteServiceFunctionResources = Action("DeleteServiceFunctionResources")
DeleteSystem = Action("DeleteSystem")
DeleteUserJourney = Action("DeleteUserJourney")
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
GetFailureModeFinding = Action("GetFailureModeFinding")
GetPolicy = Action("GetPolicy")
GetService = Action("GetService")
GetSystem = Action("GetSystem")
GetUserJourney = Action("GetUserJourney")
ImportApp = Action("ImportApp")
ImportPolicy = Action("ImportPolicy")
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
ListAssertions = Action("ListAssertions")
ListDependencies = Action("ListDependencies")
ListFailureModeAssessments = Action("ListFailureModeAssessments")
ListFailureModeFindings = Action("ListFailureModeFindings")
ListInputSources = Action("ListInputSources")
ListMetrics = Action("ListMetrics")
ListPolicies = Action("ListPolicies")
ListRecommendationTemplates = Action("ListRecommendationTemplates")
ListReports = Action("ListReports")
ListResiliencyPolicies = Action("ListResiliencyPolicies")
ListResourceGroupingRecommendations = Action("ListResourceGroupingRecommendations")
ListResources = Action("ListResources")
ListServiceEvents = Action("ListServiceEvents")
ListServiceFunctions = Action("ListServiceFunctions")
ListServiceTopologyEdges = Action("ListServiceTopologyEdges")
ListServices = Action("ListServices")
ListSopRecommendations = Action("ListSopRecommendations")
ListSuggestedResiliencyPolicies = Action("ListSuggestedResiliencyPolicies")
ListSystemEvents = Action("ListSystemEvents")
ListSystems = Action("ListSystems")
ListTagsForResource = Action("ListTagsForResource")
ListTestRecommendations = Action("ListTestRecommendations")
ListUnsupportedAppVersionResources = Action("ListUnsupportedAppVersionResources")
ListUserJourneys = Action("ListUserJourneys")
PublishAppVersion = Action("PublishAppVersion")
PutDraftAppVersionTemplate = Action("PutDraftAppVersionTemplate")
RejectResourceGroupingRecommendations = Action("RejectResourceGroupingRecommendations")
RemoveDraftAppVersionResourceMappings = Action("RemoveDraftAppVersionResourceMappings")
ResolveAppVersionResources = Action("ResolveAppVersionResources")
StartAppAssessment = Action("StartAppAssessment")
StartFailureModeAssessment = Action("StartFailureModeAssessment")
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
UpdateAssertion = Action("UpdateAssertion")
UpdateDependency = Action("UpdateDependency")
UpdateFailureModeFinding = Action("UpdateFailureModeFinding")
UpdatePolicy = Action("UpdatePolicy")
UpdateResiliencyPolicy = Action("UpdateResiliencyPolicy")
UpdateService = Action("UpdateService")
UpdateServiceFunction = Action("UpdateServiceFunction")
UpdateSystem = Action("UpdateSystem")
UpdateUserJourney = Action("UpdateUserJourney")
