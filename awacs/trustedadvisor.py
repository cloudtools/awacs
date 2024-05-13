# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Trusted Advisor"
prefix = "trustedadvisor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchUpdateRecommendationResourceExclusion = Action(
    "BatchUpdateRecommendationResourceExclusion"
)
CreateEngagement = Action("CreateEngagement")
CreateEngagementAttachment = Action("CreateEngagementAttachment")
CreateEngagementCommunication = Action("CreateEngagementCommunication")
DeleteNotificationConfigurationForDelegatedAdmin = Action(
    "DeleteNotificationConfigurationForDelegatedAdmin"
)
DescribeAccount = Action("DescribeAccount")
DescribeAccountAccess = Action("DescribeAccountAccess")
DescribeCheckItems = Action("DescribeCheckItems")
DescribeCheckRefreshStatuses = Action("DescribeCheckRefreshStatuses")
DescribeCheckStatusHistoryChanges = Action("DescribeCheckStatusHistoryChanges")
DescribeCheckSummaries = Action("DescribeCheckSummaries")
DescribeChecks = Action("DescribeChecks")
DescribeNotificationConfigurations = Action("DescribeNotificationConfigurations")
DescribeNotificationPreferences = Action("DescribeNotificationPreferences")
DescribeOrganization = Action("DescribeOrganization")
DescribeOrganizationAccounts = Action("DescribeOrganizationAccounts")
DescribeReports = Action("DescribeReports")
DescribeRisk = Action("DescribeRisk")
DescribeRiskResources = Action("DescribeRiskResources")
DescribeRisks = Action("DescribeRisks")
DescribeServiceMetadata = Action("DescribeServiceMetadata")
DownloadRisk = Action("DownloadRisk")
ExcludeCheckItems = Action("ExcludeCheckItems")
GenerateReport = Action("GenerateReport")
GetEngagement = Action("GetEngagement")
GetEngagementAttachment = Action("GetEngagementAttachment")
GetEngagementType = Action("GetEngagementType")
GetOrganizationRecommendation = Action("GetOrganizationRecommendation")
GetRecommendation = Action("GetRecommendation")
IncludeCheckItems = Action("IncludeCheckItems")
ListAccountsForParent = Action("ListAccountsForParent")
ListChecks = Action("ListChecks")
ListEngagementCommunications = Action("ListEngagementCommunications")
ListEngagementTypes = Action("ListEngagementTypes")
ListEngagements = Action("ListEngagements")
ListOrganizationRecommendationAccounts = Action(
    "ListOrganizationRecommendationAccounts"
)
ListOrganizationRecommendationResources = Action(
    "ListOrganizationRecommendationResources"
)
ListOrganizationRecommendations = Action("ListOrganizationRecommendations")
ListOrganizationalUnitsForParent = Action("ListOrganizationalUnitsForParent")
ListRecommendationResources = Action("ListRecommendationResources")
ListRecommendations = Action("ListRecommendations")
ListRoots = Action("ListRoots")
RefreshCheck = Action("RefreshCheck")
SetAccountAccess = Action("SetAccountAccess")
SetOrganizationAccess = Action("SetOrganizationAccess")
UpdateEngagement = Action("UpdateEngagement")
UpdateEngagementStatus = Action("UpdateEngagementStatus")
UpdateNotificationConfigurations = Action("UpdateNotificationConfigurations")
UpdateNotificationPreferences = Action("UpdateNotificationPreferences")
UpdateOrganizationRecommendationLifecycle = Action(
    "UpdateOrganizationRecommendationLifecycle"
)
UpdateRecommendationLifecycle = Action("UpdateRecommendationLifecycle")
UpdateRiskStatus = Action("UpdateRiskStatus")
