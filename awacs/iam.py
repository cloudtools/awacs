import warnings
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Identity And Access Management'
prefix = 'iam'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class IAM_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(IAM_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use iam.ARN instead.",
                      FutureWarning)


AddClientIDToOpenIDConnectProvider = \
    Action('AddClientIDToOpenIDConnectProvider')
AddRoleToInstanceProfile = Action('AddRoleToInstanceProfile')
AddUserToGroup = Action('AddUserToGroup')
AttachGroupPolicy = Action('AttachGroupPolicy')
AttachRolePolicy = Action('AttachRolePolicy')
AttachUserPolicy = Action('AttachUserPolicy')
ChangePassword = Action('ChangePassword')
CreateAccessKey = Action('CreateAccessKey')
CreateAccountAlias = Action('CreateAccountAlias')
CreateGroup = Action('CreateGroup')
CreateInstanceProfile = Action('CreateInstanceProfile')
CreateLoginProfile = Action('CreateLoginProfile')
CreateOpenIDConnectProvider = Action('CreateOpenIDConnectProvider')
CreatePolicy = Action('CreatePolicy')
CreatePolicyVersion = Action('CreatePolicyVersion')
CreateRole = Action('CreateRole')
CreateSAMLProvider = Action('CreateSAMLProvider')
CreateServiceLinkedRole = Action('CreateServiceLinkedRole')
CreateServiceSpecificCredential = \
    Action('CreateServiceSpecificCredential')
CreateUser = Action('CreateUser')
CreateVirtualMFADevice = Action('CreateVirtualMFADevice')
DeactivateMFADevice = Action('DeactivateMFADevice')
DeleteAccessKey = Action('DeleteAccessKey')
DeleteAccountAlias = Action('DeleteAccountAlias')
DeleteAccountPasswordPolicy = Action('DeleteAccountPasswordPolicy')
DeleteGroup = Action('DeleteGroup')
DeleteGroupPolicy = Action('DeleteGroupPolicy')
DeleteInstanceProfile = Action('DeleteInstanceProfile')
DeleteLoginProfile = Action('DeleteLoginProfile')
DeleteOpenIDConnectProvider = Action('DeleteOpenIDConnectProvider')
DeletePolicy = Action('DeletePolicy')
DeletePolicyVersion = Action('DeletePolicyVersion')
DeleteRole = Action('DeleteRole')
DeleteRolePermissionsBoundary = Action('DeleteRolePermissionsBoundary')
DeleteRolePolicy = Action('DeleteRolePolicy')
DeleteSAMLProvider = Action('DeleteSAMLProvider')
DeleteSSHPublicKey = Action('DeleteSSHPublicKey')
DeleteServerCertificate = Action('DeleteServerCertificate')
DeleteServiceLinkedRole = Action('DeleteServiceLinkedRole')
DeleteServiceSpecificCredential = \
    Action('DeleteServiceSpecificCredential')
DeleteSigningCertificate = Action('DeleteSigningCertificate')
DeleteUser = Action('DeleteUser')
DeleteUserPermissionsBoundary = Action('DeleteUserPermissionsBoundary')
DeleteUserPolicy = Action('DeleteUserPolicy')
DeleteVirtualMFADevice = Action('DeleteVirtualMFADevice')
DetachGroupPolicy = Action('DetachGroupPolicy')
DetachRolePolicy = Action('DetachRolePolicy')
DetachUserPolicy = Action('DetachUserPolicy')
EnableMFADevice = Action('EnableMFADevice')
FinalizeSmsMfaRegistration = Action('FinalizeSmsMfaRegistration')
GenerateCredentialReport = Action('GenerateCredentialReport')
GenerateServiceLastAccessedDetails = \
    Action('GenerateServiceLastAccessedDetails')
GetAccessKeyLastUsed = Action('GetAccessKeyLastUsed')
GetAccountAuthorizationDetails = Action('GetAccountAuthorizationDetails')
GetAccountPasswordPolicy = Action('GetAccountPasswordPolicy')
GetAccountSummary = Action('GetAccountSummary')
GetContextKeysForCustomPolicy = Action('GetContextKeysForCustomPolicy')
GetContextKeysForPrincipalPolicy = \
    Action('GetContextKeysForPrincipalPolicy')
GetCredentialReport = Action('GetCredentialReport')
GetGroup = Action('GetGroup')
GetGroupPolicy = Action('GetGroupPolicy')
GetInstanceProfile = Action('GetInstanceProfile')
GetLoginProfile = Action('GetLoginProfile')
GetOpenIDConnectProvider = Action('GetOpenIDConnectProvider')
GetPolicy = Action('GetPolicy')
GetPolicyVersion = Action('GetPolicyVersion')
GetRole = Action('GetRole')
GetRolePolicy = Action('GetRolePolicy')
GetSAMLProvider = Action('GetSAMLProvider')
GetSSHPublicKey = Action('GetSSHPublicKey')
GetServerCertificate = Action('GetServerCertificate')
GetServiceLastAccessedDetails = Action('GetServiceLastAccessedDetails')
GetServiceLastAccessedDetailsWithEntities = \
    Action('GetServiceLastAccessedDetailsWithEntities')
