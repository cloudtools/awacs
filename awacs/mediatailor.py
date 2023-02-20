# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaTailor"
prefix = "mediatailor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ConfigureLogsForChannel = Action("ConfigureLogsForChannel")
ConfigureLogsForPlaybackConfiguration = Action("ConfigureLogsForPlaybackConfiguration")
CreateChannel = Action("CreateChannel")
CreateLiveSource = Action("CreateLiveSource")
CreatePrefetchSchedule = Action("CreatePrefetchSchedule")
CreateProgram = Action("CreateProgram")
CreateSourceLocation = Action("CreateSourceLocation")
CreateVodSource = Action("CreateVodSource")
DeleteChannel = Action("DeleteChannel")
DeleteChannelPolicy = Action("DeleteChannelPolicy")
DeleteLiveSource = Action("DeleteLiveSource")
DeletePlaybackConfiguration = Action("DeletePlaybackConfiguration")
DeletePrefetchSchedule = Action("DeletePrefetchSchedule")
DeleteProgram = Action("DeleteProgram")
DeleteSourceLocation = Action("DeleteSourceLocation")
DeleteVodSource = Action("DeleteVodSource")
DescribeChannel = Action("DescribeChannel")
DescribeLiveSource = Action("DescribeLiveSource")
DescribeProgram = Action("DescribeProgram")
DescribeSourceLocation = Action("DescribeSourceLocation")
DescribeVodSource = Action("DescribeVodSource")
GetChannelPolicy = Action("GetChannelPolicy")
GetChannelSchedule = Action("GetChannelSchedule")
GetPlaybackConfiguration = Action("GetPlaybackConfiguration")
GetPrefetchSchedule = Action("GetPrefetchSchedule")
ListAlerts = Action("ListAlerts")
ListChannels = Action("ListChannels")
ListLiveSources = Action("ListLiveSources")
ListPlaybackConfigurations = Action("ListPlaybackConfigurations")
ListPrefetchSchedules = Action("ListPrefetchSchedules")
ListSourceLocations = Action("ListSourceLocations")
ListTagsForResource = Action("ListTagsForResource")
ListVodSources = Action("ListVodSources")
PutChannelPolicy = Action("PutChannelPolicy")
PutPlaybackConfiguration = Action("PutPlaybackConfiguration")
StartChannel = Action("StartChannel")
StopChannel = Action("StopChannel")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateLiveSource = Action("UpdateLiveSource")
UpdateProgram = Action("UpdateProgram")
UpdateSourceLocation = Action("UpdateSourceLocation")
UpdateVodSource = Action("UpdateVodSource")
