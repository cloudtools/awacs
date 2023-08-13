# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Proton"
prefix = "proton"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptEnvironmentAccountConnection = Action("AcceptEnvironmentAccountConnection")
CancelComponentDeployment = Action("CancelComponentDeployment")
CancelEnvironmentDeployment = Action("CancelEnvironmentDeployment")
CancelServiceInstanceDeployment = Action("CancelServiceInstanceDeployment")
CancelServicePipelineDeployment = Action("CancelServicePipelineDeployment")
CreateComponent = Action("CreateComponent")
CreateEnvironment = Action("CreateEnvironment")
CreateEnvironmentAccountConnection = Action("CreateEnvironmentAccountConnection")
CreateEnvironmentTemplate = Action("CreateEnvironmentTemplate")
CreateEnvironmentTemplateMajorVersion = Action("CreateEnvironmentTemplateMajorVersion")
CreateEnvironmentTemplateMinorVersion = Action("CreateEnvironmentTemplateMinorVersion")
CreateEnvironmentTemplateVersion = Action("CreateEnvironmentTemplateVersion")
CreateRepository = Action("CreateRepository")
CreateService = Action("CreateService")
CreateServiceInstance = Action("CreateServiceInstance")
CreateServiceSyncConfig = Action("CreateServiceSyncConfig")
CreateServiceTemplate = Action("CreateServiceTemplate")
CreateServiceTemplateMajorVersion = Action("CreateServiceTemplateMajorVersion")
CreateServiceTemplateMinorVersion = Action("CreateServiceTemplateMinorVersion")
CreateServiceTemplateVersion = Action("CreateServiceTemplateVersion")
CreateTemplateSyncConfig = Action("CreateTemplateSyncConfig")
DeleteAccountRoles = Action("DeleteAccountRoles")
DeleteComponent = Action("DeleteComponent")
DeleteDeployment = Action("DeleteDeployment")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteEnvironmentAccountConnection = Action("DeleteEnvironmentAccountConnection")
DeleteEnvironmentTemplate = Action("DeleteEnvironmentTemplate")
DeleteEnvironmentTemplateMajorVersion = Action("DeleteEnvironmentTemplateMajorVersion")
DeleteEnvironmentTemplateMinorVersion = Action("DeleteEnvironmentTemplateMinorVersion")
DeleteEnvironmentTemplateVersion = Action("DeleteEnvironmentTemplateVersion")
DeleteRepository = Action("DeleteRepository")
DeleteService = Action("DeleteService")
DeleteServiceSyncConfig = Action("DeleteServiceSyncConfig")
DeleteServiceTemplate = Action("DeleteServiceTemplate")
DeleteServiceTemplateMajorVersion = Action("DeleteServiceTemplateMajorVersion")
DeleteServiceTemplateMinorVersion = Action("DeleteServiceTemplateMinorVersion")
DeleteServiceTemplateVersion = Action("DeleteServiceTemplateVersion")
DeleteTemplateSyncConfig = Action("DeleteTemplateSyncConfig")
GetAccountRoles = Action("GetAccountRoles")
GetAccountSettings = Action("GetAccountSettings")
GetComponent = Action("GetComponent")
GetDeployment = Action("GetDeployment")
GetEnvironment = Action("GetEnvironment")
GetEnvironmentAccountConnection = Action("GetEnvironmentAccountConnection")
GetEnvironmentTemplate = Action("GetEnvironmentTemplate")
GetEnvironmentTemplateMajorVersion = Action("GetEnvironmentTemplateMajorVersion")
GetEnvironmentTemplateMinorVersion = Action("GetEnvironmentTemplateMinorVersion")
GetEnvironmentTemplateVersion = Action("GetEnvironmentTemplateVersion")
GetRepository = Action("GetRepository")
GetRepositorySyncStatus = Action("GetRepositorySyncStatus")
GetResourceTemplateVersionStatusCounts = Action(
    "GetResourceTemplateVersionStatusCounts"
)
GetResourcesSummary = Action("GetResourcesSummary")
GetService = Action("GetService")
GetServiceInstance = Action("GetServiceInstance")
GetServiceInstanceSyncStatus = Action("GetServiceInstanceSyncStatus")
GetServiceSyncBlockerSummary = Action("GetServiceSyncBlockerSummary")
GetServiceSyncConfig = Action("GetServiceSyncConfig")
GetServiceTemplate = Action("GetServiceTemplate")
GetServiceTemplateMajorVersion = Action("GetServiceTemplateMajorVersion")
GetServiceTemplateMinorVersion = Action("GetServiceTemplateMinorVersion")
GetServiceTemplateVersion = Action("GetServiceTemplateVersion")
GetTemplateSyncConfig = Action("GetTemplateSyncConfig")
GetTemplateSyncStatus = Action("GetTemplateSyncStatus")
ListComponentOutputs = Action("ListComponentOutputs")
ListComponentProvisionedResources = Action("ListComponentProvisionedResources")
ListComponents = Action("ListComponents")
ListDeployments = Action("ListDeployments")
ListEnvironmentAccountConnections = Action("ListEnvironmentAccountConnections")
ListEnvironmentOutputs = Action("ListEnvironmentOutputs")
ListEnvironmentProvisionedResources = Action("ListEnvironmentProvisionedResources")
ListEnvironmentTemplateMajorVersions = Action("ListEnvironmentTemplateMajorVersions")
ListEnvironmentTemplateMinorVersions = Action("ListEnvironmentTemplateMinorVersions")
ListEnvironmentTemplateVersions = Action("ListEnvironmentTemplateVersions")
ListEnvironmentTemplates = Action("ListEnvironmentTemplates")
ListEnvironments = Action("ListEnvironments")
ListRepositories = Action("ListRepositories")
ListRepositorySyncDefinitions = Action("ListRepositorySyncDefinitions")
ListServiceInstanceOutputs = Action("ListServiceInstanceOutputs")
ListServiceInstanceProvisionedResources = Action(
    "ListServiceInstanceProvisionedResources"
)
ListServiceInstances = Action("ListServiceInstances")
ListServicePipelineOutputs = Action("ListServicePipelineOutputs")
ListServicePipelineProvisionedResources = Action(
    "ListServicePipelineProvisionedResources"
)
ListServiceTemplateMajorVersions = Action("ListServiceTemplateMajorVersions")
ListServiceTemplateMinorVersions = Action("ListServiceTemplateMinorVersions")
ListServiceTemplateVersions = Action("ListServiceTemplateVersions")
ListServiceTemplates = Action("ListServiceTemplates")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
NotifyResourceDeploymentStatusChange = Action("NotifyResourceDeploymentStatusChange")
RejectEnvironmentAccountConnection = Action("RejectEnvironmentAccountConnection")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountRoles = Action("UpdateAccountRoles")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateComponent = Action("UpdateComponent")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateEnvironmentAccountConnection = Action("UpdateEnvironmentAccountConnection")
UpdateEnvironmentTemplate = Action("UpdateEnvironmentTemplate")
UpdateEnvironmentTemplateMajorVersion = Action("UpdateEnvironmentTemplateMajorVersion")
UpdateEnvironmentTemplateMinorVersion = Action("UpdateEnvironmentTemplateMinorVersion")
UpdateEnvironmentTemplateVersion = Action("UpdateEnvironmentTemplateVersion")
UpdateRepository = Action("UpdateRepository")
UpdateService = Action("UpdateService")
UpdateServiceInstance = Action("UpdateServiceInstance")
UpdateServicePipeline = Action("UpdateServicePipeline")
UpdateServiceSyncBlocker = Action("UpdateServiceSyncBlocker")
UpdateServiceSyncConfig = Action("UpdateServiceSyncConfig")
UpdateServiceTemplate = Action("UpdateServiceTemplate")
UpdateServiceTemplateMajorVersion = Action("UpdateServiceTemplateMajorVersion")
UpdateServiceTemplateMinorVersion = Action("UpdateServiceTemplateMinorVersion")
UpdateServiceTemplateVersion = Action("UpdateServiceTemplateVersion")
UpdateTemplateSyncConfig = Action("UpdateTemplateSyncConfig")
