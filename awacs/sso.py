# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IAM Identity Center (successor to AWS Single Sign-On)"
prefix = "sso"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddMemberToGroup = Action("AddMemberToGroup")
AssociateDirectory = Action("AssociateDirectory")
AssociateProfile = Action("AssociateProfile")
AttachCustomerManagedPolicyReferenceToPermissionSet = Action(
    "AttachCustomerManagedPolicyReferenceToPermissionSet"
)
AttachManagedPolicyToPermissionSet = Action("AttachManagedPolicyToPermissionSet")
CreateAccountAssignment = Action("CreateAccountAssignment")
CreateAlias = Action("CreateAlias")
CreateApplication = Action("CreateApplication")
CreateApplicationAssignment = Action("CreateApplicationAssignment")
CreateApplicationInstance = Action("CreateApplicationInstance")
CreateApplicationInstanceCertificate = Action("CreateApplicationInstanceCertificate")
CreateGroup = Action("CreateGroup")
CreateInstance = Action("CreateInstance")
CreateInstanceAccessControlAttributeConfiguration = Action(
    "CreateInstanceAccessControlAttributeConfiguration"
)
CreateManagedApplicationInstance = Action("CreateManagedApplicationInstance")
CreatePermissionSet = Action("CreatePermissionSet")
CreateProfile = Action("CreateProfile")
CreateTrust = Action("CreateTrust")
CreateTrustedTokenIssuer = Action("CreateTrustedTokenIssuer")
CreateUser = Action("CreateUser")
DeleteAccountAssignment = Action("DeleteAccountAssignment")
DeleteApplication = Action("DeleteApplication")
DeleteApplicationAccessScope = Action("DeleteApplicationAccessScope")
DeleteApplicationAssignment = Action("DeleteApplicationAssignment")
DeleteApplicationAuthenticationMethod = Action("DeleteApplicationAuthenticationMethod")
DeleteApplicationGrant = Action("DeleteApplicationGrant")
DeleteApplicationInstance = Action("DeleteApplicationInstance")
DeleteApplicationInstanceCertificate = Action("DeleteApplicationInstanceCertificate")
DeleteGroup = Action("DeleteGroup")
DeleteInlinePolicyFromPermissionSet = Action("DeleteInlinePolicyFromPermissionSet")
DeleteInstance = Action("DeleteInstance")
DeleteInstanceAccessControlAttributeConfiguration = Action(
    "DeleteInstanceAccessControlAttributeConfiguration"
)
DeleteManagedApplicationInstance = Action("DeleteManagedApplicationInstance")
DeletePermissionSet = Action("DeletePermissionSet")
DeletePermissionsBoundaryFromPermissionSet = Action(
    "DeletePermissionsBoundaryFromPermissionSet"
)
DeletePermissionsPolicy = Action("DeletePermissionsPolicy")
DeleteProfile = Action("DeleteProfile")
DeleteTrustedTokenIssuer = Action("DeleteTrustedTokenIssuer")
DeleteUser = Action("DeleteUser")
DescribeAccountAssignmentCreationStatus = Action(
    "DescribeAccountAssignmentCreationStatus"
)
DescribeAccountAssignmentDeletionStatus = Action(
    "DescribeAccountAssignmentDeletionStatus"
)
DescribeApplication = Action("DescribeApplication")
DescribeApplicationAssignment = Action("DescribeApplicationAssignment")
DescribeApplicationProvider = Action("DescribeApplicationProvider")
DescribeDirectories = Action("DescribeDirectories")
DescribeGroups = Action("DescribeGroups")
DescribeInstance = Action("DescribeInstance")
DescribeInstanceAccessControlAttributeConfiguration = Action(
    "DescribeInstanceAccessControlAttributeConfiguration"
)
DescribePermissionSet = Action("DescribePermissionSet")
DescribePermissionSetProvisioningStatus = Action(
    "DescribePermissionSetProvisioningStatus"
)
DescribePermissionsPolicies = Action("DescribePermissionsPolicies")
DescribeRegisteredRegions = Action("DescribeRegisteredRegions")
DescribeTrustedTokenIssuer = Action("DescribeTrustedTokenIssuer")
DescribeTrusts = Action("DescribeTrusts")
DescribeUsers = Action("DescribeUsers")
DetachCustomerManagedPolicyReferenceFromPermissionSet = Action(
    "DetachCustomerManagedPolicyReferenceFromPermissionSet"
)
DetachManagedPolicyFromPermissionSet = Action("DetachManagedPolicyFromPermissionSet")
DisableUser = Action("DisableUser")
DisassociateDirectory = Action("DisassociateDirectory")
DisassociateProfile = Action("DisassociateProfile")
EnableUser = Action("EnableUser")
GetApplicationAccessScope = Action("GetApplicationAccessScope")
GetApplicationAssignmentConfiguration = Action("GetApplicationAssignmentConfiguration")
GetApplicationAuthenticationMethod = Action("GetApplicationAuthenticationMethod")
GetApplicationGrant = Action("GetApplicationGrant")
GetApplicationInstance = Action("GetApplicationInstance")
GetApplicationTemplate = Action("GetApplicationTemplate")
GetInlinePolicyForPermissionSet = Action("GetInlinePolicyForPermissionSet")
GetManagedApplicationInstance = Action("GetManagedApplicationInstance")
GetMfaDeviceManagementForDirectory = Action("GetMfaDeviceManagementForDirectory")
GetPermissionSet = Action("GetPermissionSet")
GetPermissionsBoundaryForPermissionSet = Action(
    "GetPermissionsBoundaryForPermissionSet"
)
GetPermissionsPolicy = Action("GetPermissionsPolicy")
GetProfile = Action("GetProfile")
GetSSOConfiguration = Action("GetSSOConfiguration")
GetSSOStatus = Action("GetSSOStatus")
GetSharedSsoConfiguration = Action("GetSharedSsoConfiguration")
GetSsoConfiguration = Action("GetSsoConfiguration")
GetTrust = Action("GetTrust")
GetUserPoolInfo = Action("GetUserPoolInfo")
ImportApplicationInstanceServiceProviderMetadata = Action(
    "ImportApplicationInstanceServiceProviderMetadata"
)
ListAccountAssignmentCreationStatus = Action("ListAccountAssignmentCreationStatus")
ListAccountAssignmentDeletionStatus = Action("ListAccountAssignmentDeletionStatus")
ListAccountAssignments = Action("ListAccountAssignments")
ListAccountAssignmentsForPrincipal = Action("ListAccountAssignmentsForPrincipal")
ListAccountsForProvisionedPermissionSet = Action(
    "ListAccountsForProvisionedPermissionSet"
)
ListApplicationAccessScopes = Action("ListApplicationAccessScopes")
ListApplicationAssignments = Action("ListApplicationAssignments")
ListApplicationAssignmentsForPrincipal = Action(
    "ListApplicationAssignmentsForPrincipal"
)
ListApplicationAuthenticationMethods = Action("ListApplicationAuthenticationMethods")
ListApplicationGrants = Action("ListApplicationGrants")
ListApplicationInstanceCertificates = Action("ListApplicationInstanceCertificates")
ListApplicationInstances = Action("ListApplicationInstances")
ListApplicationProviders = Action("ListApplicationProviders")
ListApplicationTemplates = Action("ListApplicationTemplates")
ListApplications = Action("ListApplications")
ListCustomerManagedPolicyReferencesInPermissionSet = Action(
    "ListCustomerManagedPolicyReferencesInPermissionSet"
)
ListDirectoryAssociations = Action("ListDirectoryAssociations")
ListGroupsForUser = Action("ListGroupsForUser")
ListInstances = Action("ListInstances")
ListManagedPoliciesInPermissionSet = Action("ListManagedPoliciesInPermissionSet")
ListMembersInGroup = Action("ListMembersInGroup")
ListPermissionSetProvisioningStatus = Action("ListPermissionSetProvisioningStatus")
ListPermissionSets = Action("ListPermissionSets")
ListPermissionSetsProvisionedToAccount = Action(
    "ListPermissionSetsProvisionedToAccount"
)
ListProfileAssociations = Action("ListProfileAssociations")
ListProfiles = Action("ListProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListTrustedTokenIssuers = Action("ListTrustedTokenIssuers")
ProvisionPermissionSet = Action("ProvisionPermissionSet")
PutApplicationAccessScope = Action("PutApplicationAccessScope")
PutApplicationAssignmentConfiguration = Action("PutApplicationAssignmentConfiguration")
PutApplicationAuthenticationMethod = Action("PutApplicationAuthenticationMethod")
PutApplicationGrant = Action("PutApplicationGrant")
PutInlinePolicyToPermissionSet = Action("PutInlinePolicyToPermissionSet")
PutMfaDeviceManagementForDirectory = Action("PutMfaDeviceManagementForDirectory")
PutPermissionsBoundaryToPermissionSet = Action("PutPermissionsBoundaryToPermissionSet")
PutPermissionsPolicy = Action("PutPermissionsPolicy")
RemoveMemberFromGroup = Action("RemoveMemberFromGroup")
SearchGroups = Action("SearchGroups")
SearchUsers = Action("SearchUsers")
SetTemporaryPassword = Action("SetTemporaryPassword")
StartSSO = Action("StartSSO")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateApplicationInstanceActiveCertificate = Action(
    "UpdateApplicationInstanceActiveCertificate"
)
UpdateApplicationInstanceDisplayData = Action("UpdateApplicationInstanceDisplayData")
UpdateApplicationInstanceResponseConfiguration = Action(
    "UpdateApplicationInstanceResponseConfiguration"
)
UpdateApplicationInstanceResponseSchemaConfiguration = Action(
    "UpdateApplicationInstanceResponseSchemaConfiguration"
)
UpdateApplicationInstanceSecurityConfiguration = Action(
    "UpdateApplicationInstanceSecurityConfiguration"
)
UpdateApplicationInstanceServiceProviderConfiguration = Action(
    "UpdateApplicationInstanceServiceProviderConfiguration"
)
UpdateApplicationInstanceStatus = Action("UpdateApplicationInstanceStatus")
UpdateDirectoryAssociation = Action("UpdateDirectoryAssociation")
UpdateGroup = Action("UpdateGroup")
UpdateInstance = Action("UpdateInstance")
UpdateInstanceAccessControlAttributeConfiguration = Action(
    "UpdateInstanceAccessControlAttributeConfiguration"
)
UpdateManagedApplicationInstanceStatus = Action(
    "UpdateManagedApplicationInstanceStatus"
)
UpdatePermissionSet = Action("UpdatePermissionSet")
UpdateProfile = Action("UpdateProfile")
UpdateSSOConfiguration = Action("UpdateSSOConfiguration")
UpdateTrust = Action("UpdateTrust")
UpdateTrustedTokenIssuer = Action("UpdateTrustedTokenIssuer")
UpdateUser = Action("UpdateUser")
