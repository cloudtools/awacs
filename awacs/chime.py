# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Chime"
prefix = "chime"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptDelegate = Action("AcceptDelegate")
ActivateUsers = Action("ActivateUsers")
AddDomain = Action("AddDomain")
AddOrUpdateGroups = Action("AddOrUpdateGroups")
AssociatePhoneNumberWithUser = Action("AssociatePhoneNumberWithUser")
AssociatePhoneNumbersWithVoiceConnector = Action(
    "AssociatePhoneNumbersWithVoiceConnector"
)
AssociatePhoneNumbersWithVoiceConnectorGroup = Action(
    "AssociatePhoneNumbersWithVoiceConnectorGroup"
)
AssociateSigninDelegateGroupsWithAccount = Action(
    "AssociateSigninDelegateGroupsWithAccount"
)
AuthorizeDirectory = Action("AuthorizeDirectory")
BatchCreateAttendee = Action("BatchCreateAttendee")
BatchCreateRoomMembership = Action("BatchCreateRoomMembership")
BatchDeletePhoneNumber = Action("BatchDeletePhoneNumber")
BatchSuspendUser = Action("BatchSuspendUser")
BatchUnsuspendUser = Action("BatchUnsuspendUser")
BatchUpdatePhoneNumber = Action("BatchUpdatePhoneNumber")
BatchUpdateUser = Action("BatchUpdateUser")
Connect = Action("Connect")
ConnectDirectory = Action("ConnectDirectory")
CreateAccount = Action("CreateAccount")
CreateApiKey = Action("CreateApiKey")
CreateAppInstance = Action("CreateAppInstance")
CreateAppInstanceAdmin = Action("CreateAppInstanceAdmin")
CreateAppInstanceUser = Action("CreateAppInstanceUser")
CreateAttendee = Action("CreateAttendee")
CreateBot = Action("CreateBot")
CreateBotMembership = Action("CreateBotMembership")
CreateCDRBucket = Action("CreateCDRBucket")
CreateChannel = Action("CreateChannel")
CreateChannelBan = Action("CreateChannelBan")
CreateChannelMembership = Action("CreateChannelMembership")
CreateChannelModerator = Action("CreateChannelModerator")
CreateMeeting = Action("CreateMeeting")
CreateMeetingDialOut = Action("CreateMeetingDialOut")
CreateMeetingWithAttendees = Action("CreateMeetingWithAttendees")
CreatePhoneNumberOrder = Action("CreatePhoneNumberOrder")
CreateProxySession = Action("CreateProxySession")
CreateRoom = Action("CreateRoom")
CreateRoomMembership = Action("CreateRoomMembership")
CreateSipMediaApplication = Action("CreateSipMediaApplication")
CreateSipMediaApplicationCall = Action("CreateSipMediaApplicationCall")
CreateSipRule = Action("CreateSipRule")
CreateUser = Action("CreateUser")
CreateVoiceConnector = Action("CreateVoiceConnector")
CreateVoiceConnectorGroup = Action("CreateVoiceConnectorGroup")
DeleteAccount = Action("DeleteAccount")
DeleteAccountOpenIdConfig = Action("DeleteAccountOpenIdConfig")
DeleteApiKey = Action("DeleteApiKey")
DeleteAppInstance = Action("DeleteAppInstance")
DeleteAppInstanceAdmin = Action("DeleteAppInstanceAdmin")
DeleteAppInstanceStreamingConfigurations = Action(
    "DeleteAppInstanceStreamingConfigurations"
)
DeleteAppInstanceUser = Action("DeleteAppInstanceUser")
DeleteAttendee = Action("DeleteAttendee")
DeleteCDRBucket = Action("DeleteCDRBucket")
DeleteChannel = Action("DeleteChannel")
DeleteChannelBan = Action("DeleteChannelBan")
DeleteChannelMembership = Action("DeleteChannelMembership")
DeleteChannelMessage = Action("DeleteChannelMessage")
DeleteChannelModerator = Action("DeleteChannelModerator")
DeleteDelegate = Action("DeleteDelegate")
DeleteDomain = Action("DeleteDomain")
DeleteEventsConfiguration = Action("DeleteEventsConfiguration")
DeleteGroups = Action("DeleteGroups")
DeleteMeeting = Action("DeleteMeeting")
DeletePhoneNumber = Action("DeletePhoneNumber")
DeleteProxySession = Action("DeleteProxySession")
DeleteRoom = Action("DeleteRoom")
DeleteRoomMembership = Action("DeleteRoomMembership")
DeleteSipMediaApplication = Action("DeleteSipMediaApplication")
DeleteSipRule = Action("DeleteSipRule")
DeleteVoiceConnector = Action("DeleteVoiceConnector")
DeleteVoiceConnectorEmergencyCallingConfiguration = Action(
    "DeleteVoiceConnectorEmergencyCallingConfiguration"
)
DeleteVoiceConnectorGroup = Action("DeleteVoiceConnectorGroup")
DeleteVoiceConnectorOrigination = Action("DeleteVoiceConnectorOrigination")
DeleteVoiceConnectorProxy = Action("DeleteVoiceConnectorProxy")
DeleteVoiceConnectorStreamingConfiguration = Action(
    "DeleteVoiceConnectorStreamingConfiguration"
)
DeleteVoiceConnectorTermination = Action("DeleteVoiceConnectorTermination")
DeleteVoiceConnectorTerminationCredentials = Action(
    "DeleteVoiceConnectorTerminationCredentials"
)
DescribeAppInstance = Action("DescribeAppInstance")
DescribeAppInstanceAdmin = Action("DescribeAppInstanceAdmin")
DescribeAppInstanceUser = Action("DescribeAppInstanceUser")
DescribeChannel = Action("DescribeChannel")
DescribeChannelBan = Action("DescribeChannelBan")
DescribeChannelMembership = Action("DescribeChannelMembership")
DescribeChannelMembershipForAppInstanceUser = Action(
    "DescribeChannelMembershipForAppInstanceUser"
)
DescribeChannelModeratedByAppInstanceUser = Action(
    "DescribeChannelModeratedByAppInstanceUser"
)
DescribeChannelModerator = Action("DescribeChannelModerator")
DisassociatePhoneNumberFromUser = Action("DisassociatePhoneNumberFromUser")
DisassociatePhoneNumbersFromVoiceConnector = Action(
    "DisassociatePhoneNumbersFromVoiceConnector"
)
DisassociatePhoneNumbersFromVoiceConnectorGroup = Action(
    "DisassociatePhoneNumbersFromVoiceConnectorGroup"
)
DisassociateSigninDelegateGroupsFromAccount = Action(
    "DisassociateSigninDelegateGroupsFromAccount"
)
DisconnectDirectory = Action("DisconnectDirectory")
GetAccount = Action("GetAccount")
GetAccountResource = Action("GetAccountResource")
GetAccountSettings = Action("GetAccountSettings")
GetAccountWithOpenIdConfig = Action("GetAccountWithOpenIdConfig")
GetAppInstanceRetentionSettings = Action("GetAppInstanceRetentionSettings")
GetAppInstanceStreamingConfigurations = Action("GetAppInstanceStreamingConfigurations")
GetAttendee = Action("GetAttendee")
GetBot = Action("GetBot")
GetCDRBucket = Action("GetCDRBucket")
GetChannelMessage = Action("GetChannelMessage")
GetDomain = Action("GetDomain")
GetEventsConfiguration = Action("GetEventsConfiguration")
GetGlobalSettings = Action("GetGlobalSettings")
GetMeeting = Action("GetMeeting")
GetMeetingDetail = Action("GetMeetingDetail")
GetMessagingSessionEndpoint = Action("GetMessagingSessionEndpoint")
GetPhoneNumber = Action("GetPhoneNumber")
GetPhoneNumberOrder = Action("GetPhoneNumberOrder")
GetPhoneNumberSettings = Action("GetPhoneNumberSettings")
GetProxySession = Action("GetProxySession")
GetRetentionSettings = Action("GetRetentionSettings")
GetRoom = Action("GetRoom")
GetSipMediaApplication = Action("GetSipMediaApplication")
GetSipMediaApplicationLoggingConfiguration = Action(
    "GetSipMediaApplicationLoggingConfiguration"
)
GetSipRule = Action("GetSipRule")
GetTelephonyLimits = Action("GetTelephonyLimits")
GetUser = Action("GetUser")
GetUserActivityReportData = Action("GetUserActivityReportData")
GetUserByEmail = Action("GetUserByEmail")
GetUserSettings = Action("GetUserSettings")
GetVoiceConnector = Action("GetVoiceConnector")
GetVoiceConnectorEmergencyCallingConfiguration = Action(
    "GetVoiceConnectorEmergencyCallingConfiguration"
)
GetVoiceConnectorGroup = Action("GetVoiceConnectorGroup")
GetVoiceConnectorLoggingConfiguration = Action("GetVoiceConnectorLoggingConfiguration")
GetVoiceConnectorOrigination = Action("GetVoiceConnectorOrigination")
GetVoiceConnectorProxy = Action("GetVoiceConnectorProxy")
GetVoiceConnectorStreamingConfiguration = Action(
    "GetVoiceConnectorStreamingConfiguration"
)
GetVoiceConnectorTermination = Action("GetVoiceConnectorTermination")
GetVoiceConnectorTerminationHealth = Action("GetVoiceConnectorTerminationHealth")
InviteDelegate = Action("InviteDelegate")
InviteUsers = Action("InviteUsers")
InviteUsersFromProvider = Action("InviteUsersFromProvider")
ListAccountUsageReportData = Action("ListAccountUsageReportData")
ListAccounts = Action("ListAccounts")
ListApiKeys = Action("ListApiKeys")
ListAppInstanceAdmins = Action("ListAppInstanceAdmins")
ListAppInstanceUsers = Action("ListAppInstanceUsers")
ListAppInstances = Action("ListAppInstances")
ListAttendeeTags = Action("ListAttendeeTags")
ListAttendees = Action("ListAttendees")
ListBots = Action("ListBots")
ListCDRBucket = Action("ListCDRBucket")
ListCallingRegions = Action("ListCallingRegions")
ListChannelBans = Action("ListChannelBans")
ListChannelMemberships = Action("ListChannelMemberships")
ListChannelMembershipsForAppInstanceUser = Action(
    "ListChannelMembershipsForAppInstanceUser"
)
ListChannelMessages = Action("ListChannelMessages")
ListChannelModerators = Action("ListChannelModerators")
ListChannels = Action("ListChannels")
ListChannelsModeratedByAppInstanceUser = Action(
    "ListChannelsModeratedByAppInstanceUser"
)
ListDelegates = Action("ListDelegates")
ListDirectories = Action("ListDirectories")
ListDomains = Action("ListDomains")
ListGroups = Action("ListGroups")
ListMeetingEvents = Action("ListMeetingEvents")
ListMeetingTags = Action("ListMeetingTags")
ListMeetings = Action("ListMeetings")
ListMeetingsReportData = Action("ListMeetingsReportData")
ListPhoneNumberOrders = Action("ListPhoneNumberOrders")
ListPhoneNumbers = Action("ListPhoneNumbers")
ListProxySessions = Action("ListProxySessions")
ListRoomMemberships = Action("ListRoomMemberships")
ListRooms = Action("ListRooms")
ListSipMediaApplications = Action("ListSipMediaApplications")
ListSipRules = Action("ListSipRules")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
ListVoiceConnectorGroups = Action("ListVoiceConnectorGroups")
ListVoiceConnectorTerminationCredentials = Action(
    "ListVoiceConnectorTerminationCredentials"
)
ListVoiceConnectors = Action("ListVoiceConnectors")
LogoutUser = Action("LogoutUser")
PutAppInstanceRetentionSettings = Action("PutAppInstanceRetentionSettings")
PutAppInstanceStreamingConfigurations = Action("PutAppInstanceStreamingConfigurations")
PutEventsConfiguration = Action("PutEventsConfiguration")
PutRetentionSettings = Action("PutRetentionSettings")
PutSipMediaApplicationLoggingConfiguration = Action(
    "PutSipMediaApplicationLoggingConfiguration"
)
PutVoiceConnectorEmergencyCallingConfiguration = Action(
    "PutVoiceConnectorEmergencyCallingConfiguration"
)
PutVoiceConnectorLoggingConfiguration = Action("PutVoiceConnectorLoggingConfiguration")
PutVoiceConnectorOrigination = Action("PutVoiceConnectorOrigination")
PutVoiceConnectorProxy = Action("PutVoiceConnectorProxy")
PutVoiceConnectorStreamingConfiguration = Action(
    "PutVoiceConnectorStreamingConfiguration"
)
PutVoiceConnectorTermination = Action("PutVoiceConnectorTermination")
PutVoiceConnectorTerminationCredentials = Action(
    "PutVoiceConnectorTerminationCredentials"
)
RedactChannelMessage = Action("RedactChannelMessage")
RedactConversationMessage = Action("RedactConversationMessage")
RedactRoomMessage = Action("RedactRoomMessage")
RegenerateSecurityToken = Action("RegenerateSecurityToken")
RenameAccount = Action("RenameAccount")
RenewDelegate = Action("RenewDelegate")
ResetAccountResource = Action("ResetAccountResource")
ResetPersonalPIN = Action("ResetPersonalPIN")
ResetPersonalPin = Action("ResetPersonalPin")
RestorePhoneNumber = Action("RestorePhoneNumber")
RetrieveDataExports = Action("RetrieveDataExports")
SearchAvailablePhoneNumbers = Action("SearchAvailablePhoneNumbers")
SendChannelMessage = Action("SendChannelMessage")
StartDataExport = Action("StartDataExport")
SubmitSupportRequest = Action("SubmitSupportRequest")
SuspendUsers = Action("SuspendUsers")
TagAttendee = Action("TagAttendee")
TagMeeting = Action("TagMeeting")
TagResource = Action("TagResource")
UnauthorizeDirectory = Action("UnauthorizeDirectory")
UntagAttendee = Action("UntagAttendee")
UntagMeeting = Action("UntagMeeting")
UntagResource = Action("UntagResource")
UpdateAccount = Action("UpdateAccount")
UpdateAccountOpenIdConfig = Action("UpdateAccountOpenIdConfig")
UpdateAccountResource = Action("UpdateAccountResource")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateAppInstance = Action("UpdateAppInstance")
UpdateAppInstanceUser = Action("UpdateAppInstanceUser")
UpdateBot = Action("UpdateBot")
UpdateCDRBucket = Action("UpdateCDRBucket")
UpdateCDRSettings = Action("UpdateCDRSettings")
UpdateChannel = Action("UpdateChannel")
UpdateChannelMessage = Action("UpdateChannelMessage")
UpdateChannelReadMarker = Action("UpdateChannelReadMarker")
UpdateGlobalSettings = Action("UpdateGlobalSettings")
UpdatePhoneNumber = Action("UpdatePhoneNumber")
UpdatePhoneNumberSettings = Action("UpdatePhoneNumberSettings")
UpdateProxySession = Action("UpdateProxySession")
UpdateRoom = Action("UpdateRoom")
UpdateRoomMembership = Action("UpdateRoomMembership")
UpdateSipMediaApplication = Action("UpdateSipMediaApplication")
UpdateSipRule = Action("UpdateSipRule")
UpdateSupportedLicenses = Action("UpdateSupportedLicenses")
UpdateUser = Action("UpdateUser")
UpdateUserLicenses = Action("UpdateUserLicenses")
UpdateUserSettings = Action("UpdateUserSettings")
UpdateVoiceConnector = Action("UpdateVoiceConnector")
UpdateVoiceConnectorGroup = Action("UpdateVoiceConnectorGroup")
ValidateAccountResource = Action("ValidateAccountResource")
ValidateDelegate = Action("ValidateDelegate")
