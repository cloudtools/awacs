# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect Outbound Campaigns"
prefix = "connect-campaigns"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCampaign = Action("CreateCampaign")
DeleteCampaign = Action("DeleteCampaign")
DeleteCampaignChannelSubtypeConfig = Action("DeleteCampaignChannelSubtypeConfig")
DeleteCampaignCommunicationLimits = Action("DeleteCampaignCommunicationLimits")
DeleteCampaignCommunicationTime = Action("DeleteCampaignCommunicationTime")
DeleteConnectInstanceConfig = Action("DeleteConnectInstanceConfig")
DeleteConnectInstanceIntegration = Action("DeleteConnectInstanceIntegration")
DeleteInstanceOnboardingJob = Action("DeleteInstanceOnboardingJob")
DescribeCampaign = Action("DescribeCampaign")
GetCampaignState = Action("GetCampaignState")
GetCampaignStateBatch = Action("GetCampaignStateBatch")
GetConnectInstanceConfig = Action("GetConnectInstanceConfig")
GetInstanceOnboardingJobStatus = Action("GetInstanceOnboardingJobStatus")
ListCampaigns = Action("ListCampaigns")
ListConnectInstanceIntegrations = Action("ListConnectInstanceIntegrations")
ListTagsForResource = Action("ListTagsForResource")
PauseCampaign = Action("PauseCampaign")
PutConnectInstanceConfig = Action("PutConnectInstanceConfig")
PutConnectInstanceIntegration = Action("PutConnectInstanceIntegration")
PutDialRequestBatch = Action("PutDialRequestBatch")
PutOutboundRequestBatch = Action("PutOutboundRequestBatch")
PutProfileOutboundRequestBatch = Action("PutProfileOutboundRequestBatch")
ResumeCampaign = Action("ResumeCampaign")
StartCampaign = Action("StartCampaign")
StartInstanceOnboardingJob = Action("StartInstanceOnboardingJob")
StopCampaign = Action("StopCampaign")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCampaignChannelSubtypeConfig = Action("UpdateCampaignChannelSubtypeConfig")
UpdateCampaignCommunicationLimits = Action("UpdateCampaignCommunicationLimits")
UpdateCampaignCommunicationTime = Action("UpdateCampaignCommunicationTime")
UpdateCampaignDialerConfig = Action("UpdateCampaignDialerConfig")
UpdateCampaignFlowAssociation = Action("UpdateCampaignFlowAssociation")
UpdateCampaignName = Action("UpdateCampaignName")
UpdateCampaignOutboundCallConfig = Action("UpdateCampaignOutboundCallConfig")
UpdateCampaignSchedule = Action("UpdateCampaignSchedule")
UpdateCampaignSource = Action("UpdateCampaignSource")
