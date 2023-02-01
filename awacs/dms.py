# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Database Migration Service"
prefix = "dms"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTagsToResource = Action("AddTagsToResource")
ApplyPendingMaintenanceAction = Action("ApplyPendingMaintenanceAction")
AssociateExtensionPack = Action("AssociateExtensionPack")
CancelMetadataModelAssessment = Action("CancelMetadataModelAssessment")
CancelMetadataModelConversion = Action("CancelMetadataModelConversion")
CancelMetadataModelExport = Action("CancelMetadataModelExport")
CancelReplicationTaskAssessmentRun = Action("CancelReplicationTaskAssessmentRun")
CreateDataProvider = Action("CreateDataProvider")
CreateEndpoint = Action("CreateEndpoint")
CreateEventSubscription = Action("CreateEventSubscription")
CreateFleetAdvisorCollector = Action("CreateFleetAdvisorCollector")
CreateInstanceProfile = Action("CreateInstanceProfile")
CreateMigrationProject = Action("CreateMigrationProject")
CreateReplicationInstance = Action("CreateReplicationInstance")
CreateReplicationSubnetGroup = Action("CreateReplicationSubnetGroup")
CreateReplicationTask = Action("CreateReplicationTask")
DeleteCertificate = Action("DeleteCertificate")
DeleteConnection = Action("DeleteConnection")
DeleteDataProvider = Action("DeleteDataProvider")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteEventSubscription = Action("DeleteEventSubscription")
DeleteFleetAdvisorCollector = Action("DeleteFleetAdvisorCollector")
DeleteFleetAdvisorDatabases = Action("DeleteFleetAdvisorDatabases")
DeleteInstanceProfile = Action("DeleteInstanceProfile")
DeleteMigrationProject = Action("DeleteMigrationProject")
DeleteReplicationInstance = Action("DeleteReplicationInstance")
DeleteReplicationSubnetGroup = Action("DeleteReplicationSubnetGroup")
DeleteReplicationTask = Action("DeleteReplicationTask")
DeleteReplicationTaskAssessmentRun = Action("DeleteReplicationTaskAssessmentRun")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeApplicableIndividualAssessments = Action(
    "DescribeApplicableIndividualAssessments"
)
DescribeCertificates = Action("DescribeCertificates")
DescribeConnections = Action("DescribeConnections")
DescribeEndpointSettings = Action("DescribeEndpointSettings")
DescribeEndpointTypes = Action("DescribeEndpointTypes")
DescribeEndpoints = Action("DescribeEndpoints")
DescribeEventCategories = Action("DescribeEventCategories")
DescribeEventSubscriptions = Action("DescribeEventSubscriptions")
DescribeEvents = Action("DescribeEvents")
DescribeFleetAdvisorCollectors = Action("DescribeFleetAdvisorCollectors")
DescribeFleetAdvisorDatabases = Action("DescribeFleetAdvisorDatabases")
DescribeFleetAdvisorLsaAnalysis = Action("DescribeFleetAdvisorLsaAnalysis")
DescribeFleetAdvisorSchemaObjectSummary = Action(
    "DescribeFleetAdvisorSchemaObjectSummary"
)
DescribeFleetAdvisorSchemas = Action("DescribeFleetAdvisorSchemas")
DescribeOrderableReplicationInstances = Action("DescribeOrderableReplicationInstances")
DescribePendingMaintenanceActions = Action("DescribePendingMaintenanceActions")
DescribeRefreshSchemasStatus = Action("DescribeRefreshSchemasStatus")
DescribeReplicationInstanceTaskLogs = Action("DescribeReplicationInstanceTaskLogs")
DescribeReplicationInstances = Action("DescribeReplicationInstances")
DescribeReplicationSubnetGroups = Action("DescribeReplicationSubnetGroups")
DescribeReplicationTaskAssessmentResults = Action(
    "DescribeReplicationTaskAssessmentResults"
)
DescribeReplicationTaskAssessmentRuns = Action("DescribeReplicationTaskAssessmentRuns")
DescribeReplicationTaskIndividualAssessments = Action(
    "DescribeReplicationTaskIndividualAssessments"
)
DescribeReplicationTasks = Action("DescribeReplicationTasks")
DescribeSchemas = Action("DescribeSchemas")
DescribeTableStatistics = Action("DescribeTableStatistics")
DisassociateExtensionPack = Action("DisassociateExtensionPack")
ExportMetadataModelAssessment = Action("ExportMetadataModelAssessment")
GetMetadataModel = Action("GetMetadataModel")
ImportCertificate = Action("ImportCertificate")
ListDataProviders = Action("ListDataProviders")
ListExtensionPacks = Action("ListExtensionPacks")
ListInstanceProfiles = Action("ListInstanceProfiles")
ListMetadataModelAssessmentActionItems = Action(
    "ListMetadataModelAssessmentActionItems"
)
ListMetadataModelAssessments = Action("ListMetadataModelAssessments")
ListMetadataModelConversions = Action("ListMetadataModelConversions")
ListMetadataModelExports = Action("ListMetadataModelExports")
ListMigrationProjects = Action("ListMigrationProjects")
ListTagsForResource = Action("ListTagsForResource")
ModifyEndpoint = Action("ModifyEndpoint")
ModifyEventSubscription = Action("ModifyEventSubscription")
ModifyFleetAdvisorCollector = Action("ModifyFleetAdvisorCollector")
ModifyFleetAdvisorCollectorStatuses = Action("ModifyFleetAdvisorCollectorStatuses")
ModifyReplicationInstance = Action("ModifyReplicationInstance")
ModifyReplicationSubnetGroup = Action("ModifyReplicationSubnetGroup")
ModifyReplicationTask = Action("ModifyReplicationTask")
MoveReplicationTask = Action("MoveReplicationTask")
RebootReplicationInstance = Action("RebootReplicationInstance")
RefreshSchemas = Action("RefreshSchemas")
ReloadTables = Action("ReloadTables")
RemoveTagsFromResource = Action("RemoveTagsFromResource")
RunFleetAdvisorLsaAnalysis = Action("RunFleetAdvisorLsaAnalysis")
StartMetadataModelAssessment = Action("StartMetadataModelAssessment")
StartMetadataModelConversion = Action("StartMetadataModelConversion")
StartMetadataModelExportAsScripts = Action("StartMetadataModelExportAsScripts")
StartMetadataModelExportToTarget = Action("StartMetadataModelExportToTarget")
StartMetadataModelImport = Action("StartMetadataModelImport")
StartReplicationTask = Action("StartReplicationTask")
StartReplicationTaskAssessment = Action("StartReplicationTaskAssessment")
StartReplicationTaskAssessmentRun = Action("StartReplicationTaskAssessmentRun")
StopReplicationTask = Action("StopReplicationTask")
TestConnection = Action("TestConnection")
UpdateConversionConfiguration = Action("UpdateConversionConfiguration")
UpdateDataProvider = Action("UpdateDataProvider")
UpdateInstanceProfile = Action("UpdateInstanceProfile")
UpdateMigrationProject = Action("UpdateMigrationProject")
UpdateSubscriptionsToEventBridge = Action("UpdateSubscriptionsToEventBridge")
UploadFileMetadataList = Action("UploadFileMetadataList")
