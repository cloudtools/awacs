# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic MapReduce"
prefix = "elasticmapreduce"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddInstanceFleet = Action("AddInstanceFleet")
AddInstanceGroups = Action("AddInstanceGroups")
AddJobFlowSteps = Action("AddJobFlowSteps")
AddTags = Action("AddTags")
AttachEditor = Action("AttachEditor")
CancelSteps = Action("CancelSteps")
CreateEditor = Action("CreateEditor")
CreatePersistentAppUI = Action("CreatePersistentAppUI")
CreateRepository = Action("CreateRepository")
CreateSecurityConfiguration = Action("CreateSecurityConfiguration")
CreateStudio = Action("CreateStudio")
CreateStudioPresignedUrl = Action("CreateStudioPresignedUrl")
CreateStudioSessionMapping = Action("CreateStudioSessionMapping")
DeleteEditor = Action("DeleteEditor")
DeleteRepository = Action("DeleteRepository")
DeleteSecurityConfiguration = Action("DeleteSecurityConfiguration")
DeleteStudio = Action("DeleteStudio")
DeleteStudioSessionMapping = Action("DeleteStudioSessionMapping")
DeleteWorkspaceAccess = Action("DeleteWorkspaceAccess")
DescribeCluster = Action("DescribeCluster")
DescribeEditor = Action("DescribeEditor")
DescribeJobFlows = Action("DescribeJobFlows")
DescribeNotebookExecution = Action("DescribeNotebookExecution")
DescribePersistentAppUI = Action("DescribePersistentAppUI")
DescribeReleaseLabel = Action("DescribeReleaseLabel")
DescribeRepository = Action("DescribeRepository")
DescribeSecurityConfiguration = Action("DescribeSecurityConfiguration")
DescribeStep = Action("DescribeStep")
DescribeStudio = Action("DescribeStudio")
DetachEditor = Action("DetachEditor")
GetAutoTerminationPolicy = Action("GetAutoTerminationPolicy")
GetBlockPublicAccessConfiguration = Action("GetBlockPublicAccessConfiguration")
GetClusterSessionCredentials = Action("GetClusterSessionCredentials")
GetManagedScalingPolicy = Action("GetManagedScalingPolicy")
GetOnClusterAppUIPresignedURL = Action("GetOnClusterAppUIPresignedURL")
GetPersistentAppUIPresignedURL = Action("GetPersistentAppUIPresignedURL")
GetStudioSessionMapping = Action("GetStudioSessionMapping")
LinkRepository = Action("LinkRepository")
ListBootstrapActions = Action("ListBootstrapActions")
ListClusters = Action("ListClusters")
ListEditors = Action("ListEditors")
ListInstanceFleets = Action("ListInstanceFleets")
ListInstanceGroups = Action("ListInstanceGroups")
ListInstances = Action("ListInstances")
ListNotebookExecutions = Action("ListNotebookExecutions")
ListReleaseLabels = Action("ListReleaseLabels")
ListRepositories = Action("ListRepositories")
ListSecurityConfigurations = Action("ListSecurityConfigurations")
ListSteps = Action("ListSteps")
ListStudioSessionMappings = Action("ListStudioSessionMappings")
ListStudios = Action("ListStudios")
ListSupportedInstanceTypes = Action("ListSupportedInstanceTypes")
ListWorkspaceAccessIdentities = Action("ListWorkspaceAccessIdentities")
ModifyCluster = Action("ModifyCluster")
ModifyInstanceFleet = Action("ModifyInstanceFleet")
ModifyInstanceGroups = Action("ModifyInstanceGroups")
OpenEditorInConsole = Action("OpenEditorInConsole")
PutAutoScalingPolicy = Action("PutAutoScalingPolicy")
PutAutoTerminationPolicy = Action("PutAutoTerminationPolicy")
PutBlockPublicAccessConfiguration = Action("PutBlockPublicAccessConfiguration")
PutManagedScalingPolicy = Action("PutManagedScalingPolicy")
PutWorkspaceAccess = Action("PutWorkspaceAccess")
RemoveAutoScalingPolicy = Action("RemoveAutoScalingPolicy")
RemoveAutoTerminationPolicy = Action("RemoveAutoTerminationPolicy")
RemoveManagedScalingPolicy = Action("RemoveManagedScalingPolicy")
RemoveTags = Action("RemoveTags")
RunJobFlow = Action("RunJobFlow")
SetKeepJobFlowAliveWhenNoSteps = Action("SetKeepJobFlowAliveWhenNoSteps")
SetTerminationProtection = Action("SetTerminationProtection")
SetUnhealthyNodeReplacement = Action("SetUnhealthyNodeReplacement")
SetVisibleToAllUsers = Action("SetVisibleToAllUsers")
StartEditor = Action("StartEditor")
StartNotebookExecution = Action("StartNotebookExecution")
StopEditor = Action("StopEditor")
StopNotebookExecution = Action("StopNotebookExecution")
TerminateJobFlows = Action("TerminateJobFlows")
UnlinkRepository = Action("UnlinkRepository")
UpdateEditor = Action("UpdateEditor")
UpdateRepository = Action("UpdateRepository")
UpdateStudio = Action("UpdateStudio")
UpdateStudioSessionMapping = Action("UpdateStudioSessionMapping")
ViewEventsFromAllClustersInConsole = Action("ViewEventsFromAllClustersInConsole")
