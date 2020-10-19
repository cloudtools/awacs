# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon QuickSight'
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


CreateAccountCustomization = Action('CreateAccountCustomization')
CreateAdmin = Action('CreateAdmin')
CreateCustomPermissions = Action('CreateCustomPermissions')
CreateDashboard = Action('CreateDashboard')
CreateGroup = Action('CreateGroup')
CreateGroupMembership = Action('CreateGroupMembership')
CreateIAMPolicyAssignment = Action('CreateIAMPolicyAssignment')
CreateNamespace = Action('CreateNamespace')
CreateReader = Action('CreateReader')
CreateTemplate = Action('CreateTemplate')
CreateTemplateAlias = Action('CreateTemplateAlias')
CreateTheme = Action('CreateTheme')
CreateThemeAlias = Action('CreateThemeAlias')
CreateUser = Action('CreateUser')
DeleteAccountCustomization = Action('DeleteAccountCustomization')
DeleteDashboard = Action('DeleteDashboard')
DeleteGroup = Action('DeleteGroup')
DeleteGroupMembership = Action('DeleteGroupMembership')
DeleteIAMPolicyAssignment = Action('DeleteIAMPolicyAssignment')
DeleteNamespace = Action('DeleteNamespace')
DeleteTemplate = Action('DeleteTemplate')
DeleteTemplateAlias = Action('DeleteTemplateAlias')
DeleteTheme = Action('DeleteTheme')
DeleteThemeAlias = Action('DeleteThemeAlias')
DeleteUser = Action('DeleteUser')
DeleteUserByPrincipalId = Action('DeleteUserByPrincipalId')
DescribeAccountCustomization = Action('DescribeAccountCustomization')
DescribeAccountSettings = Action('DescribeAccountSettings')
DescribeCustomPermissions = Action('DescribeCustomPermissions')
DescribeDashboard = Action('DescribeDashboard')
DescribeDashboardPermissions = Action('DescribeDashboardPermissions')
DescribeGroup = Action('DescribeGroup')
DescribeIAMPolicyAssignment = Action('DescribeIAMPolicyAssignment')
DescribeNamespace = Action('DescribeNamespace')
DescribeTemplate = Action('DescribeTemplate')
DescribeTemplateAlias = Action('DescribeTemplateAlias')
DescribeTemplatePermissions = Action('DescribeTemplatePermissions')
DescribeTheme = Action('DescribeTheme')
DescribeThemeAlias = Action('DescribeThemeAlias')
DescribeThemePermissions = Action('DescribeThemePermissions')
DescribeUser = Action('DescribeUser')
GetAuthCode = Action('GetAuthCode')
GetDashboardEmbedUrl = Action('GetDashboardEmbedUrl')
GetGroupMapping = Action('GetGroupMapping')
GetSessionEmbedUrl = Action('GetSessionEmbedUrl')
ListCustomPermissions = Action('ListCustomPermissions')
ListDashboardVersions = Action('ListDashboardVersions')
ListDashboards = Action('ListDashboards')
ListGroupMemberships = Action('ListGroupMemberships')
ListGroups = Action('ListGroups')
ListIAMPolicyAssignments = Action('ListIAMPolicyAssignments')
ListIAMPolicyAssignmentsForUser = \
    Action('ListIAMPolicyAssignmentsForUser')
ListNamespaces = Action('ListNamespaces')
ListTagsForResource = Action('ListTagsForResource')
ListTemplateAliases = Action('ListTemplateAliases')
ListTemplateVersions = Action('ListTemplateVersions')
ListTemplates = Action('ListTemplates')
ListThemeAliases = Action('ListThemeAliases')
ListThemeVersions = Action('ListThemeVersions')
ListThemes = Action('ListThemes')
ListUserGroups = Action('ListUserGroups')
ListUsers = Action('ListUsers')
RegisterUser = Action('RegisterUser')
SearchDirectoryGroups = Action('SearchDirectoryGroups')
SetGroupMapping = Action('SetGroupMapping')
Subscribe = Action('Subscribe')
TagResource = Action('TagResource')
Unsubscribe = Action('Unsubscribe')
UntagResource = Action('UntagResource')
UpdateAccountCustomization = Action('UpdateAccountCustomization')
UpdateAccountSettings = Action('UpdateAccountSettings')
UpdateCustomPermissions = Action('UpdateCustomPermissions')
UpdateDashboard = Action('UpdateDashboard')
UpdateDashboardPermissions = Action('UpdateDashboardPermissions')
UpdateDashboardPublishedVersion = \
    Action('UpdateDashboardPublishedVersion')
UpdateGroup = Action('UpdateGroup')
UpdateIAMPolicyAssignment = Action('UpdateIAMPolicyAssignment')
UpdateTemplate = Action('UpdateTemplate')
UpdateTemplateAlias = Action('UpdateTemplateAlias')
UpdateTemplatePermissions = Action('UpdateTemplatePermissions')
UpdateTheme = Action('UpdateTheme')
UpdateThemeAlias = Action('UpdateThemeAlias')
UpdateThemePermissions = Action('UpdateThemePermissions')
UpdateUser = Action('UpdateUser')
