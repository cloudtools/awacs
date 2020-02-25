# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon AWS Cloud Contact Center'
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


CreateInstance = Action('CreateInstance')
CreateUser = Action('CreateUser')
DeleteUser = Action('DeleteUser')
DescribeInstance = Action('DescribeInstance')
DescribeUser = Action('DescribeUser')
DescribeUserHierarchyGroup = Action('DescribeUserHierarchyGroup')
DescribeUserHierarchyStructure = Action('DescribeUserHierarchyStructure')
DestroyInstance = Action('DestroyInstance')
GetContactAttributes = Action('GetContactAttributes')
GetCurrentMetricData = Action('GetCurrentMetricData')
GetFederationToken = Action('GetFederationToken')
GetFederationTokens = Action('GetFederationTokens')
GetMetricData = Action('GetMetricData')
ListContactFlows = Action('ListContactFlows')
ListHoursOfOperations = Action('ListHoursOfOperations')
ListInstances = Action('ListInstances')
ListPhoneNumbers = Action('ListPhoneNumbers')
ListQueues = Action('ListQueues')
ListRoutingProfiles = Action('ListRoutingProfiles')
ListSecurityProfiles = Action('ListSecurityProfiles')
ListTagsForResource = Action('ListTagsForResource')
ListUserHierarchyGroups = Action('ListUserHierarchyGroups')
ListUsers = Action('ListUsers')
ModifyInstance = Action('ModifyInstance')
StartChatContact = Action('StartChatContact')
StartOutboundVoiceContact = Action('StartOutboundVoiceContact')
StopContact = Action('StopContact')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateContactAttributes = Action('UpdateContactAttributes')
UpdateUserHierarchy = Action('UpdateUserHierarchy')
UpdateUserIdentityInfo = Action('UpdateUserIdentityInfo')
UpdateUserPhoneConfig = Action('UpdateUserPhoneConfig')
UpdateUserRoutingProfile = Action('UpdateUserRoutingProfile')
UpdateUserSecurityProfiles = Action('UpdateUserSecurityProfiles')
