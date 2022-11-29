# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Greengrass"
prefix = "greengrass"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateRoleToGroup = Action("AssociateRoleToGroup")
AssociateServiceRoleToAccount = Action("AssociateServiceRoleToAccount")
BatchAssociateClientDeviceWithCoreDevice = Action(
    "BatchAssociateClientDeviceWithCoreDevice"
)
BatchDisassociateClientDeviceFromCoreDevice = Action(
    "BatchDisassociateClientDeviceFromCoreDevice"
)
CancelDeployment = Action("CancelDeployment")
CreateComponentVersion = Action("CreateComponentVersion")
CreateConnectorDefinition = Action("CreateConnectorDefinition")
CreateConnectorDefinitionVersion = Action("CreateConnectorDefinitionVersion")
CreateCoreDefinition = Action("CreateCoreDefinition")
CreateCoreDefinitionVersion = Action("CreateCoreDefinitionVersion")
CreateDeployment = Action("CreateDeployment")
CreateDeviceDefinition = Action("CreateDeviceDefinition")
CreateDeviceDefinitionVersion = Action("CreateDeviceDefinitionVersion")
CreateFunctionDefinition = Action("CreateFunctionDefinition")
CreateFunctionDefinitionVersion = Action("CreateFunctionDefinitionVersion")
CreateGroup = Action("CreateGroup")
CreateGroupCertificateAuthority = Action("CreateGroupCertificateAuthority")
CreateGroupVersion = Action("CreateGroupVersion")
CreateLoggerDefinition = Action("CreateLoggerDefinition")
CreateLoggerDefinitionVersion = Action("CreateLoggerDefinitionVersion")
CreateResourceDefinition = Action("CreateResourceDefinition")
CreateResourceDefinitionVersion = Action("CreateResourceDefinitionVersion")
CreateSoftwareUpdateJob = Action("CreateSoftwareUpdateJob")
CreateSubscriptionDefinition = Action("CreateSubscriptionDefinition")
CreateSubscriptionDefinitionVersion = Action("CreateSubscriptionDefinitionVersion")
DeleteComponent = Action("DeleteComponent")
DeleteConnectorDefinition = Action("DeleteConnectorDefinition")
DeleteCoreDefinition = Action("DeleteCoreDefinition")
DeleteCoreDevice = Action("DeleteCoreDevice")
DeleteDeployment = Action("DeleteDeployment")
DeleteDeviceDefinition = Action("DeleteDeviceDefinition")
DeleteFunctionDefinition = Action("DeleteFunctionDefinition")
DeleteGroup = Action("DeleteGroup")
DeleteLoggerDefinition = Action("DeleteLoggerDefinition")
DeleteResourceDefinition = Action("DeleteResourceDefinition")
DeleteSubscriptionDefinition = Action("DeleteSubscriptionDefinition")
DescribeComponent = Action("DescribeComponent")
DisassociateRoleFromGroup = Action("DisassociateRoleFromGroup")
DisassociateServiceRoleFromAccount = Action("DisassociateServiceRoleFromAccount")
Discover = Action("Discover")
GetAssociatedRole = Action("GetAssociatedRole")
GetBulkDeploymentStatus = Action("GetBulkDeploymentStatus")
GetComponent = Action("GetComponent")
GetComponentVersionArtifact = Action("GetComponentVersionArtifact")
GetConnectivityInfo = Action("GetConnectivityInfo")
GetConnectorDefinition = Action("GetConnectorDefinition")
GetConnectorDefinitionVersion = Action("GetConnectorDefinitionVersion")
GetCoreDefinition = Action("GetCoreDefinition")
GetCoreDefinitionVersion = Action("GetCoreDefinitionVersion")
GetCoreDevice = Action("GetCoreDevice")
GetDeployment = Action("GetDeployment")
GetDeploymentStatus = Action("GetDeploymentStatus")
GetDeviceDefinition = Action("GetDeviceDefinition")
GetDeviceDefinitionVersion = Action("GetDeviceDefinitionVersion")
GetFunctionDefinition = Action("GetFunctionDefinition")
GetFunctionDefinitionVersion = Action("GetFunctionDefinitionVersion")
GetGroup = Action("GetGroup")
GetGroupCertificateAuthority = Action("GetGroupCertificateAuthority")
GetGroupCertificateConfiguration = Action("GetGroupCertificateConfiguration")
GetGroupVersion = Action("GetGroupVersion")
GetLoggerDefinition = Action("GetLoggerDefinition")
GetLoggerDefinitionVersion = Action("GetLoggerDefinitionVersion")
GetResourceDefinition = Action("GetResourceDefinition")
GetResourceDefinitionVersion = Action("GetResourceDefinitionVersion")
GetServiceRoleForAccount = Action("GetServiceRoleForAccount")
GetSubscriptionDefinition = Action("GetSubscriptionDefinition")
GetSubscriptionDefinitionVersion = Action("GetSubscriptionDefinitionVersion")
GetThingRuntimeConfiguration = Action("GetThingRuntimeConfiguration")
ListBulkDeploymentDetailedReports = Action("ListBulkDeploymentDetailedReports")
ListBulkDeployments = Action("ListBulkDeployments")
ListClientDevicesAssociatedWithCoreDevice = Action(
    "ListClientDevicesAssociatedWithCoreDevice"
)
ListComponentVersions = Action("ListComponentVersions")
ListComponents = Action("ListComponents")
ListConnectorDefinitionVersions = Action("ListConnectorDefinitionVersions")
ListConnectorDefinitions = Action("ListConnectorDefinitions")
ListCoreDefinitionVersions = Action("ListCoreDefinitionVersions")
ListCoreDefinitions = Action("ListCoreDefinitions")
ListCoreDevices = Action("ListCoreDevices")
ListDeployments = Action("ListDeployments")
ListDeviceDefinitionVersions = Action("ListDeviceDefinitionVersions")
ListDeviceDefinitions = Action("ListDeviceDefinitions")
ListEffectiveDeployments = Action("ListEffectiveDeployments")
ListFunctionDefinitionVersions = Action("ListFunctionDefinitionVersions")
ListFunctionDefinitions = Action("ListFunctionDefinitions")
ListGroupCertificateAuthorities = Action("ListGroupCertificateAuthorities")
ListGroupVersions = Action("ListGroupVersions")
ListGroups = Action("ListGroups")
ListInstalledComponents = Action("ListInstalledComponents")
ListLoggerDefinitionVersions = Action("ListLoggerDefinitionVersions")
ListLoggerDefinitions = Action("ListLoggerDefinitions")
ListResourceDefinitionVersions = Action("ListResourceDefinitionVersions")
ListResourceDefinitions = Action("ListResourceDefinitions")
ListSubscriptionDefinitionVersions = Action("ListSubscriptionDefinitionVersions")
ListSubscriptionDefinitions = Action("ListSubscriptionDefinitions")
ListTagsForResource = Action("ListTagsForResource")
ResetDeployments = Action("ResetDeployments")
ResolveComponentCandidates = Action("ResolveComponentCandidates")
StartBulkDeployment = Action("StartBulkDeployment")
StopBulkDeployment = Action("StopBulkDeployment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnectivityInfo = Action("UpdateConnectivityInfo")
UpdateConnectorDefinition = Action("UpdateConnectorDefinition")
UpdateCoreDefinition = Action("UpdateCoreDefinition")
UpdateDeviceDefinition = Action("UpdateDeviceDefinition")
UpdateFunctionDefinition = Action("UpdateFunctionDefinition")
UpdateGroup = Action("UpdateGroup")
UpdateGroupCertificateConfiguration = Action("UpdateGroupCertificateConfiguration")
UpdateLoggerDefinition = Action("UpdateLoggerDefinition")
UpdateResourceDefinition = Action("UpdateResourceDefinition")
UpdateSubscriptionDefinition = Action("UpdateSubscriptionDefinition")
UpdateThingRuntimeConfiguration = Action("UpdateThingRuntimeConfiguration")
