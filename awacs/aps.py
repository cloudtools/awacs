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
CreateLoggingConfiguration = Action("CreateLoggingConfiguration")
CreateRuleGroupsNamespace = Action("CreateRuleGroupsNamespace")
CreateScraper = Action("CreateScraper")
CreateWorkspace = Action("CreateWorkspace")
DeleteAlertManagerDefinition = Action("DeleteAlertManagerDefinition")
DeleteAlertManagerSilence = Action("DeleteAlertManagerSilence")
DeleteLoggingConfiguration = Action("DeleteLoggingConfiguration")
DeleteRuleGroupsNamespace = Action("DeleteRuleGroupsNamespace")
DeleteScraper = Action("DeleteScraper")
DeleteWorkspace = Action("DeleteWorkspace")
DescribeAlertManagerDefinition = Action("DescribeAlertManagerDefinition")
DescribeLoggingConfiguration = Action("DescribeLoggingConfiguration")
DescribeRuleGroupsNamespace = Action("DescribeRuleGroupsNamespace")
DescribeScraper = Action("DescribeScraper")
DescribeWorkspace = Action("DescribeWorkspace")
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
ListRuleGroupsNamespaces = Action("ListRuleGroupsNamespaces")
ListRules = Action("ListRules")
ListScrapers = Action("ListScrapers")
ListTagsForResource = Action("ListTagsForResource")
ListWorkspaces = Action("ListWorkspaces")
PutAlertManagerDefinition = Action("PutAlertManagerDefinition")
PutAlertManagerSilences = Action("PutAlertManagerSilences")
PutRuleGroupsNamespace = Action("PutRuleGroupsNamespace")
QueryMetrics = Action("QueryMetrics")
RemoteWrite = Action("RemoteWrite")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLoggingConfiguration = Action("UpdateLoggingConfiguration")
UpdateScraper = Action("UpdateScraper")
UpdateWorkspaceAlias = Action("UpdateWorkspaceAlias")
