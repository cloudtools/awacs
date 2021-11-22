# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elastic Disaster Recovery"
prefix = "drs"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFailbackClientToRecoveryInstanceForDrs = Action(
    "AssociateFailbackClientToRecoveryInstanceForDrs"
)
BatchCreateVolumeSnapshotGroupForDrs = Action("BatchCreateVolumeSnapshotGroupForDrs")
BatchDeleteSnapshotRequestForDrs = Action("BatchDeleteSnapshotRequestForDrs")
CreateRecoveryInstanceForDrs = Action("CreateRecoveryInstanceForDrs")
CreateReplicationConfigurationTemplate = Action(
    "CreateReplicationConfigurationTemplate"
)
CreateSessionForDrs = Action("CreateSessionForDrs")
CreateSourceServerForDrs = Action("CreateSourceServerForDrs")
DeleteJob = Action("DeleteJob")
DeleteRecoveryInstance = Action("DeleteRecoveryInstance")
DeleteReplicationConfigurationTemplate = Action(
    "DeleteReplicationConfigurationTemplate"
)
DeleteSourceServer = Action("DeleteSourceServer")
DescribeJobLogItems = Action("DescribeJobLogItems")
DescribeJobs = Action("DescribeJobs")
DescribeRecoveryInstances = Action("DescribeRecoveryInstances")
DescribeRecoverySnapshots = Action("DescribeRecoverySnapshots")
DescribeReplicationConfigurationTemplates = Action(
    "DescribeReplicationConfigurationTemplates"
)
DescribeReplicationServerAssociationsForDrs = Action(
    "DescribeReplicationServerAssociationsForDrs"
)
DescribeSnapshotRequestsForDrs = Action("DescribeSnapshotRequestsForDrs")
DescribeSourceServers = Action("DescribeSourceServers")
DisconnectRecoveryInstance = Action("DisconnectRecoveryInstance")
DisconnectSourceServer = Action("DisconnectSourceServer")
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
GetReplicationConfiguration = Action("GetReplicationConfiguration")
GetSuggestedFailbackClientDeviceMappingForDrs = Action(
    "GetSuggestedFailbackClientDeviceMappingForDrs"
)
InitializeService = Action("InitializeService")
IssueAgentCertificateForDrs = Action("IssueAgentCertificateForDrs")
ListTagsForResource = Action("ListTagsForResource")
NotifyAgentAuthenticationForDrs = Action("NotifyAgentAuthenticationForDrs")
NotifyAgentConnectedForDrs = Action("NotifyAgentConnectedForDrs")
NotifyAgentDisconnectedForDrs = Action("NotifyAgentDisconnectedForDrs")
NotifyAgentReplicationProgressForDrs = Action("NotifyAgentReplicationProgressForDrs")
NotifyConsistencyAttainedForDrs = Action("NotifyConsistencyAttainedForDrs")
NotifyReplicationServerAuthenticationForDrs = Action(
    "NotifyReplicationServerAuthenticationForDrs"
)
RetryDataReplication = Action("RetryDataReplication")
SendAgentLogsForDrs = Action("SendAgentLogsForDrs")
SendAgentMetricsForDrs = Action("SendAgentMetricsForDrs")
SendChannelCommandResultForDrs = Action("SendChannelCommandResultForDrs")
SendClientLogsForDrs = Action("SendClientLogsForDrs")
SendClientMetricsForDrs = Action("SendClientMetricsForDrs")
StartFailbackLaunch = Action("StartFailbackLaunch")
StartRecovery = Action("StartRecovery")
StopFailback = Action("StopFailback")
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
UpdateReplicationCertificateForDrs = Action("UpdateReplicationCertificateForDrs")
UpdateReplicationConfiguration = Action("UpdateReplicationConfiguration")
UpdateReplicationConfigurationTemplate = Action(
    "UpdateReplicationConfigurationTemplate"
)
