# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS SSO'
prefix = 'sso'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddMemberToGroup = Action('AddMemberToGroup')
AssociateDirectory = Action('AssociateDirectory')
AssociateProfile = Action('AssociateProfile')
AttachManagedPolicyToPermissionSet = \
    Action('AttachManagedPolicyToPermissionSet')
CreateAccountAssignment = Action('CreateAccountAssignment')
CreateAlias = Action('CreateAlias')
CreateApplicationInstance = Action('CreateApplicationInstance')
CreateApplicationInstanceCertificate = \
    Action('CreateApplicationInstanceCertificate')
CreateGroup = Action('CreateGroup')
CreateManagedApplicationInstance = \
    Action('CreateManagedApplicationInstance')
CreatePermissionSet = Action('CreatePermissionSet')
CreateProfile = Action('CreateProfile')
CreateTrust = Action('CreateTrust')
CreateUser = Action('CreateUser')
DeleteAccountAssignment = Action('DeleteAccountAssignment')
DeleteApplicationInstance = Action('DeleteApplicationInstance')
DeleteApplicationInstanceCertificate = \
    Action('DeleteApplicationInstanceCertificate')
DeleteGroup = Action('DeleteGroup')
DeleteInlinePolicyFromPermissionSet = \
    Action('DeleteInlinePolicyFromPermissionSet')
DeleteManagedApplicationInstance = \
    Action('DeleteManagedApplicationInstance')
DeletePermissionSet = Action('DeletePermissionSet')
DeletePermissionsPolicy = Action('DeletePermissionsPolicy')
DeleteProfile = Action('DeleteProfile')
DeleteUser = Action('DeleteUser')
DescribeAccountAssignmentCreationStatus = \
    Action('DescribeAccountAssignmentCreationStatus')
DescribeAccountAssignmentDeletionStatus = \
    Action('DescribeAccountAssignmentDeletionStatus')
DescribeGroups = Action('DescribeGroups')
DescribePermissionSet = Action('DescribePermissionSet')
DescribePermissionSetProvisioningStatus = \
    Action('DescribePermissionSetProvisioningStatus')
DescribePermissionsPolicies = Action('DescribePermissionsPolicies')
DescribeRegisteredRegions = Action('DescribeRegisteredRegions')
DescribeUsers = Action('DescribeUsers')
DetachManagedPolicyFromPermissionSet = \
    Action('DetachManagedPolicyFromPermissionSet')
DisableUser = Action('DisableUser')
DisassociateDirectory = Action('DisassociateDirectory')
DisassociateProfile = Action('DisassociateProfile')
EnableUser = Action('EnableUser')
GetApplicationInstance = Action('GetApplicationInstance')
GetApplicationTemplate = Action('GetApplicationTemplate')
GetInlinePolicyForPermissionSet = \
    Action('GetInlinePolicyForPermissionSet')
GetManagedApplicationInstance = Action('GetManagedApplicationInstance')
GetMfaDeviceManagementForDirectory = \
    Action('GetMfaDeviceManagementForDirectory')
GetPermissionSet = Action('GetPermissionSet')
GetPermissionsPolicy = Action('GetPermissionsPolicy')
GetProfile = Action('GetProfile')
GetSSOConfiguration = Action('GetSSOConfiguration')
GetSSOStatus = Action('GetSSOStatus')
GetSharedSsoConfiguration = Action('GetSharedSsoConfiguration')
GetSsoConfiguration = Action('GetSsoConfiguration')
GetTrust = Action('GetTrust')
GetUserPoolInfo = Action('GetUserPoolInfo')
ImportApplicationInstanceServiceProviderMetadata = \
    Action('ImportApplicationInstanceServiceProviderMetadata')
ListAccountAssignmentCreationStatus = \
    Action('ListAccountAssignmentCreationStatus')
ListAccountAssignmentDeletionStatus = \
    Action('ListAccountAssignmentDeletionStatus')
ListAccountAssignments = Action('ListAccountAssignments')
ListAccountsForProvisionedPermissionSet = \
    Action('ListAccountsForProvisionedPermissionSet')
ListApplicationInstanceCertificates = \
    Action('ListApplicationInstanceCertificates')
ListApplicationInstances = Action('ListApplicationInstances')
ListApplicationTemplates = Action('ListApplicationTemplates')
ListApplications = Action('ListApplications')
ListDirectoryAssociations = Action('ListDirectoryAssociations')
ListGroupsForUser = Action('ListGroupsForUser')
ListInstances = Action('ListInstances')
ListManagedPoliciesInPermissionSet = \
    Action('ListManagedPoliciesInPermissionSet')
ListMembersInGroup = Action('ListMembersInGroup')
ListPermissionSetProvisioningStatus = \
    Action('ListPermissionSetProvisioningStatus')
ListPermissionSets = Action('ListPermissionSets')
ListPermissionSetsProvisionedToAccount = \
    Action('ListPermissionSetsProvisionedToAccount')
ListProfileAssociations = Action('ListProfileAssociations')
ListProfiles = Action('ListProfiles')
ListTagsForResource = Action('ListTagsForResource')
ProvisionPermissionSet = Action('ProvisionPermissionSet')
PutInlinePolicyToPermissionSet = Action('PutInlinePolicyToPermissionSet')
PutMfaDeviceManagementForDirectory = \
    Action('PutMfaDeviceManagementForDirectory')
PutPermissionsPolicy = Action('PutPermissionsPolicy')
RemoveMemberFromGroup = Action('RemoveMemberFromGroup')
SearchGroups = Action('SearchGroups')
SearchUsers = Action('SearchUsers')
SetTemporaryPassword = Action('SetTemporaryPassword')
StartSSO = Action('StartSSO')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApplicationInstanceActiveCertificate = \
    Action('UpdateApplicationInstanceActiveCertificate')
UpdateApplicationInstanceDisplayData = \
    Action('UpdateApplicationInstanceDisplayData')
UpdateApplicationInstanceResponseConfiguration = \
    Action('UpdateApplicationInstanceResponseConfiguration')
UpdateApplicationInstanceResponseSchemaConfiguration = \
    Action('UpdateApplicationInstanceResponseSchemaConfiguration')
UpdateApplicationInstanceSecurityConfiguration = \
    Action('UpdateApplicationInstanceSecurityConfiguration')
UpdateApplicationInstanceServiceProviderConfiguration = \
    Action('UpdateApplicationInstanceServiceProviderConfiguration')
UpdateApplicationInstanceStatus = \
    Action('UpdateApplicationInstanceStatus')
UpdateDirectoryAssociation = Action('UpdateDirectoryAssociation')
UpdateGroup = Action('UpdateGroup')
UpdateManagedApplicationInstanceStatus = \
    Action('UpdateManagedApplicationInstanceStatus')
UpdatePermissionSet = Action('UpdatePermissionSet')
UpdateProfile = Action('UpdateProfile')
UpdateSSOConfiguration = Action('UpdateSSOConfiguration')
UpdateTrust = Action('UpdateTrust')
UpdateUser = Action('UpdateUser')
