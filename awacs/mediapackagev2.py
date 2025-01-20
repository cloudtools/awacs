# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaPackage V2"
prefix = "mediapackagev2"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelHarvestJob = Action("CancelHarvestJob")
CreateChannel = Action("CreateChannel")
CreateChannelGroup = Action("CreateChannelGroup")
CreateHarvestJob = Action("CreateHarvestJob")
CreateOriginEndpoint = Action("CreateOriginEndpoint")
DeleteChannel = Action("DeleteChannel")
DeleteChannelGroup = Action("DeleteChannelGroup")
DeleteChannelPolicy = Action("DeleteChannelPolicy")
DeleteOriginEndpoint = Action("DeleteOriginEndpoint")
DeleteOriginEndpointPolicy = Action("DeleteOriginEndpointPolicy")
GetChannel = Action("GetChannel")
GetChannelGroup = Action("GetChannelGroup")
GetChannelPolicy = Action("GetChannelPolicy")
GetHarvestJob = Action("GetHarvestJob")
GetHeadObject = Action("GetHeadObject")
GetObject = Action("GetObject")
GetOriginEndpoint = Action("GetOriginEndpoint")
GetOriginEndpointPolicy = Action("GetOriginEndpointPolicy")
HarvestObject = Action("HarvestObject")
ListChannelGroups = Action("ListChannelGroups")
ListChannels = Action("ListChannels")
ListHarvestJobs = Action("ListHarvestJobs")
ListOriginEndpoints = Action("ListOriginEndpoints")
ListTagsForResource = Action("ListTagsForResource")
PutChannelPolicy = Action("PutChannelPolicy")
PutObject = Action("PutObject")
PutOriginEndpointPolicy = Action("PutOriginEndpointPolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateChannelGroup = Action("UpdateChannelGroup")
UpdateOriginEndpoint = Action("UpdateOriginEndpoint")
