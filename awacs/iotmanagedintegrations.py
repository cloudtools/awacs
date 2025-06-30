# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Managed Integrations"
prefix = "iotmanagedintegrations"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAccountAssociation = Action("CreateAccountAssociation")
CreateCloudConnector = Action("CreateCloudConnector")
CreateConnectorDestination = Action("CreateConnectorDestination")
CreateCredentialLocker = Action("CreateCredentialLocker")
CreateDestination = Action("CreateDestination")
CreateEventLogConfiguration = Action("CreateEventLogConfiguration")
CreateManagedThing = Action("CreateManagedThing")
CreateNotificationConfiguration = Action("CreateNotificationConfiguration")
CreateOtaTask = Action("CreateOtaTask")
CreateOtaTaskConfiguration = Action("CreateOtaTaskConfiguration")
CreateProvisioningProfile = Action("CreateProvisioningProfile")
DeleteAccountAssociation = Action("DeleteAccountAssociation")
DeleteCloudConnector = Action("DeleteCloudConnector")
DeleteConnectorDestination = Action("DeleteConnectorDestination")
DeleteCredentialLocker = Action("DeleteCredentialLocker")
DeleteDestination = Action("DeleteDestination")
DeleteEventLogConfiguration = Action("DeleteEventLogConfiguration")
DeleteManagedThing = Action("DeleteManagedThing")
DeleteNotificationConfiguration = Action("DeleteNotificationConfiguration")
DeleteOtaTask = Action("DeleteOtaTask")
DeleteOtaTaskConfiguration = Action("DeleteOtaTaskConfiguration")
DeleteProvisioningProfile = Action("DeleteProvisioningProfile")
DeregisterAccountAssociation = Action("DeregisterAccountAssociation")
GetAccountAssociation = Action("GetAccountAssociation")
GetCloudConnector = Action("GetCloudConnector")
GetConnectorDestination = Action("GetConnectorDestination")
GetCredentialLocker = Action("GetCredentialLocker")
GetCustomEndpoint = Action("GetCustomEndpoint")
GetDefaultEncryptionConfiguration = Action("GetDefaultEncryptionConfiguration")
GetDestination = Action("GetDestination")
GetDeviceDiscovery = Action("GetDeviceDiscovery")
GetEventLogConfiguration = Action("GetEventLogConfiguration")
GetHubConfiguration = Action("GetHubConfiguration")
GetManagedThing = Action("GetManagedThing")
GetManagedThingCapabilities = Action("GetManagedThingCapabilities")
GetManagedThingConnectivityData = Action("GetManagedThingConnectivityData")
GetManagedThingMetaData = Action("GetManagedThingMetaData")
GetManagedThingState = Action("GetManagedThingState")
GetNotificationConfiguration = Action("GetNotificationConfiguration")
GetOtaTask = Action("GetOtaTask")
GetOtaTaskConfiguration = Action("GetOtaTaskConfiguration")
GetProvisioningProfile = Action("GetProvisioningProfile")
GetRuntimeLogConfiguration = Action("GetRuntimeLogConfiguration")
GetSchemaVersion = Action("GetSchemaVersion")
ListAccountAssociations = Action("ListAccountAssociations")
ListCloudConnectors = Action("ListCloudConnectors")
ListConnectorDestinations = Action("ListConnectorDestinations")
ListCredentialLockers = Action("ListCredentialLockers")
ListDestinations = Action("ListDestinations")
ListDeviceDiscoveries = Action("ListDeviceDiscoveries")
ListDiscoveredDevices = Action("ListDiscoveredDevices")
ListEventLogConfigurations = Action("ListEventLogConfigurations")
ListManagedThingAccountAssociations = Action("ListManagedThingAccountAssociations")
ListManagedThingSchemas = Action("ListManagedThingSchemas")
ListManagedThings = Action("ListManagedThings")
ListNotificationConfigurations = Action("ListNotificationConfigurations")
ListOtaTaskConfigurations = Action("ListOtaTaskConfigurations")
ListOtaTaskExecutions = Action("ListOtaTaskExecutions")
ListOtaTasks = Action("ListOtaTasks")
ListProvisioningProfiles = Action("ListProvisioningProfiles")
ListSchemaVersions = Action("ListSchemaVersions")
ListTagsForResource = Action("ListTagsForResource")
PutDefaultEncryptionConfiguration = Action("PutDefaultEncryptionConfiguration")
PutHubConfiguration = Action("PutHubConfiguration")
PutRuntimeLogConfiguration = Action("PutRuntimeLogConfiguration")
RegisterAccountAssociation = Action("RegisterAccountAssociation")
RegisterCustomEndpoint = Action("RegisterCustomEndpoint")
ResetRuntimeLogConfiguration = Action("ResetRuntimeLogConfiguration")
SendConnectorEvent = Action("SendConnectorEvent")
SendManagedThingCommand = Action("SendManagedThingCommand")
StartAccountAssociationRefresh = Action("StartAccountAssociationRefresh")
StartDeviceDiscovery = Action("StartDeviceDiscovery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountAssociation = Action("UpdateAccountAssociation")
UpdateCloudConnector = Action("UpdateCloudConnector")
UpdateConnectorDestination = Action("UpdateConnectorDestination")
UpdateDestination = Action("UpdateDestination")
UpdateEventLogConfiguration = Action("UpdateEventLogConfiguration")
UpdateManagedThing = Action("UpdateManagedThing")
UpdateNotificationConfiguration = Action("UpdateNotificationConfiguration")
UpdateOtaTask = Action("UpdateOtaTask")
