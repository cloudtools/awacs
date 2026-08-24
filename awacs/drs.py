# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elastic Disaster Recovery"
prefix = "drs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFailbackClientToRecoveryInstanceForDrs = Action(
    "AssociateFailbackClientToRecoveryInstanceForDrs"
)
AssociateSourceNetworkStack = Action("AssociateSourceNetworkStack")
BatchCreateVolumeSnapshotGroupForDrs = Action("BatchCreateVolumeSnapshotGroupForDrs")
BatchDeleteSnapshotRequestForDrs = Action("BatchDeleteSnapshotRequestForDrs")
CancelRecoveryPlanExecution = Action("CancelRecoveryPlanExecution")
CreateConvertedSnapshotForDrs = Action("CreateConvertedSnapshotForDrs")
CreateExtendedSourceServer = Action("CreateExtendedSourceServer")
CreateLaunchConfigurationTemplate = Action("CreateLaunchConfigurationTemplate")
CreateRecoveryInstanceForDrs = Action("CreateRecoveryInstanceForDrs")
CreateRecoveryPlan = Action("CreateRecoveryPlan")
CreateRecoveryPlanStep = Action("CreateRecoveryPlanStep")
CreateReplicationConfigurationTemplate = Action(
    "CreateReplicationConfigurationTemplate"
)
CreateSessionForDrs = Action("CreateSessionForDrs")
CreateSourceNetwork = Action("CreateSourceNetwork")
CreateSourceServerForDrs = Action("CreateSourceServerForDrs")
DeleteJob = Action("DeleteJob")
DeleteLaunchAction = Action("DeleteLaunchAction")
DeleteLaunchConfigurationTemplate = Action("DeleteLaunchConfigurationTemplate")
DeleteRecoveryInstance = Action("DeleteRecoveryInstance")
DeleteRecoveryPlan = Action("DeleteRecoveryPlan")
DeleteRecoveryPlanExecution = Action("DeleteRecoveryPlanExecution")
DeleteRecoveryPlanStep = Action("DeleteRecoveryPlanStep")
DeleteReplicationConfigurationTemplate = Action(
    "DeleteReplicationConfigurationTemplate"
)
DeleteSourceNetwork = Action("DeleteSourceNetwork")
DeleteSourceServer = Action("DeleteSourceServer")
DescribeJobLogItems = Action("DescribeJobLogItems")
DescribeJobs = Action("DescribeJobs")
DescribeLaunchConfigurationTemplates = Action("DescribeLaunchConfigurationTemplates")
DescribeRecoveryInstances = Action("DescribeRecoveryInstances")
DescribeRecoverySnapshots = Action("DescribeRecoverySnapshots")
DescribeReplicationConfigurationTemplates = Action(
    "DescribeReplicationConfigurationTemplates"
)
DescribeReplicationServerAssociationsForDrs = Action(
    "DescribeReplicationServerAssociationsForDrs"
)
DescribeSnapshotRequestsForDrs = Action("DescribeSnapshotRequestsForDrs")
DescribeSourceNetworks = Action("DescribeSourceNetworks")
DescribeSourceServers = Action("DescribeSourceServers")
DisconnectRecoveryInstance = Action("DisconnectRecoveryInstance")
DisconnectSourceServer = Action("DisconnectSourceServer")
ExportSourceNetworkCfnTemplate = Action("ExportSourceNetworkCfnTemplate")
GetAgentCommandForDrs = Action("GetAgentCommandForDrs")
GetAgentConfirmedResumeInfoForDrs = Action("GetAgentConfirmedResumeInfoForDrs")
GetAgentInstallationAssetsForDrs = Action("GetAgentInstallationAssetsForDrs")
GetAgentReplicationInfoForDrs = Action("GetAgentReplicationInfoForDrs")
GetAgentRuntimeConfigurationForDrs = Action("GetAgentRuntimeConfigurationForDrs")
GetAgentSnapshotCreditsForDrs = Action("GetAgentSnapshotCreditsForDrs")
GetChannelCommandsForDrs = Action("GetChannelCommandsForDrs")
GetFailbackCommandForDrs = Action("GetFailbackCommandForDrs")
GetFailbackLaunchRequestedForDrs = Action("GetFailbackLaunchRequestedForDrs")
GetFailbackReplicationConfiguration = Action("GetFailbackReplicationConfiguration")
GetLaunchConfiguration = Action("GetLaunchConfiguration")
GetRecoveryPlan = Action("GetRecoveryPlan")
GetRecoveryPlanExecution = Action("GetRecoveryPlanExecution")
GetRecoveryPlanExecutionStep = Action("GetRecoveryPlanExecutionStep")
GetRecoveryPlanStep = Action("GetRecoveryPlanStep")
GetReplicationConfiguration = Action("GetReplicationConfiguration")
GetSuggestedFailbackClientDeviceMappingForDrs = Action(
    "GetSuggestedFailbackClientDeviceMappingForDrs"
)
InitializeService = Action("InitializeService")
IssueAgentCertificateForDrs = Action("IssueAgentCertificateForDrs")
ListExtensibleSourceServers = Action("ListExtensibleSourceServers")
ListLaunchActions = Action("ListLaunchActions")
ListRecoveryPlanExecutionSteps = Action("ListRecoveryPlanExecutionSteps")
ListRecoveryPlanExecutions = Action("ListRecoveryPlanExecutions")
ListRecoveryPlanSteps = Action("ListRecoveryPlanSteps")
ListRecoveryPlans = Action("ListRecoveryPlans")
ListStagingAccounts = Action("ListStagingAccounts")
ListTagsForResource = Action("ListTagsForResource")
NotifyAgentAuthenticationForDrs = Action("NotifyAgentAuthenticationForDrs")
NotifyAgentConnectedForDrs = Action("NotifyAgentConnectedForDrs")
NotifyAgentDisconnectedForDrs = Action("NotifyAgentDisconnectedForDrs")
NotifyAgentReplicationProgressForDrs = Action("NotifyAgentReplicationProgressForDrs")
NotifyConsistencyAttainedForDrs = Action("NotifyConsistencyAttainedForDrs")
NotifyReplicationServerAuthenticationForDrs = Action(
    "NotifyReplicationServerAuthenticationForDrs"
)
NotifyVolumeEventForDrs = Action("NotifyVolumeEventForDrs")
PutLaunchAction = Action("PutLaunchAction")
ReorderRecoveryPlanSteps = Action("ReorderRecoveryPlanSteps")
RetryDataReplication = Action("RetryDataReplication")
RetryRecoveryPlanExecutionStep = Action("RetryRecoveryPlanExecutionStep")
ReverseReplication = Action("ReverseReplication")
SendAgentLogsForDrs = Action("SendAgentLogsForDrs")
SendAgentMetricsForDrs = Action("SendAgentMetricsForDrs")
SendChannelCommandResultForDrs = Action("SendChannelCommandResultForDrs")
SendClientLogsForDrs = Action("SendClientLogsForDrs")
SendClientMetricsForDrs = Action("SendClientMetricsForDrs")
SendVolumeStatsForDrs = Action("SendVolumeStatsForDrs")
StartFailbackLaunch = Action("StartFailbackLaunch")
StartRecovery = Action("StartRecovery")
StartRecoveryPlanExecution = Action("StartRecoveryPlanExecution")
StartReplication = Action("StartReplication")
StartSourceNetworkRecovery = Action("StartSourceNetworkRecovery")
StartSourceNetworkReplication = Action("StartSourceNetworkReplication")
StopFailback = Action("StopFailback")
StopReplication = Action("StopReplication")
StopSourceNetworkReplication = Action("StopSourceNetworkReplication")
TagResource = Action("TagResource")
TerminateRecoveryInstances = Action("TerminateRecoveryInstances")
UntagResource = Action("UntagResource")
UpdateAgentBacklogForDrs = Action("UpdateAgentBacklogForDrs")
UpdateAgentConversionInfoForDrs = Action("UpdateAgentConversionInfoForDrs")
UpdateAgentReplicationInfoForDrs = Action("UpdateAgentReplicationInfoForDrs")
UpdateAgentReplicationProcessStateForDrs = Action(
    "UpdateAgentReplicationProcessStateForDrs"
)
UpdateAgentSourcePropertiesForDrs = Action("UpdateAgentSourcePropertiesForDrs")
UpdateFailbackClientDeviceMappingForDrs = Action(
    "UpdateFailbackClientDeviceMappingForDrs"
)
UpdateFailbackClientLastSeenForDrs = Action("UpdateFailbackClientLastSeenForDrs")
UpdateFailbackReplicationConfiguration = Action(
    "UpdateFailbackReplicationConfiguration"
)
UpdateLaunchConfiguration = Action("UpdateLaunchConfiguration")
UpdateLaunchConfigurationTemplate = Action("UpdateLaunchConfigurationTemplate")
UpdateRecoveryPlan = Action("UpdateRecoveryPlan")
UpdateRecoveryPlanExecutionStep = Action("UpdateRecoveryPlanExecutionStep")
UpdateRecoveryPlanStep = Action("UpdateRecoveryPlanStep")
UpdateReplicationCertificateForDrs = Action("UpdateReplicationCertificateForDrs")
UpdateReplicationConfiguration = Action("UpdateReplicationConfiguration")
UpdateReplicationConfigurationTemplate = Action(
    "UpdateReplicationConfigurationTemplate"
)
