# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SNS"
prefix = "sns"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddPermission = Action("AddPermission")
CheckIfPhoneNumberIsOptedOut = Action("CheckIfPhoneNumberIsOptedOut")
ConfirmSubscription = Action("ConfirmSubscription")
CreatePlatformApplication = Action("CreatePlatformApplication")
CreatePlatformEndpoint = Action("CreatePlatformEndpoint")
CreateSMSSandboxPhoneNumber = Action("CreateSMSSandboxPhoneNumber")
CreateTopic = Action("CreateTopic")
DeleteEndpoint = Action("DeleteEndpoint")
DeletePlatformApplication = Action("DeletePlatformApplication")
DeleteSMSSandboxPhoneNumber = Action("DeleteSMSSandboxPhoneNumber")
DeleteTopic = Action("DeleteTopic")
GetDataProtectionPolicy = Action("GetDataProtectionPolicy")
GetEndpointAttributes = Action("GetEndpointAttributes")
GetPlatformApplicationAttributes = Action("GetPlatformApplicationAttributes")
GetSMSAttributes = Action("GetSMSAttributes")
GetSMSSandboxAccountStatus = Action("GetSMSSandboxAccountStatus")
GetSubscriptionAttributes = Action("GetSubscriptionAttributes")
GetTopicAttributes = Action("GetTopicAttributes")
ListEndpointsByPlatformApplication = Action("ListEndpointsByPlatformApplication")
ListOriginationNumbers = Action("ListOriginationNumbers")
ListPhoneNumbersOptedOut = Action("ListPhoneNumbersOptedOut")
ListPlatformApplications = Action("ListPlatformApplications")
ListSMSSandboxPhoneNumbers = Action("ListSMSSandboxPhoneNumbers")
ListSubscriptions = Action("ListSubscriptions")
ListSubscriptionsByTopic = Action("ListSubscriptionsByTopic")
ListTagsForResource = Action("ListTagsForResource")
ListTopics = Action("ListTopics")
OptInPhoneNumber = Action("OptInPhoneNumber")
Publish = Action("Publish")
PutDataProtectionPolicy = Action("PutDataProtectionPolicy")
RemovePermission = Action("RemovePermission")
SetEndpointAttributes = Action("SetEndpointAttributes")
SetPlatformApplicationAttributes = Action("SetPlatformApplicationAttributes")
SetSMSAttributes = Action("SetSMSAttributes")
SetSubscriptionAttributes = Action("SetSubscriptionAttributes")
SetTopicAttributes = Action("SetTopicAttributes")
Subscribe = Action("Subscribe")
TagResource = Action("TagResource")
Unsubscribe = Action("Unsubscribe")
UntagResource = Action("UntagResource")
VerifySMSSandboxPhoneNumber = Action("VerifySMSSandboxPhoneNumber")
