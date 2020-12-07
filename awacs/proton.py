# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Proton'
prefix = 'proton'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateEnvironment = Action('CreateEnvironment')
CreateEnvironmentTemplate = Action('CreateEnvironmentTemplate')
CreateEnvironmentTemplateMajorVersion = \
    Action('CreateEnvironmentTemplateMajorVersion')
CreateEnvironmentTemplateMinorVersion = \
    Action('CreateEnvironmentTemplateMinorVersion')
CreateService = Action('CreateService')
CreateServiceTemplate = Action('CreateServiceTemplate')
CreateServiceTemplateMajorVersion = \
    Action('CreateServiceTemplateMajorVersion')
CreateServiceTemplateMinorVersion = \
    Action('CreateServiceTemplateMinorVersion')
DeleteAccountRoles = Action('DeleteAccountRoles')
DeleteEnvironment = Action('DeleteEnvironment')
DeleteEnvironmentTemplate = Action('DeleteEnvironmentTemplate')
DeleteEnvironmentTemplateMajorVersion = \
    Action('DeleteEnvironmentTemplateMajorVersion')
DeleteEnvironmentTemplateMinorVersion = \
    Action('DeleteEnvironmentTemplateMinorVersion')
DeleteService = Action('DeleteService')
DeleteServiceTemplate = Action('DeleteServiceTemplate')
DeleteServiceTemplateMajorVersion = \
    Action('DeleteServiceTemplateMajorVersion')
DeleteServiceTemplateMinorVersion = \
    Action('DeleteServiceTemplateMinorVersion')
GetAccountRoles = Action('GetAccountRoles')
GetEnvironment = Action('GetEnvironment')
GetEnvironmentTemplate = Action('GetEnvironmentTemplate')
GetEnvironmentTemplateMajorVersion = \
    Action('GetEnvironmentTemplateMajorVersion')
GetEnvironmentTemplateMinorVersion = \
    Action('GetEnvironmentTemplateMinorVersion')
GetService = Action('GetService')
GetServiceInstance = Action('GetServiceInstance')
GetServiceTemplate = Action('GetServiceTemplate')
GetServiceTemplateMajorVersion = Action('GetServiceTemplateMajorVersion')
GetServiceTemplateMinorVersion = Action('GetServiceTemplateMinorVersion')
ListEnvironmentTemplateMajorVersions = \
    Action('ListEnvironmentTemplateMajorVersions')
ListEnvironmentTemplateMinorVersions = \
    Action('ListEnvironmentTemplateMinorVersions')
ListEnvironmentTemplates = Action('ListEnvironmentTemplates')
ListEnvironments = Action('ListEnvironments')
ListServiceInstances = Action('ListServiceInstances')
ListServiceTemplateMajorVersions = \
    Action('ListServiceTemplateMajorVersions')
ListServiceTemplateMinorVersions = \
    Action('ListServiceTemplateMinorVersions')
ListServiceTemplates = Action('ListServiceTemplates')
ListServices = Action('ListServices')
UpdateAccountRoles = Action('UpdateAccountRoles')
UpdateEnvironment = Action('UpdateEnvironment')
UpdateEnvironmentTemplate = Action('UpdateEnvironmentTemplate')
UpdateEnvironmentTemplateMajorVersion = \
    Action('UpdateEnvironmentTemplateMajorVersion')
UpdateEnvironmentTemplateMinorVersion = \
    Action('UpdateEnvironmentTemplateMinorVersion')
UpdateService = Action('UpdateService')
UpdateServiceInstance = Action('UpdateServiceInstance')
UpdateServicePipeline = Action('UpdateServicePipeline')
UpdateServiceTemplate = Action('UpdateServiceTemplate')
UpdateServiceTemplateMajorVersion = \
    Action('UpdateServiceTemplateMajorVersion')
UpdateServiceTemplateMinorVersion = \
    Action('UpdateServiceTemplateMinorVersion')
