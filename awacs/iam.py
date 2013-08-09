# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, ARN

service_name = 'AWS Identity and Access Management'
prefix = 'iam'


class IAM_ARN(ARN):
    def __init__(self, account, resource):
        sup = super(IAM_ARN, self)
        sup.__init__('iam', region='', account=account, resource=resource)

AddRoleToInstanceProfile = Action(prefix, 'AddRoleToInstanceProfile')
AddUserToGroup = Action(prefix, 'AddUserToGroup')
ChangePassword = Action(prefix, 'ChangePassword')
CreateAccessKey = Action(prefix, 'CreateAccessKey')
CreateAccountAlias = Action(prefix, 'CreateAccountAlias')
CreateGroup = Action(prefix, 'CreateGroup')
CreateInstanceProfile = Action(prefix, 'CreateInstanceProfile')
CreateLoginProfile = Action(prefix, 'CreateLoginProfile')
CreateRole = Action(prefix, 'CreateRole')
CreateUser = Action(prefix, 'CreateUser')
CreateVirtualMFADevice = Action(prefix, 'CreateVirtualMFADevice')
DeactivateMFADevice = Action(prefix, 'DeactivateMFADevice')
DeleteAccessKey = Action(prefix, 'DeleteAccessKey')
DeleteAccountAlias = Action(prefix, 'DeleteAccountAlias')
DeleteAccountPasswordPolicy = \
    Action(prefix, 'DeleteAccountPasswordPolicy')
DeleteGroup = Action(prefix, 'DeleteGroup')
DeleteGroupPolicy = Action(prefix, 'DeleteGroupPolicy')
DeleteInstanceProfile = Action(prefix, 'DeleteInstanceProfile')
DeleteLoginProfile = Action(prefix, 'DeleteLoginProfile')
DeleteRole = Action(prefix, 'DeleteRole')
DeleteRolePolicy = Action(prefix, 'DeleteRolePolicy')
DeleteServerCertificate = Action(prefix, 'DeleteServerCertificate')
DeleteSigningCertificate = Action(prefix, 'DeleteSigningCertificate')
DeleteUser = Action(prefix, 'DeleteUser')
DeleteUserPolicy = Action(prefix, 'DeleteUserPolicy')
DeleteVirtualMFADevice = Action(prefix, 'DeleteVirtualMFADevice')
EnableMFADevice = Action(prefix, 'EnableMFADevice')
GetAccountPasswordPolicy = Action(prefix, 'GetAccountPasswordPolicy')
GetAccountSummary = Action(prefix, 'GetAccountSummary')
GetGroup = Action(prefix, 'GetGroup')
GetGroupPolicy = Action(prefix, 'GetGroupPolicy')
GetInstanceProfile = Action(prefix, 'GetInstanceProfile')
GetLoginProfile = Action(prefix, 'GetLoginProfile')
GetRole = Action(prefix, 'GetRole')
GetRolePolicy = Action(prefix, 'GetRolePolicy')
GetServerCertificate = Action(prefix, 'GetServerCertificate')
GetUser = Action(prefix, 'GetUser')
GetUserPolicy = Action(prefix, 'GetUserPolicy')
ListAccessKeys = Action(prefix, 'ListAccessKeys')
ListAccountAliases = Action(prefix, 'ListAccountAliases')
ListGroupPolicies = Action(prefix, 'ListGroupPolicies')
ListGroups = Action(prefix, 'ListGroups')
ListGroupsForUser = Action(prefix, 'ListGroupsForUser')
ListInstanceProfiles = Action(prefix, 'ListInstanceProfiles')
ListInstanceProfilesForRole = \
    Action(prefix, 'ListInstanceProfilesForRole')
ListMFADevices = Action(prefix, 'ListMFADevices')
ListRolePolicies = Action(prefix, 'ListRolePolicies')
ListRoles = Action(prefix, 'ListRoles')
ListServerCertificates = Action(prefix, 'ListServerCertificates')
ListSigningCertificates = Action(prefix, 'ListSigningCertificates')
ListUserPolicies = Action(prefix, 'ListUserPolicies')
ListUsers = Action(prefix, 'ListUsers')
ListVirtualMFADevices = Action(prefix, 'ListVirtualMFADevices')
PassRole = Action(prefix, 'PassRole')
PutGroupPolicy = Action(prefix, 'PutGroupPolicy')
PutRolePolicy = Action(prefix, 'PutRolePolicy')
PutUserPolicy = Action(prefix, 'PutUserPolicy')
RemoveRoleFromInstanceProfile = \
    Action(prefix, 'RemoveRoleFromInstanceProfile')
RemoveUserFromGroup = Action(prefix, 'RemoveUserFromGroup')
ResyncMFADevice = Action(prefix, 'ResyncMFADevice')
UpdateAccessKey = Action(prefix, 'UpdateAccessKey')
UpdateAccountPasswordPolicy = \
    Action(prefix, 'UpdateAccountPasswordPolicy')
UpdateAssumeRolePolicy = Action(prefix, 'UpdateAssumeRolePolicy')
UpdateGroup = Action(prefix, 'UpdateGroup')
UpdateLoginProfile = Action(prefix, 'UpdateLoginProfile')
UpdateServerCertificate = Action(prefix, 'UpdateServerCertificate')
UpdateSigningCertificate = Action(prefix, 'UpdateSigningCertificate')
UpdateUser = Action(prefix, 'UpdateUser')
UploadServerCertificate = Action(prefix, 'UploadServerCertificate')
UploadSigningCertificate = Action(prefix, 'UploadSigningCertificate')
