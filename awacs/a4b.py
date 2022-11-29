# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Alexa for Business"
prefix = "a4b"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ApproveSkill = Action("ApproveSkill")
AssociateContactWithAddressBook = Action("AssociateContactWithAddressBook")
AssociateDeviceWithNetworkProfile = Action("AssociateDeviceWithNetworkProfile")
AssociateDeviceWithRoom = Action("AssociateDeviceWithRoom")
AssociateSkillGroupWithRoom = Action("AssociateSkillGroupWithRoom")
AssociateSkillWithSkillGroup = Action("AssociateSkillWithSkillGroup")
AssociateSkillWithUsers = Action("AssociateSkillWithUsers")
CompleteRegistration = Action("CompleteRegistration")
CreateAddressBook = Action("CreateAddressBook")
CreateBusinessReportSchedule = Action("CreateBusinessReportSchedule")
CreateConferenceProvider = Action("CreateConferenceProvider")
CreateContact = Action("CreateContact")
CreateGatewayGroup = Action("CreateGatewayGroup")
CreateNetworkProfile = Action("CreateNetworkProfile")
CreateProfile = Action("CreateProfile")
CreateRoom = Action("CreateRoom")
CreateSkillGroup = Action("CreateSkillGroup")
CreateUser = Action("CreateUser")
DeleteAddressBook = Action("DeleteAddressBook")
DeleteBusinessReportSchedule = Action("DeleteBusinessReportSchedule")
DeleteConferenceProvider = Action("DeleteConferenceProvider")
DeleteContact = Action("DeleteContact")
DeleteDevice = Action("DeleteDevice")
DeleteDeviceUsageData = Action("DeleteDeviceUsageData")
DeleteGatewayGroup = Action("DeleteGatewayGroup")
DeleteNetworkProfile = Action("DeleteNetworkProfile")
DeleteProfile = Action("DeleteProfile")
DeleteRoom = Action("DeleteRoom")
DeleteRoomSkillParameter = Action("DeleteRoomSkillParameter")
DeleteSkillAuthorization = Action("DeleteSkillAuthorization")
DeleteSkillGroup = Action("DeleteSkillGroup")
DeleteUser = Action("DeleteUser")
DisassociateContactFromAddressBook = Action("DisassociateContactFromAddressBook")
DisassociateDeviceFromRoom = Action("DisassociateDeviceFromRoom")
DisassociateSkillFromSkillGroup = Action("DisassociateSkillFromSkillGroup")
DisassociateSkillFromUsers = Action("DisassociateSkillFromUsers")
DisassociateSkillGroupFromRoom = Action("DisassociateSkillGroupFromRoom")
ForgetSmartHomeAppliances = Action("ForgetSmartHomeAppliances")
GetAddressBook = Action("GetAddressBook")
GetConferencePreference = Action("GetConferencePreference")
GetConferenceProvider = Action("GetConferenceProvider")
GetContact = Action("GetContact")
GetDevice = Action("GetDevice")
GetGateway = Action("GetGateway")
GetGatewayGroup = Action("GetGatewayGroup")
GetInvitationConfiguration = Action("GetInvitationConfiguration")
GetNetworkProfile = Action("GetNetworkProfile")
GetProfile = Action("GetProfile")
GetRoom = Action("GetRoom")
GetRoomSkillParameter = Action("GetRoomSkillParameter")
GetSkillGroup = Action("GetSkillGroup")
ListBusinessReportSchedules = Action("ListBusinessReportSchedules")
ListConferenceProviders = Action("ListConferenceProviders")
ListDeviceEvents = Action("ListDeviceEvents")
ListGatewayGroups = Action("ListGatewayGroups")
ListGateways = Action("ListGateways")
ListSkills = Action("ListSkills")
ListSkillsStoreCategories = Action("ListSkillsStoreCategories")
ListSkillsStoreSkillsByCategory = Action("ListSkillsStoreSkillsByCategory")
ListSmartHomeAppliances = Action("ListSmartHomeAppliances")
ListTags = Action("ListTags")
PutConferencePreference = Action("PutConferencePreference")
PutDeviceSetupEvents = Action("PutDeviceSetupEvents")
PutInvitationConfiguration = Action("PutInvitationConfiguration")
PutRoomSkillParameter = Action("PutRoomSkillParameter")
PutSkillAuthorization = Action("PutSkillAuthorization")
RegisterAVSDevice = Action("RegisterAVSDevice")
RegisterDevice = Action("RegisterDevice")
RejectSkill = Action("RejectSkill")
ResolveRoom = Action("ResolveRoom")
RevokeInvitation = Action("RevokeInvitation")
SearchAddressBooks = Action("SearchAddressBooks")
SearchContacts = Action("SearchContacts")
SearchDevices = Action("SearchDevices")
SearchNetworkProfiles = Action("SearchNetworkProfiles")
SearchProfiles = Action("SearchProfiles")
SearchRooms = Action("SearchRooms")
SearchSkillGroups = Action("SearchSkillGroups")
SearchUsers = Action("SearchUsers")
SendAnnouncement = Action("SendAnnouncement")
SendInvitation = Action("SendInvitation")
StartDeviceSync = Action("StartDeviceSync")
StartSmartHomeApplianceDiscovery = Action("StartSmartHomeApplianceDiscovery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAddressBook = Action("UpdateAddressBook")
UpdateBusinessReportSchedule = Action("UpdateBusinessReportSchedule")
UpdateConferenceProvider = Action("UpdateConferenceProvider")
UpdateContact = Action("UpdateContact")
UpdateDevice = Action("UpdateDevice")
UpdateGateway = Action("UpdateGateway")
UpdateGatewayGroup = Action("UpdateGatewayGroup")
UpdateNetworkProfile = Action("UpdateNetworkProfile")
UpdateProfile = Action("UpdateProfile")
UpdateRoom = Action("UpdateRoom")
UpdateSkillGroup = Action("UpdateSkillGroup")
