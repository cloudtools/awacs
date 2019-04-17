# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Single Sign-On'
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
CreateAlias = Action('CreateAlias')
CreateApplicationInstance = Action('CreateApplicationInstance')
CreateApplicationInstanceCertificate = \
    Action('CreateApplicationInstanceCertificate')
CreateGroup = Action('CreateGroup')
CreatePermissionSet = Action('CreatePermissionSet')
CreateProfile = Action('CreateProfile')
CreateTrust = Action('CreateTrust')
CreateUser = Action('CreateUser')
DeleteApplicationInstance = Action('DeleteApplicationInstance')
DeleteApplicationInstanceCertificate = \
    Action('DeleteApplicationInstanceCertificate')
DeleteGroup = Action('DeleteGroup')
DeletePermissionSet = Action('DeletePermissionSet')
DeletePermissionsPolicy = Action('DeletePermissionsPolicy')
DeleteProfile = Action('DeleteProfile')
DeleteUser = Action('DeleteUser')
DescribeGroups = Action('DescribeGroups')
DescribePermissionsPolicies = Action('DescribePermissionsPolicies')
DescribeUsers = Action('DescribeUsers')
DisableUser = Action('DisableUser')
DisassociateDirectory = Action('DisassociateDirectory')
DisassociateProfile = Action('DisassociateProfile')
EnableUser = Action('EnableUser')
GetApplicationInstance = Action('GetApplicationInstance')
GetApplicationTemplate = Action('GetApplicationTemplate')
GetPermissionSet = Action('GetPermissionSet')
GetPermissionsPolicy = Action('GetPermissionsPolicy')
GetProfile = Action('GetProfile')
GetSSOConfiguration = Action('GetSSOConfiguration')
GetSSOStatus = Action('GetSSOStatus')
GetTrust = Action('GetTrust')
GetUserPoolInfo = Action('GetUserPoolInfo')
ImportApplicationInstanceServiceProviderMetadata = \
    Action('ImportApplicationInstanceServiceProviderMetadata')
ListApplicationInstanceCertificates = \
    Action('ListApplicationInstanceCertificates')
ListApplicationInstances = Action('ListApplicationInstances')
ListApplicationTemplates = Action('ListApplicationTemplates')
ListApplications = Action('ListApplications')
ListDirectoryAssociations = Action('ListDirectoryAssociations')
ListGroupsForUser = Action('ListGroupsForUser')
ListMembersInGroup = Action('ListMembersInGroup')
ListPermissionSets = Action('ListPermissionSets')
ListProfileAssociations = Action('ListProfileAssociations')
ListProfiles = Action('ListProfiles')
PutPermissionsPolicy = Action('PutPermissionsPolicy')
RemoveMemberFromGroup = Action('RemoveMemberFromGroup')
SearchGroups = Action('SearchGroups')
SearchUsers = Action('SearchUsers')
SetTemporaryPassword = Action('SetTemporaryPassword')
StartSSO = Action('StartSSO')
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
UpdateProfile = Action('UpdateProfile')
UpdateSSOConfiguration = Action('UpdateSSOConfiguration')
UpdateTrust = Action('UpdateTrust')
UpdateUser = Action('UpdateUser')
