# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'QuickSight'
prefix = 'quicksight'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAdmin = Action('CreateAdmin')
CreateDashboard = Action('CreateDashboard')
CreateGroup = Action('CreateGroup')
CreateGroupMembership = Action('CreateGroupMembership')
CreateIAMPolicyAssignment = Action('CreateIAMPolicyAssignment')
CreateReader = Action('CreateReader')
CreateTemplate = Action('CreateTemplate')
CreateTemplateAlias = Action('CreateTemplateAlias')
CreateUser = Action('CreateUser')
DeleteDashboard = Action('DeleteDashboard')
DeleteGroup = Action('DeleteGroup')
DeleteGroupMembership = Action('DeleteGroupMembership')
DeleteIAMPolicyAssignment = Action('DeleteIAMPolicyAssignment')
DeleteTemplate = Action('DeleteTemplate')
DeleteTemplateAlias = Action('DeleteTemplateAlias')
DeleteUser = Action('DeleteUser')
DeleteUserByPrincipalId = Action('DeleteUserByPrincipalId')
DescribeDashboard = Action('DescribeDashboard')
DescribeDashboardPermissions = Action('DescribeDashboardPermissions')
DescribeGroup = Action('DescribeGroup')
DescribeIAMPolicyAssignment = Action('DescribeIAMPolicyAssignment')
DescribeTemplate = Action('DescribeTemplate')
DescribeTemplateAlias = Action('DescribeTemplateAlias')
DescribeTemplatePermissions = Action('DescribeTemplatePermissions')
DescribeUser = Action('DescribeUser')
GetAuthCode = Action('GetAuthCode')
GetDashboardEmbedUrl = Action('GetDashboardEmbedUrl')
GetGroupMapping = Action('GetGroupMapping')
ListDashboardVersions = Action('ListDashboardVersions')
ListDashboards = Action('ListDashboards')
ListGroupMemberships = Action('ListGroupMemberships')
ListGroups = Action('ListGroups')
ListIAMPolicyAssignments = Action('ListIAMPolicyAssignments')
ListIAMPolicyAssignmentsForUser = \
    Action('ListIAMPolicyAssignmentsForUser')
ListTagsForResource = Action('ListTagsForResource')
ListTemplateAliases = Action('ListTemplateAliases')
ListTemplateVersions = Action('ListTemplateVersions')
ListTemplates = Action('ListTemplates')
ListUserGroups = Action('ListUserGroups')
ListUsers = Action('ListUsers')
RegisterUser = Action('RegisterUser')
SearchDirectoryGroups = Action('SearchDirectoryGroups')
SetGroupMapping = Action('SetGroupMapping')
Subscribe = Action('Subscribe')
TagResource = Action('TagResource')
Unsubscribe = Action('Unsubscribe')
UntagResource = Action('UntagResource')
UpdateDashboard = Action('UpdateDashboard')
UpdateDashboardPermissions = Action('UpdateDashboardPermissions')
UpdateDashboardPublishedVersion = \
    Action('UpdateDashboardPublishedVersion')
UpdateGroup = Action('UpdateGroup')
UpdateIAMPolicyAssignment = Action('UpdateIAMPolicyAssignment')
UpdateTemplate = Action('UpdateTemplate')
UpdateTemplateAlias = Action('UpdateTemplateAlias')
UpdateTemplatePermissions = Action('UpdateTemplatePermissions')
UpdateUser = Action('UpdateUser')
