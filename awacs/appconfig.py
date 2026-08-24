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
CreateExperimentDefinition = Action("CreateExperimentDefinition")
CreateExtension = Action("CreateExtension")
CreateExtensionAssociation = Action("CreateExtensionAssociation")
CreateHostedConfigurationVersion = Action("CreateHostedConfigurationVersion")
DeleteApplication = Action("DeleteApplication")
DeleteConfigurationProfile = Action("DeleteConfigurationProfile")
DeleteDeploymentStrategy = Action("DeleteDeploymentStrategy")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteExperimentDefinition = Action("DeleteExperimentDefinition")
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
GetExperimentDefinition = Action("GetExperimentDefinition")
GetExperimentRun = Action("GetExperimentRun")
GetExtension = Action("GetExtension")
GetExtensionAssociation = Action("GetExtensionAssociation")
GetHostedConfigurationVersion = Action("GetHostedConfigurationVersion")
GetLatestConfiguration = Action("GetLatestConfiguration")
ListApplications = Action("ListApplications")
ListConfigurationProfiles = Action("ListConfigurationProfiles")
ListDeploymentStrategies = Action("ListDeploymentStrategies")
ListDeployments = Action("ListDeployments")
ListEnvironments = Action("ListEnvironments")
ListExperimentDefinitions = Action("ListExperimentDefinitions")
ListExperimentRunEvents = Action("ListExperimentRunEvents")
ListExperimentRuns = Action("ListExperimentRuns")
ListExtensionAssociations = Action("ListExtensionAssociations")
ListExtensions = Action("ListExtensions")
ListHostedConfigurationVersions = Action("ListHostedConfigurationVersions")
ListTagsForResource = Action("ListTagsForResource")
StartConfigurationSession = Action("StartConfigurationSession")
StartDeployment = Action("StartDeployment")
StartExperimentRun = Action("StartExperimentRun")
StopDeployment = Action("StopDeployment")
StopExperimentRun = Action("StopExperimentRun")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateApplication = Action("UpdateApplication")
UpdateConfigurationProfile = Action("UpdateConfigurationProfile")
UpdateDeploymentStrategy = Action("UpdateDeploymentStrategy")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateExperimentDefinition = Action("UpdateExperimentDefinition")
UpdateExperimentRun = Action("UpdateExperimentRun")
UpdateExtension = Action("UpdateExtension")
UpdateExtensionAssociation = Action("UpdateExtensionAssociation")
ValidateConfiguration = Action("ValidateConfiguration")
