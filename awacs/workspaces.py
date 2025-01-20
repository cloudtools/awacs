# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkSpaces"
prefix = "workspaces"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAccountLinkInvitation = Action("AcceptAccountLinkInvitation")
AssociateConnectionAlias = Action("AssociateConnectionAlias")
AssociateIpGroups = Action("AssociateIpGroups")
AssociateWorkspaceApplication = Action("AssociateWorkspaceApplication")
AuthorizeIpRules = Action("AuthorizeIpRules")
CopyWorkspaceImage = Action("CopyWorkspaceImage")
CreateAccountLinkInvitation = Action("CreateAccountLinkInvitation")
CreateConnectClientAddIn = Action("CreateConnectClientAddIn")
CreateConnectionAlias = Action("CreateConnectionAlias")
CreateIpGroup = Action("CreateIpGroup")
CreateStandbyWorkspaces = Action("CreateStandbyWorkspaces")
CreateTags = Action("CreateTags")
CreateUpdatedWorkspaceImage = Action("CreateUpdatedWorkspaceImage")
CreateWorkspaceBundle = Action("CreateWorkspaceBundle")
CreateWorkspaceImage = Action("CreateWorkspaceImage")
CreateWorkspaces = Action("CreateWorkspaces")
CreateWorkspacesPool = Action("CreateWorkspacesPool")
DeleteAccountLinkInvitation = Action("DeleteAccountLinkInvitation")
DeleteClientBranding = Action("DeleteClientBranding")
DeleteConnectClientAddIn = Action("DeleteConnectClientAddIn")
DeleteConnectionAlias = Action("DeleteConnectionAlias")
DeleteIpGroup = Action("DeleteIpGroup")
DeleteTags = Action("DeleteTags")
DeleteWorkspaceBundle = Action("DeleteWorkspaceBundle")
DeleteWorkspaceImage = Action("DeleteWorkspaceImage")
DeployWorkspaceApplications = Action("DeployWorkspaceApplications")
DeregisterWorkspaceDirectory = Action("DeregisterWorkspaceDirectory")
DescribeAccount = Action("DescribeAccount")
DescribeAccountModifications = Action("DescribeAccountModifications")
DescribeApplicationAssociations = Action("DescribeApplicationAssociations")
DescribeApplications = Action("DescribeApplications")
DescribeBundleAssociations = Action("DescribeBundleAssociations")
DescribeClientBranding = Action("DescribeClientBranding")
DescribeClientProperties = Action("DescribeClientProperties")
DescribeConnectClientAddIns = Action("DescribeConnectClientAddIns")
DescribeConnectionAliasPermissions = Action("DescribeConnectionAliasPermissions")
DescribeConnectionAliases = Action("DescribeConnectionAliases")
DescribeImageAssociations = Action("DescribeImageAssociations")
DescribeIpGroups = Action("DescribeIpGroups")
DescribeTags = Action("DescribeTags")
DescribeWorkspaceAssociations = Action("DescribeWorkspaceAssociations")
DescribeWorkspaceBundles = Action("DescribeWorkspaceBundles")
DescribeWorkspaceDirectories = Action("DescribeWorkspaceDirectories")
DescribeWorkspaceImagePermissions = Action("DescribeWorkspaceImagePermissions")
DescribeWorkspaceImages = Action("DescribeWorkspaceImages")
DescribeWorkspaceSnapshots = Action("DescribeWorkspaceSnapshots")
DescribeWorkspaces = Action("DescribeWorkspaces")
DescribeWorkspacesConnectionStatus = Action("DescribeWorkspacesConnectionStatus")
DescribeWorkspacesPoolSessions = Action("DescribeWorkspacesPoolSessions")
DescribeWorkspacesPools = Action("DescribeWorkspacesPools")
DisassociateConnectionAlias = Action("DisassociateConnectionAlias")
DisassociateIpGroups = Action("DisassociateIpGroups")
DisassociateWorkspaceApplication = Action("DisassociateWorkspaceApplication")
GetAccountLink = Action("GetAccountLink")
ImportClientBranding = Action("ImportClientBranding")
ImportWorkspaceImage = Action("ImportWorkspaceImage")
ListAccountLinks = Action("ListAccountLinks")
ListAvailableManagementCidrRanges = Action("ListAvailableManagementCidrRanges")
MigrateWorkspace = Action("MigrateWorkspace")
ModifyAccount = Action("ModifyAccount")
ModifyCertificateBasedAuthProperties = Action("ModifyCertificateBasedAuthProperties")
ModifyClientProperties = Action("ModifyClientProperties")
ModifySamlProperties = Action("ModifySamlProperties")
ModifySelfservicePermissions = Action("ModifySelfservicePermissions")
ModifyStreamingProperties = Action("ModifyStreamingProperties")
ModifyWorkspaceAccessProperties = Action("ModifyWorkspaceAccessProperties")
ModifyWorkspaceCreationProperties = Action("ModifyWorkspaceCreationProperties")
ModifyWorkspaceProperties = Action("ModifyWorkspaceProperties")
ModifyWorkspaceState = Action("ModifyWorkspaceState")
RebootWorkspaces = Action("RebootWorkspaces")
RebuildWorkspaces = Action("RebuildWorkspaces")
RegisterWorkspaceDirectory = Action("RegisterWorkspaceDirectory")
RejectAccountLinkInvitation = Action("RejectAccountLinkInvitation")
RestoreWorkspace = Action("RestoreWorkspace")
RevokeIpRules = Action("RevokeIpRules")
StartWorkspaces = Action("StartWorkspaces")
StartWorkspacesPool = Action("StartWorkspacesPool")
StopWorkspaces = Action("StopWorkspaces")
StopWorkspacesPool = Action("StopWorkspacesPool")
Stream = Action("Stream")
TerminateWorkspaces = Action("TerminateWorkspaces")
TerminateWorkspacesPool = Action("TerminateWorkspacesPool")
TerminateWorkspacesPoolSession = Action("TerminateWorkspacesPoolSession")
UpdateConnectClientAddIn = Action("UpdateConnectClientAddIn")
UpdateConnectionAliasPermission = Action("UpdateConnectionAliasPermission")
UpdateRulesOfIpGroup = Action("UpdateRulesOfIpGroup")
UpdateWorkspaceBundle = Action("UpdateWorkspaceBundle")
UpdateWorkspaceImagePermission = Action("UpdateWorkspaceImagePermission")
UpdateWorkspacesPool = Action("UpdateWorkspacesPool")
