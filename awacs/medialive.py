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
CreateInput = Action("CreateInput")
CreateInputSecurityGroup = Action("CreateInputSecurityGroup")
CreateMultiplex = Action("CreateMultiplex")
CreateMultiplexProgram = Action("CreateMultiplexProgram")
CreatePartnerInput = Action("CreatePartnerInput")
CreateTags = Action("CreateTags")
DeleteChannel = Action("DeleteChannel")
DeleteInput = Action("DeleteInput")
DeleteInputSecurityGroup = Action("DeleteInputSecurityGroup")
DeleteMultiplex = Action("DeleteMultiplex")
DeleteMultiplexProgram = Action("DeleteMultiplexProgram")
DeleteReservation = Action("DeleteReservation")
DeleteSchedule = Action("DeleteSchedule")
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
ListChannels = Action("ListChannels")
ListInputDeviceTransfers = Action("ListInputDeviceTransfers")
ListInputDevices = Action("ListInputDevices")
ListInputSecurityGroups = Action("ListInputSecurityGroups")
ListInputs = Action("ListInputs")
ListMultiplexPrograms = Action("ListMultiplexPrograms")
ListMultiplexes = Action("ListMultiplexes")
ListOfferings = Action("ListOfferings")
ListReservations = Action("ListReservations")
ListTagsForResource = Action("ListTagsForResource")
PurchaseOffering = Action("PurchaseOffering")
RebootInputDevice = Action("RebootInputDevice")
RejectInputDeviceTransfer = Action("RejectInputDeviceTransfer")
StartChannel = Action("StartChannel")
StartInputDevice = Action("StartInputDevice")
StartInputDeviceMaintenanceWindow = Action("StartInputDeviceMaintenanceWindow")
StartMultiplex = Action("StartMultiplex")
StopChannel = Action("StopChannel")
StopInputDevice = Action("StopInputDevice")
StopMultiplex = Action("StopMultiplex")
TransferInputDevice = Action("TransferInputDevice")
UpdateAccountConfiguration = Action("UpdateAccountConfiguration")
UpdateChannel = Action("UpdateChannel")
UpdateChannelClass = Action("UpdateChannelClass")
UpdateInput = Action("UpdateInput")
UpdateInputDevice = Action("UpdateInputDevice")
UpdateInputSecurityGroup = Action("UpdateInputSecurityGroup")
UpdateMultiplex = Action("UpdateMultiplex")
UpdateMultiplexProgram = Action("UpdateMultiplexProgram")
UpdateReservation = Action("UpdateReservation")
