# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "High-volume outbound communications"
prefix = "connect-campaigns"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCampaign = Action("CreateCampaign")
DeleteCampaign = Action("DeleteCampaign")
DescribeCampaign = Action("DescribeCampaign")
GetCampaignState = Action("GetCampaignState")
GetCampaignStateBatch = Action("GetCampaignStateBatch")
ListCampaigns = Action("ListCampaigns")
ListTagsForResource = Action("ListTagsForResource")
PauseCampaign = Action("PauseCampaign")
PutConnectInstanceConfig = Action("PutConnectInstanceConfig")
PutDialRequestBatch = Action("PutDialRequestBatch")
ResumeCampaign = Action("ResumeCampaign")
StartCampaign = Action("StartCampaign")
StopCampaign = Action("StopCampaign")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCampaignDialerConfig = Action("UpdateCampaignDialerConfig")
UpdateCampaignName = Action("UpdateCampaignName")
UpdateCampaignOutboundCallConfig = Action("UpdateCampaignOutboundCallConfig")
