# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Service for Prometheus"
prefix = "aps"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAlertManagerAlerts = Action("CreateAlertManagerAlerts")
CreateAlertManagerDefinition = Action("CreateAlertManagerDefinition")
CreateAnomalyDetector = Action("CreateAnomalyDetector")
CreateLoggingConfiguration = Action("CreateLoggingConfiguration")
CreateQueryLoggingConfiguration = Action("CreateQueryLoggingConfiguration")
CreateRuleGroupsNamespace = Action("CreateRuleGroupsNamespace")
CreateScraper = Action("CreateScraper")
CreateWorkspace = Action("CreateWorkspace")
DeleteAlertManagerDefinition = Action("DeleteAlertManagerDefinition")
DeleteAlertManagerSilence = Action("DeleteAlertManagerSilence")
DeleteAnomalyDetector = Action("DeleteAnomalyDetector")
DeleteLoggingConfiguration = Action("DeleteLoggingConfiguration")
DeleteQueryLoggingConfiguration = Action("DeleteQueryLoggingConfiguration")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRuleGroupsNamespace = Action("DeleteRuleGroupsNamespace")
DeleteScraper = Action("DeleteScraper")
DeleteScraperLoggingConfiguration = Action("DeleteScraperLoggingConfiguration")
DeleteWorkspace = Action("DeleteWorkspace")
DescribeAlertManagerDefinition = Action("DescribeAlertManagerDefinition")
DescribeAnomalyDetector = Action("DescribeAnomalyDetector")
DescribeLoggingConfiguration = Action("DescribeLoggingConfiguration")
DescribeQueryLoggingConfiguration = Action("DescribeQueryLoggingConfiguration")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeRuleGroupsNamespace = Action("DescribeRuleGroupsNamespace")
DescribeScraper = Action("DescribeScraper")
DescribeScraperLoggingConfiguration = Action("DescribeScraperLoggingConfiguration")
DescribeWorkspace = Action("DescribeWorkspace")
DescribeWorkspaceConfiguration = Action("DescribeWorkspaceConfiguration")
GetAlertManagerSilence = Action("GetAlertManagerSilence")
GetAlertManagerStatus = Action("GetAlertManagerStatus")
GetDefaultScraperConfiguration = Action("GetDefaultScraperConfiguration")
GetLabels = Action("GetLabels")
GetMetricMetadata = Action("GetMetricMetadata")
GetSeries = Action("GetSeries")
ListAlertManagerAlertGroups = Action("ListAlertManagerAlertGroups")
ListAlertManagerAlerts = Action("ListAlertManagerAlerts")
ListAlertManagerReceivers = Action("ListAlertManagerReceivers")
ListAlertManagerSilences = Action("ListAlertManagerSilences")
ListAlerts = Action("ListAlerts")
ListAnomalyDetectors = Action("ListAnomalyDetectors")
ListRuleGroupsNamespaces = Action("ListRuleGroupsNamespaces")
ListRules = Action("ListRules")
ListScrapers = Action("ListScrapers")
ListTagsForResource = Action("ListTagsForResource")
ListWorkspaces = Action("ListWorkspaces")
PreviewAnomalyDetector = Action("PreviewAnomalyDetector")
PutAlertManagerDefinition = Action("PutAlertManagerDefinition")
PutAlertManagerSilences = Action("PutAlertManagerSilences")
PutAnomalyDetector = Action("PutAnomalyDetector")
PutResourcePolicy = Action("PutResourcePolicy")
PutRuleGroupsNamespace = Action("PutRuleGroupsNamespace")
QueryMetrics = Action("QueryMetrics")
RemoteWrite = Action("RemoteWrite")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLoggingConfiguration = Action("UpdateLoggingConfiguration")
UpdateQueryLoggingConfiguration = Action("UpdateQueryLoggingConfiguration")
UpdateScraper = Action("UpdateScraper")
UpdateScraperLoggingConfiguration = Action("UpdateScraperLoggingConfiguration")
UpdateWorkspaceAlias = Action("UpdateWorkspaceAlias")
UpdateWorkspaceConfiguration = Action("UpdateWorkspaceConfiguration")
