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
CreateSettingsSet = Action("CreateSettingsSet")
DeleteAdditionalNode = Action("DeleteAdditionalNode")
DeleteApp = Action("DeleteApp")
DeleteSettingsSet = Action("DeleteSettingsSet")
DescribeAdditionalNode = Action("DescribeAdditionalNode")
DescribeProvisionedApp = Action("DescribeProvisionedApp")
DescribeProvisioningEvents = Action("DescribeProvisioningEvents")
DescribeSettingsSet = Action("DescribeSettingsSet")
GetInfrastructureSuggestion = Action("GetInfrastructureSuggestion")
GetIpAddress = Action("GetIpAddress")
GetResourceCostEstimate = Action("GetResourceCostEstimate")
GetWorkloadAssets = Action("GetWorkloadAssets")
ListAdditionalNodes = Action("ListAdditionalNodes")
ListProvisionedApps = Action("ListProvisionedApps")
ListSettingsSets = Action("ListSettingsSets")
ListWorkloadDeploymentOptions = Action("ListWorkloadDeploymentOptions")
ListWorkloads = Action("ListWorkloads")
StartProvisioning = Action("StartProvisioning")
UpdateSettingsSet = Action("UpdateSettingsSet")
