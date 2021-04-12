# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Interactive Video Service"
prefix = "ivs"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetChannel = Action("BatchGetChannel")
BatchGetStreamKey = Action("BatchGetStreamKey")
CreateChannel = Action("CreateChannel")
CreateRecordingConfiguration = Action("CreateRecordingConfiguration")
CreateStreamKey = Action("CreateStreamKey")
DeleteChannel = Action("DeleteChannel")
DeletePlaybackKeyPair = Action("DeletePlaybackKeyPair")
DeleteRecordingConfiguration = Action("DeleteRecordingConfiguration")
DeleteStreamKey = Action("DeleteStreamKey")
GetChannel = Action("GetChannel")
GetPlaybackKeyPair = Action("GetPlaybackKeyPair")
GetRecordingConfiguration = Action("GetRecordingConfiguration")
GetStream = Action("GetStream")
GetStreamKey = Action("GetStreamKey")
ImportPlaybackKeyPair = Action("ImportPlaybackKeyPair")
ListChannels = Action("ListChannels")
ListPlaybackKeyPairs = Action("ListPlaybackKeyPairs")
ListRecordingConfigurations = Action("ListRecordingConfigurations")
ListStreamKeys = Action("ListStreamKeys")
ListStreams = Action("ListStreams")
ListTagsForResource = Action("ListTagsForResource")
PutMetadata = Action("PutMetadata")
StopStream = Action("StopStream")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
