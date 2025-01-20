# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Launch Wizard"
prefix = "launchwizard"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAdditionalNode = Action("CreateAdditionalNode")
CreateDeployment = Action("CreateDeployment")
CreateSettingsSet = Action("CreateSettingsSet")
DeleteAdditionalNode = Action("DeleteAdditionalNode")
DeleteApp = Action("DeleteApp")
DeleteDeployment = Action("DeleteDeployment")
DeleteSettingsSet = Action("DeleteSettingsSet")
DescribeAdditionalNode = Action("DescribeAdditionalNode")
DescribeProvisionedApp = Action("DescribeProvisionedApp")
DescribeProvisioningEvents = Action("DescribeProvisioningEvents")
DescribeSettingsSet = Action("DescribeSettingsSet")
GetDeployment = Action("GetDeployment")
GetInfrastructureSuggestion = Action("GetInfrastructureSuggestion")
GetIpAddress = Action("GetIpAddress")
GetResourceCostEstimate = Action("GetResourceCostEstimate")
GetResourceRecommendation = Action("GetResourceRecommendation")
GetSettingsSet = Action("GetSettingsSet")
GetWorkload = Action("GetWorkload")
GetWorkloadAsset = Action("GetWorkloadAsset")
GetWorkloadAssets = Action("GetWorkloadAssets")
GetWorkloadDeploymentPattern = Action("GetWorkloadDeploymentPattern")
ListAdditionalNodes = Action("ListAdditionalNodes")
ListAllowedResources = Action("ListAllowedResources")
ListDeploymentEvents = Action("ListDeploymentEvents")
ListDeployments = Action("ListDeployments")
ListProvisionedApps = Action("ListProvisionedApps")
ListResourceCostEstimates = Action("ListResourceCostEstimates")
ListSettingsSets = Action("ListSettingsSets")
ListTagsForResource = Action("ListTagsForResource")
ListWorkloadDeploymentOptions = Action("ListWorkloadDeploymentOptions")
ListWorkloadDeploymentPatterns = Action("ListWorkloadDeploymentPatterns")
ListWorkloads = Action("ListWorkloads")
PutSettingsSet = Action("PutSettingsSet")
StartProvisioning = Action("StartProvisioning")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateSettingsSet = Action("UpdateSettingsSet")
