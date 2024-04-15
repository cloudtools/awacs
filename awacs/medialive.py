# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaLive"
prefix = "medialive"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptInputDeviceTransfer = Action("AcceptInputDeviceTransfer")
BatchDelete = Action("BatchDelete")
BatchStart = Action("BatchStart")
BatchStop = Action("BatchStop")
BatchUpdateSchedule = Action("BatchUpdateSchedule")
CancelInputDeviceTransfer = Action("CancelInputDeviceTransfer")
ClaimDevice = Action("ClaimDevice")
CreateChannel = Action("CreateChannel")
CreateCloudWatchAlarmTemplate = Action("CreateCloudWatchAlarmTemplate")
CreateCloudWatchAlarmTemplateGroup = Action("CreateCloudWatchAlarmTemplateGroup")
CreateEventBridgeRuleTemplate = Action("CreateEventBridgeRuleTemplate")
CreateEventBridgeRuleTemplateGroup = Action("CreateEventBridgeRuleTemplateGroup")
CreateInput = Action("CreateInput")
CreateInputSecurityGroup = Action("CreateInputSecurityGroup")
CreateMultiplex = Action("CreateMultiplex")
CreateMultiplexProgram = Action("CreateMultiplexProgram")
CreatePartnerInput = Action("CreatePartnerInput")
CreateSignalMap = Action("CreateSignalMap")
CreateTags = Action("CreateTags")
DeleteChannel = Action("DeleteChannel")
DeleteCloudWatchAlarmTemplate = Action("DeleteCloudWatchAlarmTemplate")
DeleteCloudWatchAlarmTemplateGroup = Action("DeleteCloudWatchAlarmTemplateGroup")
DeleteEventBridgeRuleTemplate = Action("DeleteEventBridgeRuleTemplate")
DeleteEventBridgeRuleTemplateGroup = Action("DeleteEventBridgeRuleTemplateGroup")
DeleteInput = Action("DeleteInput")
DeleteInputSecurityGroup = Action("DeleteInputSecurityGroup")
DeleteMultiplex = Action("DeleteMultiplex")
DeleteMultiplexProgram = Action("DeleteMultiplexProgram")
DeleteReservation = Action("DeleteReservation")
DeleteSchedule = Action("DeleteSchedule")
DeleteSignalMap = Action("DeleteSignalMap")
DeleteTags = Action("DeleteTags")
DescribeAccountConfiguration = Action("DescribeAccountConfiguration")
DescribeChannel = Action("DescribeChannel")
DescribeInput = Action("DescribeInput")
DescribeInputDevice = Action("DescribeInputDevice")
DescribeInputDeviceThumbnail = Action("DescribeInputDeviceThumbnail")
DescribeInputSecurityGroup = Action("DescribeInputSecurityGroup")
DescribeMultiplex = Action("DescribeMultiplex")
DescribeMultiplexProgram = Action("DescribeMultiplexProgram")
DescribeOffering = Action("DescribeOffering")
DescribeReservation = Action("DescribeReservation")
DescribeSchedule = Action("DescribeSchedule")
DescribeThumbnails = Action("DescribeThumbnails")
GetCloudWatchAlarmTemplate = Action("GetCloudWatchAlarmTemplate")
GetCloudWatchAlarmTemplateGroup = Action("GetCloudWatchAlarmTemplateGroup")
GetEventBridgeRuleTemplate = Action("GetEventBridgeRuleTemplate")
GetEventBridgeRuleTemplateGroup = Action("GetEventBridgeRuleTemplateGroup")
GetSignalMap = Action("GetSignalMap")
ListChannels = Action("ListChannels")
ListCloudWatchAlarmTemplateGroups = Action("ListCloudWatchAlarmTemplateGroups")
ListCloudWatchAlarmTemplates = Action("ListCloudWatchAlarmTemplates")
ListEventBridgeRuleTemplateGroups = Action("ListEventBridgeRuleTemplateGroups")
ListEventBridgeRuleTemplates = Action("ListEventBridgeRuleTemplates")
ListInputDeviceTransfers = Action("ListInputDeviceTransfers")
ListInputDevices = Action("ListInputDevices")
ListInputSecurityGroups = Action("ListInputSecurityGroups")
ListInputs = Action("ListInputs")
ListMultiplexPrograms = Action("ListMultiplexPrograms")
ListMultiplexes = Action("ListMultiplexes")
ListOfferings = Action("ListOfferings")
ListReservations = Action("ListReservations")
ListSignalMaps = Action("ListSignalMaps")
ListTagsForResource = Action("ListTagsForResource")
PurchaseOffering = Action("PurchaseOffering")
RebootInputDevice = Action("RebootInputDevice")
RejectInputDeviceTransfer = Action("RejectInputDeviceTransfer")
RestartChannelPipelines = Action("RestartChannelPipelines")
StartChannel = Action("StartChannel")
StartDeleteMonitorDeployment = Action("StartDeleteMonitorDeployment")
StartInputDevice = Action("StartInputDevice")
StartInputDeviceMaintenanceWindow = Action("StartInputDeviceMaintenanceWindow")
StartMonitorDeployment = Action("StartMonitorDeployment")
StartMultiplex = Action("StartMultiplex")
StartUpdateSignalMap = Action("StartUpdateSignalMap")
StopChannel = Action("StopChannel")
StopInputDevice = Action("StopInputDevice")
StopMultiplex = Action("StopMultiplex")
TransferInputDevice = Action("TransferInputDevice")
UpdateAccountConfiguration = Action("UpdateAccountConfiguration")
UpdateChannel = Action("UpdateChannel")
UpdateChannelClass = Action("UpdateChannelClass")
UpdateCloudWatchAlarmTemplate = Action("UpdateCloudWatchAlarmTemplate")
UpdateCloudWatchAlarmTemplateGroup = Action("UpdateCloudWatchAlarmTemplateGroup")
UpdateEventBridgeRuleTemplate = Action("UpdateEventBridgeRuleTemplate")
UpdateEventBridgeRuleTemplateGroup = Action("UpdateEventBridgeRuleTemplateGroup")
UpdateInput = Action("UpdateInput")
UpdateInputDevice = Action("UpdateInputDevice")
UpdateInputSecurityGroup = Action("UpdateInputSecurityGroup")
UpdateMultiplex = Action("UpdateMultiplex")
UpdateMultiplexProgram = Action("UpdateMultiplexProgram")
UpdateReservation = Action("UpdateReservation")
