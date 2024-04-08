# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Wireless"
prefix = "iotwireless"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAwsAccountWithPartnerAccount = Action("AssociateAwsAccountWithPartnerAccount")
AssociateMulticastGroupWithFuotaTask = Action("AssociateMulticastGroupWithFuotaTask")
AssociateWirelessDeviceWithFuotaTask = Action("AssociateWirelessDeviceWithFuotaTask")
AssociateWirelessDeviceWithMulticastGroup = Action(
    "AssociateWirelessDeviceWithMulticastGroup"
)
AssociateWirelessDeviceWithThing = Action("AssociateWirelessDeviceWithThing")
AssociateWirelessGatewayWithCertificate = Action(
    "AssociateWirelessGatewayWithCertificate"
)
AssociateWirelessGatewayWithThing = Action("AssociateWirelessGatewayWithThing")
CancelMulticastGroupSession = Action("CancelMulticastGroupSession")
CreateDestination = Action("CreateDestination")
CreateDeviceProfile = Action("CreateDeviceProfile")
CreateFuotaTask = Action("CreateFuotaTask")
CreateMulticastGroup = Action("CreateMulticastGroup")
CreateNetworkAnalyzerConfiguration = Action("CreateNetworkAnalyzerConfiguration")
CreateServiceProfile = Action("CreateServiceProfile")
CreateWirelessDevice = Action("CreateWirelessDevice")
CreateWirelessGateway = Action("CreateWirelessGateway")
CreateWirelessGatewayTask = Action("CreateWirelessGatewayTask")
CreateWirelessGatewayTaskDefinition = Action("CreateWirelessGatewayTaskDefinition")
DeleteDestination = Action("DeleteDestination")
DeleteDeviceProfile = Action("DeleteDeviceProfile")
DeleteFuotaTask = Action("DeleteFuotaTask")
DeleteMulticastGroup = Action("DeleteMulticastGroup")
DeleteNetworkAnalyzerConfiguration = Action("DeleteNetworkAnalyzerConfiguration")
DeleteQueuedMessages = Action("DeleteQueuedMessages")
DeleteServiceProfile = Action("DeleteServiceProfile")
DeleteWirelessDevice = Action("DeleteWirelessDevice")
DeleteWirelessDeviceImportTask = Action("DeleteWirelessDeviceImportTask")
DeleteWirelessGateway = Action("DeleteWirelessGateway")
DeleteWirelessGatewayTask = Action("DeleteWirelessGatewayTask")
DeleteWirelessGatewayTaskDefinition = Action("DeleteWirelessGatewayTaskDefinition")
DeregisterWirelessDevice = Action("DeregisterWirelessDevice")
DisassociateAwsAccountFromPartnerAccount = Action(
    "DisassociateAwsAccountFromPartnerAccount"
)
DisassociateMulticastGroupFromFuotaTask = Action(
    "DisassociateMulticastGroupFromFuotaTask"
)
DisassociateWirelessDeviceFromFuotaTask = Action(
    "DisassociateWirelessDeviceFromFuotaTask"
)
DisassociateWirelessDeviceFromMulticastGroup = Action(
    "DisassociateWirelessDeviceFromMulticastGroup"
)
DisassociateWirelessDeviceFromThing = Action("DisassociateWirelessDeviceFromThing")
DisassociateWirelessGatewayFromCertificate = Action(
    "DisassociateWirelessGatewayFromCertificate"
)
DisassociateWirelessGatewayFromThing = Action("DisassociateWirelessGatewayFromThing")
GetDestination = Action("GetDestination")
GetDeviceProfile = Action("GetDeviceProfile")
GetEventConfigurationByResourceTypes = Action("GetEventConfigurationByResourceTypes")
GetEventConfigurationsByResourceTypes = Action("GetEventConfigurationsByResourceTypes")
GetFuotaTask = Action("GetFuotaTask")
GetLogLevelsByResourceTypes = Action("GetLogLevelsByResourceTypes")
GetMetricConfiguration = Action("GetMetricConfiguration")
GetMetrics = Action("GetMetrics")
GetMulticastGroup = Action("GetMulticastGroup")
GetMulticastGroupSession = Action("GetMulticastGroupSession")
GetNetworkAnalyzerConfiguration = Action("GetNetworkAnalyzerConfiguration")
GetPartnerAccount = Action("GetPartnerAccount")
GetPosition = Action("GetPosition")
GetPositionConfiguration = Action("GetPositionConfiguration")
GetPositionEstimate = Action("GetPositionEstimate")
GetResourceEventConfiguration = Action("GetResourceEventConfiguration")
GetResourceLogLevel = Action("GetResourceLogLevel")
GetResourcePosition = Action("GetResourcePosition")
GetServiceEndpoint = Action("GetServiceEndpoint")
GetServiceProfile = Action("GetServiceProfile")
GetWirelessDevice = Action("GetWirelessDevice")
GetWirelessDeviceImportTask = Action("GetWirelessDeviceImportTask")
GetWirelessDeviceStatistics = Action("GetWirelessDeviceStatistics")
GetWirelessGateway = Action("GetWirelessGateway")
GetWirelessGatewayCertificate = Action("GetWirelessGatewayCertificate")
GetWirelessGatewayFirmwareInformation = Action("GetWirelessGatewayFirmwareInformation")
GetWirelessGatewayStatistics = Action("GetWirelessGatewayStatistics")
GetWirelessGatewayTask = Action("GetWirelessGatewayTask")
GetWirelessGatewayTaskDefinition = Action("GetWirelessGatewayTaskDefinition")
ListDestinations = Action("ListDestinations")
ListDeviceProfiles = Action("ListDeviceProfiles")
ListDevicesForWirelessDeviceImportTask = Action(
    "ListDevicesForWirelessDeviceImportTask"
)
ListEventConfigurations = Action("ListEventConfigurations")
ListFuotaTasks = Action("ListFuotaTasks")
ListMulticastGroups = Action("ListMulticastGroups")
ListMulticastGroupsByFuotaTask = Action("ListMulticastGroupsByFuotaTask")
ListNetworkAnalyzerConfigurations = Action("ListNetworkAnalyzerConfigurations")
ListPartnerAccounts = Action("ListPartnerAccounts")
ListPositionConfigurations = Action("ListPositionConfigurations")
ListQueuedMessages = Action("ListQueuedMessages")
ListServiceProfiles = Action("ListServiceProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListWirelessDeviceImportTasks = Action("ListWirelessDeviceImportTasks")
ListWirelessDevices = Action("ListWirelessDevices")
ListWirelessGatewayTaskDefinitions = Action("ListWirelessGatewayTaskDefinitions")
ListWirelessGateways = Action("ListWirelessGateways")
PutPositionConfiguration = Action("PutPositionConfiguration")
PutResourceLogLevel = Action("PutResourceLogLevel")
ResetAllResourceLogLevels = Action("ResetAllResourceLogLevels")
ResetResourceLogLevel = Action("ResetResourceLogLevel")
SendDataToMulticastGroup = Action("SendDataToMulticastGroup")
SendDataToWirelessDevice = Action("SendDataToWirelessDevice")
StartBulkAssociateWirelessDeviceWithMulticastGroup = Action(
    "StartBulkAssociateWirelessDeviceWithMulticastGroup"
)
StartBulkDisassociateWirelessDeviceFromMulticastGroup = Action(
    "StartBulkDisassociateWirelessDeviceFromMulticastGroup"
)
StartFuotaTask = Action("StartFuotaTask")
StartMulticastGroupSession = Action("StartMulticastGroupSession")
StartNetworkAnalyzerStream = Action("StartNetworkAnalyzerStream")
StartSingleWirelessDeviceImportTask = Action("StartSingleWirelessDeviceImportTask")
StartWirelessDeviceImportTask = Action("StartWirelessDeviceImportTask")
TagResource = Action("TagResource")
TestWirelessDevice = Action("TestWirelessDevice")
UntagResource = Action("UntagResource")
UpdateDestination = Action("UpdateDestination")
UpdateEventConfigurationByResourceTypes = Action(
    "UpdateEventConfigurationByResourceTypes"
)
UpdateEventConfigurationsByResourceTypes = Action(
    "UpdateEventConfigurationsByResourceTypes"
)
UpdateFuotaTask = Action("UpdateFuotaTask")
UpdateLogLevelsByResourceTypes = Action("UpdateLogLevelsByResourceTypes")
UpdateMetricConfiguration = Action("UpdateMetricConfiguration")
UpdateMulticastGroup = Action("UpdateMulticastGroup")
UpdateNetworkAnalyzerConfiguration = Action("UpdateNetworkAnalyzerConfiguration")
UpdatePartnerAccount = Action("UpdatePartnerAccount")
UpdatePosition = Action("UpdatePosition")
UpdateResourceEventConfiguration = Action("UpdateResourceEventConfiguration")
UpdateResourcePosition = Action("UpdateResourcePosition")
UpdateWirelessDevice = Action("UpdateWirelessDevice")
UpdateWirelessDeviceImportTask = Action("UpdateWirelessDeviceImportTask")
UpdateWirelessGateway = Action("UpdateWirelessGateway")
