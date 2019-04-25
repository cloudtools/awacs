# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon WorkSpaces'
prefix = 'workspaces'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateIpGroups = Action('AssociateIpGroups')
AuthorizeIpRules = Action('AuthorizeIpRules')
CreateIpGroup = Action('CreateIpGroup')
CreateTags = Action('CreateTags')
CreateWorkspaces = Action('CreateWorkspaces')
DeleteIpGroup = Action('DeleteIpGroup')
DeleteTags = Action('DeleteTags')
DeleteWorkspaceImage = Action('DeleteWorkspaceImage')
DescribeAccount = Action('DescribeAccount')
DescribeAccountModifications = Action('DescribeAccountModifications')
DescribeClientProperties = Action('DescribeClientProperties')
DescribeIpGroups = Action('DescribeIpGroups')
DescribeTags = Action('DescribeTags')
DescribeWorkspaceBundles = Action('DescribeWorkspaceBundles')
DescribeWorkspaceDirectories = Action('DescribeWorkspaceDirectories')
DescribeWorkspaceImages = Action('DescribeWorkspaceImages')
DescribeWorkspaces = Action('DescribeWorkspaces')
DescribeWorkspacesConnectionStatus = \
    Action('DescribeWorkspacesConnectionStatus')
DisassociateIpGroups = Action('DisassociateIpGroups')
ImportWorkspaceImage = Action('ImportWorkspaceImage')
ListAvailableManagementCidrRanges = \
    Action('ListAvailableManagementCidrRanges')
ModifyAccount = Action('ModifyAccount')
ModifyClientProperties = Action('ModifyClientProperties')
ModifyWorkspaceProperties = Action('ModifyWorkspaceProperties')
ModifyWorkspaceState = Action('ModifyWorkspaceState')
RebootWorkspaces = Action('RebootWorkspaces')
RebuildWorkspaces = Action('RebuildWorkspaces')
RevokeIpRules = Action('RevokeIpRules')
StartWorkspaces = Action('StartWorkspaces')
StopWorkspaces = Action('StopWorkspaces')
TerminateWorkspaces = Action('TerminateWorkspaces')
UpdateRulesOfIpGroup = Action('UpdateRulesOfIpGroup')
