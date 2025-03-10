# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT managed integrations feature of IoT Device Management"
prefix = "iotmanagedintegrations"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCredentialLocker = Action("CreateCredentialLocker")
CreateDestination = Action("CreateDestination")
CreateEventLogConfiguration = Action("CreateEventLogConfiguration")
CreateManagedThing = Action("CreateManagedThing")
CreateNotificationConfiguration = Action("CreateNotificationConfiguration")
CreateOtaTask = Action("CreateOtaTask")
CreateOtaTaskConfiguration = Action("CreateOtaTaskConfiguration")
CreateProvisioningProfile = Action("CreateProvisioningProfile")
DeleteCredentialLocker = Action("DeleteCredentialLocker")
DeleteDestination = Action("DeleteDestination")
DeleteEventLogConfiguration = Action("DeleteEventLogConfiguration")
DeleteManagedThing = Action("DeleteManagedThing")
DeleteNotificationConfiguration = Action("DeleteNotificationConfiguration")
DeleteOtaTask = Action("DeleteOtaTask")
DeleteOtaTaskConfiguration = Action("DeleteOtaTaskConfiguration")
DeleteProvisioningProfile = Action("DeleteProvisioningProfile")
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
ListCredentialLockers = Action("ListCredentialLockers")
ListDestinations = Action("ListDestinations")
ListEventLogConfigurations = Action("ListEventLogConfigurations")
ListManagedThingSchemas = Action("ListManagedThingSchemas")
ListManagedThings = Action("ListManagedThings")
ListNotificationConfigurations = Action("ListNotificationConfigurations")
ListOtaTaskConfigurations = Action("ListOtaTaskConfigurations")
ListOtaTaskExecutions = Action("ListOtaTaskExecutions")
ListOtaTasks = Action("ListOtaTasks")
ListProvisioningProfiles = Action("ListProvisioningProfiles")
ListSchemaVersions = Action("ListSchemaVersions")
PutDefaultEncryptionConfiguration = Action("PutDefaultEncryptionConfiguration")
PutHubConfiguration = Action("PutHubConfiguration")
PutRuntimeLogConfiguration = Action("PutRuntimeLogConfiguration")
RegisterCustomEndpoint = Action("RegisterCustomEndpoint")
ResetRuntimeLogConfiguration = Action("ResetRuntimeLogConfiguration")
SendManagedThingCommand = Action("SendManagedThingCommand")
StartDeviceDiscovery = Action("StartDeviceDiscovery")
UpdateDestination = Action("UpdateDestination")
UpdateEventLogConfiguration = Action("UpdateEventLogConfiguration")
UpdateManagedThing = Action("UpdateManagedThing")
UpdateNotificationConfiguration = Action("UpdateNotificationConfiguration")
UpdateOtaTask = Action("UpdateOtaTask")
