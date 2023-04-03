# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Ground Station"
prefix = "groundstation"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelContact = Action("CancelContact")
CreateConfig = Action("CreateConfig")
CreateDataflowEndpointGroup = Action("CreateDataflowEndpointGroup")
CreateEphemeris = Action("CreateEphemeris")
CreateMissionProfile = Action("CreateMissionProfile")
DeleteConfig = Action("DeleteConfig")
DeleteDataflowEndpointGroup = Action("DeleteDataflowEndpointGroup")
DeleteEphemeris = Action("DeleteEphemeris")
DeleteMissionProfile = Action("DeleteMissionProfile")
DescribeContact = Action("DescribeContact")
DescribeEphemeris = Action("DescribeEphemeris")
GetAgentConfiguration = Action("GetAgentConfiguration")
GetConfig = Action("GetConfig")
GetDataflowEndpointGroup = Action("GetDataflowEndpointGroup")
GetMinuteUsage = Action("GetMinuteUsage")
GetMissionProfile = Action("GetMissionProfile")
GetSatellite = Action("GetSatellite")
ListConfigs = Action("ListConfigs")
ListContacts = Action("ListContacts")
ListDataflowEndpointGroups = Action("ListDataflowEndpointGroups")
ListEphemerides = Action("ListEphemerides")
ListGroundStations = Action("ListGroundStations")
ListMissionProfiles = Action("ListMissionProfiles")
ListSatellites = Action("ListSatellites")
ListTagsForResource = Action("ListTagsForResource")
RegisterAgent = Action("RegisterAgent")
ReserveContact = Action("ReserveContact")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgentStatus = Action("UpdateAgentStatus")
UpdateConfig = Action("UpdateConfig")
UpdateEphemeris = Action("UpdateEphemeris")
UpdateMissionProfile = Action("UpdateMissionProfile")
