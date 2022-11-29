# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Pinpoint SMS and Voice Service"
prefix = "sms-voice"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateOriginationIdentity = Action("AssociateOriginationIdentity")
CreateConfigurationSet = Action("CreateConfigurationSet")
CreateConfigurationSetEventDestination = Action(
    "CreateConfigurationSetEventDestination"
)
CreateEventDestination = Action("CreateEventDestination")
CreateOptOutList = Action("CreateOptOutList")
CreatePool = Action("CreatePool")
DeleteConfigurationSet = Action("DeleteConfigurationSet")
DeleteConfigurationSetEventDestination = Action(
    "DeleteConfigurationSetEventDestination"
)
DeleteDefaultMessageType = Action("DeleteDefaultMessageType")
DeleteDefaultSenderId = Action("DeleteDefaultSenderId")
DeleteEventDestination = Action("DeleteEventDestination")
DeleteKeyword = Action("DeleteKeyword")
DeleteOptOutList = Action("DeleteOptOutList")
DeleteOptedOutNumber = Action("DeleteOptedOutNumber")
DeletePool = Action("DeletePool")
DeleteTextMessageSpendLimitOverride = Action("DeleteTextMessageSpendLimitOverride")
DeleteVoiceMessageSpendLimitOverride = Action("DeleteVoiceMessageSpendLimitOverride")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeAccountLimits = Action("DescribeAccountLimits")
DescribeConfigurationSets = Action("DescribeConfigurationSets")
DescribeKeywords = Action("DescribeKeywords")
DescribeOptOutLists = Action("DescribeOptOutLists")
DescribeOptedOutNumbers = Action("DescribeOptedOutNumbers")
DescribePhoneNumbers = Action("DescribePhoneNumbers")
DescribePools = Action("DescribePools")
DescribeSenderIds = Action("DescribeSenderIds")
DescribeSpendLimits = Action("DescribeSpendLimits")
DisassociateOriginationIdentity = Action("DisassociateOriginationIdentity")
GetConfigurationSetEventDestinations = Action("GetConfigurationSetEventDestinations")
ListConfigurationSets = Action("ListConfigurationSets")
ListPoolOriginationIdentities = Action("ListPoolOriginationIdentities")
ListTagsForResource = Action("ListTagsForResource")
PutKeyword = Action("PutKeyword")
PutOptedOutNumber = Action("PutOptedOutNumber")
ReleasePhoneNumber = Action("ReleasePhoneNumber")
RequestPhoneNumber = Action("RequestPhoneNumber")
SendTextMessage = Action("SendTextMessage")
SendVoiceMessage = Action("SendVoiceMessage")
SetDefaultMessageType = Action("SetDefaultMessageType")
SetDefaultSenderId = Action("SetDefaultSenderId")
SetTextMessageSpendLimitOverride = Action("SetTextMessageSpendLimitOverride")
SetVoiceMessageSpendLimitOverride = Action("SetVoiceMessageSpendLimitOverride")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConfigurationSetEventDestination = Action(
    "UpdateConfigurationSetEventDestination"
)
UpdateEventDestination = Action("UpdateEventDestination")
UpdatePhoneNumber = Action("UpdatePhoneNumber")
UpdatePool = Action("UpdatePool")
