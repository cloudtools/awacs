# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Application Discovery Service"
prefix = "discovery"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateConfigurationItemsToApplication = Action(
    "AssociateConfigurationItemsToApplication"
)
BatchDeleteAgents = Action("BatchDeleteAgents")
BatchDeleteImportData = Action("BatchDeleteImportData")
CreateApplication = Action("CreateApplication")
CreateTags = Action("CreateTags")
DeleteApplications = Action("DeleteApplications")
DeleteTags = Action("DeleteTags")
DescribeAgents = Action("DescribeAgents")
DescribeBatchDeleteConfigurationTask = Action("DescribeBatchDeleteConfigurationTask")
DescribeConfigurations = Action("DescribeConfigurations")
DescribeContinuousExports = Action("DescribeContinuousExports")
DescribeExportConfigurations = Action("DescribeExportConfigurations")
DescribeExportTasks = Action("DescribeExportTasks")
DescribeImportTasks = Action("DescribeImportTasks")
DescribeTags = Action("DescribeTags")
DisassociateConfigurationItemsFromApplication = Action(
    "DisassociateConfigurationItemsFromApplication"
)
ExportConfigurations = Action("ExportConfigurations")
GetDiscoverySummary = Action("GetDiscoverySummary")
GetNetworkConnectionGraph = Action("GetNetworkConnectionGraph")
ListConfigurations = Action("ListConfigurations")
ListServerNeighbors = Action("ListServerNeighbors")
StartBatchDeleteConfigurationTask = Action("StartBatchDeleteConfigurationTask")
StartContinuousExport = Action("StartContinuousExport")
StartDataCollectionByAgentIds = Action("StartDataCollectionByAgentIds")
StartExportTask = Action("StartExportTask")
StartImportTask = Action("StartImportTask")
StopContinuousExport = Action("StopContinuousExport")
StopDataCollectionByAgentIds = Action("StopDataCollectionByAgentIds")
UpdateApplication = Action("UpdateApplication")
