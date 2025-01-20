# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Application Migration Service"
prefix = "mgn"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ArchiveApplication = Action("ArchiveApplication")
ArchiveWave = Action("ArchiveWave")
AssociateApplications = Action("AssociateApplications")
AssociateSourceServers = Action("AssociateSourceServers")
BatchCreateVolumeSnapshotGroupForMgn = Action("BatchCreateVolumeSnapshotGroupForMgn")
BatchDeleteSnapshotRequestForMgn = Action("BatchDeleteSnapshotRequestForMgn")
ChangeServerLifeCycleState = Action("ChangeServerLifeCycleState")
CreateApplication = Action("CreateApplication")
CreateConnector = Action("CreateConnector")
CreateLaunchConfigurationTemplate = Action("CreateLaunchConfigurationTemplate")
CreateNetworkMigrationDefinition = Action("CreateNetworkMigrationDefinition")
CreateReplicationConfigurationTemplate = Action(
    "CreateReplicationConfigurationTemplate"
)
CreateVcenterClientForMgn = Action("CreateVcenterClientForMgn")
CreateWave = Action("CreateWave")
DeleteApplication = Action("DeleteApplication")
DeleteConnector = Action("DeleteConnector")
DeleteJob = Action("DeleteJob")
DeleteLaunchConfigurationTemplate = Action("DeleteLaunchConfigurationTemplate")
DeleteNetworkMigrationDefinition = Action("DeleteNetworkMigrationDefinition")
DeleteReplicationConfigurationTemplate = Action(
    "DeleteReplicationConfigurationTemplate"
)
DeleteSourceServer = Action("DeleteSourceServer")
DeleteVcenterClient = Action("DeleteVcenterClient")
DeleteWave = Action("DeleteWave")
DescribeJobLogItems = Action("DescribeJobLogItems")
DescribeJobs = Action("DescribeJobs")
DescribeLaunchConfigurationTemplates = Action("DescribeLaunchConfigurationTemplates")
DescribeReplicationConfigurationTemplates = Action(
    "DescribeReplicationConfigurationTemplates"
)
DescribeReplicationServerAssociationsForMgn = Action(
    "DescribeReplicationServerAssociationsForMgn"
)
DescribeSnapshotRequestsForMgn = Action("DescribeSnapshotRequestsForMgn")
DescribeSourceServers = Action("DescribeSourceServers")
DescribeVcenterClients = Action("DescribeVcenterClients")
DisassociateApplications = Action("DisassociateApplications")
DisassociateSourceServers = Action("DisassociateSourceServers")
DisconnectFromService = Action("DisconnectFromService")
FinalizeCutover = Action("FinalizeCutover")
GetAgentCommandForMgn = Action("GetAgentCommandForMgn")
GetAgentConfirmedResumeInfoForMgn = Action("GetAgentConfirmedResumeInfoForMgn")
GetAgentInstallationAssetsForMgn = Action("GetAgentInstallationAssetsForMgn")
GetAgentReplicationInfoForMgn = Action("GetAgentReplicationInfoForMgn")
GetAgentRuntimeConfigurationForMgn = Action("GetAgentRuntimeConfigurationForMgn")
GetAgentSnapshotCreditsForMgn = Action("GetAgentSnapshotCreditsForMgn")
GetChannelCommandsForMgn = Action("GetChannelCommandsForMgn")
GetLaunchConfiguration = Action("GetLaunchConfiguration")
GetNetworkMigrationDefinition = Action("GetNetworkMigrationDefinition")
GetNetworkMigrationMapperSegmentConstruct = Action(
    "GetNetworkMigrationMapperSegmentConstruct"
)
GetReplicationConfiguration = Action("GetReplicationConfiguration")
GetVcenterClientCommandsForMgn = Action("GetVcenterClientCommandsForMgn")
InitializeService = Action("InitializeService")
IssueClientCertificateForMgn = Action("IssueClientCertificateForMgn")
ListApplications = Action("ListApplications")
ListConnectors = Action("ListConnectors")
ListExportErrors = Action("ListExportErrors")
ListExports = Action("ListExports")
ListImportErrors = Action("ListImportErrors")
ListImports = Action("ListImports")
ListManagedAccounts = Action("ListManagedAccounts")
ListNetworkMigrationAnalyses = Action("ListNetworkMigrationAnalyses")
ListNetworkMigrationAnalysisResults = Action("ListNetworkMigrationAnalysisResults")
ListNetworkMigrationCodeGenerationSegments = Action(
    "ListNetworkMigrationCodeGenerationSegments"
)
ListNetworkMigrationCodeGenerations = Action("ListNetworkMigrationCodeGenerations")
ListNetworkMigrationDefinitions = Action("ListNetworkMigrationDefinitions")
ListNetworkMigrationDeployedStacks = Action("ListNetworkMigrationDeployedStacks")
ListNetworkMigrationDeployedStacksDeletions = Action(
    "ListNetworkMigrationDeployedStacksDeletions"
)
ListNetworkMigrationDeployments = Action("ListNetworkMigrationDeployments")
ListNetworkMigrationExecutions = Action("ListNetworkMigrationExecutions")
ListNetworkMigrationMapperSegmentConstructs = Action(
    "ListNetworkMigrationMapperSegmentConstructs"
)
ListNetworkMigrationMapperSegments = Action("ListNetworkMigrationMapperSegments")
ListNetworkMigrationMappings = Action("ListNetworkMigrationMappings")
ListSourceServerActions = Action("ListSourceServerActions")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateActions = Action("ListTemplateActions")
ListWaves = Action("ListWaves")
MarkAsArchived = Action("MarkAsArchived")
NotifyAgentAuthenticationForMgn = Action("NotifyAgentAuthenticationForMgn")
NotifyAgentConnectedForMgn = Action("NotifyAgentConnectedForMgn")
NotifyAgentDisconnectedForMgn = Action("NotifyAgentDisconnectedForMgn")
NotifyAgentReplicationProgressForMgn = Action("NotifyAgentReplicationProgressForMgn")
NotifyVcenterClientStartedForMgn = Action("NotifyVcenterClientStartedForMgn")
PauseReplication = Action("PauseReplication")
PutSourceServerAction = Action("PutSourceServerAction")
PutTemplateAction = Action("PutTemplateAction")
RegisterAgentForMgn = Action("RegisterAgentForMgn")
RemoveSourceServerAction = Action("RemoveSourceServerAction")
RemoveTemplateAction = Action("RemoveTemplateAction")
ResumeReplication = Action("ResumeReplication")
RetryDataReplication = Action("RetryDataReplication")
SendAgentLogsForMgn = Action("SendAgentLogsForMgn")
SendAgentMetricsForMgn = Action("SendAgentMetricsForMgn")
SendChannelCommandResultForMgn = Action("SendChannelCommandResultForMgn")
SendClientLogsForMgn = Action("SendClientLogsForMgn")
SendClientMetricsForMgn = Action("SendClientMetricsForMgn")
SendVcenterClientCommandResultForMgn = Action("SendVcenterClientCommandResultForMgn")
SendVcenterClientLogsForMgn = Action("SendVcenterClientLogsForMgn")
SendVcenterClientMetricsForMgn = Action("SendVcenterClientMetricsForMgn")
StartCutover = Action("StartCutover")
StartExport = Action("StartExport")
StartImport = Action("StartImport")
StartNetworkMigrationAnalysis = Action("StartNetworkMigrationAnalysis")
StartNetworkMigrationCodeGeneration = Action("StartNetworkMigrationCodeGeneration")
StartNetworkMigrationDeployedStacksDeletion = Action(
    "StartNetworkMigrationDeployedStacksDeletion"
)
StartNetworkMigrationDeployment = Action("StartNetworkMigrationDeployment")
StartNetworkMigrationMapping = Action("StartNetworkMigrationMapping")
StartReplication = Action("StartReplication")
StartTest = Action("StartTest")
StopReplication = Action("StopReplication")
TagResource = Action("TagResource")
TerminateTargetInstances = Action("TerminateTargetInstances")
UnarchiveApplication = Action("UnarchiveApplication")
UnarchiveWave = Action("UnarchiveWave")
UntagResource = Action("UntagResource")
UpdateAgentBacklogForMgn = Action("UpdateAgentBacklogForMgn")
UpdateAgentConversionInfoForMgn = Action("UpdateAgentConversionInfoForMgn")
UpdateAgentReplicationInfoForMgn = Action("UpdateAgentReplicationInfoForMgn")
UpdateAgentReplicationProcessStateForMgn = Action(
    "UpdateAgentReplicationProcessStateForMgn"
)
UpdateAgentSourcePropertiesForMgn = Action("UpdateAgentSourcePropertiesForMgn")
UpdateApplication = Action("UpdateApplication")
UpdateConnector = Action("UpdateConnector")
UpdateLaunchConfiguration = Action("UpdateLaunchConfiguration")
UpdateLaunchConfigurationTemplate = Action("UpdateLaunchConfigurationTemplate")
UpdateNetworkMigrationDefinition = Action("UpdateNetworkMigrationDefinition")
UpdateNetworkMigrationMapperSegment = Action("UpdateNetworkMigrationMapperSegment")
UpdateNetworkMigrationMapperSegmentConstruct = Action(
    "UpdateNetworkMigrationMapperSegmentConstruct"
)
UpdateReplicationConfiguration = Action("UpdateReplicationConfiguration")
UpdateReplicationConfigurationTemplate = Action(
    "UpdateReplicationConfigurationTemplate"
)
UpdateSourceServer = Action("UpdateSourceServer")
UpdateSourceServerReplicationType = Action("UpdateSourceServerReplicationType")
UpdateWave = Action("UpdateWave")
VerifyClientRoleForMgn = Action("VerifyClientRoleForMgn")
