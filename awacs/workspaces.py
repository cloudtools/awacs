# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkSpaces"
prefix = "workspaces"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateConnectionAlias = Action("AssociateConnectionAlias")
AssociateIpGroups = Action("AssociateIpGroups")
AuthorizeIpRules = Action("AuthorizeIpRules")
CopyWorkspaceImage = Action("CopyWorkspaceImage")
CreateConnectionAlias = Action("CreateConnectionAlias")
CreateIpGroup = Action("CreateIpGroup")
CreateTags = Action("CreateTags")
CreateWorkspaceBundle = Action("CreateWorkspaceBundle")
CreateWorkspaces = Action("CreateWorkspaces")
DeleteConnectionAlias = Action("DeleteConnectionAlias")
DeleteIpGroup = Action("DeleteIpGroup")
DeleteTags = Action("DeleteTags")
DeleteWorkspaceBundle = Action("DeleteWorkspaceBundle")
DeleteWorkspaceImage = Action("DeleteWorkspaceImage")
DeregisterWorkspaceDirectory = Action("DeregisterWorkspaceDirectory")
DescribeAccount = Action("DescribeAccount")
DescribeAccountModifications = Action("DescribeAccountModifications")
DescribeClientProperties = Action("DescribeClientProperties")
DescribeConnectionAliasPermissions = Action("DescribeConnectionAliasPermissions")
DescribeConnectionAliases = Action("DescribeConnectionAliases")
DescribeIpGroups = Action("DescribeIpGroups")
DescribeTags = Action("DescribeTags")
DescribeWorkspaceBundles = Action("DescribeWorkspaceBundles")
DescribeWorkspaceDirectories = Action("DescribeWorkspaceDirectories")
DescribeWorkspaceImagePermissions = Action("DescribeWorkspaceImagePermissions")
DescribeWorkspaceImages = Action("DescribeWorkspaceImages")
DescribeWorkspaceSnapshots = Action("DescribeWorkspaceSnapshots")
DescribeWorkspaces = Action("DescribeWorkspaces")
DescribeWorkspacesConnectionStatus = Action("DescribeWorkspacesConnectionStatus")
DisassociateConnectionAlias = Action("DisassociateConnectionAlias")
DisassociateIpGroups = Action("DisassociateIpGroups")
ImportWorkspaceImage = Action("ImportWorkspaceImage")
ListAvailableManagementCidrRanges = Action("ListAvailableManagementCidrRanges")
MigrateWorkspace = Action("MigrateWorkspace")
ModifyAccount = Action("ModifyAccount")
ModifyClientProperties = Action("ModifyClientProperties")
ModifySelfservicePermissions = Action("ModifySelfservicePermissions")
ModifyWorkspaceAccessProperties = Action("ModifyWorkspaceAccessProperties")
ModifyWorkspaceCreationProperties = Action("ModifyWorkspaceCreationProperties")
ModifyWorkspaceProperties = Action("ModifyWorkspaceProperties")
ModifyWorkspaceState = Action("ModifyWorkspaceState")
RebootWorkspaces = Action("RebootWorkspaces")
RebuildWorkspaces = Action("RebuildWorkspaces")
RegisterWorkspaceDirectory = Action("RegisterWorkspaceDirectory")
RestoreWorkspace = Action("RestoreWorkspace")
RevokeIpRules = Action("RevokeIpRules")
StartWorkspaces = Action("StartWorkspaces")
StopWorkspaces = Action("StopWorkspaces")
TerminateWorkspaces = Action("TerminateWorkspaces")
UpdateConnectionAliasPermission = Action("UpdateConnectionAliasPermission")
UpdateRulesOfIpGroup = Action("UpdateRulesOfIpGroup")
UpdateWorkspaceBundle = Action("UpdateWorkspaceBundle")
UpdateWorkspaceImagePermission = Action("UpdateWorkspaceImagePermission")
