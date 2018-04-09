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


AssociateDirectory = Action('AssociateDirectory')
AssociateProfile = Action('AssociateProfile')
CreateApplicationInstance = Action('CreateApplicationInstance')
CreateApplicationInstanceCertificate = \
    Action('CreateApplicationInstanceCertificate')
CreatePermissionSet = Action('CreatePermissionSet')
CreateProfile = Action('CreateProfile')
CreateTrust = Action('CreateTrust')
DeleteApplicationInstance = Action('DeleteApplicationInstance')
DeleteApplicationInstanceCertificate = \
    Action('DeleteApplicationInstanceCertificate')
DeletePermissionSet = Action('DeletePermissionSet')
DeletePermissionsPolicy = Action('DeletePermissionsPolicy')
DeleteProfile = Action('DeleteProfile')
DescribePermissionsPolicies = Action('DescribePermissionsPolicies')
DisassociateDirectory = Action('DisassociateDirectory')
DisassociateProfile = Action('DisassociateProfile')
GetApplicationInstance = Action('GetApplicationInstance')
GetApplicationTemplate = Action('GetApplicationTemplate')
GetPermissionSet = Action('GetPermissionSet')
GetProfile = Action('GetProfile')
GetSSOStatus = Action('GetSSOStatus')
GetTrust = Action('GetTrust')
ImportApplicationInstanceServiceProviderMetadata = \
    Action('ImportApplicationInstanceServiceProviderMetadata')
ListApplicationInstanceCertificates = \
    Action('ListApplicationInstanceCertificates')
ListApplicationInstances = Action('ListApplicationInstances')
ListApplicationTemplates = Action('ListApplicationTemplates')
ListDirectoryAssociations = Action('ListDirectoryAssociations')
ListPermissionSets = Action('ListPermissionSets')
ListProfileAssociations = Action('ListProfileAssociations')
ListProfiles = Action('ListProfiles')
PutPermissionsPolicy = Action('PutPermissionsPolicy')
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
UpdateProfile = Action('UpdateProfile')
UpdateTrust = Action('UpdateTrust')
