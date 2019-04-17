# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Alexa for Business'
prefix = 'a4b'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ApproveSkill = Action('ApproveSkill')
AssociateContactWithAddressBook = \
    Action('AssociateContactWithAddressBook')
AssociateDeviceWithRoom = Action('AssociateDeviceWithRoom')
AssociateSkillGroupWithRoom = Action('AssociateSkillGroupWithRoom')
AssociateSkillWithSkillGroup = Action('AssociateSkillWithSkillGroup')
AssociateSkillWithUsers = Action('AssociateSkillWithUsers')
CreateAddressBook = Action('CreateAddressBook')
CreateBusinessReportSchedule = Action('CreateBusinessReportSchedule')
CreateConferenceProvider = Action('CreateConferenceProvider')
CreateContact = Action('CreateContact')
CreateProfile = Action('CreateProfile')
CreateRoom = Action('CreateRoom')
CreateSkillGroup = Action('CreateSkillGroup')
CreateUser = Action('CreateUser')
DeleteAddressBook = Action('DeleteAddressBook')
DeleteBusinessReportSchedule = Action('DeleteBusinessReportSchedule')
DeleteConferenceProvider = Action('DeleteConferenceProvider')
DeleteContact = Action('DeleteContact')
DeleteDevice = Action('DeleteDevice')
DeleteProfile = Action('DeleteProfile')
DeleteRoom = Action('DeleteRoom')
DeleteRoomSkillParameter = Action('DeleteRoomSkillParameter')
DeleteSkillAuthorization = Action('DeleteSkillAuthorization')
DeleteSkillGroup = Action('DeleteSkillGroup')
DeleteUser = Action('DeleteUser')
DisassociateContactFromAddressBook = \
    Action('DisassociateContactFromAddressBook')
DisassociateDeviceFromRoom = Action('DisassociateDeviceFromRoom')
DisassociateSkillFromSkillGroup = \
    Action('DisassociateSkillFromSkillGroup')
DisassociateSkillFromUsers = Action('DisassociateSkillFromUsers')
DisassociateSkillGroupFromRoom = Action('DisassociateSkillGroupFromRoom')
ForgetSmartHomeAppliances = Action('ForgetSmartHomeAppliances')
GetAddressBook = Action('GetAddressBook')
GetConferencePreference = Action('GetConferencePreference')
GetConferenceProvider = Action('GetConferenceProvider')
GetContact = Action('GetContact')
GetDevice = Action('GetDevice')
GetProfile = Action('GetProfile')
GetRoom = Action('GetRoom')
GetRoomSkillParameter = Action('GetRoomSkillParameter')
GetSkillGroup = Action('GetSkillGroup')
ListBusinessReportSchedules = Action('ListBusinessReportSchedules')
ListConferenceProviders = Action('ListConferenceProviders')
ListDeviceEvents = Action('ListDeviceEvents')
ListSkills = Action('ListSkills')
ListSkillsStoreCategories = Action('ListSkillsStoreCategories')
ListSkillsStoreSkillsByCategory = \
    Action('ListSkillsStoreSkillsByCategory')
ListSmartHomeAppliances = Action('ListSmartHomeAppliances')
ListTags = Action('ListTags')
PutConferencePreference = Action('PutConferencePreference')
PutRoomSkillParameter = Action('PutRoomSkillParameter')
PutSkillAuthorization = Action('PutSkillAuthorization')
RegisterAVSDevice = Action('RegisterAVSDevice')
RejectSkill = Action('RejectSkill')
ResolveRoom = Action('ResolveRoom')
RevokeInvitation = Action('RevokeInvitation')
SearchAddressBooks = Action('SearchAddressBooks')
SearchContacts = Action('SearchContacts')
SearchDevices = Action('SearchDevices')
SearchProfiles = Action('SearchProfiles')
SearchRooms = Action('SearchRooms')
SearchSkillGroups = Action('SearchSkillGroups')
SearchUsers = Action('SearchUsers')
SendInvitation = Action('SendInvitation')
StartDeviceSync = Action('StartDeviceSync')
StartSmartHomeApplianceDiscovery = \
    Action('StartSmartHomeApplianceDiscovery')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAddressBook = Action('UpdateAddressBook')
UpdateBusinessReportSchedule = Action('UpdateBusinessReportSchedule')
UpdateConferenceProvider = Action('UpdateConferenceProvider')
UpdateContact = Action('UpdateContact')
UpdateDevice = Action('UpdateDevice')
UpdateProfile = Action('UpdateProfile')
UpdateRoom = Action('UpdateRoom')
UpdateSkillGroup = Action('UpdateSkillGroup')
