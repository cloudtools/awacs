# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Migration Hub Strategy Recommendations"
prefix = "migrationhub-strategy"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


GetAntiPattern = Action("GetAntiPattern")
GetApplicationComponentDetails = Action("GetApplicationComponentDetails")
GetApplicationComponentStrategies = Action("GetApplicationComponentStrategies")
GetAssessment = Action("GetAssessment")
GetImportFileTask = Action("GetImportFileTask")
GetLatestAssessmentId = Action("GetLatestAssessmentId")
GetMessage = Action("GetMessage")
GetPortfolioPreferences = Action("GetPortfolioPreferences")
GetPortfolioSummary = Action("GetPortfolioSummary")
GetRecommendationReportDetails = Action("GetRecommendationReportDetails")
GetServerDetails = Action("GetServerDetails")
GetServerStrategies = Action("GetServerStrategies")
ListAnalyzableServers = Action("ListAnalyzableServers")
ListAntiPatterns = Action("ListAntiPatterns")
ListApplicationComponents = Action("ListApplicationComponents")
ListCollectors = Action("ListCollectors")
ListImportFileTask = Action("ListImportFileTask")
ListJarArtifacts = Action("ListJarArtifacts")
ListServers = Action("ListServers")
PutLogData = Action("PutLogData")
PutMetricData = Action("PutMetricData")
PutPortfolioPreferences = Action("PutPortfolioPreferences")
RegisterCollector = Action("RegisterCollector")
SendMessage = Action("SendMessage")
StartAssessment = Action("StartAssessment")
StartImportFileTask = Action("StartImportFileTask")
StartRecommendationReportGeneration = Action("StartRecommendationReportGeneration")
StopAssessment = Action("StopAssessment")
UpdateApplicationComponentConfig = Action("UpdateApplicationComponentConfig")
UpdateCollectorConfiguration = Action("UpdateCollectorConfiguration")
UpdateServerConfig = Action("UpdateServerConfig")
