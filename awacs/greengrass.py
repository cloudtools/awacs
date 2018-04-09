# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Greengrass'
prefix = 'greengrass'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateRoleToGroup = Action('AssociateRoleToGroup')
AssociateServiceRoleToAccount = Action('AssociateServiceRoleToAccount')
CreateCoreDefinition = Action('CreateCoreDefinition')
CreateCoreDefinitionVersion = Action('CreateCoreDefinitionVersion')
CreateDeployment = Action('CreateDeployment')
CreateDeviceDefinition = Action('CreateDeviceDefinition')
CreateDeviceDefinitionVersion = Action('CreateDeviceDefinitionVersion')
CreateFunctionDefinition = Action('CreateFunctionDefinition')
CreateFunctionDefinitionVersion = \
    Action('CreateFunctionDefinitionVersion')
CreateGroup = Action('CreateGroup')
CreateGroupCertificateAuthority = \
    Action('CreateGroupCertificateAuthority')
CreateGroupVersion = Action('CreateGroupVersion')
CreateLoggerDefinition = Action('CreateLoggerDefinition')
CreateLoggerDefinitionVersion = Action('CreateLoggerDefinitionVersion')
CreateResourceDefinition = Action('CreateResourceDefinition')
CreateResourceDefinitionVersion = \
    Action('CreateResourceDefinitionVersion')
CreateSoftwareUpdateJob = Action('CreateSoftwareUpdateJob')
CreateSubscriptionDefinition = Action('CreateSubscriptionDefinition')
CreateSubscriptionDefinitionVersion = \
    Action('CreateSubscriptionDefinitionVersion')
DeleteCoreDefinition = Action('DeleteCoreDefinition')
DeleteDeviceDefinition = Action('DeleteDeviceDefinition')
DeleteFunctionDefinition = Action('DeleteFunctionDefinition')
DeleteGroup = Action('DeleteGroup')
DeleteLoggerDefinition = Action('DeleteLoggerDefinition')
DeleteResourceDefinition = Action('DeleteResourceDefinition')
DeleteSubscriptionDefinition = Action('DeleteSubscriptionDefinition')
DisassociateRoleFromGroup = Action('DisassociateRoleFromGroup')
DisassociateServiceRoleFromAccount = \
    Action('DisassociateServiceRoleFromAccount')
GetAssociatedRole = Action('GetAssociatedRole')
GetConnectivityInfo = Action('GetConnectivityInfo')
GetCoreDefinition = Action('GetCoreDefinition')
GetCoreDefinitionVersion = Action('GetCoreDefinitionVersion')
GetDeploymentStatus = Action('GetDeploymentStatus')
GetDeviceDefinition = Action('GetDeviceDefinition')
GetDeviceDefinitionVersion = Action('GetDeviceDefinitionVersion')
GetFunctionDefinition = Action('GetFunctionDefinition')
GetFunctionDefinitionVersion = Action('GetFunctionDefinitionVersion')
GetGroup = Action('GetGroup')
GetGroupCertificateAuthority = Action('GetGroupCertificateAuthority')
GetGroupCertificateConfiguration = \
    Action('GetGroupCertificateConfiguration')
GetGroupVersion = Action('GetGroupVersion')
GetLoggerDefinition = Action('GetLoggerDefinition')
GetLoggerDefinitionVersion = Action('GetLoggerDefinitionVersion')
GetResourceDefinition = Action('GetResourceDefinition')
GetResourceDefinitionVersion = Action('GetResourceDefinitionVersion')
GetServiceRoleForAccount = Action('GetServiceRoleForAccount')
GetSubscriptionDefinition = Action('GetSubscriptionDefinition')
GetSubscriptionDefinitionVersion = \
    Action('GetSubscriptionDefinitionVersion')
ListCoreDefinitionVersions = Action('ListCoreDefinitionVersions')
ListCoreDefinitions = Action('ListCoreDefinitions')
ListDeployments = Action('ListDeployments')
ListDeviceDefinitionVersions = Action('ListDeviceDefinitionVersions')
ListDeviceDefinitions = Action('ListDeviceDefinitions')
ListFunctionDefinitionVersions = Action('ListFunctionDefinitionVersions')
ListFunctionDefinitions = Action('ListFunctionDefinitions')
ListGroupCertificateAuthorities = \
    Action('ListGroupCertificateAuthorities')
ListGroupVersions = Action('ListGroupVersions')
ListGroups = Action('ListGroups')
ListLoggerDefinitionVersions = Action('ListLoggerDefinitionVersions')
ListLoggerDefinitions = Action('ListLoggerDefinitions')
ListResourceDefinitionVersions = Action('ListResourceDefinitionVersions')
ListResourceDefinitions = Action('ListResourceDefinitions')
ListSubscriptionDefinitionVersions = \
    Action('ListSubscriptionDefinitionVersions')
ListSubscriptionDefinitions = Action('ListSubscriptionDefinitions')
ResetDeployments = Action('ResetDeployments')
UpdateConnectivityInfo = Action('UpdateConnectivityInfo')
UpdateCoreDefinition = Action('UpdateCoreDefinition')
UpdateDeviceDefinition = Action('UpdateDeviceDefinition')
UpdateFunctionDefinition = Action('UpdateFunctionDefinition')
UpdateGroup = Action('UpdateGroup')
UpdateGroupCertificateConfiguration = \
    Action('UpdateGroupCertificateConfiguration')
UpdateLoggerDefinition = Action('UpdateLoggerDefinition')
UpdateResourceDefinition = Action('UpdateResourceDefinition')
UpdateSubscriptionDefinition = Action('UpdateSubscriptionDefinition')
