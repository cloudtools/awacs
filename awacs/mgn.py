# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Application Migration Service"
prefix = "mgn"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreateVolumeSnapshotGroupForMgn = Action("BatchCreateVolumeSnapshotGroupForMgn")
BatchDeleteSnapshotRequestForMgn = Action("BatchDeleteSnapshotRequestForMgn")
ChangeServerLifeCycleState = Action("ChangeServerLifeCycleState")
CreateReplicationConfigurationTemplate = Action(
    "CreateReplicationConfigurationTemplate"
)
DeleteJob = Action("DeleteJob")
DeleteReplicationConfigurationTemplate = Action(
    "DeleteReplicationConfigurationTemplate"
)
DeleteSourceServer = Action("DeleteSourceServer")
DescribeJobLogItems = Action("DescribeJobLogItems")
DescribeJobs = Action("DescribeJobs")
DescribeReplicationConfigurationTemplates = Action(
    "DescribeReplicationConfigurationTemplates"
)
DescribeReplicationServerAssociationsForMgn = Action(
    "DescribeReplicationServerAssociationsForMgn"
)
DescribeSnapshotRequestsForMgn = Action("DescribeSnapshotRequestsForMgn")
DescribeSourceServers = Action("DescribeSourceServers")
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
GetReplicationConfiguration = Action("GetReplicationConfiguration")
InitializeService = Action("InitializeService")
ListTagsForResource = Action("ListTagsForResource")
MarkAsArchived = Action("MarkAsArchived")
NotifyAgentAuthenticationForMgn = Action("NotifyAgentAuthenticationForMgn")
NotifyAgentConnectedForMgn = Action("NotifyAgentConnectedForMgn")
NotifyAgentDisconnectedForMgn = Action("NotifyAgentDisconnectedForMgn")
NotifyAgentReplicationProgressForMgn = Action("NotifyAgentReplicationProgressForMgn")
RegisterAgentForMgn = Action("RegisterAgentForMgn")
RetryDataReplication = Action("RetryDataReplication")
SendAgentLogsForMgn = Action("SendAgentLogsForMgn")
SendAgentMetricsForMgn = Action("SendAgentMetricsForMgn")
SendChannelCommandResultForMgn = Action("SendChannelCommandResultForMgn")
SendClientLogsForMgn = Action("SendClientLogsForMgn")
SendClientMetricsForMgn = Action("SendClientMetricsForMgn")
StartCutover = Action("StartCutover")
StartTest = Action("StartTest")
TagResource = Action("TagResource")
TerminateTargetInstances = Action("TerminateTargetInstances")
UntagResource = Action("UntagResource")
UpdateAgentBacklogForMgn = Action("UpdateAgentBacklogForMgn")
UpdateAgentConversionInfoForMgn = Action("UpdateAgentConversionInfoForMgn")
UpdateAgentReplicationInfoForMgn = Action("UpdateAgentReplicationInfoForMgn")
UpdateAgentReplicationProcessStateForMgn = Action(
    "UpdateAgentReplicationProcessStateForMgn"
)
UpdateAgentSourcePropertiesForMgn = Action("UpdateAgentSourcePropertiesForMgn")
UpdateLaunchConfiguration = Action("UpdateLaunchConfiguration")
UpdateReplicationConfiguration = Action("UpdateReplicationConfiguration")
UpdateReplicationConfigurationTemplate = Action(
    "UpdateReplicationConfigurationTemplate"
)