GetServiceLinkedRoleDeletionStatus = \
    Action('GetServiceLinkedRoleDeletionStatus')
GetUser = Action('GetUser')
GetUserPolicy = Action('GetUserPolicy')
ListAccessKeys = Action('ListAccessKeys')
ListAccountAliases = Action('ListAccountAliases')
ListAttachedGroupPolicies = Action('ListAttachedGroupPolicies')
ListAttachedRolePolicies = Action('ListAttachedRolePolicies')
ListAttachedUserPolicies = Action('ListAttachedUserPolicies')
ListEntitiesForPolicy = Action('ListEntitiesForPolicy')
ListGroupPolicies = Action('ListGroupPolicies')
ListGroups = Action('ListGroups')
ListGroupsForUser = Action('ListGroupsForUser')
ListInstanceProfiles = Action('ListInstanceProfiles')
ListInstanceProfilesForRole = Action('ListInstanceProfilesForRole')
ListMFADevices = Action('ListMFADevices')
ListOpenIDConnectProviders = Action('ListOpenIDConnectProviders')
ListPolicies = Action('ListPolicies')
ListPoliciesGrantingServiceAccess = \
    Action('ListPoliciesGrantingServiceAccess')
ListPolicyVersions = Action('ListPolicyVersions')
ListRolePolicies = Action('ListRolePolicies')
ListRoleTags = Action('ListRoleTags')
ListRoles = Action('ListRoles')
ListSAMLProviders = Action('ListSAMLProviders')
ListSSHPublicKeys = Action('ListSSHPublicKeys')
ListServerCertificates = Action('ListServerCertificates')
ListServiceSpecificCredentials = Action('ListServiceSpecificCredentials')
ListSigningCertificates = Action('ListSigningCertificates')
ListUserPolicies = Action('ListUserPolicies')
ListUserTags = Action('ListUserTags')
ListUsers = Action('ListUsers')
ListVirtualMFADevices = Action('ListVirtualMFADevices')
PassRole = Action('PassRole')
PutGroupPolicy = Action('PutGroupPolicy')
PutRolePermissionsBoundary = Action('PutRolePermissionsBoundary')
PutRolePolicy = Action('PutRolePolicy')
PutUserPermissionsBoundary = Action('PutUserPermissionsBoundary')
PutUserPolicy = Action('PutUserPolicy')
RemoveClientIDFromOpenIDConnectProvider = \
    Action('RemoveClientIDFromOpenIDConnectProvider')
RemoveRoleFromInstanceProfile = Action('RemoveRoleFromInstanceProfile')
RemoveUserFromGroup = Action('RemoveUserFromGroup')
RequestSmsMfaRegistration = Action('RequestSmsMfaRegistration')
ResetServiceSpecificCredential = Action('ResetServiceSpecificCredential')
ResyncMFADevice = Action('ResyncMFADevice')
SetDefaultPolicyVersion = Action('SetDefaultPolicyVersion')
SimulateCustomPolicy = Action('SimulateCustomPolicy')
SimulatePrincipalPolicy = Action('SimulatePrincipalPolicy')
TagRole = Action('TagRole')
TagUser = Action('TagUser')
UntagRole = Action('UntagRole')
UntagUser = Action('UntagUser')
UpdateAccessKey = Action('UpdateAccessKey')
UpdateAccountPasswordPolicy = Action('UpdateAccountPasswordPolicy')
UpdateAssumeRolePolicy = Action('UpdateAssumeRolePolicy')
UpdateGroup = Action('UpdateGroup')
UpdateLoginProfile = Action('UpdateLoginProfile')
UpdateOpenIDConnectProviderThumbprint = \
    Action('UpdateOpenIDConnectProviderThumbprint')
UpdateRole = Action('UpdateRole')
UpdateRoleDescription = Action('UpdateRoleDescription')
UpdateSAMLProvider = Action('UpdateSAMLProvider')
UpdateSSHPublicKey = Action('UpdateSSHPublicKey')
UpdateServerCertificate = Action('UpdateServerCertificate')
UpdateServiceSpecificCredential = \
    Action('UpdateServiceSpecificCredential')
UpdateSigningCertificate = Action('UpdateSigningCertificate')
UpdateUser = Action('UpdateUser')
UploadSSHPublicKey = Action('UploadSSHPublicKey')
UploadServerCertificate = Action('UploadServerCertificate')
UploadSigningCertificate = Action('UploadSigningCertificate')
