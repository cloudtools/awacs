# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Connect'
prefix = 'connect'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateRoutingProfileQueues = Action('AssociateRoutingProfileQueues')
CreateContactFlow = Action('CreateContactFlow')
CreateInstance = Action('CreateInstance')
CreateRoutingProfile = Action('CreateRoutingProfile')
CreateUser = Action('CreateUser')
DeleteUser = Action('DeleteUser')
DescribeContactFlow = Action('DescribeContactFlow')
DescribeInstance = Action('DescribeInstance')
DescribeRoutingProfile = Action('DescribeRoutingProfile')
DescribeUser = Action('DescribeUser')
DescribeUserHierarchyGroup = Action('DescribeUserHierarchyGroup')
DescribeUserHierarchyStructure = Action('DescribeUserHierarchyStructure')
DestroyInstance = Action('DestroyInstance')
DisassociateRoutingProfileQueues = \
    Action('DisassociateRoutingProfileQueues')
GetContactAttributes = Action('GetContactAttributes')
GetCurrentMetricData = Action('GetCurrentMetricData')
GetFederationToken = Action('GetFederationToken')
GetFederationTokens = Action('GetFederationTokens')
GetMetricData = Action('GetMetricData')
ListContactFlows = Action('ListContactFlows')
ListHoursOfOperations = Action('ListHoursOfOperations')
ListInstances = Action('ListInstances')
ListPhoneNumbers = Action('ListPhoneNumbers')
ListPrompts = Action('ListPrompts')
ListQueues = Action('ListQueues')
ListRoutingProfileQueues = Action('ListRoutingProfileQueues')
ListRoutingProfiles = Action('ListRoutingProfiles')
ListSecurityProfiles = Action('ListSecurityProfiles')
ListTagsForResource = Action('ListTagsForResource')
ListUserHierarchyGroups = Action('ListUserHierarchyGroups')
ListUsers = Action('ListUsers')
ModifyInstance = Action('ModifyInstance')
ResumeContactRecording = Action('ResumeContactRecording')
StartChatContact = Action('StartChatContact')
StartContactRecording = Action('StartContactRecording')
StartOutboundVoiceContact = Action('StartOutboundVoiceContact')
StopContact = Action('StopContact')
StopContactRecording = Action('StopContactRecording')
SuspendContactRecording = Action('SuspendContactRecording')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateContactAttributes = Action('UpdateContactAttributes')
UpdateContactFlowContent = Action('UpdateContactFlowContent')
UpdateContactFlowName = Action('UpdateContactFlowName')
UpdateRoutingProfileConcurrency = \
    Action('UpdateRoutingProfileConcurrency')
UpdateRoutingProfileDefaultOutboundQueue = \
    Action('UpdateRoutingProfileDefaultOutboundQueue')
UpdateRoutingProfileName = Action('UpdateRoutingProfileName')
UpdateRoutingProfileQueues = Action('UpdateRoutingProfileQueues')
UpdateUserHierarchy = Action('UpdateUserHierarchy')
UpdateUserIdentityInfo = Action('UpdateUserIdentityInfo')
UpdateUserPhoneConfig = Action('UpdateUserPhoneConfig')
UpdateUserRoutingProfile = Action('UpdateUserRoutingProfile')
UpdateUserSecurityProfiles = Action('UpdateUserSecurityProfiles')
