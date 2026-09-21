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
AssociateProtectConfiguration = Action("AssociateProtectConfiguration")
CarrierLookup = Action("CarrierLookup")
CreateConfigurationSet = Action("CreateConfigurationSet")
CreateConfigurationSetEventDestination = Action(
    "CreateConfigurationSetEventDestination"
)
CreateEventDestination = Action("CreateEventDestination")
CreateNotifyConfiguration = Action("CreateNotifyConfiguration")
CreateOptOutList = Action("CreateOptOutList")
CreatePool = Action("CreatePool")
CreateProtectConfiguration = Action("CreateProtectConfiguration")
CreateRcsAgent = Action("CreateRcsAgent")
CreateRegistration = Action("CreateRegistration")
CreateRegistrationAssociation = Action("CreateRegistrationAssociation")
CreateRegistrationAttachment = Action("CreateRegistrationAttachment")
CreateRegistrationVersion = Action("CreateRegistrationVersion")
CreateVerifiedDestinationNumber = Action("CreateVerifiedDestinationNumber")
DeleteAccountDefaultProtectConfiguration = Action(
    "DeleteAccountDefaultProtectConfiguration"
)
DeleteConfigurationSet = Action("DeleteConfigurationSet")
DeleteConfigurationSetEventDestination = Action(
    "DeleteConfigurationSetEventDestination"
)
DeleteDefaultMessageType = Action("DeleteDefaultMessageType")
DeleteDefaultSenderId = Action("DeleteDefaultSenderId")
DeleteEventDestination = Action("DeleteEventDestination")
DeleteKeyword = Action("DeleteKeyword")
DeleteMediaMessageSpendLimitOverride = Action("DeleteMediaMessageSpendLimitOverride")
DeleteNotifyConfiguration = Action("DeleteNotifyConfiguration")
DeleteNotifyMessageSpendLimitOverride = Action("DeleteNotifyMessageSpendLimitOverride")
DeleteOptOutList = Action("DeleteOptOutList")
DeleteOptedOutNumber = Action("DeleteOptedOutNumber")
DeletePool = Action("DeletePool")
DeleteProtectConfiguration = Action("DeleteProtectConfiguration")
DeleteProtectConfigurationRuleSetNumberOverride = Action(
    "DeleteProtectConfigurationRuleSetNumberOverride"
)
DeleteRcsAgent = Action("DeleteRcsAgent")
DeleteRcsMessageSpendLimitOverride = Action("DeleteRcsMessageSpendLimitOverride")
DeleteRegistration = Action("DeleteRegistration")
DeleteRegistrationAttachment = Action("DeleteRegistrationAttachment")
DeleteRegistrationFieldValue = Action("DeleteRegistrationFieldValue")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteTextMessageSpendLimitOverride = Action("DeleteTextMessageSpendLimitOverride")
DeleteVerifiedDestinationNumber = Action("DeleteVerifiedDestinationNumber")
DeleteVoiceMessageSpendLimitOverride = Action("DeleteVoiceMessageSpendLimitOverride")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeAccountLimits = Action("DescribeAccountLimits")
DescribeConfigurationSets = Action("DescribeConfigurationSets")
DescribeKeywords = Action("DescribeKeywords")
DescribeNotifyConfigurations = Action("DescribeNotifyConfigurations")
DescribeNotifyTemplates = Action("DescribeNotifyTemplates")
DescribeOptOutLists = Action("DescribeOptOutLists")
DescribeOptedOutNumbers = Action("DescribeOptedOutNumbers")
DescribePhoneNumbers = Action("DescribePhoneNumbers")
DescribePools = Action("DescribePools")
DescribeProtectConfigurations = Action("DescribeProtectConfigurations")
DescribeRcsAgentCountryLaunchStatus = Action("DescribeRcsAgentCountryLaunchStatus")
DescribeRcsAgents = Action("DescribeRcsAgents")
DescribeRegistrationAttachments = Action("DescribeRegistrationAttachments")
DescribeRegistrationFieldDefinitions = Action("DescribeRegistrationFieldDefinitions")
DescribeRegistrationFieldValues = Action("DescribeRegistrationFieldValues")
DescribeRegistrationSectionDefinitions = Action(
    "DescribeRegistrationSectionDefinitions"
)
DescribeRegistrationTypeDefinitions = Action("DescribeRegistrationTypeDefinitions")
DescribeRegistrationVersions = Action("DescribeRegistrationVersions")
DescribeRegistrations = Action("DescribeRegistrations")
DescribeSenderIds = Action("DescribeSenderIds")
DescribeSpendLimits = Action("DescribeSpendLimits")
DescribeVerifiedDestinationNumbers = Action("DescribeVerifiedDestinationNumbers")
DisassociateOriginationIdentity = Action("DisassociateOriginationIdentity")
DisassociateProtectConfiguration = Action("DisassociateProtectConfiguration")
DiscardRegistrationVersion = Action("DiscardRegistrationVersion")
GetConfigurationSetEventDestinations = Action("GetConfigurationSetEventDestinations")
GetProtectConfigurationCountryRuleSet = Action("GetProtectConfigurationCountryRuleSet")
GetResourcePolicy = Action("GetResourcePolicy")
ListAvailablePhoneNumbers = Action("ListAvailablePhoneNumbers")
ListConfigurationSets = Action("ListConfigurationSets")
ListNotifyCountries = Action("ListNotifyCountries")
ListPoolOriginationIdentities = Action("ListPoolOriginationIdentities")
ListProtectConfigurationRuleSetNumberOverrides = Action(
    "ListProtectConfigurationRuleSetNumberOverrides"
)
ListRegistrationAssociations = Action("ListRegistrationAssociations")
ListTagsForResource = Action("ListTagsForResource")
PutKeyword = Action("PutKeyword")
PutMessageFeedback = Action("PutMessageFeedback")
PutOptedOutNumber = Action("PutOptedOutNumber")
PutProtectConfigurationRuleSetNumberOverride = Action(
    "PutProtectConfigurationRuleSetNumberOverride"
)
PutRegistrationFieldValue = Action("PutRegistrationFieldValue")
PutResourcePolicy = Action("PutResourcePolicy")
ReleasePhoneNumber = Action("ReleasePhoneNumber")
ReleaseSenderId = Action("ReleaseSenderId")
RequestPhoneNumber = Action("RequestPhoneNumber")
RequestSenderId = Action("RequestSenderId")
SendDestinationNumberVerificationCode = Action("SendDestinationNumberVerificationCode")
SendMediaMessage = Action("SendMediaMessage")
SendNotifyTextMessage = Action("SendNotifyTextMessage")
SendNotifyVoiceMessage = Action("SendNotifyVoiceMessage")
SendRcsMessage = Action("SendRcsMessage")
SendTextMessage = Action("SendTextMessage")
SendVoiceMessage = Action("SendVoiceMessage")
SetAccountDefaultProtectConfiguration = Action("SetAccountDefaultProtectConfiguration")
SetDefaultMessageFeedbackEnabled = Action("SetDefaultMessageFeedbackEnabled")
SetDefaultMessageType = Action("SetDefaultMessageType")
SetDefaultSenderId = Action("SetDefaultSenderId")
SetMediaMessageSpendLimitOverride = Action("SetMediaMessageSpendLimitOverride")
SetNotifyMessageSpendLimitOverride = Action("SetNotifyMessageSpendLimitOverride")
SetRcsMessageSpendLimitOverride = Action("SetRcsMessageSpendLimitOverride")
SetTextMessageSpendLimitOverride = Action("SetTextMessageSpendLimitOverride")
SetVoiceMessageSpendLimitOverride = Action("SetVoiceMessageSpendLimitOverride")
SubmitRegistrationVersion = Action("SubmitRegistrationVersion")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConfigurationSetEventDestination = Action(
    "UpdateConfigurationSetEventDestination"
)
UpdateEventDestination = Action("UpdateEventDestination")
UpdateNotifyConfiguration = Action("UpdateNotifyConfiguration")
UpdatePhoneNumber = Action("UpdatePhoneNumber")
UpdatePool = Action("UpdatePool")
UpdateProtectConfiguration = Action("UpdateProtectConfiguration")
UpdateProtectConfigurationCountryRuleSet = Action(
    "UpdateProtectConfigurationCountryRuleSet"
)
UpdateRcsAgent = Action("UpdateRcsAgent")
UpdateSenderId = Action("UpdateSenderId")
VerifyDestinationNumber = Action("VerifyDestinationNumber")
