# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic MapReduce"
prefix = "elasticmapreduce"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CancelSteps = Action("CancelSteps")
CreateEditor = Action("CreateEditor")
CreateRepository = Action("CreateRepository")
CreateSecurityConfiguration = Action("CreateSecurityConfiguration")
CreateStudio = Action("CreateStudio")
CreateStudioSessionMapping = Action("CreateStudioSessionMapping")
DeleteEditor = Action("DeleteEditor")
DeleteRepository = Action("DeleteRepository")
DeleteSecurityConfiguration = Action("DeleteSecurityConfiguration")
DeleteStudio = Action("DeleteStudio")
DeleteStudioSessionMapping = Action("DeleteStudioSessionMapping")
DescribeCluster = Action("DescribeCluster")
DescribeEditor = Action("DescribeEditor")
DescribeJobFlows = Action("DescribeJobFlows")
DescribeNotebookExecution = Action("DescribeNotebookExecution")
DescribeRepository = Action("DescribeRepository")
DescribeSecurityConfiguration = Action("DescribeSecurityConfiguration")
DescribeStep = Action("DescribeStep")
DescribeStudio = Action("DescribeStudio")
GetBlockPublicAccessConfiguration = Action("GetBlockPublicAccessConfiguration")
GetManagedScalingPolicy = Action("GetManagedScalingPolicy")
GetStudioSessionMapping = Action("GetStudioSessionMapping")
LinkRepository = Action("LinkRepository")
ListBootstrapActions = Action("ListBootstrapActions")
ListClusters = Action("ListClusters")
ListEditors = Action("ListEditors")
ListInstanceFleets = Action("ListInstanceFleets")
ListInstanceGroups = Action("ListInstanceGroups")
ListInstances = Action("ListInstances")
ListNotebookExecutions = Action("ListNotebookExecutions")
ListRepositories = Action("ListRepositories")
ListSecurityConfigurations = Action("ListSecurityConfigurations")
ListSteps = Action("ListSteps")
ListStudioSessionMappings = Action("ListStudioSessionMappings")
ListStudios = Action("ListStudios")
ModifyCluster = Action("ModifyCluster")
ModifyInstanceFleet = Action("ModifyInstanceFleet")
ModifyInstanceGroups = Action("ModifyInstanceGroups")
OpenEditorInConsole = Action("OpenEditorInConsole")
PutAutoScalingPolicy = Action("PutAutoScalingPolicy")
PutBlockPublicAccessConfiguration = Action("PutBlockPublicAccessConfiguration")
PutManagedScalingPolicy = Action("PutManagedScalingPolicy")
RemoveAutoScalingPolicy = Action("RemoveAutoScalingPolicy")
RemoveManagedScalingPolicy = Action("RemoveManagedScalingPolicy")
RemoveTags = Action("RemoveTags")
RunJobFlow = Action("RunJobFlow")
SetTerminationProtection = Action("SetTerminationProtection")
SetVisibleToAllUsers = Action("SetVisibleToAllUsers")
StartEditor = Action("StartEditor")
StartNotebookExecution = Action("StartNotebookExecution")
StopEditor = Action("StopEditor")
StopNotebookExecution = Action("StopNotebookExecution")
TerminateJobFlows = Action("TerminateJobFlows")
UnlinkRepository = Action("UnlinkRepository")
UpdateRepository = Action("UpdateRepository")
UpdateStudio = Action("UpdateStudio")
UpdateStudioSessionMapping = Action("UpdateStudioSessionMapping")
ViewEventsFromAllClustersInConsole = Action("ViewEventsFromAllClustersInConsole")
