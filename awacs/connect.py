# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect"
prefix = "connect"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateApprovedOrigin = Action("AssociateApprovedOrigin")
AssociateInstanceStorageConfig = Action("AssociateInstanceStorageConfig")
AssociateLambdaFunction = Action("AssociateLambdaFunction")
AssociateLexBot = Action("AssociateLexBot")
AssociateQueueQuickConnects = Action("AssociateQueueQuickConnects")
AssociateRoutingProfileQueues = Action("AssociateRoutingProfileQueues")
AssociateSecurityKey = Action("AssociateSecurityKey")
CreateContactFlow = Action("CreateContactFlow")
CreateInstance = Action("CreateInstance")
CreateQueue = Action("CreateQueue")
CreateQuickConnect = Action("CreateQuickConnect")
CreateRoutingProfile = Action("CreateRoutingProfile")
CreateUser = Action("CreateUser")
CreateUserHierarchyGroup = Action("CreateUserHierarchyGroup")
DeleteInstance = Action("DeleteInstance")
DeleteQuickConnect = Action("DeleteQuickConnect")
DeleteUser = Action("DeleteUser")
DeleteUserHierarchyGroup = Action("DeleteUserHierarchyGroup")
DescribeContactFlow = Action("DescribeContactFlow")
DescribeHoursOfOperation = Action("DescribeHoursOfOperation")
DescribeInstance = Action("DescribeInstance")
DescribeInstanceAttribute = Action("DescribeInstanceAttribute")
DescribeInstanceStorageConfig = Action("DescribeInstanceStorageConfig")
DescribeQueue = Action("DescribeQueue")
DescribeQuickConnect = Action("DescribeQuickConnect")
DescribeRoutingProfile = Action("DescribeRoutingProfile")
DescribeUser = Action("DescribeUser")
DescribeUserHierarchyGroup = Action("DescribeUserHierarchyGroup")
DescribeUserHierarchyStructure = Action("DescribeUserHierarchyStructure")
DestroyInstance = Action("DestroyInstance")
DisassociateApprovedOrigin = Action("DisassociateApprovedOrigin")
DisassociateInstanceStorageConfig = Action("DisassociateInstanceStorageConfig")
DisassociateLambdaFunction = Action("DisassociateLambdaFunction")
DisassociateLexBot = Action("DisassociateLexBot")
DisassociateQueueQuickConnects = Action("DisassociateQueueQuickConnects")
DisassociateRoutingProfileQueues = Action("DisassociateRoutingProfileQueues")
DisassociateSecurityKey = Action("DisassociateSecurityKey")
GetContactAttributes = Action("GetContactAttributes")
GetCurrentMetricData = Action("GetCurrentMetricData")
GetFederationToken = Action("GetFederationToken")
GetFederationTokens = Action("GetFederationTokens")
GetMetricData = Action("GetMetricData")
ListApprovedOrigins = Action("ListApprovedOrigins")
ListContactFlows = Action("ListContactFlows")
ListHoursOfOperations = Action("ListHoursOfOperations")
ListInstanceAttributes = Action("ListInstanceAttributes")
ListInstanceStorageConfigs = Action("ListInstanceStorageConfigs")
ListInstances = Action("ListInstances")
ListLambdaFunctions = Action("ListLambdaFunctions")
ListLexBots = Action("ListLexBots")
ListPhoneNumbers = Action("ListPhoneNumbers")
ListPrompts = Action("ListPrompts")
ListQueueQuickConnects = Action("ListQueueQuickConnects")
ListQueues = Action("ListQueues")
ListQuickConnects = Action("ListQuickConnects")
ListRoutingProfileQueues = Action("ListRoutingProfileQueues")
ListRoutingProfiles = Action("ListRoutingProfiles")
ListSecurityKeys = Action("ListSecurityKeys")
ListSecurityProfiles = Action("ListSecurityProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListUserHierarchyGroups = Action("ListUserHierarchyGroups")
ListUsers = Action("ListUsers")
ModifyInstance = Action("ModifyInstance")
ResumeContactRecording = Action("ResumeContactRecording")
StartChatContact = Action("StartChatContact")
StartContactRecording = Action("StartContactRecording")
StartOutboundVoiceContact = Action("StartOutboundVoiceContact")
StartTaskContact = Action("StartTaskContact")
StopContact = Action("StopContact")
StopContactRecording = Action("StopContactRecording")
SuspendContactRecording = Action("SuspendContactRecording")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateContactAttributes = Action("UpdateContactAttributes")
UpdateContactFlowContent = Action("UpdateContactFlowContent")
UpdateContactFlowName = Action("UpdateContactFlowName")
UpdateInstanceAttribute = Action("UpdateInstanceAttribute")
UpdateInstanceStorageConfig = Action("UpdateInstanceStorageConfig")
UpdateQueueHoursOfOperation = Action("UpdateQueueHoursOfOperation")
UpdateQueueMaxContacts = Action("UpdateQueueMaxContacts")
UpdateQueueName = Action("UpdateQueueName")
UpdateQueueOutboundCallerConfig = Action("UpdateQueueOutboundCallerConfig")
UpdateQueueStatus = Action("UpdateQueueStatus")
UpdateQuickConnectConfig = Action("UpdateQuickConnectConfig")
UpdateQuickConnectName = Action("UpdateQuickConnectName")
UpdateRoutingProfileConcurrency = Action("UpdateRoutingProfileConcurrency")
UpdateRoutingProfileDefaultOutboundQueue = Action(
    "UpdateRoutingProfileDefaultOutboundQueue"
)
UpdateRoutingProfileName = Action("UpdateRoutingProfileName")
UpdateRoutingProfileQueues = Action("UpdateRoutingProfileQueues")
UpdateUserHierarchy = Action("UpdateUserHierarchy")
UpdateUserHierarchyGroupName = Action("UpdateUserHierarchyGroupName")
UpdateUserHierarchyStructure = Action("UpdateUserHierarchyStructure")
UpdateUserIdentityInfo = Action("UpdateUserIdentityInfo")
UpdateUserPhoneConfig = Action("UpdateUserPhoneConfig")
UpdateUserRoutingProfile = Action("UpdateUserRoutingProfile")
UpdateUserSecurityProfiles = Action("UpdateUserSecurityProfiles")
