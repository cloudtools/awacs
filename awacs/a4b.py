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


AssociateDeviceWithRoom = Action('AssociateDeviceWithRoom')
AssociateSkillGroupWithRoom = Action('AssociateSkillGroupWithRoom')
CreateProfile = Action('CreateProfile')
CreateRoom = Action('CreateRoom')
CreateSkillGroup = Action('CreateSkillGroup')
CreateUser = Action('CreateUser')
DeleteProfile = Action('DeleteProfile')
DeleteRoom = Action('DeleteRoom')
DeleteRoomSkillParameter = Action('DeleteRoomSkillParameter')
DeleteSkillGroup = Action('DeleteSkillGroup')
DeleteUser = Action('DeleteUser')
DisassociateDeviceFromRoom = Action('DisassociateDeviceFromRoom')
DisassociateSkillGroupFromRoom = Action('DisassociateSkillGroupFromRoom')
GetDevice = Action('GetDevice')
GetProfile = Action('GetProfile')
GetRoom = Action('GetRoom')
GetRoomSkillParameter = Action('GetRoomSkillParameter')
GetSkillGroup = Action('GetSkillGroup')
ListSkills = Action('ListSkills')
ListTags = Action('ListTags')
PutRoomSkillParameter = Action('PutRoomSkillParameter')
ResolveRoom = Action('ResolveRoom')
RevokeInvitation = Action('RevokeInvitation')
SearchDevices = Action('SearchDevices')
SearchProfiles = Action('SearchProfiles')
SearchRooms = Action('SearchRooms')
SearchSkillGroups = Action('SearchSkillGroups')
SearchUsers = Action('SearchUsers')
SendInvitation = Action('SendInvitation')
StartDeviceSync = Action('StartDeviceSync')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDevice = Action('UpdateDevice')
UpdateProfile = Action('UpdateProfile')
UpdateRoom = Action('UpdateRoom')
UpdateSkillGroup = Action('UpdateSkillGroup')
