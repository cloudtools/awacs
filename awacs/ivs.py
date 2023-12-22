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
BatchStartViewerSessionRevocation = Action("BatchStartViewerSessionRevocation")
CreateChannel = Action("CreateChannel")
CreateEncoderConfiguration = Action("CreateEncoderConfiguration")
CreateParticipantToken = Action("CreateParticipantToken")
CreateRecordingConfiguration = Action("CreateRecordingConfiguration")
CreateStage = Action("CreateStage")
CreateStorageConfiguration = Action("CreateStorageConfiguration")
CreateStreamKey = Action("CreateStreamKey")
DeleteChannel = Action("DeleteChannel")
DeleteEncoderConfiguration = Action("DeleteEncoderConfiguration")
DeletePlaybackKeyPair = Action("DeletePlaybackKeyPair")
DeleteRecordingConfiguration = Action("DeleteRecordingConfiguration")
DeleteStage = Action("DeleteStage")
DeleteStorageConfiguration = Action("DeleteStorageConfiguration")
DeleteStreamKey = Action("DeleteStreamKey")
DisconnectParticipant = Action("DisconnectParticipant")
GetChannel = Action("GetChannel")
GetComposition = Action("GetComposition")
GetEncoderConfiguration = Action("GetEncoderConfiguration")
GetParticipant = Action("GetParticipant")
GetPlaybackKeyPair = Action("GetPlaybackKeyPair")
GetRecordingConfiguration = Action("GetRecordingConfiguration")
GetStage = Action("GetStage")
GetStageSession = Action("GetStageSession")
GetStorageConfiguration = Action("GetStorageConfiguration")
GetStream = Action("GetStream")
GetStreamKey = Action("GetStreamKey")
GetStreamSession = Action("GetStreamSession")
ImportPlaybackKeyPair = Action("ImportPlaybackKeyPair")
ListChannels = Action("ListChannels")
ListCompositions = Action("ListCompositions")
ListEncoderConfigurations = Action("ListEncoderConfigurations")
ListParticipantEvents = Action("ListParticipantEvents")
ListParticipants = Action("ListParticipants")
ListPlaybackKeyPairs = Action("ListPlaybackKeyPairs")
ListRecordingConfigurations = Action("ListRecordingConfigurations")
ListStageSessions = Action("ListStageSessions")
ListStages = Action("ListStages")
ListStorageConfigurations = Action("ListStorageConfigurations")
ListStreamKeys = Action("ListStreamKeys")
ListStreamSessions = Action("ListStreamSessions")
ListStreams = Action("ListStreams")
ListTagsForResource = Action("ListTagsForResource")
PutMetadata = Action("PutMetadata")
StartComposition = Action("StartComposition")
StartViewerSessionRevocation = Action("StartViewerSessionRevocation")
StopComposition = Action("StopComposition")
StopStream = Action("StopStream")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateStage = Action("UpdateStage")
