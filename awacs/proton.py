# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Proton"
prefix = "proton"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptEnvironmentAccountConnection = Action("AcceptEnvironmentAccountConnection")
CancelEnvironmentDeployment = Action("CancelEnvironmentDeployment")
CancelServiceInstanceDeployment = Action("CancelServiceInstanceDeployment")
CancelServicePipelineDeployment = Action("CancelServicePipelineDeployment")
CreateEnvironment = Action("CreateEnvironment")
CreateEnvironmentAccountConnection = Action("CreateEnvironmentAccountConnection")
CreateEnvironmentTemplate = Action("CreateEnvironmentTemplate")
CreateEnvironmentTemplateMajorVersion = Action("CreateEnvironmentTemplateMajorVersion")
CreateEnvironmentTemplateMinorVersion = Action("CreateEnvironmentTemplateMinorVersion")
CreateEnvironmentTemplateVersion = Action("CreateEnvironmentTemplateVersion")
CreateService = Action("CreateService")
CreateServiceTemplate = Action("CreateServiceTemplate")
CreateServiceTemplateMajorVersion = Action("CreateServiceTemplateMajorVersion")
CreateServiceTemplateMinorVersion = Action("CreateServiceTemplateMinorVersion")
CreateServiceTemplateVersion = Action("CreateServiceTemplateVersion")
DeleteAccountRoles = Action("DeleteAccountRoles")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteEnvironmentAccountConnection = Action("DeleteEnvironmentAccountConnection")
DeleteEnvironmentTemplate = Action("DeleteEnvironmentTemplate")
DeleteEnvironmentTemplateMajorVersion = Action("DeleteEnvironmentTemplateMajorVersion")
DeleteEnvironmentTemplateMinorVersion = Action("DeleteEnvironmentTemplateMinorVersion")
DeleteEnvironmentTemplateVersion = Action("DeleteEnvironmentTemplateVersion")
DeleteService = Action("DeleteService")
DeleteServiceTemplate = Action("DeleteServiceTemplate")
DeleteServiceTemplateMajorVersion = Action("DeleteServiceTemplateMajorVersion")
DeleteServiceTemplateMinorVersion = Action("DeleteServiceTemplateMinorVersion")
DeleteServiceTemplateVersion = Action("DeleteServiceTemplateVersion")
GetAccountRoles = Action("GetAccountRoles")
GetAccountSettings = Action("GetAccountSettings")
GetEnvironment = Action("GetEnvironment")
GetEnvironmentAccountConnection = Action("GetEnvironmentAccountConnection")
GetEnvironmentTemplate = Action("GetEnvironmentTemplate")
GetEnvironmentTemplateMajorVersion = Action("GetEnvironmentTemplateMajorVersion")
GetEnvironmentTemplateMinorVersion = Action("GetEnvironmentTemplateMinorVersion")
GetEnvironmentTemplateVersion = Action("GetEnvironmentTemplateVersion")
GetService = Action("GetService")
GetServiceInstance = Action("GetServiceInstance")
GetServiceTemplate = Action("GetServiceTemplate")
GetServiceTemplateMajorVersion = Action("GetServiceTemplateMajorVersion")
GetServiceTemplateMinorVersion = Action("GetServiceTemplateMinorVersion")
GetServiceTemplateVersion = Action("GetServiceTemplateVersion")
ListEnvironmentAccountConnections = Action("ListEnvironmentAccountConnections")
ListEnvironmentTemplateMajorVersions = Action("ListEnvironmentTemplateMajorVersions")
ListEnvironmentTemplateMinorVersions = Action("ListEnvironmentTemplateMinorVersions")
ListEnvironmentTemplateVersions = Action("ListEnvironmentTemplateVersions")
ListEnvironmentTemplates = Action("ListEnvironmentTemplates")
ListEnvironments = Action("ListEnvironments")
ListServiceInstances = Action("ListServiceInstances")
ListServiceTemplateMajorVersions = Action("ListServiceTemplateMajorVersions")
ListServiceTemplateMinorVersions = Action("ListServiceTemplateMinorVersions")
ListServiceTemplateVersions = Action("ListServiceTemplateVersions")
ListServiceTemplates = Action("ListServiceTemplates")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
RejectEnvironmentAccountConnection = Action("RejectEnvironmentAccountConnection")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountRoles = Action("UpdateAccountRoles")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateEnvironmentAccountConnection = Action("UpdateEnvironmentAccountConnection")
UpdateEnvironmentTemplate = Action("UpdateEnvironmentTemplate")
UpdateEnvironmentTemplateMajorVersion = Action("UpdateEnvironmentTemplateMajorVersion")
UpdateEnvironmentTemplateMinorVersion = Action("UpdateEnvironmentTemplateMinorVersion")
UpdateEnvironmentTemplateVersion = Action("UpdateEnvironmentTemplateVersion")
UpdateService = Action("UpdateService")
UpdateServiceInstance = Action("UpdateServiceInstance")
UpdateServicePipeline = Action("UpdateServicePipeline")
UpdateServiceTemplate = Action("UpdateServiceTemplate")
UpdateServiceTemplateMajorVersion = Action("UpdateServiceTemplateMajorVersion")
UpdateServiceTemplateMinorVersion = Action("UpdateServiceTemplateMinorVersion")
UpdateServiceTemplateVersion = Action("UpdateServiceTemplateVersion")
