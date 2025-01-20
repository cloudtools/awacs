# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IAM Identity Center (successor to AWS Single Sign-On) directory"
prefix = "sso-directory"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddMemberToGroup = Action("AddMemberToGroup")
CompleteVirtualMfaDeviceRegistration = Action("CompleteVirtualMfaDeviceRegistration")
CompleteWebAuthnDeviceRegistration = Action("CompleteWebAuthnDeviceRegistration")
CreateAlias = Action("CreateAlias")
CreateBearerToken = Action("CreateBearerToken")
CreateExternalIdPConfigurationForDirectory = Action(
    "CreateExternalIdPConfigurationForDirectory"
)
CreateGroup = Action("CreateGroup")
CreateProvisioningTenant = Action("CreateProvisioningTenant")
CreateUser = Action("CreateUser")
DeleteBearerToken = Action("DeleteBearerToken")
DeleteExternalIdPCertificate = Action("DeleteExternalIdPCertificate")
DeleteExternalIdPConfigurationForDirectory = Action(
    "DeleteExternalIdPConfigurationForDirectory"
)
DeleteGroup = Action("DeleteGroup")
DeleteMfaDeviceForUser = Action("DeleteMfaDeviceForUser")
DeleteProvisioningTenant = Action("DeleteProvisioningTenant")
DeleteUser = Action("DeleteUser")
DescribeDirectory = Action("DescribeDirectory")
DescribeGroup = Action("DescribeGroup")
DescribeGroups = Action("DescribeGroups")
DescribeProvisioningTenant = Action("DescribeProvisioningTenant")
DescribeUser = Action("DescribeUser")
DescribeUserByUniqueAttribute = Action("DescribeUserByUniqueAttribute")
DescribeUsers = Action("DescribeUsers")
DisableExternalIdPConfigurationForDirectory = Action(
    "DisableExternalIdPConfigurationForDirectory"
)
DisableUser = Action("DisableUser")
EnableExternalIdPConfigurationForDirectory = Action(
    "EnableExternalIdPConfigurationForDirectory"
)
EnableUser = Action("EnableUser")
GetAWSSPConfigurationForDirectory = Action("GetAWSSPConfigurationForDirectory")
GetGroupId = Action("GetGroupId")
GetUserId = Action("GetUserId")
GetUserPoolInfo = Action("GetUserPoolInfo")
ImportExternalIdPCertificate = Action("ImportExternalIdPCertificate")
IsMemberInGroup = Action("IsMemberInGroup")
ListBearerTokens = Action("ListBearerTokens")
ListExternalIdPCertificates = Action("ListExternalIdPCertificates")
ListExternalIdPConfigurationsForDirectory = Action(
    "ListExternalIdPConfigurationsForDirectory"
)
ListGroups = Action("ListGroups")
ListGroupsForMember = Action("ListGroupsForMember")
ListGroupsForUser = Action("ListGroupsForUser")
ListMembersInGroup = Action("ListMembersInGroup")
ListMfaDevicesForUser = Action("ListMfaDevicesForUser")
ListProvisioningTenants = Action("ListProvisioningTenants")
ListUsers = Action("ListUsers")
RemoveMemberFromGroup = Action("RemoveMemberFromGroup")
SearchGroups = Action("SearchGroups")
SearchUsers = Action("SearchUsers")
StartVirtualMfaDeviceRegistration = Action("StartVirtualMfaDeviceRegistration")
StartWebAuthnDeviceRegistration = Action("StartWebAuthnDeviceRegistration")
UpdateExternalIdPConfigurationForDirectory = Action(
    "UpdateExternalIdPConfigurationForDirectory"
)
UpdateGroup = Action("UpdateGroup")
UpdateGroupDisplayName = Action("UpdateGroupDisplayName")
UpdateMfaDeviceForUser = Action("UpdateMfaDeviceForUser")
UpdatePassword = Action("UpdatePassword")
UpdateUser = Action("UpdateUser")
UpdateUserName = Action("UpdateUserName")
VerifyEmail = Action("VerifyEmail")
