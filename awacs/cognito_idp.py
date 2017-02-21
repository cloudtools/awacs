# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Cognito User Pools'
prefix = 'cognito-idp'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddCustomAttributes = Action('AddCustomAttributes')
AdminAddUserToGroup = Action('AdminAddUserToGroup')
AdminConfirmSignUp = Action('AdminConfirmSignUp')
AdminCreateUser = Action('AdminCreateUser')
AdminDeleteUser = Action('AdminDeleteUser')
AdminDeleteUserAttributes = Action('AdminDeleteUserAttributes')
AdminDisableUser = Action('AdminDisableUser')
AdminEnableUser = Action('AdminEnableUser')
AdminForgetDevice = Action('AdminForgetDevice')
AdminGetDevice = Action('AdminGetDevice')
AdminGetUser = Action('AdminGetUser')
AdminInitiateAuth = Action('AdminInitiateAuth')
AdminListDevices = Action('AdminListDevices')
AdminListGroupsForUser = Action('AdminListGroupsForUser')
AdminRemoveUserFromGroup = Action('AdminRemoveUserFromGroup')
AdminResetUserPassword = Action('AdminResetUserPassword')
AdminRespondToAuthChallenge = Action('AdminRespondToAuthChallenge')
AdminSetUserSettings = Action('AdminSetUserSettings')
AdminUpdateDeviceStatus = Action('AdminUpdateDeviceStatus')
AdminUpdateUserAttributes = Action('AdminUpdateUserAttributes')
AdminUserGlobalSignOut = Action('AdminUserGlobalSignOut')
CreateGroup = Action('CreateGroup')
CreateUserImportJob = Action('CreateUserImportJob')
CreateUserPool = Action('CreateUserPool')
CreateUserPoolClient = Action('CreateUserPoolClient')
DeleteGroup = Action('DeleteGroup')
DeleteUserPool = Action('DeleteUserPool')
DeleteUserPoolClient = Action('DeleteUserPoolClient')
DescribeUserImportJob = Action('DescribeUserImportJob')
DescribeUserPool = Action('DescribeUserPool')
DescribeUserPoolClient = Action('DescribeUserPoolClient')
GetCSVHeader = Action('GetCSVHeader')
GetGroup = Action('GetGroup')
ListGroups = Action('ListGroups')
ListUserImportJobs = Action('ListUserImportJobs')
ListUserPoolClients = Action('ListUserPoolClients')
ListUserPools = Action('ListUserPools')
ListUsers = Action('ListUsers')
ListUsersInGroup = Action('ListUsersInGroup')
StartUserImportJob = Action('StartUserImportJob')
StopUserImportJob = Action('StopUserImportJob')
UpdateGroup = Action('UpdateGroup')
UpdateUserPool = Action('UpdateUserPool')
UpdateUserPoolClient = Action('UpdateUserPoolClient')
