# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Neptune Analytics"
prefix = "neptune-graph"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelExportTask = Action("CancelExportTask")
CancelImportTask = Action("CancelImportTask")
CancelQuery = Action("CancelQuery")
CreateGraph = Action("CreateGraph")
CreateGraphSnapshot = Action("CreateGraphSnapshot")
CreateGraphUsingImportTask = Action("CreateGraphUsingImportTask")
CreatePrivateGraphEndpoint = Action("CreatePrivateGraphEndpoint")
DeleteDataViaQuery = Action("DeleteDataViaQuery")
DeleteGraph = Action("DeleteGraph")
DeleteGraphSnapshot = Action("DeleteGraphSnapshot")
DeletePrivateGraphEndpoint = Action("DeletePrivateGraphEndpoint")
GetEngineStatus = Action("GetEngineStatus")
GetExportTask = Action("GetExportTask")
GetGraph = Action("GetGraph")
GetGraphSnapshot = Action("GetGraphSnapshot")
GetGraphSummary = Action("GetGraphSummary")
GetImportTask = Action("GetImportTask")
GetPrivateGraphEndpoint = Action("GetPrivateGraphEndpoint")
GetQueryStatus = Action("GetQueryStatus")
GetStatisticsStatus = Action("GetStatisticsStatus")
ListExportTasks = Action("ListExportTasks")
ListGraphSnapshots = Action("ListGraphSnapshots")
ListGraphs = Action("ListGraphs")
ListImportTasks = Action("ListImportTasks")
ListPrivateGraphEndpoints = Action("ListPrivateGraphEndpoints")
ListQueries = Action("ListQueries")
ListTagsForResource = Action("ListTagsForResource")
ReadDataViaQuery = Action("ReadDataViaQuery")
ResetGraph = Action("ResetGraph")
RestoreGraphFromSnapshot = Action("RestoreGraphFromSnapshot")
StartExportTask = Action("StartExportTask")
StartImportTask = Action("StartImportTask")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGraph = Action("UpdateGraph")
WriteDataViaQuery = Action("WriteDataViaQuery")
