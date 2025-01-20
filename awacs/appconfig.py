# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS AppConfig"
prefix = "appconfig"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApplication = Action("CreateApplication")
CreateConfigurationProfile = Action("CreateConfigurationProfile")
CreateDeploymentStrategy = Action("CreateDeploymentStrategy")
CreateEnvironment = Action("CreateEnvironment")
CreateExtension = Action("CreateExtension")
CreateExtensionAssociation = Action("CreateExtensionAssociation")
CreateHostedConfigurationVersion = Action("CreateHostedConfigurationVersion")
DeleteApplication = Action("DeleteApplication")
DeleteConfigurationProfile = Action("DeleteConfigurationProfile")
DeleteDeploymentStrategy = Action("DeleteDeploymentStrategy")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteExtension = Action("DeleteExtension")
DeleteExtensionAssociation = Action("DeleteExtensionAssociation")
DeleteHostedConfigurationVersion = Action("DeleteHostedConfigurationVersion")
GetAccountSettings = Action("GetAccountSettings")
GetApplication = Action("GetApplication")
GetConfiguration = Action("GetConfiguration")
GetConfigurationProfile = Action("GetConfigurationProfile")
GetDeployment = Action("GetDeployment")
GetDeploymentStrategy = Action("GetDeploymentStrategy")
GetEnvironment = Action("GetEnvironment")
GetExtension = Action("GetExtension")
GetExtensionAssociation = Action("GetExtensionAssociation")
GetHostedConfigurationVersion = Action("GetHostedConfigurationVersion")
GetLatestConfiguration = Action("GetLatestConfiguration")
ListApplications = Action("ListApplications")
ListConfigurationProfiles = Action("ListConfigurationProfiles")
ListDeploymentStrategies = Action("ListDeploymentStrategies")
ListDeployments = Action("ListDeployments")
ListEnvironments = Action("ListEnvironments")
ListExtensionAssociations = Action("ListExtensionAssociations")
ListExtensions = Action("ListExtensions")
ListHostedConfigurationVersions = Action("ListHostedConfigurationVersions")
ListTagsForResource = Action("ListTagsForResource")
StartConfigurationSession = Action("StartConfigurationSession")
StartDeployment = Action("StartDeployment")
StopDeployment = Action("StopDeployment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateApplication = Action("UpdateApplication")
UpdateConfigurationProfile = Action("UpdateConfigurationProfile")
UpdateDeploymentStrategy = Action("UpdateDeploymentStrategy")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateExtension = Action("UpdateExtension")
UpdateExtensionAssociation = Action("UpdateExtensionAssociation")
ValidateConfiguration = Action("ValidateConfiguration")
