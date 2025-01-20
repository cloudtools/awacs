# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Kinesis Video Streams"
prefix = "kinesisvideo"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ConnectAsMaster = Action("ConnectAsMaster")
ConnectAsViewer = Action("ConnectAsViewer")
CreateSignalingChannel = Action("CreateSignalingChannel")
CreateStream = Action("CreateStream")
DeleteEdgeConfiguration = Action("DeleteEdgeConfiguration")
DeleteSignalingChannel = Action("DeleteSignalingChannel")
DeleteStream = Action("DeleteStream")
DescribeEdgeConfiguration = Action("DescribeEdgeConfiguration")
DescribeImageGenerationConfiguration = Action("DescribeImageGenerationConfiguration")
DescribeMappedResourceConfiguration = Action("DescribeMappedResourceConfiguration")
DescribeMediaStorageConfiguration = Action("DescribeMediaStorageConfiguration")
DescribeNotificationConfiguration = Action("DescribeNotificationConfiguration")
DescribeSignalingChannel = Action("DescribeSignalingChannel")
DescribeStream = Action("DescribeStream")
GetClip = Action("GetClip")
GetDASHStreamingSessionURL = Action("GetDASHStreamingSessionURL")
GetDataEndpoint = Action("GetDataEndpoint")
GetHLSStreamingSessionURL = Action("GetHLSStreamingSessionURL")
GetIceServerConfig = Action("GetIceServerConfig")
GetImages = Action("GetImages")
GetMedia = Action("GetMedia")
GetMediaForFragmentList = Action("GetMediaForFragmentList")
GetSignalingChannelEndpoint = Action("GetSignalingChannelEndpoint")
JoinStorageSession = Action("JoinStorageSession")
JoinStorageSessionAsViewer = Action("JoinStorageSessionAsViewer")
ListEdgeAgentConfigurations = Action("ListEdgeAgentConfigurations")
ListFragments = Action("ListFragments")
ListSignalingChannels = Action("ListSignalingChannels")
ListStreams = Action("ListStreams")
ListTagsForResource = Action("ListTagsForResource")
ListTagsForStream = Action("ListTagsForStream")
PutMedia = Action("PutMedia")
SendAlexaOfferToMaster = Action("SendAlexaOfferToMaster")
StartEdgeConfigurationUpdate = Action("StartEdgeConfigurationUpdate")
TagResource = Action("TagResource")
TagStream = Action("TagStream")
UntagResource = Action("UntagResource")
UntagStream = Action("UntagStream")
UpdateDataRetention = Action("UpdateDataRetention")
UpdateImageGenerationConfiguration = Action("UpdateImageGenerationConfiguration")
UpdateMediaStorageConfiguration = Action("UpdateMediaStorageConfiguration")
UpdateNotificationConfiguration = Action("UpdateNotificationConfiguration")
UpdateSignalingChannel = Action("UpdateSignalingChannel")
UpdateStream = Action("UpdateStream")
