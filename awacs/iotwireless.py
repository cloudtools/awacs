# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Core for LoRaWAN"
prefix = "iotwireless"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CreateServiceProfile = Action("CreateServiceProfile")
CreateWirelessDevice = Action("CreateWirelessDevice")
CreateWirelessGateway = Action("CreateWirelessGateway")
CreateWirelessGatewayTask = Action("CreateWirelessGatewayTask")
CreateWirelessGatewayTaskDefinition = Action("CreateWirelessGatewayTaskDefinition")
DeleteDestination = Action("DeleteDestination")
DeleteDeviceProfile = Action("DeleteDeviceProfile")
DeleteFuotaTask = Action("DeleteFuotaTask")
DeleteMulticastGroup = Action("DeleteMulticastGroup")
DeleteServiceProfile = Action("DeleteServiceProfile")
DeleteWirelessDevice = Action("DeleteWirelessDevice")
DeleteWirelessGateway = Action("DeleteWirelessGateway")
DeleteWirelessGatewayTask = Action("DeleteWirelessGatewayTask")
DeleteWirelessGatewayTaskDefinition = Action("DeleteWirelessGatewayTaskDefinition")
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
GetFuotaTask = Action("GetFuotaTask")
GetLogLevelsByResourceTypes = Action("GetLogLevelsByResourceTypes")
GetMulticastGroup = Action("GetMulticastGroup")
GetMulticastGroupSession = Action("GetMulticastGroupSession")
GetNetworkAnalyzerConfiguration = Action("GetNetworkAnalyzerConfiguration")
GetPartnerAccount = Action("GetPartnerAccount")
GetResourceEventConfiguration = Action("GetResourceEventConfiguration")
GetResourceLogLevel = Action("GetResourceLogLevel")
GetServiceEndpoint = Action("GetServiceEndpoint")
GetServiceProfile = Action("GetServiceProfile")
GetWirelessDevice = Action("GetWirelessDevice")
GetWirelessDeviceStatistics = Action("GetWirelessDeviceStatistics")
GetWirelessGateway = Action("GetWirelessGateway")
GetWirelessGatewayCertificate = Action("GetWirelessGatewayCertificate")
GetWirelessGatewayFirmwareInformation = Action("GetWirelessGatewayFirmwareInformation")
GetWirelessGatewayStatistics = Action("GetWirelessGatewayStatistics")
GetWirelessGatewayTask = Action("GetWirelessGatewayTask")
GetWirelessGatewayTaskDefinition = Action("GetWirelessGatewayTaskDefinition")
ListDestinations = Action("ListDestinations")
ListDeviceProfiles = Action("ListDeviceProfiles")
ListFuotaTasks = Action("ListFuotaTasks")
ListMulticastGroups = Action("ListMulticastGroups")
ListMulticastGroupsByFuotaTask = Action("ListMulticastGroupsByFuotaTask")
ListPartnerAccounts = Action("ListPartnerAccounts")
ListServiceProfiles = Action("ListServiceProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListWirelessDevices = Action("ListWirelessDevices")
ListWirelessGatewayTaskDefinitions = Action("ListWirelessGatewayTaskDefinitions")
ListWirelessGateways = Action("ListWirelessGateways")
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
TagResource = Action("TagResource")
TestWirelessDevice = Action("TestWirelessDevice")
UntagResource = Action("UntagResource")
UpdateDestination = Action("UpdateDestination")
UpdateFuotaTask = Action("UpdateFuotaTask")
UpdateLogLevelsByResourceTypes = Action("UpdateLogLevelsByResourceTypes")
UpdateMulticastGroup = Action("UpdateMulticastGroup")
UpdateNetworkAnalyzerConfiguration = Action("UpdateNetworkAnalyzerConfiguration")
UpdatePartnerAccount = Action("UpdatePartnerAccount")
UpdateResourceEventConfiguration = Action("UpdateResourceEventConfiguration")
UpdateWirelessDevice = Action("UpdateWirelessDevice")
UpdateWirelessGateway = Action("UpdateWirelessGateway")
