# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Interactive Video Service"
prefix = "ivs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetChannel = Action("BatchGetChannel")
BatchGetStreamKey = Action("BatchGetStreamKey")
CreateChannel = Action("CreateChannel")
CreateParticipantToken = Action("CreateParticipantToken")
CreateRecordingConfiguration = Action("CreateRecordingConfiguration")
CreateStage = Action("CreateStage")
CreateStreamKey = Action("CreateStreamKey")
DeleteChannel = Action("DeleteChannel")
DeletePlaybackKeyPair = Action("DeletePlaybackKeyPair")
DeleteRecordingConfiguration = Action("DeleteRecordingConfiguration")
DeleteStage = Action("DeleteStage")
DeleteStreamKey = Action("DeleteStreamKey")
DisconnectParticipant = Action("DisconnectParticipant")
GetChannel = Action("GetChannel")
GetPlaybackKeyPair = Action("GetPlaybackKeyPair")
GetRecordingConfiguration = Action("GetRecordingConfiguration")
GetStage = Action("GetStage")
GetStream = Action("GetStream")
GetStreamKey = Action("GetStreamKey")
GetStreamSession = Action("GetStreamSession")
ImportPlaybackKeyPair = Action("ImportPlaybackKeyPair")
ListChannels = Action("ListChannels")
ListPlaybackKeyPairs = Action("ListPlaybackKeyPairs")
ListRecordingConfigurations = Action("ListRecordingConfigurations")
ListStages = Action("ListStages")
ListStreamKeys = Action("ListStreamKeys")
ListStreamSessions = Action("ListStreamSessions")
ListStreams = Action("ListStreams")
ListTagsForResource = Action("ListTagsForResource")
PutMetadata = Action("PutMetadata")
StopStream = Action("StopStream")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateStage = Action("UpdateStage")
