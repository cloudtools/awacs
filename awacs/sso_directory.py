# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS SSO Directory'
prefix = 'sso-directory'


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
CompleteVirtualMfaDeviceRegistration = \
    Action('CompleteVirtualMfaDeviceRegistration')
CompleteWebAuthnDeviceRegistration = \
    Action('CompleteWebAuthnDeviceRegistration')
CreateAlias = Action('CreateAlias')
CreateBearerToken = Action('CreateBearerToken')
CreateExternalIdPConfigurationForDirectory = \
    Action('CreateExternalIdPConfigurationForDirectory')
CreateGroup = Action('CreateGroup')
CreateProvisioningTenant = Action('CreateProvisioningTenant')
CreateUser = Action('CreateUser')
DeleteBearerToken = Action('DeleteBearerToken')
DeleteExternalIdPCertificate = Action('DeleteExternalIdPCertificate')
DeleteExternalIdPConfigurationForDirectory = \
    Action('DeleteExternalIdPConfigurationForDirectory')
DeleteGroup = Action('DeleteGroup')
DeleteMfaDeviceForUser = Action('DeleteMfaDeviceForUser')
DeleteProvisioningTenant = Action('DeleteProvisioningTenant')
DeleteUser = Action('DeleteUser')
DescribeDirectory = Action('DescribeDirectory')
DescribeGroups = Action('DescribeGroups')
DescribeUser = Action('DescribeUser')
DescribeUsers = Action('DescribeUsers')
DisableExternalIdPConfigurationForDirectory = \
    Action('DisableExternalIdPConfigurationForDirectory')
DisableUser = Action('DisableUser')
EnableExternalIdPConfigurationForDirectory = \
    Action('EnableExternalIdPConfigurationForDirectory')
EnableUser = Action('EnableUser')
GetAWSSPConfigurationForDirectory = \
    Action('GetAWSSPConfigurationForDirectory')
ImportExternalIdPCertificate = Action('ImportExternalIdPCertificate')
IsMemberInGroup = Action('IsMemberInGroup')
ListBearerTokens = Action('ListBearerTokens')
ListExternalIdPCertificates = Action('ListExternalIdPCertificates')
ListExternalIdPConfigurationsForDirectory = \
    Action('ListExternalIdPConfigurationsForDirectory')
ListGroupsForUser = Action('ListGroupsForUser')
ListMembersInGroup = Action('ListMembersInGroup')
ListMfaDevicesForUser = Action('ListMfaDevicesForUser')
ListProvisioningTenants = Action('ListProvisioningTenants')
RemoveMemberFromGroup = Action('RemoveMemberFromGroup')
SearchGroups = Action('SearchGroups')
SearchUsers = Action('SearchUsers')
StartVirtualMfaDeviceRegistration = \
    Action('StartVirtualMfaDeviceRegistration')
StartWebAuthnDeviceRegistration = \
    Action('StartWebAuthnDeviceRegistration')
UpdateExternalIdPConfigurationForDirectory = \
    Action('UpdateExternalIdPConfigurationForDirectory')
UpdateGroup = Action('UpdateGroup')
UpdateMfaDeviceForUser = Action('UpdateMfaDeviceForUser')
UpdatePassword = Action('UpdatePassword')
UpdateUser = Action('UpdateUser')
VerifyEmail = Action('VerifyEmail')
