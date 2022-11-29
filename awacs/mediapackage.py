# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaPackage"
prefix = "mediapackage"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ConfigureLogs = Action("ConfigureLogs")
CreateChannel = Action("CreateChannel")
CreateHarvestJob = Action("CreateHarvestJob")
CreateOriginEndpoint = Action("CreateOriginEndpoint")
DeleteChannel = Action("DeleteChannel")
DeleteOriginEndpoint = Action("DeleteOriginEndpoint")
DescribeChannel = Action("DescribeChannel")
DescribeHarvestJob = Action("DescribeHarvestJob")
DescribeOriginEndpoint = Action("DescribeOriginEndpoint")
ListChannels = Action("ListChannels")
ListHarvestJobs = Action("ListHarvestJobs")
ListOriginEndpoints = Action("ListOriginEndpoints")
ListTagsForResource = Action("ListTagsForResource")
RotateChannelCredentials = Action("RotateChannelCredentials")
RotateIngestEndpointCredentials = Action("RotateIngestEndpointCredentials")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateOriginEndpoint = Action("UpdateOriginEndpoint")
